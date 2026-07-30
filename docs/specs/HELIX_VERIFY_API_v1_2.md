# HELIX INTELLIGENCE — API SPECIFICATION
## Product 1: OSINT & Journalism Verifier
### HELIX VERIFY v1.0 — Инженерная спецификация
#### Основа: WPL (Патч 65) · PDE (Патч 58) · CHF-A · ECT · FRCP-GI

---

```
ДОКУМЕНТ:     HELIX_VERIFY_API_v1.0.md
ПРОДУКТ:      HELIX INTELLIGENCE / VERIFY
БЮДЖЕТ:       $50,000
АУДИТОРИЯ:    Backend-инженеры, DevOps, ML-команда
СТЕК:         REST API · JSON · Python/Go · Neo4j · Redis
ОСНОВА HELIX: WPL · PDE · CHF-A · ECT · FRCP-GI · SCA
```

---

## АРХИТЕКТУРА ПРОДУКТА

```
┌─────────────────────────────────────────────────────────────┐
│                  HELIX VERIFY — RUNTIME                      │
│                                                             │
│  INPUT                                                      │
│  transcript / media / claim                                 │
│         ↓                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  CHF-A NLP   │  │  WPL Engine  │  │  PDE Engine  │      │
│  │  Classifier  │  │  (Neo4j)     │  │  (Neo4j)     │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         └─────────────────┴─────────────────┘              │
│                           ↓                                 │
│                   SCORING ENGINE                            │
│              trust_score · ect_level · flags                │
│                           ↓                                 │
│              HITL QUEUE (при escalation)                    │
│                           ↓                                 │
│                       OUTPUT JSON                           │
└─────────────────────────────────────────────────────────────┘
```

---

## ENDPOINT 1: CHF-A EVALUATE
### Оценка коллапса внимания источника

```
POST /api/v1/verify/chf-evaluate

НАЗНАЧЕНИЕ:
  Принимает текстовый корпус (транскрипт показаний, интервью,
  публикацию) и возвращает оценку деградации внимания.
  Реализует алгоритм эскалации CHF-A из HELIX Phase 1.

━━━ REQUEST ━━━

Content-Type: application/json

{
  "source_id":   "string — уникальный ID источника (UUID)",
  "corpus":      "string — текст показаний / транскрипт",
  "source_meta": {
    "type":        "string — enum: witness | journalist | document | media",
    "platform":    "string — enum: direct | social_media | telegram | press",
    "timestamp":   "ISO8601 — время получения показаний",
    "prior_statements": ["array of source_id — предыдущие показания того же источника"]
  },
  "context": {
    "event_timestamp":  "ISO8601 — время события",
    "investigation_id": "string — ID расследования",
    "viral_threshold":  "boolean — превысил ли материал 100k просмотров до интервью"
  }
}

ПРИМЕР:
{
  "source_id": "src-2024-001",
  "corpus": "Я точно помню что видел красный автомобиль...",
  "source_meta": {
    "type": "witness",
    "platform": "direct",
    "timestamp": "2024-11-15T14:30:00Z",
    "prior_statements": []
  },
  "context": {
    "event_timestamp": "2024-11-14T09:00:00Z",
    "investigation_id": "inv-2024-042",
    "viral_threshold": false
  }
}

━━━ RESPONSE 200 ━━━

{
  "source_id": "src-2024-001",
  "investigation_id": "inv-2024-042",
  "chf_a_result": {
    "escalation_level": "string — enum: CLEAR | FLAG | ALERT | ESCALATION | DISQUALIFICATION",
    "active_indicators": [
      {
        "code":        "string — enum: ATT-1 | ATT-2 | ATT-3 | ATT-4 | ATT-5",
        "weight":      "string — enum: LOW | MEDIUM | HIGH",
        "description": "string — описание сработавшего индикатора",
        "evidence":    "string — фрагмент текста, активировавший индикатор"
      }
    ],
    "indicator_counts": {
      "LOW":    "integer",
      "MEDIUM": "integer",
      "HIGH":   "integer"
    },
    "trust_score_ac": "float — скорректированный Trust Score [0.0–1.0]",
    "trust_score_base": "float — базовый Trust Score до коррекции",
    "ac_weight_applied": "float — применённый штраф (0.15 | 0.25 | 0.40)",
    "partial_disqualification": "boolean",
    "disqualified_claims": [
      "string — конкретные утверждения, дисквалифицированные по AC-I-04+AC-I-06"
    ]
  },
  "analyst_directives": [
    "string — конкретные инструкции аналитику"
  ],
  "hitl_required": "boolean",
  "hitl_reason":   "string | null",
  "metadata": {
    "processed_at": "ISO8601",
    "model_version": "chf-a-classifier-v1.0",
    "processing_ms": "integer"
  }
}

ПРИМЕР RESPONSE:
{
  "source_id": "src-2024-001",
  "investigation_id": "inv-2024-042",
  "chf_a_result": {
    "escalation_level": "ALERT",
    "active_indicators": [
      {
        "code": "ATT-2",
        "weight": "HIGH",
        "description": "Shallow retention — источник воспроизводит аффект, не детали",
        "evidence": "«точно помню... что-то красное»"
      },
      {
        "code": "ATT-1",
        "weight": "MEDIUM",
        "description": "Headline-fact divergence — детали события недоступны",
        "evidence": "отсутствуют временны́е метки и имена"
      }
    ],
    "indicator_counts": { "LOW": 0, "MEDIUM": 1, "HIGH": 1 },
    "trust_score_ac": 0.595,
    "trust_score_base": 0.70,
    "ac_weight_applied": 0.15,
    "partial_disqualification": false,
    "disqualified_claims": []
  },
  "analyst_directives": [
    "Перестроить опрос по временны́м якорям",
    "Запросить детали до появления медийного освещения события"
  ],
  "hitl_required": false,
  "hitl_reason": null,
  "metadata": {
    "processed_at": "2024-11-15T14:31:02Z",
    "model_version": "chf-a-classifier-v1.0",
    "processing_ms": 340
  }
}

━━━ ФОРМУЛА РАСЧЁТА trust_score_ac ━━━

  trust_score_ac = trust_score_base × (1 - ac_weight)

  ac_weight:
    0.15  при 1 HIGH индикаторе
    0.25  при 2 HIGH индикаторах
    0.40  при 3+ HIGH индикаторах
    0.00  при отсутствии HIGH (только LOW/MEDIUM)

  Частичная дисквалификация (AC-I-04 + AC-I-06 одновременно):
    trust_score_ac = max(trust_score_base × 0.5, 0.20)

━━━ ЭСКАЛАЦИОННЫЕ ПОРОГИ ━━━

  CLEAR:           0 индикаторов HIGH, < 3 MEDIUM
  FLAG:            1–2 индикатора LOW/MEDIUM
  ALERT:           ≥ 1 HIGH или ≥ 3 MEDIUM в одной категории
                   → hitl_required: false, но analyst_directives заполнены
  ESCALATION:      ≥ 2 HIGH у источника ИЛИ ≥ 1 HIGH у следователя
                   → hitl_required: true
  DISQUALIFICATION:AC-I-04 + AC-I-06 одновременно
                   → hitl_required: true, конкретные claims дисквалифицированы

━━━ ERROR RESPONSES ━━━

400 Bad Request:
{
  "error": "INVALID_INPUT",
  "message": "corpus field required, min 50 characters",
  "field": "corpus"
}

422 Unprocessable:
{
  "error": "NLP_PARSE_FAILED",
  "message": "Unable to extract indicators from corpus",
  "fallback": "manual_review_required"
}

503 Service Unavailable:
{
  "error": "CLASSIFIER_UNAVAILABLE",
  "message": "NLP classifier temporarily offline",
  "retry_after": 30
}
```

