# HELIX MARKET v1.0
## Corporate Narrative Risk Audit Engine
### Автономный движок аудита корпоративного нарратива

```
ДОКУМЕНТ:     HELIX_MARKET_v1_0.md
ПРОДУКТ:      HELIX MARKET — отдельный продукт
ВЕРСИЯ:       1.0
ДАТА:         31 мая 2026
СТЕК:         Python 3.11 · FastAPI · PostgreSQL · Neo4j · Redis · GPT-4o API
АУДИТОРИЯ:    Backend-инженеры, архитекторы, ML-команда
ОСНОВА HELIX: ECT · SAP · ICoI · ACH · SAD · CAG · Independence Vector
ПРИНЦИП:      Claude/GPT — только семантика. Python — только числа.
              Это не торговый бот. Это аудит корпоративного нарратива.
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 0 — ИДЕНТИЧНОСТЬ ПРОДУКТА
# ═══════════════════════════════════════

## Что такое HELIX MARKET

HELIX MARKET — движок аудита корпоративного нарратива.

Он не предсказывает цену акций.
Он не даёт рекомендаций покупать или продавать.
Он не является финансовым советником.

Он делает одно: измеряет **Confidence-Accuracy Gap** —
разрыв между тем, что менеджмент уверенно заявляет,
и тем, что реально подтверждается верифицируемыми данными.

## Что он обнаруживает

```
1. Corporate Narrative Markers (CNM) — языковые маркеры риска в тексте
2. SAD Topics — ожидаемые темы отсутствующие в документе
3. ICoI — конфликты интересов каждого источника
4. ACH — конкурирующие гипотезы о реальном состоянии компании
5. CAG — итоговый разрыв между уверенностью и доказательствами
6. Market Risk Index — детерминированный индекс 0–100
```

## Что он НЕ делает

```
— НЕ выдаёт: "купить", "продать", "шортить"
— НЕ предсказывает движение цены
— НЕ является торговым сигналом
— НЕ даёт инвестиционных советов
— НЕ работает как брокер или портфельный менеджер

Каждый вывод содержит:
  "This is not financial advice.
   This is a corporate narrative risk audit."
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 1 — АРХИТЕКТУРА ПРОДУКТА
# ═══════════════════════════════════════

## Runtime схема

```
┌─────────────────────────────────────────────────────────────────┐
│                    HELIX MARKET — RUNTIME                        │
│                                                                  │
│  INPUT                                                           │
│  ticker · document_type · material · period · source_url        │
│         ↓                                                        │
│  ┌──────────────────────────────────────────────────────┐       │
│  │           GPT-4o SEMANTIC EXTRACTOR                   │       │
│  │  CNM Markers · SAD Topics · Claims · ICoI signals    │       │
│  │  OUTPUT: strict JSON — NO SCORES                     │       │
│  └─────────────────────┬────────────────────────────────┘       │
│                         ↓                                        │
│  ┌──────────────────────────────────────────────────────┐       │
│  │           PYTHON HELIX MATH ENGINE                   │       │
│  │  CAG · Market Risk Index · Independence Vector       │       │
│  │  ICoI Risk · Manipulation Risk · SAD Risk            │       │
│  │  DETERMINISTIC — same input = same output always     │       │
│  └─────────────────────┬────────────────────────────────┘       │
│                         ↓                                        │
│  ┌──────────────────────────────────────────────────────┐       │
│  │           REPORT GENERATOR                           │       │
│  │  Market Risk Report A–F · Human-readable + JSON      │       │
│  └─────────────────────┬────────────────────────────────┘       │
│                         ↓                                        │
│              HITL QUEUE (при escalation)                         │
│                         ↓                                        │
│                     OUTPUT JSON + PDF                            │
└─────────────────────────────────────────────────────────────────┘
```

## Файловая структура

