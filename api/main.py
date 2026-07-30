"""
api/main.py
===========
HELIX Module 3 — FastAPI сервис.

Первый реальный HTTP-эндпоинт: POST /governance/analyze
Собирает воедино: claude_classifier → governance_service → GICore/OAS.

Запуск локально:
    uvicorn api.main:app --reload --port 8000

Запуск на Railway:
    задаётся через Procfile (см. корень репозитория)
    обязательная переменная окружения: ANTHROPIC_API_KEY
"""

from __future__ import annotations

import os
import uuid
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from engine.gi_core import GICore
from engine.governance_service import (
    GovernanceService,
    GovernanceRequest,
    ClassifierResponseError,
)
from engine.claude_classifier import ClaudeClassifierClient

app = FastAPI(
    title="HELIX GOVERNANCE API",
    version="1.3",
    description="Детерминированный аудит AI-вывода. GI v6.2 + GOVERNANCE v1.3.",
)

# Один GICore-инстанс на процесс — OAS журнал накапливается за время жизни
# процесса (как и заявлено в архитектуре: investigation state внутри рантайма).
# TODO Railway: при масштабировании на несколько инстансов OAS нужно вынести
# в PostgreSQL (см. HELIX_Runtime_Spec) — это единая точка не переживёт рестарт.
_gi_core = GICore(investigation_id=f"HELIX-GOV-{uuid.uuid4().hex[:8]}")
_service = GovernanceService(gi_core=_gi_core)

_classifier: Optional[ClaudeClassifierClient] = None


def get_classifier() -> ClaudeClassifierClient:
    """Ленивая инициализация — чтобы приложение стартовало даже без ключа
    (например для /health), и падало только при реальном вызове /analyze."""
    global _classifier
    if _classifier is None:
        _classifier = ClaudeClassifierClient()
    return _classifier


# ─── Pydantic-схемы запроса/ответа ────────────────────────────────────────

class BusinessRule(BaseModel):
    rule_id:    str
    description: str


class GovernanceAnalyzeRequest(BaseModel):
    ai_output:       str = Field(..., description="Текст AI-вывода для аудита")
    business_rules:  List[BusinessRule] = Field(default_factory=list)
    context_type:    str = Field(
        default="internal",
        description="customer_facing | internal | regulatory | agent_action",
    )
    eu_ai_act_tier_hint: str = Field(default="minimal_risk")
    block_on_types:  List[str] = Field(default_factory=lambda: ["TYPE-1", "TYPE-7"])
    tenant_id:       Optional[str] = None
    required_hours:  float = 0.0
    allocated_hours: float = 0.0


class GovernanceAnalyzeResponse(BaseModel):
    decision:           str
    decision_reason:    Optional[str]
    block_source:       Optional[str]
    confidence_score:   float
    confidence_level:   str
    rpl_factor:          float
    rpl_blocked_ect4:    bool
    ngi:                Dict[str, Any]
    ciri:               Dict[str, Any]
    hallucinations:     List[Dict[str, Any]]
    eu_ai_act_violations: List[str]
    business_rule_violations: List[str]
    oas_record_id:      Optional[str]
    context_type:       str


# ─── Endpoints ──────────────────────────────────────────────────────────────

@app.get("/health")
def health() -> Dict[str, str]:
    """Проверка живости сервиса — не требует ANTHROPIC_API_KEY."""
    return {
        "status": "ok",
        "service": "HELIX GOVERNANCE",
        "version": "1.3",
        "investigation_id": _gi_core.investigation_id,
        "oas_records_this_session": str(len(_gi_core.oas.records)),
    }


@app.post("/governance/analyze", response_model=GovernanceAnalyzeResponse)
def analyze(req: GovernanceAnalyzeRequest) -> GovernanceAnalyzeResponse:
    """
    Полный governance-аудит одного AI-вывода.

    1. Отправляет ai_output в Claude-классификатор (РАЗДЕЛ 16 промпт)
    2. Парсит и валидирует JSON-контракт
    3. Прогоняет через детерминированную математику (Module 0)
    4. Логирует решение в OAS (Module 1)
    5. Возвращает структурированный вердикт
    """
    try:
        classifier = get_classifier()
    except ImportError as e:
        raise HTTPException(status_code=500, detail=str(e))

    try:
        raw = classifier.classify(
            ai_output=req.ai_output,
            business_rules=[r.model_dump() for r in req.business_rules],
            context_type=req.context_type,
            eu_ai_act_tier_hint=req.eu_ai_act_tier_hint,
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Ошибка вызова классификатора: {e}")

    governance_request = GovernanceRequest(
        ai_output=req.ai_output,
        business_rules=[r.model_dump() for r in req.business_rules],
        context_type=req.context_type,
        eu_ai_act_tier_hint=req.eu_ai_act_tier_hint,
        block_on_types=req.block_on_types,
        tenant_id=req.tenant_id,
        required_hours=req.required_hours,
        allocated_hours=req.allocated_hours,
    )

    try:
        result = _service.evaluate(governance_request, raw)
    except ClassifierResponseError as e:
        # Классификатор нарушил контракт — это ошибка нашей системы
        # (промпт/модель), не ошибка пользователя. 502, не 400.
        raise HTTPException(status_code=502, detail=f"Классификатор нарушил контракт: {e}")

    return GovernanceAnalyzeResponse(**_service.to_api_response(result))


@app.get("/governance/oas/summary")
def oas_summary() -> Dict[str, Any]:
    """Сводка журнала аудита за время жизни процесса (Module 1, P56)."""
    return _gi_core.oas.summary()