---

## ENDPOINT 2: WPL ASSESS
### Оценка провенанса источника

```
POST /api/v1/verify/wpl-assess

НАЗНАЧЕНИЕ:
  Строит граф провенанса источника, рассчитывает Trust Score
  с учётом цепочки передачи, ICoI, coercion_risk и expertise_scope.
  Реализует WPL (Патч 65) + PDE (Патч 58) из GI v6.1.

━━━ REQUEST ━━━

{
  "source_id": "string",
  "provenance_chain": [
    {
      "node_id":    "string — UUID узла",
      "node_type":  "string — enum: primary | relay | document | media",
      "identity": {
        "name":       "string | null — имя или псевдоним",
        "anonymous":  "boolean",
        "verified":   "boolean — верифицирована ли личность"
      },
      "expertise": {
        "domain":     "string — область компетенции",
        "scope":      "string — конкретная область данного утверждения",
        "in_scope":   "boolean — утверждение в пределах экспертизы"
      },
      "transmission": {
        "from_node":  "string | null — UUID предыдущего узла",
        "channel":    "string — enum: direct | document | social | anonymous",
        "timestamp":  "ISO8601",
        "authorized": "boolean — авторизованная передача"
      },
      "risk_flags": {
        "icoi_level":    "string — enum: NONE | LOW | MEDIUM | HIGH | CRITICAL",
        "coercion_risk": "float — [0.0–1.0]",
        "motive":        "string — описание мотива источника"
      }
    }
  ],
  "claim": {
    "text":      "string — верифицируемое утверждение",
    "timestamp": "ISO8601 — время события в утверждении"
  }
}

━━━ RESPONSE 200 ━━━

{
  "source_id": "string",
  "claim_hash": "string — SHA256 от claim.text",
  "wpl_result": {
    "trust_score":      "float — [0.0–1.0]",
    "wpl_status":       "string — enum: CLEAN | PARTIAL | CONTAMINATED | CRITICAL",
    "ect_ceiling":      "integer — максимально возможный ECT [1–4]",
    "relay_count":      "integer — количество узлов передачи",
    "pde_decay_applied":"boolean",
    "pde_decay_factor": "float — суммарный коэффициент деградации",
    "icoi_flags":       ["string — node_id узлов с ICoI"],
    "coercion_flags":   ["string — node_id узлов с coercion_risk > 0.5"],
    "expertise_flags":  ["string — node_id с out-of-scope утверждениями"],
    "unauthorized_relays": ["string — node_id неавторизованных передач"]
  },
  "provenance_graph": {
    "format": "dag",
    "nodes":  [
      {
        "id":     "string",
        "type":   "string",
        "ect":    "integer",
        "status": "string — enum: VERIFIED | DEGRADED | CONTAMINATED | BLOCKED"
      }
    ],
    "edges": [
      {
        "from":     "string",
        "to":       "string",
        "weight":   "float — [0.0–1.0] достоверность передачи",
        "authorized":"boolean"
      }
    ]
  },
  "hitl_required": "boolean",
  "hitl_reason":   "string | null",
  "maltego_export": "boolean — доступен ли экспорт в Maltego-формат"
}

━━━ ФОРМУЛА PDE DECAY ━━━

  Для каждого неавторизованного транзитного узла:
    ect_level = ect_level - 1

  Суммарный decay_factor:
    pde_decay_factor = 1 - (0.15 × unauthorized_relay_count)
    trust_score = trust_score_base × pde_decay_factor

  ECT ceiling правило:
    relay_count ≥ 3 → ect_ceiling = max(ect_ceiling - 1, 1)
    unauthorized relay → ect_ceiling = max(ect_ceiling - 1, 1) за каждый

━━━ WPL STATUS RULES ━━━

  CLEAN:       trust_score ≥ 0.70, icoi = NONE/LOW, coercion_risk < 0.3
  PARTIAL:     trust_score 0.50–0.69 OR icoi = MEDIUM OR coercion_risk 0.3–0.6
  CONTAMINATED:trust_score < 0.50 OR icoi = HIGH OR coercion_risk > 0.6
  CRITICAL:    icoi = CRITICAL OR coercion_risk > 0.85 OR unauthorized_relays ≥ 3
               → hitl_required: true
```