```
helix_market/
│
├── main.py                          ← FastAPI точка входа
├── requirements.txt
├── docker-compose.yml
├── .env.example
│
├── api/
│   ├── router.py                    ← POST /api/market/analyze и другие
│   └── middleware.py                ← Auth, rate limit, logging
│
├── classifier/
│   ├── gpt_extractor.py             ← Вызов GPT-4o API
│   ├── classifier_prompt.md         ← Системный промпт GPT-4o
│   └── extractor_types.py           ← Типы данных экстрактора
│
├── engine/
│   ├── math_engine.py               ← Детерминированный расчёт
│   ├── cag_calculator.py            ← CAG отдельным модулем
│   ├── icoi_engine.py               ← ICoI rules
│   ├── sad_engine.py                ← SAD Topic Map
│   └── ach_builder.py               ← ACH Matrix
│
├── report/
│   ├── report_generator.py          ← Отчёт A–F
│   └── pdf_renderer.py              ← PDF экспорт
│
├── models/
│   ├── market_types.py              ← Pydantic модели
│   └── db_models.py                 ← SQLAlchemy модели
│
├── db/
│   ├── postgres.py                  ← PostgreSQL соединение
│   ├── neo4j_client.py              ← Neo4j клиент
│   └── redis_client.py              ← Redis кэш
│
├── hitl/
│   └── hitl_queue.py                ← HITL очередь
│
└── tests/
    ├── test_cag.py
    ├── test_icoi.py
    ├── test_sad.py
    ├── test_classifier_no_scores.py
    ├── test_deterministic.py
    └── test_document_types.py
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 2 — ВХОДНЫЕ ДАННЫЕ
# ═══════════════════════════════════════

## Основной запрос

```json
POST /api/market/analyze

{
  "ticker": "TSLA",
  "document_type": "earnings_call",
  "material": "полный текст документа",
  "period": "Q1 2026",
  "source_url": "https://...",
  "options": {
    "language": "en",
    "track_record_override": null,
    "hitl_threshold": 75
  }
}
```

## Допустимые типы документов

```
earnings_call    — транскрипт звонка с аналитиками
10-k             — годовой отчёт SEC
10-q             — квартальный отчёт SEC
8-k              — материальное событие SEC
press_release    — пресс-релиз компании
ceo_statement    — заявление CEO/CFO
analyst_report   — отчёт аналитика
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 3 — CAG: CONFIDENCE-ACCURACY GAP
# ═══════════════════════════════════════

## Определение

CAG — главная метрика HELIX MARKET.

```
CAG = declared_confidence - evidence_support
CAG ∈ [0.0, 1.0]
```

## Как считается declared_confidence

GPT-4o экстрагирует из текста:
- прогнозы и forward-looking statements
- экстремально позитивный язык
- каузальные атрибуции успеха менеджменту
- уверенные утверждения без числового подтверждения

Python считает взвешенную плотность по секциям:

```python
SECTION_WEIGHTS = {
    "guidance":            1.5,
    "operational_results": 1.2,
    "management_discussion": 1.1,
    "risk_factors":        0.8,
    "safe_harbor":         0.3,
    "legal_boilerplate":   0.2,
}

def compute_declared_confidence(claims: list, section: str) -> float:
    weight = SECTION_WEIGHTS.get(section, 1.0)
    raw = len(claims) / max(1, word_count(section_text))
    return min(1.0, raw * weight * confidence_intensity_factor(claims))
```

## Как считается evidence_support

GPT-4o экстрагирует:
- конкретные числа с источниками
- верифицируемые ссылки на внешние данные
- количественные метрики с периодами
- первичные источники (аудированная отчётность, SEC filings)

Python считает:

```python
def compute_evidence_support(evidence_items: list) -> float:
    score = 0.0
    for item in evidence_items:
        if item.source_type == "audited_financial":
            score += 0.15
        elif item.source_type == "sec_filing":
            score += 0.12
        elif item.source_type == "verified_metric":
            score += 0.10
        elif item.source_type == "management_claim_only":
            score += 0.02
    return min(1.0, score)
```

## Интерпретация CAG

```
0.0–0.19:  LOW      — нарратив в целом подтверждён
0.20–0.39: MODERATE — есть расхождения, рекомендуется проверка
0.40–0.59: HIGH     — значительный разрыв, требуется верификация
0.60–0.79: CRITICAL — нарратив существенно опережает доказательства
0.80–1.0:  HITL     — система останавливается, нужен аналитик
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 4 — CNM: CORPORATE NARRATIVE MARKERS
# ═══════════════════════════════════════

## Семь маркеров корпоративного нарратива

GPT-4o обнаруживает. Python не интерпретирует текст — только считает.

```
CNM-1: PRONOUN_SHIFT
  Определение: смена местоимения при переходе к негативу.
  Шаблон: "I drove this growth" → "We faced headwinds" →
          "The market created challenges"
  Успех персонализируется. Провал деперсонализируется.
  Severity: LOW / MEDIUM / HIGH
  HIGH: в одном абзаце успех = "I", провал = безличный

