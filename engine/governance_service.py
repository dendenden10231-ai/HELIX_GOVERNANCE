"""
engine/governance_service.py
=============================
HELIX Module 2 — Governance Service.

Связывает три слоя:
  1. JSON от Claude-классификатора (РАЗДЕЛ 16 спецификации GOVERNANCE v1.3)
  2. HelixGovernanceMath (Module 0) — детерминированная математика
  3. GICore / OASJournal (Module 1) — журнал аудита решений

Это первый слой который реально ПРОИЗВОДИТ governance-результат
из сырого ответа Claude, а не просто содержит формулы.

Контракт входного JSON (строго по РАЗДЕЛ 16):
{
  "hallucinations": [
    {"type": "TYPE-1".."TYPE-7", "severity_signal": "CRITICAL|HIGH|MEDIUM|LOW",
     "description": str, "evidence": str, "rule_violated": str|null}
  ],
  "ngi_dimensions": {"emotional":0-3,"political":0-3,"archetypal":0-3,"industry":0-3,"explanation":str},
  "eu_ai_act_signals": {"risk_tier": str, "violations": [str]},
  "business_rule_violations": [str]
}
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .governance_math import (
    HelixGovernanceMath,
    Hallucination,
    GovernanceResult,
)
from .gi_core import GICore, OASRecord


class ClassifierResponseError(Exception):
    """Классификатор вернул невалидный JSON или нарушил контракт РАЗДЕЛ 16."""


@dataclass
class GovernanceRequest:
    """Входные данные для одного прохода governance-аудита."""
    ai_output:      str
    business_rules: List[Dict[str, Any]] = field(default_factory=list)
    context_type:   str = "internal"   # customer_facing | internal | regulatory | agent_action
    eu_ai_act_tier_hint: str = "minimal_risk"  # предварительная оценка до классификации
    block_on_types: List[str] = field(default_factory=lambda: ["TYPE-1", "TYPE-7"])
    tenant_id:      Optional[str] = None
    required_hours: float = 0.0
    allocated_hours: float = 0.0


@dataclass
class GovernanceServiceResult:
    """Полный результат сервиса — то что возвращает API наружу."""
    request_context_type: str
    math_result:           GovernanceResult
    ngi_explanation:       str
    eu_ai_act_violations:  List[str]
    business_rule_violations: List[str]
    oas_record:             Optional[OASRecord]
    raw_classifier_json:    Dict[str, Any]


# ─── Парсинг ответа классификатора ─────────────────────────────────────────

REQUIRED_TOP_KEYS = {
    "hallucinations", "ngi_dimensions", "eu_ai_act_signals", "business_rule_violations",
}
VALID_TYPES = {f"TYPE-{i}" for i in range(1, 8)}
VALID_SEVERITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}
VALID_EU_TIERS = {"minimal_risk", "limited_risk", "high_risk", "unacceptable"}


def parse_classifier_response(raw: str | Dict[str, Any]) -> Dict[str, Any]:
    """
    Парсит и валидирует JSON от Claude-классификатора.

    Args:
        raw: либо сырая строка JSON (возможно с ```json fences),
             либо уже распарсенный dict

    Raises:
        ClassifierResponseError: если JSON невалиден или нарушает контракт
    """
    if isinstance(raw, str):
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            # Убираем возможные markdown fences — модели иногда их добавляют
            # вопреки инструкции "только JSON"
            cleaned = cleaned.strip("`")
            if cleaned.startswith("json"):
                cleaned = cleaned[4:]
            cleaned = cleaned.strip()
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as e:
            raise ClassifierResponseError(f"Классификатор вернул невалидный JSON: {e}") from e
    else:
        data = raw

    missing = REQUIRED_TOP_KEYS - set(data.keys())
    if missing:
        raise ClassifierResponseError(
            f"Ответ классификатора не соответствует контракту РАЗДЕЛ 16. "
            f"Отсутствуют ключи: {missing}"
        )

    for h in data["hallucinations"]:
        if h.get("type") not in VALID_TYPES:
            raise ClassifierResponseError(
                f"Невалидный hallucination type: {h.get('type')!r}. "
                f"Должен быть один из {sorted(VALID_TYPES)}"
            )
        if h.get("severity_signal") not in VALID_SEVERITIES:
            raise ClassifierResponseError(
                f"Невалидный severity_signal: {h.get('severity_signal')!r}. "
                f"Должен быть один из {sorted(VALID_SEVERITIES)}"
            )
        # Защита от нарушения контракта: классификатору запрещено
        # присылать числа confidence/scores/weights — это работа Python-движка
        for forbidden_key in ("confidence", "score", "weight", "governance_decision"):
            if forbidden_key in h:
                raise ClassifierResponseError(
                    f"Классификатор нарушил контракт РАЗДЕЛ 16: вернул '{forbidden_key}' "
                    f"— это должен считать только Python-движок, не LLM."
                )

    eu_tier = data["eu_ai_act_signals"].get("risk_tier")
    if eu_tier not in VALID_EU_TIERS:
        raise ClassifierResponseError(
            f"Невалидный eu_ai_act risk_tier: {eu_tier!r}. "
            f"Должен быть один из {sorted(VALID_EU_TIERS)}"
        )

    ngi = data["ngi_dimensions"]
    for dim in ("emotional", "political", "archetypal", "industry"):
        val = ngi.get(dim)
        if not isinstance(val, int) or not (0 <= val <= 3):
            raise ClassifierResponseError(
                f"NGI измерение '{dim}' должно быть целым числом 0-3, получено: {val!r}"
            )

    return data


def hallucinations_from_classifier(data: Dict[str, Any]) -> List[Hallucination]:
    """Конвертирует блок 'hallucinations' классификатора в List[Hallucination]."""
    return [
        Hallucination(
            type=h["type"],
            severity=h["severity_signal"],
            description=h.get("description", ""),
            evidence=h.get("evidence", ""),
            rule_violated=h.get("rule_violated"),
        )
        for h in data["hallucinations"]
    ]


# ─── Сервис ─────────────────────────────────────────────────────────────────

class GovernanceService:
    """
    Оркестрирует один governance-проход: классификатор JSON → математика → OAS.

    Использование:
        gi = GICore(investigation_id="TENANT-42-REQ-001")
        service = GovernanceService(gi)
        result = service.evaluate(request, classifier_raw_json)
    """

    def __init__(self, gi_core: Optional[GICore] = None):
        self.gi = gi_core or GICore()
        self.math = HelixGovernanceMath()

    def evaluate(
        self,
        request: GovernanceRequest,
        classifier_raw: str | Dict[str, Any],
    ) -> GovernanceServiceResult:
        """
        Полный проход: валидировать классификатор → посчитать математику → залогировать.

        Args:
            request:        параметры запроса (business_rules, context_type, block_on_types...)
            classifier_raw: сырой ответ Claude-классификатора (строка JSON или dict)
        """
        data = parse_classifier_response(classifier_raw)
        hallucinations = hallucinations_from_classifier(data)
        ngi_dims = {
            k: data["ngi_dimensions"][k]
            for k in ("emotional", "political", "archetypal", "industry")
        }
        eu_tier = data["eu_ai_act_signals"]["risk_tier"]

        math_result = self.math.run(
            hallucinations=hallucinations,
            ngi_dimensions=ngi_dims,
            eu_tier=eu_tier,
            block_on_types=request.block_on_types,
            required_hours=request.required_hours,
            allocated_hours=request.allocated_hours,
        )

        # Business rule violations — либо из классификатора, либо пересечение
        # rule_violated полей галлюцинаций с business_rule_violations
        brv = list(data.get("business_rule_violations", []))

        oas_record = self.gi.oas.log(
            event_type="GOVERNANCE_DECISION",
            decision=f"{math_result.decision.decision}"
                     + (f": {math_result.decision.reason}" if math_result.decision.reason else ""),
            basis=[
                f"confidence={math_result.confidence_score}",
                f"ciri={math_result.ciri.value}",
                f"ngi={math_result.ngi.total}({math_result.ngi.level})",
                f"hallucinations={len(hallucinations)}",
            ] + [f"rule_violated:{r}" for r in brv],
            protocol_used="GOVERNANCE-MATH",
            ect_level=None,
            challenge_condition=(
                "Пересмотр при появлении новой верификации ключевых утверждений"
                if math_result.decision.decision != "PASS" else None
            ),
        )

        return GovernanceServiceResult(
            request_context_type=request.context_type,
            math_result=math_result,
            ngi_explanation=data["ngi_dimensions"].get("explanation", ""),
            eu_ai_act_violations=data["eu_ai_act_signals"].get("violations", []),
            business_rule_violations=brv,
            oas_record=oas_record,
            raw_classifier_json=data,
        )

    def to_api_response(self, result: GovernanceServiceResult) -> Dict[str, Any]:
        """Сериализует результат в JSON-совместимый dict для HTTP-ответа."""
        mr = result.math_result
        return {
            "decision": mr.decision.decision,
            "decision_reason": mr.decision.reason,
            "block_source": mr.decision.block_source,
            "confidence_score": mr.confidence_score,
            "confidence_level": mr.confidence_level,
            "rpl_factor": mr.rpl_factor,
            "rpl_blocked_ect4": mr.rpl_blocked,
            "ngi": {
                "emotional": mr.ngi.emotional,
                "political": mr.ngi.political,
                "archetypal": mr.ngi.archetypal,
                "industry": mr.ngi.industry,
                "total": mr.ngi.total,
                "level": mr.ngi.level,
                "explanation": result.ngi_explanation,
            },
            "ciri": {
                "value": mr.ciri.value,
                "base_risk": mr.ciri.base_risk,
                "ngi_risk": mr.ciri.ngi_risk,
                "hallucination_risk": mr.ciri.hallucination_risk,
                "rpl_risk": mr.ciri.rpl_risk,
            },
            "hallucinations": [
                {
                    "type": h.type,
                    "severity": h.severity,
                    "description": h.description,
                    "evidence": h.evidence,
                    "rule_violated": h.rule_violated,
                }
                for h in mr.hallucinations
            ],
            "eu_ai_act_violations": result.eu_ai_act_violations,
            "business_rule_violations": result.business_rule_violations,
            "oas_record_id": result.oas_record.record_id if result.oas_record else None,
            "context_type": result.request_context_type,
        }