---

## ENDPOINT 3: PDE DECAY
### Расчёт энтропийной деградации провенанса

```
POST /api/v1/verify/pde-decay

НАЗНАЧЕНИЕ:
  Вычисляет деградацию ECT при транзите через цепочку узлов.
  Возвращает функцию apply_pde_decay() в исполняемом виде.
  Используется как sub-call из wpl-assess или самостоятельно.

━━━ REQUEST ━━━

{
  "origin_ect":    "integer — исходный ECT [1–4]",
  "transit_nodes": [
    {
      "node_id":    "string",
      "authorized": "boolean",
      "node_type":  "string — enum: human | document | media | ai"
    }
  ],
  "time_delta_hours": "float — часов от события до получения"
}

━━━ RESPONSE 200 ━━━

{
  "origin_ect":      "integer",
  "final_ect":       "integer — ECT после деградации",
  "decay_steps": [
    {
      "node_id":       "string",
      "ect_before":    "integer",
      "ect_after":     "integer",
      "reason":        "string — причина снижения"
    }
  ],
  "time_decay_applied": "boolean",
  "time_decay_factor":  "float",
  "total_decay":        "float — суммарный коэффициент [0.0–1.0]",
  "final_trust_score":  "float"
}

━━━ АЛГОРИТМ apply_pde_decay ━━━

def apply_pde_decay(origin_ect: int,
                    transit_nodes: list,
                    time_delta_hours: float) -> dict:

    ect = origin_ect
    trust = 1.0
    steps = []

    for node in transit_nodes:
        before = ect
        if not node["authorized"]:
            ect = max(ect - 1, 1)
            trust *= 0.85
            reason = "unauthorized_relay"
        elif node["node_type"] == "ai":
            # AI-транзит: ECT не снижается но trust деградирует
            trust *= 0.90
            reason = "ai_relay_trust_decay"
        else:
            reason = "authorized_relay"

        steps.append({
            "node_id":    node["node_id"],
            "ect_before": before,
            "ect_after":  ect,
            "reason":     reason
        })

    # Временна́я деградация: > 72 часов = -1 ECT для показаний
    time_decay_applied = False
    if time_delta_hours > 72 and origin_ect <= 3:
        ect = max(ect - 1, 1)
        trust *= 0.90
        time_decay_applied = True

    return {
        "origin_ect":         origin_ect,
        "final_ect":          ect,
        "decay_steps":        steps,
        "time_decay_applied": time_decay_applied,
        "time_decay_factor":  round(1 - trust, 3),
        "total_decay":        round(1 - trust, 3),
        "final_trust_score":  round(trust, 3)
    }
```

---

## ENDPOINT 4: TRUST RESTORE
### Восстановление Trust Score через верификацию

```
POST /api/v1/verify/restore-trust

НАЗНАЧЕНИЕ:
  Принимает структурированные ответы источника по временны́м якорям.
  При прохождении валидации накладывает [TRUST_RESTORED] и
  пересчитывает trust_score_ac до базового значения.

━━━ REQUEST ━━━

{
  "source_id":      "string",
  "investigation_id":"string",
  "temporal_anchors": [
    {
      "anchor_id":    "string",
      "timestamp_ref":"ISO8601 — временна́я точка в событии",
      "claim":        "string — утверждение источника",
      "corroboration":{
        "type":       "string — enum: document | witness | physical | digital",
        "reference":  "string — ссылка на корроборирующий источник",
        "ect_level":  "integer"
      }
    }
  ],
  "validation_method": "string — enum: cryptographic | logical | cross_source"
}

━━━ RESPONSE 200 ━━━

{
  "source_id":             "string",
  "restoration_result": {
    "status":              "string — enum: RESTORED | PARTIAL | FAILED",
    "anchors_validated":   "integer",
    "anchors_failed":      "integer",
    "trust_score_before":  "float",
    "trust_score_after":   "float",
    "ect_restored":        "integer | null",
    "marker":              "string — [TRUST_RESTORED] | [PARTIAL_RESTORE] | null"
  },
  "failed_anchors": [
    {
      "anchor_id": "string",
      "reason":    "string"
    }
  ],
  "hitl_required": "boolean"
}

━━━ ЛОГИКА ВОССТАНОВЛЕНИЯ ━━━

  RESTORED:  ≥ 80% якорей валидированы → trust возвращается к base
  PARTIAL:   50–79% якорей → trust = base × 0.80
  FAILED:    < 50% якорей → trust не изменяется, HITL если ≥ 1 HIGH индикатор
```

---