CNM-2: TEMPORAL_REDIRECT
  Определение: уход от текущих проблем к будущим обещаниям.
  Шаблон: "Yes, this quarter was difficult, but by [future date]..."
  Сигнал: текущее состояние не объясняется, только обещается будущее.
  Связь: H-TYPE-2 (Temporal Drift) из GOVERNANCE
  Severity: по соотношению future_claims / current_evidence

CNM-3: EXTREME_POSITIVITY
  Определение: супerlative язык без числового подтверждения.
  Маркерные слова: "record", "unprecedented", "incredible",
                   "fantastic", "transformative", "revolutionary",
                   "best ever", "рекордный", "беспрецедентный"
  Severity: LOW — одно слово с числом
            MEDIUM — слово без числа
            HIGH — множество без единого числа
  Связь: H-TYPE-3 (Semantic Amplification)

CNM-4: FALSE_CAUSAL_ATTRIBUTION
  Определение: менеджмент приписывает успехи себе, провалы — внешним силам.
  Шаблон успех: "Our strategy delivered 23% growth"
  Шаблон провал: "Macro headwinds impacted our results"
  Тест: если убрать "our strategy" — изменится ли утверждение?
  Severity: HIGH при систематическом паттерне (≥3 случаев)
  Связь: H-TYPE-6 (Causal Bridge)

CNM-5: EVASION_METRIC
  Определение: замена конкретных метрик расплывчатыми формулировками.
  Примеры:
    "significant growth" вместо "X%"
    "within expected range" без указания диапазона
    "strong performance" без сравнительной базы
    "improving trends" без данных
  Severity: HIGH при замене обязательных метрик (guidance, margin)

CNM-6: SELECTIVE_BENCHMARK
  Определение: компания выбирает выгодный бенчмарк для сравнения.
  Паттерны:
    — сравнение с кризисным годом ("better than 2020")
    — выбор слабейших конкурентов
    — нестандартный временной период
    — изменение метрики для сравнения год к году
  Тест: был ли бенчмарк использован в прошлых периодах?
  Severity: MEDIUM по умолчанию, HIGH при изменении метрики

CNM-7: SAD_CORPORATE (Strategic Absence of Data)
  Определение: ожидаемая тема отсутствует в документе данного типа.
  Это не просто "не сказали" — это сигнал что тема намеренно обойдена.
  Примеры:
    — нет обсуждения крупного судебного иска в 10-K
    — нет упоминания конкурента захватившего 15% рынка в earnings call
    — нет обновления guidance после материального события
    — нет ответа на прямой вопрос аналитика (уклонение)
  Severity: по важности отсутствующей темы
  Обрабатывается отдельным SAD Engine
```

## Severity weights для Math Engine

```python
CNM_SEVERITY_WEIGHTS = {
    "LOW":      1,
    "MEDIUM":   3,
    "HIGH":     6,
    "CRITICAL": 10,
}

CNM_TYPE_MULTIPLIERS = {
    "CNM-1": 1.0,   # PRONOUN_SHIFT
    "CNM-2": 1.2,   # TEMPORAL_REDIRECT — чуть серьёзнее
    "CNM-3": 0.9,   # EXTREME_POSITIVITY — часто стиль
    "CNM-4": 1.5,   # FALSE_CAUSAL — серьёзный маркер
    "CNM-5": 1.3,   # EVASION_METRIC — прямое уклонение
    "CNM-6": 1.1,   # SELECTIVE_BENCHMARK
    "CNM-7": 1.8,   # SAD_CORPORATE — молчание = самый сильный сигнал
}
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 5 — DOCUMENT TYPE ENGINE
# ═══════════════════════════════════════

## Ожидаемые темы по типу документа

При отсутствии ожидаемой темы → CNM-7 (SAD_CORPORATE).

