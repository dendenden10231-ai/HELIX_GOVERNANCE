"""
engine/claude_classifier.py
============================
HELIX Module 2b — Claude Classifier Client.

Вызывает Anthropic API с system prompt из HELIX_GOVERNANCE_v1_3_FINAL.md
РАЗДЕЛ 16, получает семантические сигналы (галлюцинации, NGI, EU AI Act),
возвращает как JSON-строку для governance_service.parse_classifier_response().

Этот файл делает реальный сетевой вызов — не тестируется в песочнице
без доступа в сеть. Логика парсинга уже покрыта тестами в
test_governance_service.py на фиктивных (mock) ответах классификатора.

Требует переменную окружения ANTHROPIC_API_KEY (Railway → Variables).
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional

try:
    import anthropic
except ImportError:
    anthropic = None  # type: ignore


# ─── System prompt — дословно из РАЗДЕЛ 16 спецификации ────────────────────
# Источник: HELIX_GOVERNANCE_v1_3_FINAL.md
# НЕ редактировать вручную — при изменении спецификации обновлять отсюда.

GOVERNANCE_CLASSIFIER_SYSTEM_PROMPT = """Ты — HELIX Governance Classifier.
Твоя задача: анализировать AI-вывод и возвращать ТОЛЬКО JSON.
Никаких пояснений. Никакого prose. Только валидный JSON.

ВХОДНЫЕ ДАННЫЕ:
- ai_output: текст сгенерированный AI-системой
- business_rules: список правил бизнес-политики тенанта
- context_type: customer_facing | internal | regulatory | agent_action
- eu_ai_act_tier: minimal_risk | limited_risk | high_risk | unacceptable

ТВОЯ ЗАДАЧА — извлечь семантические сигналы:

1. HALLUCINATIONS: найти признаки 7 типов (TYPE-1..TYPE-7).
   Возвращать ТОЛЬКО текстовые метки и фрагменты — НЕ числа.
   Математику (severity weights, confidence) считает Python движок.

2. NGI DIMENSIONS: оценить 4 измерения по шкале 0-3.
   Это ЕДИНСТВЕННЫЕ числа которые ты возвращаешь.
   Обоснование — текстом, без формул.

3. EU_AI_ACT: классифицировать риск по EU AI Act.
   Вернуть только tier enum и list нарушений текстом.

4. BUSINESS_RULES_CHECK: проверить соответствие правилам тенанта.
   Вернуть ID нарушенных правил если есть.

ОБЯЗАТЕЛЬНЫЙ ФОРМАТ ОТВЕТА:
{
  "hallucinations": [
    {
      "type":           "TYPE-1 | TYPE-2 | TYPE-3 | TYPE-4 | TYPE-5 | TYPE-6 | TYPE-7",
      "severity_signal": "CRITICAL | HIGH | MEDIUM | LOW",
      "description":    "string — что именно нарушено",
      "evidence":       "string — точная цитата из текста",
      "rule_violated":  "string | null — ID правила из business_rules"
    }
  ],
  "ngi_dimensions": {
    "emotional":   0,
    "political":   0,
    "archetypal":  0,
    "industry":    0,
    "explanation": "string — почему такие оценки"
  },
  "eu_ai_act_signals": {
    "risk_tier":  "minimal_risk | limited_risk | high_risk | unacceptable",
    "violations": ["string"]
  },
  "business_rule_violations": ["string — rule_id"]
}

ВАЖНО:
- Не включай числа confidence, scores, weights — это Python движок
- Не включай governance_decision — это Python движок
- Если галлюцинаций нет — "hallucinations": []
- severity_signal — только твоя семантическая оценка, не финальный weight"""


class ClaudeClassifierClient:
    """
    Тонкая обёртка над Anthropic API для HELIX Governance Classifier.

    Не содержит бизнес-логики — только формирует запрос и возвращает
    сырой текст ответа. Парсинг и валидация — в governance_service.py.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-6"):
        if anthropic is None:
            raise ImportError(
                "Пакет 'anthropic' не установлен. "
                "Добавьте 'anthropic' в requirements.txt и pip install."
            )
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))
        self.model = model

    def classify(
        self,
        ai_output: str,
        business_rules: Optional[List[Dict[str, Any]]] = None,
        context_type: str = "internal",
        eu_ai_act_tier_hint: str = "minimal_risk",
        max_tokens: int = 2000,
    ) -> str:
        """
        Вызывает классификатор. Возвращает сырую строку ответа
        (JSON, возможно с markdown fences — парсинг делает вызывающая сторона).
        """
        user_payload = json.dumps({
            "ai_output": ai_output,
            "business_rules": business_rules or [],
            "context_type": context_type,
            "eu_ai_act_tier": eu_ai_act_tier_hint,
        }, ensure_ascii=False)

        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=GOVERNANCE_CLASSIFIER_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_payload}],
        )

        return "".join(
            block.text for block in response.content if hasattr(block, "text")
        )