## ENDPOINT 5: PROVENANCE MAP
### Карта провенанса для визуализации

```
GET /api/v1/verify/provenance-map/{investigation_id}

НАЗНАЧЕНИЕ:
  Возвращает полный граф провенанса расследования в форматах
  совместимых с Maltego, Neo4j и стандартными DAG-визуализаторами.

━━━ QUERY PARAMETERS ━━━

  format:   string — enum: json | maltego | neo4j | graphml (default: json)
  ect_filter: integer — показывать только узлы с ECT ≤ N (default: все)

━━━ RESPONSE 200 (format=json) ━━━

{
  "investigation_id": "string",
  "summary": {
    "total_nodes":         "integer",
    "ect4_nodes":          "integer — зелёные (абсолютно достоверные)",
    "ect3_nodes":          "integer — жёлтые",
    "ect2_nodes":          "integer — оранжевые",
    "ect1_nodes":          "integer — красные",
    "blocked_nodes":       "integer — серые (дисквалифицированы)",
    "hitl_pending_nodes":  "integer",
    "overall_trust_score": "float"
  },
  "graph": {
    "nodes": [
      {
        "id":           "string",
        "label":        "string",
        "type":         "string",
        "ect":          "integer",
        "trust_score":  "float",
        "status":       "string — VERIFIED | DEGRADED | CONTAMINATED | BLOCKED | HITL_PENDING",
        "color":        "string — #2ECC71 | #F39C12 | #E67E22 | #E74C3C | #95A5A6",
        "flags":        ["string — активные флаги: CHF-A | ICoI | PDE | coercion"]
      }
    ],
    "edges": [
      {
        "source":     "string",
        "target":     "string",
        "weight":     "float",
        "authorized": "boolean",
        "color":      "string — #2ECC71 (authorized) | #E74C3C (unauthorized)"
      }
    ]
  }
}

━━━ ЦВЕТОВОЕ КОДИРОВАНИЕ ━━━

  ECT-4 (абсолютная достоверность):  #2ECC71  зелёный
  ECT-3 (высокая вероятность):        #F39C12  жёлтый
  ECT-2 (средняя вероятность):        #E67E22  оранжевый
  ECT-1 (низкая достоверность):       #E74C3C  красный
  BLOCKED (дисквалифицирован):        #95A5A6  серый
  HITL_PENDING:                        #9B59B6  фиолетовый
```

---

## ENDPOINT 6: HITL QUEUE
### Управление очередью Human-in-the-Loop

```
GET  /api/v1/verify/hitl-queue
POST /api/v1/verify/hitl-queue/{ticket_id}/resolve

НАЗНАЧЕНИЕ:
  Список тикетов требующих ручного аналитика.
  Интерфейс для аппрува или отклонения факта.

━━━ GET RESPONSE 200 ━━━

{
  "queue": [
    {
      "ticket_id":        "string — UUID",
      "investigation_id": "string",
      "source_id":        "string",
      "created_at":       "ISO8601",
      "priority":         "string — enum: CRITICAL | HIGH | NORMAL",
      "reason":           "string — почему требуется HITL",
      "trigger":          "string — код триггера: ESCALATION | DISQUALIFICATION | WPL_CRITICAL",
      "context": {
        "trust_score_current": "float",
        "ect_current":         "integer",
        "active_flags":        ["string"],
        "claim_preview":       "string — первые 200 символов утверждения"
      }
    }
  ],
  "total":    "integer",
  "pending":  "integer",
  "resolved_today": "integer"
}

━━━ POST RESOLVE REQUEST ━━━

{
  "analyst_id":  "string",
  "decision":    "string — enum: APPROVE | REJECT | ESCALATE",
  "rationale":   "string — обоснование решения",
  "ect_override":"integer | null — переопределение ECT аналитиком",
  "notes":       "string | null"
}

━━━ POST RESOLVE RESPONSE 200 ━━━

{
  "ticket_id":   "string",
  "status":      "RESOLVED",
  "decision":    "string",
  "analyst_id":  "string",
  "resolved_at": "ISO8601",
  "ect_final":   "integer",
  "trust_score_final": "float",
  "oас_log_id":  "string — ID записи в OAS (неизменяемый лог)"
}
```

---

## ENDPOINT 7: SCA MEDIA AUDIT
### Аудит подлинности медиафайлов

```
POST /api/v1/verify/sca-audit

НАЗНАЧЕНИЕ:
  Проверяет медиафайл на признаки синтетического происхождения.
  Реализует SCA (Патч 36) + CHF-E из HELIX.

━━━ REQUEST ━━━

Content-Type: multipart/form-data

Fields:
  file:           binary — медиафайл (image/jpeg, image/png,
                           audio/mp3, video/mp4, application/pdf)
  source_id:      string
  investigation_id: string
  context:        JSON string — {
    "domain":       "string — тема расследования",
    "high_risk":    "boolean — тема высокого риска (политика/война/etc)",
    "chain_of_custody": ["array of node_id — цепочка получения"]
  }

━━━ RESPONSE 200 ━━━

{
  "file_hash":    "string — SHA256",
  "file_type":    "string",
  "sca_result": {
    "synthetic_probability": "float — [0.0–1.0]",
    "chf_e_flags": [
      "string — enum: SYN-1 | SYN-2 | SYN-3 | SYN-4 | SYN-5"
    ],
    "ect_ceiling":  "integer — максимальный ECT для этого медиафайла",
    "verdict":      "string — enum: AUTHENTIC | SUSPICIOUS | SYNTHETIC | UNDETERMINED",
    "pde_chain":    "boolean — нарушена ли цепочка хранения"
  },
  "cached":       "boolean — результат из Redis-кэша",
  "hitl_required":"boolean",
  "processed_at": "ISO8601"
}

━━━ КЭШИРОВАНИЕ ━━━

  Redis key: sca:{file_hash}
  TTL: 86400 секунд (24 часа)
  При повторном запросе с тем же file_hash → cached: true
  Логика: один и тот же файл не проверяется дважды за 24 часа
```