```python
EXPECTED_TOPICS = {

    "10-k": [
        "risk_factors",
        "business_description",
        "financial_statements",
        "management_discussion",
        "legal_proceedings",
        "internal_controls",
        "forward_looking_statements",
        "segment_reporting",
    ],

    "10-q": [
        "quarterly_results",
        "liquidity_analysis",
        "material_changes_vs_prior",
        "forward_looking_statements",
        "legal_updates",
        "segment_comparison",
    ],

    "earnings_call": [
        "guidance_update",
        "segment_results",
        "margin_commentary",
        "capex_discussion",
        "q_and_a_responses",
        "headcount_or_hiring",
        "competitive_landscape",
    ],

    "8-k": [
        "material_event_description",
        "effective_date",
        "officer_certification",
        "financial_impact",
    ],

    "press_release": [
        "headline_metric",
        "context_and_comparison",
        "forward_looking_statement",
        "safe_harbor_language",
        "contact_information",
    ],

    "ceo_statement": [
        "current_performance",
        "strategic_direction",
        "acknowledgment_of_challenges",
        "team_or_execution_reference",
    ],

    "analyst_report": [
        "price_target",
        "rating",
        "risk_factors",
        "financial_model_assumptions",
        "conflict_of_interest_disclosure",
    ],
}
```

## SAD Risk weights

```python
SAD_TOPIC_RISK = {
    "risk_factors":              "HIGH",
    "legal_proceedings":         "HIGH",
    "guidance_update":           "HIGH",
    "internal_controls":         "MEDIUM",
    "q_and_a_responses":         "HIGH",    # уклонение от вопроса аналитика
    "conflict_of_interest_disclosure": "CRITICAL",
    "financial_impact":          "HIGH",
    "liquidity_analysis":        "HIGH",
    "segment_results":           "MEDIUM",
    "default":                   "LOW",
}
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 6 — ICoI: КОНФЛИКТ ИНТЕРЕСОВ
# ═══════════════════════════════════════

## Правила ICoI для финансовых источников

```python
ICOI_RULES = {

    "CEO": {
        "icoi_type":   "STRUCTURAL",
        "trust_cap":   0.40,
        "reason":      "Direct financial interest in company performance",
        "track_record_modifier": True,
    },

    "CFO": {
        "icoi_type":   "STRUCTURAL",
        "trust_cap":   0.45,
        "reason":      "Controls financial reporting",
        "track_record_modifier": True,
    },

    "company_pr": {
        "icoi_type":   "STRUCTURAL",
        "trust_cap":   0.30,
        "reason":      "Hired to promote company narrative",
    },

    "sell_side_analyst": {
        "icoi_type":   "HIGH",
        "trust_cap":   0.55,
        "reason":      "Bank has investment banking interest in issuer",
        "independence_check": True,
    },

    "independent_analyst": {
        "icoi_type":   "PARTIAL",
        "trust_cap":   0.75,
        "reason":      "Independence requires SAP-3 verification",
        "independence_check": True,
    },

    "hired_auditor": {
        "icoi_type":   "PARTIAL",
        "trust_cap":   0.65,
        "reason":      "Auditor hired by subject — SDF-2 pattern",
    },

    "rating_agency": {
        "icoi_type":   "PARTIAL",
        "trust_cap":   0.60,
        "reason":      "Issuer-pay model creates structural tension",
    },
}
```

## Track Record Modifier

```python
def apply_track_record_modifier(base_cap: float,
                                 accurate_rate: float | None) -> float:
    """
    Модифицирует trust_cap на основе истории точности прогнозов.
    accurate_rate: доля guidance попавшего в диапазон ±10%.
    None = нет данных → не применяется.
    """
    if accurate_rate is None:
        return base_cap

    if accurate_rate >= 0.80:
        modified = base_cap * 1.2
    elif accurate_rate <= 0.50:
        modified = base_cap * 0.8
    else:
        modified = base_cap

    # Границы: не выше 0.60, не ниже 0.25
    return round(min(0.60, max(0.25, modified)), 2)
