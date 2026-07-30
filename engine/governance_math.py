"""
engine/governance_math.py
=========================
HELIX Module 0 — Детерминированный математический движок.

Источник: HELIX_GOVERNANCE_v1_3_FINAL.md, Раздел 14–15
Zero third-party ML. Только Python stdlib + typing.
CVE-2026-45758: никаких PyPI ML-пакетов.

Архитектурный принцип:
  Claude (LLM) → возвращает семантические сигналы (текст, метки, 4 NGI-числа)
  HelixGovernanceMath → считает всё числовое детерминированно
  Никогда наоборот.

Порядок в pipeline:
  [1] Claude-классификатор → JSON с hallucinations + ngi_dimensions + eu_ai_act_signals
  [2] calculate_rpl_factor()       → RPL_Factor
  [3] calculate_confidence_score() → Confidence Score [0–1]
  [4] calculate_ngi_score()        → NGI total + level
  [5] calculate_ciri()             → CIRI [0–100]
  [6] calculate_article9_score()   → EU AI Act Article 9
  [7] make_governance_decision()   → PASS | WARN | BLOCK | HITL_REQUIRED
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ─── Константы (из спецификации, не менять без обновления спеки) ──────────────

HALLUCINATION_WEIGHTS: Dict[str, float] = {
    "CRITICAL": 0.80,
    "HIGH":     0.40,
    "MEDIUM":   0.15,
    "LOW":      0.05,
}

NGI_THRESHOLDS: Dict[str, tuple] = {
    "LOW":      (0,  3),
    "MODERATE": (4,  6),
    "HIGH":     (7,  9),
    "CRITICAL": (10, 12),
}

CIRI_WEIGHTS: Dict[str, float] = {
    "base":          0.50,
    "ngi":           0.20,
    "hallucination": 0.20,
    "rpl":           0.10,
}

# Article 9 EU AI Act — веса требований
ARTICLE9_WEIGHTS: Dict[str, int] = {
    "A9-R1": 20,  # Risk Management System
    "A9-R2": 10,  # Data Governance
    "A9-R3": 15,  # Technical Documentation
    "A9-R4": 15,  # Record-keeping
    "A9-R5": 10,  # Transparency
    "A9-R6": 15,  # Human Oversight
    "A9-R7": 10,  # Accuracy & Robustness
    "A9-R8":  5,  # Cybersecurity
}

# Пороги Confidence Score → HITL
CONFIDENCE_THRESHOLDS = {
    "HIGH":     (0.90, 1.00),
    "MEDIUM":   (0.61, 0.89),
    "LOW":      (0.31, 0.60),
    "CRITICAL": (0.00, 0.30),
}

# RPL_Factor ниже этого → блокировать ECT-4
RPL_BLOCK_THRESHOLD = 0.70

# CIRI выше этого → WARN
CIRI_WARN_THRESHOLD = 70

# Confidence ниже этого → HITL_REQUIRED
CONFIDENCE_HITL_THRESHOLD = 0.30

# NGI total выше этого → HITL_REQUIRED (default)
NGI_HITL_THRESHOLD = 7


# ─── Датаклассы ───────────────────────────────────────────────────────────────

@dataclass
class Hallucination:
    """Одна обнаруженная галлюцинация (из Claude-классификатора)."""
    type: str            # TYPE-1 … TYPE-7
    severity: str        # CRITICAL | HIGH | MEDIUM | LOW
    description: str
    evidence: str
    rule_violated: Optional[str] = None


@dataclass
class NGIResult:
    """Результат расчёта Narrative Gravity Index."""
    emotional:  int
    political:  int
    archetypal: int
    industry:   int
    total:      int
    level:      str  # LOW | MODERATE | HIGH | CRITICAL


@dataclass
class CIRIResult:
    """Composite Integrity Risk Index."""
    value:             int        # 0–100
    base_risk:         float
    ngi_risk:          float
    hallucination_risk: float
    rpl_risk:          float


@dataclass
class Article9Result:
    """EU AI Act Article 9 compliance."""
    score:  int    # 0–100
    level:  str    # COMPLIANT | PARTIAL | NON_COMPLIANT
    max:    int = 100


@dataclass
class GovernanceDecision:
    """Финальное решение движка."""
    decision:     str             # PASS | WARN | BLOCK | HITL_REQUIRED
    reason:       Optional[str]
    block_source: Optional[str]   # HALLUCINATION_BLOCK_RULE | EU_AI_ACT | NGI_THRESHOLD | LOW_CONFIDENCE | CIRI_THRESHOLD


@dataclass
class GovernanceResult:
    """Полный результат одного прохода через HelixGovernanceMath."""
    confidence_score:  float
    confidence_level:  str
    rpl_factor:        float
    rpl_blocked:       bool
    ngi:               NGIResult
    ciri:              CIRIResult
    article9:          Optional[Article9Result]
    decision:          GovernanceDecision
    hallucinations:    List[Hallucination] = field(default_factory=list)


# ─── Движок ───────────────────────────────────────────────────────────────────

class HelixGovernanceMath:
    """
    Детерминированный математический движок HELIX GOVERNANCE.

    Принимает семантические сигналы от Claude-классификатора,
    возвращает числовые результаты и финальное решение.

    Не вызывает LLM. Не делает HTTP-запросов. Детерминирован.
    """

    # ── 1. RPL Factor ─────────────────────────────────────────────────────────

    def calculate_rpl_factor(
        self,
        required_hours:  float,
        allocated_hours: float,
        penalty_weight:  float = 0.5,
    ) -> float:
        """
        Resource Pressure Level Factor.

        RPL_Factor = 1 − (max(0, Required − Allocated) / Required × Penalty_Weight)

        Если allocated >= required → RPL_Factor = 1.0 (давления нет).
        Если allocated = 0 и required > 0 → RPL_Factor = 1 − penalty_weight.

        Args:
            required_hours:  сколько часов требует задача
            allocated_hours: сколько часов выделено
            penalty_weight:  коэффициент штрафа за дефицит (по умолчанию 0.5)

        Returns:
            float в диапазоне [0.0, 1.0]
        """
        if required_hours <= 0:
            return 1.0
        deficit = max(0.0, required_hours - allocated_hours)
        penalty = (deficit / required_hours) * penalty_weight
        return max(0.0, round(1.0 - penalty, 4))

    def should_block_ect4(
        self,
        rpl_factor: float,
        threshold:  float = RPL_BLOCK_THRESHOLD,
    ) -> bool:
        """
        True если RPL_Factor ниже порога — нельзя присваивать ECT-4.
        Защита от ситуации когда ECT-4 выдаётся при нехватке ресурсов.
        """
        return rpl_factor < threshold

    # ── 2. Confidence Score ───────────────────────────────────────────────────

    def calculate_confidence_score(
        self,
        hallucinations: List[Hallucination],
        rpl_factor:     float = 1.0,
    ) -> float:
        """
        Мультипликативная модель:
        Confidence = 1.0 × Π(1 − weight_i) × rpl_factor

        Каждая галлюцинация независимо снижает уверенность.
        Несколько CRITICAL-галлюцинаций → score близок к 0.

        Returns:
            float в диапазоне [0.0, 1.0]
        """
        score = 1.0
        for h in hallucinations:
            weight = HALLUCINATION_WEIGHTS.get(h.severity, 0.05)
            score *= (1.0 - weight)
        score *= rpl_factor
        return max(0.0, round(score, 4))

    def confidence_level(self, score: float) -> str:
        """HIGH | MEDIUM | LOW | CRITICAL"""
        if score >= 0.90:
            return "HIGH"
        if score >= 0.61:
            return "MEDIUM"
        if score >= 0.31:
            return "LOW"
        return "CRITICAL"

    # ── 3. NGI Score ──────────────────────────────────────────────────────────

    def calculate_ngi_score(
        self,
        emotional:  int,
        political:  int,
        archetypal: int,
        industry:   int,
    ) -> NGIResult:
        """
        Narrative Gravity Index.

        Каждое измерение 0–3, сумма 0–12.
        Claude-классификатор оценивает измерения — не мы.
        Мы только считаем итог и level.

        Args:
            emotional:  давление эмоциональных триггеров (0–3)
            political:  политическая поляризация (0–3)
            archetypal: архетипические нарративы герой/злодей (0–3)
            industry:   отраслевая эхо-камера (0–3)
        """
        dims = {
            "emotional":  max(0, min(3, emotional)),
            "political":  max(0, min(3, political)),
            "archetypal": max(0, min(3, archetypal)),
            "industry":   max(0, min(3, industry)),
        }
        total = sum(dims.values())
        level = "LOW"
        for lvl, (lo, hi) in NGI_THRESHOLDS.items():
            if lo <= total <= hi:
                level = lvl
                break
        return NGIResult(
            emotional=dims["emotional"],
            political=dims["political"],
            archetypal=dims["archetypal"],
            industry=dims["industry"],
            total=total,
            level=level,
        )

    # ── 4. CIRI ───────────────────────────────────────────────────────────────

    def calculate_ciri(
        self,
        confidence_score: float,
        ngi:              NGIResult,
        hallucinations:   List[Hallucination],
        rpl_factor:       float = 1.0,
    ) -> CIRIResult:
        """
        Composite Integrity Risk Index [0–100].

        Формула:
          base_risk           = (1 − confidence) × 50
          ngi_risk            = ngi.total × (20 / 12)
          hallucination_risk  = min(critical×10 + high×5, 20)
          rpl_risk            = (1 − rpl_factor) × 10
          CIRI = min(100, int(sum))
        """
        base_risk          = (1.0 - confidence_score) * 50.0
        ngi_risk           = ngi.total * (20.0 / 12.0)
        critical_count     = sum(1 for h in hallucinations if h.severity == "CRITICAL")
        high_count         = sum(1 for h in hallucinations if h.severity == "HIGH")
        hallucination_risk = min(critical_count * 10 + high_count * 5, 20)
        rpl_risk           = (1.0 - rpl_factor) * 10.0
        raw                = base_risk + ngi_risk + hallucination_risk + rpl_risk
        return CIRIResult(
            value=min(100, int(raw)),
            base_risk=round(base_risk, 2),
            ngi_risk=round(ngi_risk, 2),
            hallucination_risk=round(hallucination_risk, 2),
            rpl_risk=round(rpl_risk, 2),
        )

    # ── 5. Article 9 EU AI Act ────────────────────────────────────────────────

    def calculate_article9_score(
        self,
        requirements_met: Dict[str, bool],
        evidence_counts:  Dict[str, int],
    ) -> Article9Result:
        """
        EU AI Act Article 9 — Risk Management System.

        Для каждого из 8 требований (A9-R1..A9-R8):
          met + evidence >= 3 → полный вес
          met + evidence >= 1 → 70% веса
          not met + evidence >= 1 → 30% веса (частично)
          not met + no evidence → 0

        Итоговый score:
          >= 85 → COMPLIANT
          >= 60 → PARTIAL
          <  60 → NON_COMPLIANT
        """
        score = 0.0
        for req_id, weight in ARTICLE9_WEIGHTS.items():
            met      = requirements_met.get(req_id, False)
            evidence = evidence_counts.get(req_id, 0)
            if met and evidence >= 3:
                score += weight
            elif met and evidence >= 1:
                score += weight * 0.7
            elif not met and evidence >= 1:
                score += weight * 0.3
        score_int = round(score)
        level = (
            "COMPLIANT"     if score_int >= 85 else
            "PARTIAL"       if score_int >= 60 else
            "NON_COMPLIANT"
        )
        return Article9Result(score=score_int, level=level)

    # ── 6. Governance Decision ────────────────────────────────────────────────

    def make_governance_decision(
        self,
        confidence_score: float,
        ciri:             CIRIResult,
        hallucinations:   List[Hallucination],
        ngi:              NGIResult,
        eu_tier:          str,
        block_on_types:   List[str],
        ngi_threshold:    int = NGI_HITL_THRESHOLD,
    ) -> GovernanceDecision:
        """
        Финальное решение. Приоритет строго сверху вниз:

        1. BLOCK если найдена галлюцинация запрещённого типа
        2. BLOCK если EU AI Act tier = unacceptable
        3. HITL_REQUIRED если NGI total >= threshold
        4. HITL_REQUIRED если confidence < 0.30
        5. WARN если CIRI > 70
        6. PASS

        Args:
            block_on_types: типы галлюцинаций которые всегда дают BLOCK
                            (настраивается тенантом через Business Rules)
        """
        # 1. Галлюцинационный BLOCK
        for h in hallucinations:
            if h.type in block_on_types:
                return GovernanceDecision(
                    decision="BLOCK",
                    reason=f"{h.type} {h.severity}: {h.description[:100]}",
                    block_source="HALLUCINATION_BLOCK_RULE",
                )

        # 2. EU AI Act unacceptable
        if eu_tier == "unacceptable":
            return GovernanceDecision(
                decision="BLOCK",
                reason="EU AI Act: unacceptable risk tier",
                block_source="EU_AI_ACT",
            )

        # 3. NGI threshold
        if ngi.total >= ngi_threshold:
            return GovernanceDecision(
                decision="HITL_REQUIRED",
                reason=f"NGI {ngi.level} (total={ngi.total}) ≥ threshold {ngi_threshold}",
                block_source="NGI_THRESHOLD",
            )

        # 4. Low confidence
        if confidence_score < CONFIDENCE_HITL_THRESHOLD:
            return GovernanceDecision(
                decision="HITL_REQUIRED",
                reason=f"Confidence {confidence_score:.4f} < {CONFIDENCE_HITL_THRESHOLD}",
                block_source="LOW_CONFIDENCE",
            )

        # 5. CIRI warn
        if ciri.value > CIRI_WARN_THRESHOLD:
            return GovernanceDecision(
                decision="WARN",
                reason=f"CIRI {ciri.value} > {CIRI_WARN_THRESHOLD}",
                block_source="CIRI_THRESHOLD",
            )

        # 6. Pass
        return GovernanceDecision(decision="PASS", reason=None, block_source=None)

    # ── 7. Полный проход ──────────────────────────────────────────────────────

    def run(
        self,
        hallucinations:   List[Hallucination],
        ngi_dimensions:   Dict[str, int],
        eu_tier:          str,
        block_on_types:   List[str],
        required_hours:   float = 0.0,
        allocated_hours:  float = 0.0,
        requirements_met: Optional[Dict[str, bool]] = None,
        evidence_counts:  Optional[Dict[str, int]] = None,
        ngi_threshold:    int = NGI_HITL_THRESHOLD,
    ) -> GovernanceResult:
        """
        Единая точка входа. Прогоняет весь математический конвейер.

        Args:
            hallucinations:  список Hallucination от Claude-классификатора
            ngi_dimensions:  dict с ключами emotional/political/archetypal/industry (0–3)
            eu_tier:         EU AI Act tier из Claude-классификатора
            block_on_types:  типы которые всегда BLOCK (из Business Rules тенанта)
            required_hours:  для RPL расчёта (0 = давления нет)
            allocated_hours: для RPL расчёта
            requirements_met: для Article 9 (None = пропустить)
            evidence_counts:  для Article 9 (None = пропустить)
            ngi_threshold:   порог NGI для HITL_REQUIRED

        Returns:
            GovernanceResult с полным набором метрик и финальным решением
        """
        rpl = self.calculate_rpl_factor(required_hours, allocated_hours)
        cs  = self.calculate_confidence_score(hallucinations, rpl)
        cl  = self.confidence_level(cs)
        ngi = self.calculate_ngi_score(**{k: ngi_dimensions.get(k, 0)
                                          for k in ("emotional","political","archetypal","industry")})
        ciri = self.calculate_ciri(cs, ngi, hallucinations, rpl)
        a9 = (
            self.calculate_article9_score(requirements_met, evidence_counts)
            if requirements_met is not None
            else None
        )
        decision = self.make_governance_decision(
            confidence_score=cs,
            ciri=ciri,
            hallucinations=hallucinations,
            ngi=ngi,
            eu_tier=eu_tier,
            block_on_types=block_on_types,
            ngi_threshold=ngi_threshold,
        )
        return GovernanceResult(
            confidence_score=cs,
            confidence_level=cl,
            rpl_factor=rpl,
            rpl_blocked=self.should_block_ect4(rpl),
            ngi=ngi,
            ciri=ciri,
            article9=a9,
            decision=decision,
            hallucinations=hallucinations,
        )