---

## ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ

```
━━━ БАЗА ДАННЫХ ━━━

  Neo4j (граф провенанса):
    Узлы: Source, Claim, Document, MediaFile, Event
    Рёбра: TRANSMITTED_TO, REFERENCES, CORROBORATES, CONTRADICTS
    Индексы: source_id, investigation_id, ect_level, timestamp
    Запрос ECT-деградации: traversal по цепочке TRANSMITTED_TO
      с применением apply_pde_decay() на каждом ребре

  PostgreSQL (основная БД):
    Таблицы: investigations, sources, claims, hitl_queue,
             oas_log, analytics
    HITL Queue: status, priority, assigned_analyst_id
    OAS Log: append-only, no DELETE/UPDATE (SOC2 совместимость)

  Redis (кэш):
    SCA file hashes: TTL 24h
    Trust Score кэш: TTL 1h (инвалидируется при новых данных)
    Session токены: TTL 8h

━━━ NLP КЛАССИФИКАТОР CHF-A ━━━

  Задача: бинарная + мультикласс классификация индикаторов ATT-1..5
  Вход: текст показаний
  Выход: массив {code, weight, evidence}

  Архитектура:
    Base model: fine-tuned BERT/RoBERTa на корпусе показаний
    Классы: [ATT-1, ATT-2, ATT-3, ATT-4, ATT-5, NONE]
    Веса классов: LOW / MEDIUM / HIGH (3-class per indicator)
    Threshold: 0.65 для LOW, 0.75 для MEDIUM, 0.85 для HIGH
    Fallback: при confidence < 0.60 → indicator не активируется

  Данные для обучения:
    Позитивные: показания с задокументированными ATT-паттернами
    Негативные: чистые транскрипты без деградации внимания
    Аугментация: синтетические примеры по каждому ATT-коду

━━━ БЕЗОПАСНОСТЬ ━━━

  Auth:        OAuth2 / JWT (Bearer token)
  Rate limit:  100 req/min per API key (chf-evaluate)
               20 req/min per API key (sca-audit — тяжёлый endpoint)
  Encryption:  TLS 1.3 в транзите, AES-256 в покое
  PII:         source_id — только UUID, имена в зашифрованном поле
  OAS Log:     write-only, cryptographically signed (HMAC-SHA256)
  GDPR/CCPA:   /api/v1/verify/source/{id}/delete (право на удаление)

━━━ ПРОИЗВОДИТЕЛЬНОСТЬ ━━━

  chf-evaluate:    p95 < 500ms (NLP inference)
  wpl-assess:      p95 < 300ms (Neo4j traversal)
  pde-decay:       p95 < 50ms  (детерминированный расчёт)
  sca-audit:       p95 < 2000ms (media analysis)
  provenance-map:  p95 < 800ms (граф + форматирование)

━━━ MALTEGO ИНТЕГРАЦИЯ ━━━

  Формат: Maltego Transform API v4
  Endpoint: GET /api/v1/verify/provenance-map/{id}?format=maltego
  Output: MaltegoMessage XML с Entity типами:
    VerifiedSource (ECT-4) → зелёный
    DegradedSource (ECT-2/3) → оранжевый
    BlockedSource (ECT-1/BLOCKED) → красный
    HITLPending → фиолетовый
```

---

## OAS LOG — СТРУКТУРА НЕИЗМЕНЯЕМОГО ЖУРНАЛА

```
Каждое действие системы логируется в append-only OAS Log.
Используется для HITL-аудита и юридической защиты.

Схема записи:

{
  "log_id":        "UUID",
  "timestamp":     "ISO8601",
  "investigation_id": "string",
  "source_id":     "string | null",
  "action":        "string — enum: CHF_EVALUATE | WPL_ASSESS | PDE_DECAY |
                             TRUST_RESTORE | SCA_AUDIT | HITL_CREATED |
                             HITL_RESOLVED | ECT_OVERRIDE",
  "actor":         "string — system | analyst_id",
  "input_hash":    "string — SHA256 от входных данных",
  "output_hash":   "string — SHA256 от выходных данных",
  "result_summary":{
    "ect_before":  "integer | null",
    "ect_after":   "integer | null",
    "trust_before":"float | null",
    "trust_after": "float | null",
    "flags_added": ["string"],
    "hitl_triggered": "boolean"
  },
  "signature":     "string — HMAC-SHA256(log_id + timestamp + input_hash)"
}

Запрет: DELETE, UPDATE на таблице oas_log.
SOC2 совместимость: все записи immutable + signed.
Retention: минимум 7 лет (настраивается по юрисдикции).
```

---

## DOCKER COMPOSE — МИНИМАЛЬНАЯ КОНФИГУРАЦИЯ