```

## Independence Vector

```python
def compute_independence_vector(sources: list) -> float:
    """
    Измеряет насколько источники независимы друг от друга.
    Падает если несколько источников зависят от одного нарратива.
    Нижний порог 0.10 — полного нуля не бывает без доказанной координации.
    """
    if not sources:
        return 1.0

    unique_origins = count_unique_primary_origins(sources)
    cascade_factor = compute_cascade_factor(sources)

    raw = unique_origins / len(sources)
    adjusted = raw * (1 - cascade_factor)

    return round(max(0.10, adjusted), 2)
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 7 — ACH MATRIX
# ═══════════════════════════════════════

## Analysis of Competing Hypotheses

Для каждого документа строится матрица из трёх гипотез минимум:

```python
class ACHMatrix:
    h1:  str   # Гипотеза менеджмента: нарратив точен
    h_null: str  # H-NULL: нарратив не подтверждён или скрывает риск
    alternatives: list[str]  # H2, H3 — альтернативные объяснения
    current_winner: str  # "H1" | "H_NULL" | "NON_LIQUET"
    confidence: float    # 0.0–1.0
    reason: str
    evidence_for_h1: list[str]
    evidence_for_h_null: list[str]
    inconsistent_with_h1: list[str]
```

## Логика определения победителя

```python
def determine_ach_winner(matrix: ACHMatrix,
                          cag_score: float,
                          risk_index: int) -> str:
    """
    Победитель определяется детерминированно на основе метрик.
    """
    # H-NULL побеждает при высоком CAG + высоком риске
    if cag_score >= 0.60 and risk_index >= 65:
        return "H_NULL"

    # NON_LIQUET при недостаточных данных
    if count_verified_claims(matrix) < 3:
        return "NON_LIQUET"

    # H1 при низком CAG и малом количестве маркеров
    if cag_score <= 0.25 and risk_index <= 30:
        return "H1"

    return "NON_LIQUET"
```

## SSD — тест фальсифицируемости (из TRACE)

```python
def ssd_test(claim: str, evidence_items: list) -> dict:
    """
    Тест Поппера: можно ли принципиально опровергнуть утверждение?
    Нефальсифицируемые корпоративные утверждения = флаг.
    """
    patterns_unfalsifiable = [
        "我们相信",  # "мы верим что"
        "we believe",
        "we are confident",
        "positioned for",
        "long-term value",
        "мы уверены что",
        "в долгосрочной перспективе",
    ]
    is_falsifiable = not any(p in claim.lower()
                              for p in patterns_unfalsifiable)
    return {
        "claim": claim,
        "falsifiable": is_falsifiable,
        "flag": "[SSD-UNFALSIFIABLE]" if not is_falsifiable else None
    }
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 8 — MATH ENGINE
# ═══════════════════════════════════════

## Market Risk Index

```python
def compute_market_risk_index(
    extractor_output: ExtractorOutput,
    icoi_results: list[ICoIResult],
    sad_results: list[SADResult],
    independence_vector: float,
) -> RiskBreakdown:
    """
    Детерминированный расчёт.
    GPT-4o не вызывается. Только чистая математика.
    """

    # BASE RISK: из ECT уровней утверждений
    base_risk = compute_base_risk(extractor_output.claims)
    # 0–20: ECT-1 × 3pts, ECT-2 × 1pt, ECT-4 × -1pt, max 20

    # ICoI RISK: из типов конфликта интересов
    icoi_risk = compute_icoi_risk(icoi_results)
    # STRUCTURAL = 20, HIGH = 14, PARTIAL = 8, NONE = 0; max 20

    # MANIPULATION RISK: из CNM маркеров
    manipulation_risk = compute_manipulation_risk(
        extractor_output.cnm_markers
    )
    # sum(severity_weight × type_multiplier); clamp 0–25

    # SAD RISK: из отсутствующих ожидаемых тем
    sad_risk = compute_sad_risk(sad_results)
    # HIGH_missing × 6 + MEDIUM_missing × 3 + LOW_missing × 1; max 20

    # INDEPENDENCE RISK: из Independence Vector
    independence_risk = round((1 - independence_vector) * 15)
    # 0–15

    total = (base_risk + icoi_risk + manipulation_risk
             + sad_risk + independence_risk)
    total = min(100, max(0, total))

    return RiskBreakdown(
        base_risk=base_risk,
        icoi_risk=icoi_risk,
        manipulation_risk=manipulation_risk,
        sad_risk=sad_risk,
        independence_risk=independence_risk,
        total=total,
        risk_level=get_risk_level(total),
    )