```yaml
version: '3.8'

services:

  api:
    image: helix-verify-api:1.0
    ports:
      - "8080:8080"
    environment:
      - NEO4J_URI=bolt://neo4j:7687
      - POSTGRES_URI=postgresql://postgres:5432/helix_verify
      - REDIS_URI=redis://redis:6379
      - JWT_SECRET=${JWT_SECRET}
      - NLP_MODEL_PATH=/models/chf-a-classifier-v1.0
    depends_on:
      - neo4j
      - postgres
      - redis

  nlp-classifier:
    image: helix-nlp:1.0
    ports:
      - "8081:8081"
    volumes:
      - ./models:/models
    environment:
      - MODEL_NAME=chf-a-classifier-v1.0
      - BATCH_SIZE=32
      - DEVICE=cpu  # gpu для продакшена

  neo4j:
    image: neo4j:5.15
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - neo4j_data:/data
    environment:
      - NEO4J_AUTH=neo4j/${NEO4J_PASSWORD}

  postgres:
    image: postgres:16
    volumes:
      - pg_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=helix_verify
      - POSTGRES_PASSWORD=${PG_PASSWORD}

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  neo4j_data:
  pg_data:
  redis_data:
```

---

## ОБНОВЛЕНИЕ v1.1 — НА ОСНОВЕ ПОЛЬЗОВАТЕЛЬСКОГО ИССЛЕДОВАНИЯ

```
ИСТОЧНИК: Исследование конкурентов и пользователей HELIX (Направление 2)

ГЛАВНЫЙ БАРЬЕР СЕГМЕНТА A (журналист/OSINT):
  «Журналист не может написать в статье "ИИ сказал что это правда".
   Ему требуется 100% прозрачность алгоритмической логики,
   чтобы показать цепочку доказательств юристам редакции
   или правоохранительным органам.»

  Текущий v1.0 имеет provenance-map для визуализации.
  Но нет экспорта в формате пригодном для юридических целей.
  Нет структурированного объяснения почему каждый факт
  получил свой ECT-уровень — с указанием конкретных оснований.

ДОБАВЛЕНО В v1.1:
  Endpoint 8: /verify/legal-export    — юридический пакет
  Endpoint 9: /verify/audit-chain     — цепочка верификации
  Endpoint 10: /verify/explain-ect    — объяснение ECT для нетехника
  Обновление Endpoint 5: формат PDF + юридический язык
  Обновление SAD-терминологии: Strategic Absence of Data (корректно)
```

---

## ENDPOINT 8: LEGAL EXPORT
### Юридический пакет доказательств

```
POST /api/v1/verify/legal-export

НАЗНАЧЕНИЕ:
  Главный ответ на барьер доверия Сегмента A.
  Журналист может показать этот документ:
    — юристам редакции перед публикацией
    — адвокатам при судебном иске
    — правоохранительным органам как цепочка доказательств
    — редактору как обоснование достоверности материала

  Формат: структурированный PDF/JSON с человекочитаемым
  объяснением каждого решения системы.
  Никаких «ИИ сказал» — только верифицируемые шаги.

━━━ REQUEST ━━━

{
  "investigation_id": "string",
  "export_config": {
    "format":          "string — enum: pdf | json | both",
    "language":        "string — enum: ru | en | de | fr (default: ru)",
    "include_sections": {
      "provenance_chain":    "boolean — цепочка передачи каждого источника",
      "ect_rationale":       "boolean — обоснование каждого ECT-уровня",
      "trust_score_history": "boolean — история изменений Trust Score",
      "hitl_decisions":      "boolean — решения аналитиков с обоснованием",
      "methodology_annex":   "boolean — приложение с методологией",
      "non_liquet_log":      "boolean — факты где достоверность не установлена"
    },
    "redaction": {
      "anonymize_sources": "boolean — анонимизировать источники (default: false)",
      "redact_fields":     ["string — поля для редактирования: name | location | date"]
    },
    "legal_jurisdiction": "string — enum: RU | EU | US | UK (влияет на язык правовых формулировок)"
  }
}

━━━ RESPONSE 200 ━━━

{
  "export_id":         "UUID",
  "investigation_id":  "string",
  "generated_at":      "ISO8601",
  "format":            "string",
  "documents": {
    "pdf_url":         "string | null — ссылка на PDF (действительна 48 часов)",
    "json_url":        "string | null — ссылка на JSON"
  },
  "summary": {
    "total_sources":        "integer",
    "ect4_sources":         "integer — абсолютно верифицированные",
    "ect3_sources":         "integer",
    "ect2_sources":         "integer",
    "ect1_sources":         "integer",
    "non_liquet_count":     "integer — факты без установленной достоверности",
    "hitl_decisions_count": "integer",
    "methodology_version":  "string"
  },
  "legal_statement": "string — стандартная преамбула для юридического документа",
  "oас_record_id":   "UUID — запись в криптографическом журнале"
}

━━━ СТРУКТУРА PDF-ДОКУМЕНТА ━━━

  РАЗДЕЛ 1: ПРЕАМБУЛА
    Стандартная юридическая преамбула на языке юрисдикции.
    Пример (RU): «Настоящий документ сформирован автоматизированной
    системой HELIX INTELLIGENCE v1.1 по методологии [URL]. Каждое
    утверждение о достоверности источника основано на верифицируемых
    алгоритмических шагах, задокументированных в OAS Audit Log
    [record_id]. Система не делает выводов за пределами
    доказательной базы (принцип NON LIQUET).»

  РАЗДЕЛ 2: КАРТА ИСТОЧНИКОВ
    Для каждого источника:
      — Идентификатор (анонимный при redaction)
      — ECT-уровень с ТЕКСТОВЫМ обоснованием (не только число)
      — Trust Score с историей изменений
      — Активные флаги (CHF-A, ICoI, PDE) с объяснением на языке нетехника
      — Вывод: «Показания этого источника могут быть использованы
        как [VERIFIABLE FACT | CORROBORATING EVIDENCE |
        BACKGROUND CONTEXT | UNVERIFIED CLAIM]»

  РАЗДЕЛ 3: ЦЕПОЧКА ПРОВЕНАНСА
    Визуализация DAG в формате дерева (текстовый ASCII-формат для PDF).
    Для каждого ребра: авторизованная/неавторизованная передача,
    коэффициент деградации.

  РАЗДЕЛ 4: NON LIQUET РЕЕСТР
    Все факты где система не смогла установить достоверность.
    Честная декларация пределов — ключевое доверие для CAIO и юристов.
    Пример: «Факт X: два верифицированных источника дают
    противоречивые показания. Истина не установлена. Требуется
    дополнительная верификация.»

  РАЗДЕЛ 5: РЕШЕНИЯ АНАЛИТИКОВ (HITL)
    Каждое решение человека-аналитика с timestamp, ID,
    обоснованием и ECT до/после.

  РАЗДЕЛ 6: МЕТОДОЛОГИЧЕСКОЕ ПРИЛОЖЕНИЕ
    Описание ECT шкалы, WPL, CHF-A на языке нетехника.
    Ссылка на публичную методологию.
    «Это приложение позволяет любому независимому эксперту
    воспроизвести и проверить расчёты системы.»

━━━ HUMAN-READABLE ECT LABELS ━━━

  ECT-4: «Абсолютно верифицировано — первичный источник,
          чистая цепочка передачи, независимая корроборация»
  ECT-3: «Высокая вероятность — надёжный источник,
          незначительные пробелы в провенансе»
  ECT-2: «Средняя достоверность — ограниченная верификация,
          использовать только как контекст»
  ECT-1: «Низкая достоверность — не верифицировано,
          не использовать как основание для публикации»

━━━ ERROR: 422 INCOMPLETE INVESTIGATION ━━━

{
  "error":   "EXPORT_INCOMPLETE",
  "message": "Investigation has unresolved HITL tickets. Legal export requires all HITL resolved.",
  "pending_tickets": ["UUID"],
  "override_available": true
}
```