```

## Risk Level пороги

```python
def get_risk_level(index: int) -> str:
    if index >= 90: return "HITL_REQUIRED"
    if index >= 75: return "CRITICAL"
    if index >= 50: return "HIGH"
    if index >= 25: return "MODERATE"
    return "LOW"
```

## Детерминизм — обязательное требование

```python
# ТЕСТ: один и тот же ExtractorOutput
# при 100 запусках даёт идентичный Market Risk Index.
# Это гарантируется отсутствием любого random/стохастического кода
# в Math Engine. GPT-4o вызывается ТОЛЬКО на этапе экстракции.
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 9 — HITL ПРОТОКОЛ
# ═══════════════════════════════════════

## HITL_REQUIRED — система останавливается

```
Триггеры:
  — Market Risk Index ≥ 90
  — CAG ≥ 0.80
  — SAD_CORPORATE CRITICAL × 2 или больше
  — ICoI STRUCTURAL + Independence Vector < 0.15
  — Прямое уклонение от вопроса аналитика в earnings call

Действие:
  → Отчёт помечается HITL_REQUIRED
  → Задача добавляется в HITL Queue
  → Результат НЕ публикуется без подтверждения аналитика
  → Клиент получает: "Analysis requires human review.
                      Contact your analyst."
```

## HITL_ADVISORY — продолжаем, предупреждаем

```
Триггеры:
  — Market Risk Index 65–89
  — CAG 0.60–0.79
  — Track Record менеджмента неизвестен при STRUCTURAL ICoI
  — Первый анализ компании (нет исторической базы)

Действие:
  → Отчёт публикуется с флагом [HITL_ADVISORY]
  → В Required Actions: конкретные шаги верификации
  → Клиент видит: "External verification strongly recommended."
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 10 — СТРУКТУРА ВЫХОДНОГО ОТЧЁТА
# ═══════════════════════════════════════

```
═══════════════════════════════════════════
HELIX MARKET — CORPORATE NARRATIVE RISK AUDIT
Ticker: [TICKER] · Document: [TYPE] · Period: [PERIOD]
Analysis ID: [UUID] · Date: [TIMESTAMP]
═══════════════════════════════════════════

РАЗДЕЛ A: EXECUTIVE SUMMARY
────────────────────────────
[2–3 предложения: что это за документ, главный вывод]

MARKET RISK INDEX:  [0–100] — [LOW/MODERATE/HIGH/CRITICAL/HITL_REQUIRED]
CAG SCORE:          [0.0–1.0]
INDEPENDENCE:       [0.0–1.0]
HITL STATUS:        [REQUIRED / ADVISORY / CLEAR]

РАЗДЕЛ B: CORPORATE NARRATIVE MAP
────────────────────────────────────
Для каждого маркера:
  QUOTE:       "[точная цитата из документа]"
  MARKER:      CNM-N · [тип]
  SEVERITY:    LOW / MEDIUM / HIGH / CRITICAL
  DIAGNOSIS:   [что именно делает этот маркер проблематичным]
  VERIFY:      [что конкретно нужно проверить]

CAG BREAKDOWN:
  Declared confidence: [0.0–1.0]  ([N] confident claims)
  Evidence support:    [0.0–1.0]  ([N] verified items)
  Gap:                 [0.0–1.0]

РАЗДЕЛ C: ICoI AUDIT
──────────────────────
Для каждого источника/спикера:
  ACTOR:       [CEO / CFO / Analyst / Company]
  ICoI TYPE:   [STRUCTURAL / HIGH / PARTIAL / NONE]
  TRUST CAP:   [0.00–1.00]
  REASON:      [основание]
  MODIFIER:    [track record если доступен]

INDEPENDENCE VECTOR: [0.0–1.0]
[объяснение если низкий]

РАЗДЕЛ D: ACH MATRIX
──────────────────────
H1:     [нарратив менеджмента точен]
H-NULL: [нарратив не подтверждён / скрывает риск]
H2:     [альтернативное объяснение если есть]

CURRENT WINNER: [H1 / H-NULL / NON_LIQUET]
REASON:         [детерминированное обоснование]

SSD FLAGS: [нефальсифицируемые утверждения если есть]

РАЗДЕЛ E: SAD TOPIC MAP
─────────────────────────
Для каждой отсутствующей ожидаемой темы:
  MISSING TOPIC:  [название]
  EXPECTED:       [почему ожидалась в этом типе документа]
  RISK:           LOW / MEDIUM / HIGH / CRITICAL
  ACTION:         [что нужно запросить у компании]

РАЗДЕЛ F: RISK INDEX BREAKDOWN + REQUIRED ACTIONS
────────────────────────────────────────────────────
BASE RISK:          [0–20]  | [объяснение]
ICoI RISK:          [0–20]  | [объяснение]
MANIPULATION RISK:  [0–25]  | [объяснение]
SAD RISK:           [0–20]  | [объяснение]
INDEPENDENCE RISK:  [0–15]  | [объяснение]
──────────────────────────────────────────
MARKET RISK INDEX:  [0–100] — [LEVEL]

REQUIRED ACTIONS:
  [конкретные шаги верификации — каждый с приоритетом]

HITL TASKS (если есть):
  [что требует человека-аналитика и почему]

─────────────────────────────────────────────────────
DISCLAIMER: This is not financial advice.
This is a corporate narrative risk audit.
HELIX MARKET identifies narrative risk, not price direction.
─────────────────────────────────────────────────────
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 11 — API ENDPOINTS
# ═══════════════════════════════════════

## Endpoint 1: Analyze

```
POST /api/market/analyze

Входные данные: AnalyzeRequest
Выходные данные: MarketRiskReport
Время ответа: p95 < 8000ms (GPT-4o latency included)
Auth: Bearer JWT
Rate limit: 10 req/min per API key
```

## Endpoint 2: Report Export

```
GET /api/market/report/{analysis_id}?format=json|pdf|markdown

Выходные данные: MarketRiskReport в выбранном формате
Auth: Bearer JWT
```

## Endpoint 3: HITL Queue

```
GET  /api/market/hitl/queue          — список задач
POST /api/market/hitl/{id}/resolve   — решение аналитика
```

## Endpoint 4: History

```
GET /api/market/history/{ticker}     — история анализов по тикеру
```

## Endpoint 5: Health

```
GET /api/market/health
→ {"status": "ok", "gpt_api": "ok", "db": "ok", "version": "1.0"}
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 12 — БАЗА ДАННЫХ
# ═══════════════════════════════════════

## PostgreSQL

```sql
-- Анализы
CREATE TABLE market_analyses (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ticker          VARCHAR(10) NOT NULL,
    document_type   VARCHAR(50) NOT NULL,
    period          VARCHAR(20),
    source_url      TEXT,
    material_hash   VARCHAR(64) NOT NULL,   -- SHA256 входного текста
    risk_index      INTEGER NOT NULL,
    risk_level      VARCHAR(20) NOT NULL,
    cag_score       NUMERIC(4,3) NOT NULL,
    independence_v  NUMERIC(4,3) NOT NULL,
    hitl_required   BOOLEAN DEFAULT FALSE,
    hitl_resolved   BOOLEAN DEFAULT FALSE,
    report_json     JSONB NOT NULL,
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    created_by      UUID REFERENCES users(id)
);