---

## ENDPOINT 9: AUDIT CHAIN
### Полная цепочка верификации — для адвоката

```
GET /api/v1/verify/audit-chain/{investigation_id}

НАЗНАЧЕНИЕ:
  Хронологическая цепочка КАЖДОГО действия системы по расследованию.
  В отличие от OAS Log (технический) — это нарратив:
  «Вот что система делала и почему, шаг за шагом».

  Журналист может передать этот документ адвокату и тот
  увидит: не «ИИ решил», а «система применила правило X
  к факту Y потому что источник Z имел признаки ATT-2».

━━━ RESPONSE 200 ━━━

{
  "investigation_id": "string",
  "chain": [
    {
      "step":          "integer — номер шага",
      "timestamp":     "ISO8601",
      "actor":         "string — system | analyst:{id}",
      "action_type":   "string — SOURCE_ASSESSED | ECT_ASSIGNED | TRUST_UPDATED |
                                  CHF_FLAG_DETECTED | HITL_CREATED | HITL_RESOLVED |
                                  NON_LIQUET | EXPORT_GENERATED",
      "subject":       "string — source_id или claim_id к которому относится шаг",
      "before_state": {
        "ect":         "integer | null",
        "trust_score": "float | null",
        "flags":       ["string"]
      },
      "after_state": {
        "ect":         "integer | null",
        "trust_score": "float | null",
        "flags":       ["string"]
      },
      "rule_applied":  "string — какое правило/протокол применён",
      "plain_language":"string — объяснение на языке нетехника",
      "oас_record_id": "UUID — ссылка на криптографическую запись"
    }
  ],
  "chain_integrity": {
    "verified":        "boolean — SHA-256 цепочка не нарушена",
    "total_steps":     "integer",
    "analyst_steps":   "integer — сколько шагов сделал человек",
    "system_steps":    "integer"
  }
}

━━━ ПРИМЕР ШАГА plain_language ━━━

  action_type: CHF_FLAG_DETECTED
  rule_applied: "CHF-A ATT-2: Shallow Retention"
  plain_language: "Источник src-2024-001 воспроизводил эмоциональный
    тон события (страх, растерянность) но не смог назвать конкретные
    детали: время, имена участников, последовательность событий.
    Это паттерн 'поверхностного удержания' — источник помнит как
    себя чувствовал, но не что именно произошло. Trust Score снижен
    с 0.70 до 0.595. Показания этого источника могут подтверждать
    общий контекст события, но не конкретные факты."
```

---

## ENDPOINT 10: EXPLAIN ECT
### Объяснение ECT-уровня для нетехнического читателя