-- HITL очередь
CREATE TABLE hitl_queue (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    analysis_id     UUID REFERENCES market_analyses(id),
    trigger_reason  TEXT NOT NULL,
    status          VARCHAR(20) DEFAULT 'PENDING',
    assigned_to     UUID REFERENCES users(id),
    resolved_at     TIMESTAMPTZ,
    resolution_note TEXT,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- OAS Log — append only
CREATE TABLE oas_log (
    id              BIGSERIAL PRIMARY KEY,
    analysis_id     UUID,
    event_type      VARCHAR(50) NOT NULL,
    event_data      JSONB NOT NULL,
    hmac_signature  VARCHAR(64) NOT NULL,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);
-- ЗАПРЕЩЕНО: DELETE, UPDATE на oas_log
```

## Neo4j — граф ICoI

```cypher
// Узлы
(:Company {ticker, name})
(:Person {role, trust_cap, icoi_type})
(:Analyst {firm, independence_score})
(:Statement {text, cnm_markers, ect_level})

// Рёбра
(:Person)-[:MADE_STATEMENT]->(:Statement)
(:Person)-[:EMPLOYED_BY]->(:Company)
(:Analyst)-[:COVERS]->(:Company)
(:Analyst)-[:WORKS_FOR]->(:Bank)
(:Bank)-[:HAS_DEAL_WITH]->(:Company)
// Если Bank HAS_DEAL_WITH Company → Analyst ICoI HIGH автоматически
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 13 — DOCKER COMPOSE
# ═══════════════════════════════════════

```yaml
version: '3.8'

services:

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - NEO4J_URI=bolt://neo4j:7687
      - POSTGRES_URI=postgresql://postgres:5432/helix_market
      - REDIS_URI=redis://redis:6379
      - JWT_SECRET=${JWT_SECRET}
      - ENVIRONMENT=production
    depends_on:
      - postgres
      - neo4j
      - redis
    restart: unless-stopped

  postgres:
    image: postgres:16-alpine
    volumes:
      - pg_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=helix_market
      - POSTGRES_USER=helix
      - POSTGRES_PASSWORD=${PG_PASSWORD}

  neo4j:
    image: neo4j:5.15-community
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - neo4j_data:/data
    environment:
      - NEO4J_AUTH=neo4j/${NEO4J_PASSWORD}

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes

volumes:
  pg_data:
  neo4j_data:
  redis_data:
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 14 — ТЕСТЫ
# ═══════════════════════════════════════

```python
# test_cag.py
def test_high_cag_when_many_claims_no_evidence():
    """Много уверенных утверждений без доказательств → CAG > 0.6"""

def test_low_cag_when_evidence_matches_claims():
    """Конкретные числа + источники → CAG < 0.3"""

def test_section_weight_applied():
    """Guidance section weighted 1.5x vs safe_harbor 0.3x"""

# test_icoi.py
def test_ceo_gets_structural_icoi():
    """CEO statement → ICoI STRUCTURAL, trust_cap 0.40"""

def test_track_record_raises_cap():
    """accurate_rate=0.85 → trust_cap = base × 1.2, max 0.60"""

def test_independent_analyst_gets_partial():
    """No bank affiliation → ICoI PARTIAL, trust_cap 0.75"""

# test_sad.py
def test_missing_risk_factors_in_10k():
    """10-K без risk_factors → SAD_CORPORATE HIGH"""

def test_missing_qa_in_earnings_call():
    """earnings_call без q_and_a_responses → SAD_CORPORATE HIGH"""

# test_classifier_no_scores.py
def test_gpt_output_has_no_numeric_scores():
    """GPT-4o output не содержит market_risk_index, cag_score, risk_level"""
    output = call_gpt_extractor(sample_earnings_call)
    assert "market_risk_index" not in output
    assert "cag_score" not in output
    assert "risk_level" not in output

# test_deterministic.py
def test_math_engine_is_deterministic():
    """100 запусков с одним input = идентичный risk_index"""
    results = [compute_market_risk_index(fixed_input) for _ in range(100)]
    assert len(set(r.total for r in results)) == 1
```

---

# ═══════════════════════════════════════
# РАЗДЕЛ 15 — CHANGELOG
# ═══════════════════════════════════════

```
v1.0 — 31 мая 2026
  Создан как отдельный продукт. Не часть MR_HELIX.
  Стек: Python 3.11 · FastAPI · GPT-4o · PostgreSQL · Neo4j · Redis.
  CAG: Confidence-Accuracy Gap с section weights.
  CNM: 7 корпоративных нарративных маркеров.
  Document Type Engine: 7 типов, expected topics per type.
  ICoI Financial: 7 типов источников с track_record_modifier.
  Independence Vector: нижний порог 0.10.
  ACH Matrix + SSD тест Поппера.
  Math Engine: детерминированный, 5 компонентов, 0–100.
  HITL: REQUIRED и ADVISORY с чёткими триггерами.
  Отчёт: A–F sections.
  БД: PostgreSQL + Neo4j граф ICoI.
  5 групп тестов.
```