```
GET /api/v1/verify/explain-ect/{source_id}?investigation_id={id}

НАЗНАЧЕНИЕ:
  Журналист хочет объяснить редактору или юристу:
  «Почему этот источник получил ECT-2, а не ECT-4?»
  Endpoint возвращает пошаговое объяснение на языке нетехника.

━━━ RESPONSE 200 ━━━

{
  "source_id":      "string",
  "ect_current":    "integer",
  "ect_label":      "string — human-readable label",
  "trust_score":    "float",

  "explanation": {
    "headline":     "string — одно предложение для неспециалиста",
    "factors": [
      {
        "factor":       "string — название фактора",
        "impact":       "string — enum: POSITIVE | NEGATIVE | NEUTRAL",
        "description":  "string — что это значит на практике",
        "weight":       "string — MAJOR | MINOR"
      }
    ],
    "what_this_means_for_publication":
      "string — конкретная рекомендация журналисту",
    "what_would_raise_ect":
      "string — что нужно сделать чтобы повысить достоверность"
  },

  "comparable_standard": "string — аналогия из журналистской практики",
  "flags_plain": [
    {
      "flag":        "string — код флага",
      "meaning":     "string — что значит для читателя",
      "actionable":  "string — что делать"
    }
  ]
}

━━━ ПРИМЕР RESPONSE ━━━

{
  "source_id":   "src-2024-001",
  "ect_current": 2,
  "ect_label":   "Средняя достоверность — использовать как контекст",
  "trust_score": 0.52,

  "explanation": {
    "headline": "Источник достоверен как свидетель общей картины,
      но его конкретные утверждения требуют подтверждения.",
    "factors": [
      {
        "factor":      "Анонимность источника",
        "impact":      "NEGATIVE",
        "description": "Личность источника не верифицирована.
          Мы не можем подтвердить что он был на месте события.",
        "weight":      "MAJOR"
      },
      {
        "factor":      "Поверхностное удержание деталей",
        "impact":      "NEGATIVE",
        "description": "Источник помнит эмоции но не конкретные
          факты (время, имена, последовательность).",
        "weight":      "MAJOR"
      },
      {
        "factor":      "Отсутствие давления или конфликта интересов",
        "impact":      "POSITIVE",
        "description": "Нет признаков что источник заинтересован
          в конкретной версии событий.",
        "weight":      "MINOR"
      }
    ],
    "what_this_means_for_publication":
      "Показания этого источника можно использовать для описания
       общей атмосферы или контекста события. Нельзя публиковать
       конкретные факты со ссылкой только на этот источник.",
    "what_would_raise_ect":
      "Найти второй независимый источник подтверждающий ключевые
       детали. Или получить документальное подтверждение (видео,
       документ, физические улики)."
  },

  "comparable_standard":
    "В журналистике это соответствует 'фоновому источнику' —
     ценен для понимания контекста, недостаточен для прямого
     цитирования как факта.",

  "flags_plain": [
    {
      "flag":       "CHF-A ATT-2",
      "meaning":    "Источник помнит эмоции события лучше чем факты",
      "actionable": "Провести повторное интервью с конкретными
                     вопросами о деталях: время, место, имена"
    }
  ]
}
```

---

## ОБНОВЛЕНИЕ ENDPOINT 5: ЮРИДИЧЕСКИЙ ФОРМАТ PDF

```
Добавить к существующему GET /api/v1/verify/provenance-map:

?format=legal_pdf   → PDF с юридической преамбулой
?format=legal_json  → структурированный JSON для адвоката
?jurisdiction=RU|EU|US|UK → язык правовых формулировок

Структура legal_pdf — идентична Endpoint 8 но без
полной SAD-цепочки (только граф + ECT-таблица).
Для полного пакета → использовать Endpoint 8.
```

---

## ИСПРАВЛЕНИЕ: SAD ТЕРМИНОЛОГИЯ

```
ВАЖНО: В HELIX v2.0.1 SAD = Strategic Absence of Data
  Анализ молчания источников — когда отсутствие информации
  само является данными (источник стратегически замолчал).

В предыдущей версии Outreach Package SAD использовался как
«Sequential Action Deconstruction» (для агентных pipeline).
Это НЕВЕРНО для HELIX-архитектуры.

ИСПРАВЛЕНИЕ В ENDPOINT 2 (WPL ASSESS):
  Поле "wpl_status: CONTAMINATED" теперь включает:
  "sad_analysis": {
    "type":    "string — enum: STRATEGIC | TRAUMA | TECHNICAL | VACUUM",
    "signal":  "string — что именно отсутствует",
    "weight":  "float — SAD weight 0.0–2.0 по HELIX Phase 9 SIL"
  }

  SAD-STRATEGIC (источник знает но молчит) → Trust Score −0.15
  SAD-TRAUMA (источник не может говорить) → PDP-X активируется
  SAD-TECHNICAL (данные недоступны технически) → ECT без изменений
  SAD-VACUUM (> 3 тактов молчания) → HITL рекомендован
```

---

## ОБНОВЛЁННЫЕ ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ v1.1

```
НОВЫЕ ЗАВИСИМОСТИ:
  reportlab или weasyprint — генерация PDF (legal-export)
  Только stdlib зависимости — никаких ML-пакетов (урок Guardrails)

НОВЫЕ ENDPOINTS: 8, 9, 10
  legal-export:    p95 < 5000ms (PDF генерация)
  audit-chain:     p95 < 800ms
  explain-ect:     p95 < 500ms

ХРАНЕНИЕ:
  PDF exports: S3-совместимое хранилище, TTL 48 часов
  audit-chain: строится из OAS append-only log (не отдельная таблица)

GDPR/CCPA ДОПОЛНЕНИЕ:
  legal-export с anonymize_sources: true → GDPR-совместимый экспорт
  Имена источников заменяются на Source-[UUID-prefix]
  Все PII поля шифруются или редактируются согласно redact_fields
```

---

*HELIX INTELLIGENCE — API Specification v1.1*
*Product 1: OSINT & Journalism Verifier*
*Endpoints: 10 (было 7) | Stack: REST · Neo4j · PostgreSQL · Redis · NLP*
*Обновление v1.1: Legal Export · Audit Chain · Explain ECT · SAD correction*
*Источник: пользовательское исследование Сегмент A — барьер доверия журналистов*
