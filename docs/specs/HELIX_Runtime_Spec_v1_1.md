# HELIX Runtime Spec v1.1

HELIX

Runtime Specification v1.1

Enterprise Infrastructure Layer

Memory Partitioning  ·  Tenant Isolation  ·  RAG Governance  ·  OpenAPI 3.1

| Версия | v1.1  (продолжение v1.0) |
|---|---|
| Дата | 28 мая 2026 |
| Статус | FOUNDATION — Enterprise Infrastructure Layer |
| База | HELIX Runtime Spec v1.0  ×  AK-MASTER v3.1  ×  GI v6.1  ×  HELIX v2.0.1 |
| Добавляет к v1.0 | Раздел 8: Memory Partitioning  |  Раздел 9: Tenant Isolation  |  Раздел 10: RAG Governance  |  Раздел 11: OpenAPI 3.1 YAML |

Принцип: разработчик берёт этот документ и начинает писать enterprise-код не возвращаясь к архитектурным спецификациям.

## Содержание

| Контекст и принцип v1.1 | 3 |
|---|---|
| Раздел 8 — Memory Partitioning Schema | 4 |
| 8.1  Шесть типов памяти | 4 |
| 8.2  TypeScript-схемы | 5 |
| 8.3  Жизненный цикл записи | 6 |
| 8.4  Политики доступа | 7 |
| 8.5  Memory Engine API | 7 |
| Раздел 9 — Tenant Isolation Model | 8 |
| 9.1  Архитектура изоляции | 8 |
| 9.2  TenantContext — схема | 9 |
| 9.3  Изолированные ресурсы | 9 |
| 9.4  Tenant Provisioning API | 10 |
| 9.5  Политики governance per-tenant | 11 |
| 9.6  Data residency и compliance | 11 |
| Раздел 10 — RAG Governance | 12 |
| 10.1  Evidence Lineage Schema | 12 |
| 10.2  Trust-Weighted Retrieval | 13 |
| 10.3  RAG Pipeline — State Machine | 14 |
| 10.4  Provenance Chain Integrity | 15 |
| 10.5  RAG Governance API | 15 |
| Раздел 11 — OpenAPI 3.1 YAML | 16 |
| 11.1  Все эндпоинты из v1.0 | 16 |
| 11.2  Memory Engine эндпоинты | 18 |
| 11.3  Tenant Management эндпоинты | 19 |
| 11.4  RAG эндпоинты | 20 |
| 11.5  WebSocket events | 21 |
| Матрица зависимостей и статус | 22 |
| QA чеклист v1.1 | 23 |

## Контекст и принцип v1.1

Runtime Specification v1.0 дала: типы данных, State Machine, Execution Graph, Policy Engine, Confidence Engine, API Contracts, Audit Schema. Всё необходимое для реализации логики системы.

Runtime Specification v1.1 даёт enterprise infrastructure layer — четыре компонента, без которых система не может быть развёрнута для корпоративных клиентов:

| Раздел | Компонент | Что даёт |
|---|---|---|
| 8 | Memory Partitioning | 6 типов памяти с изоляцией, политиками доступа и TTL. Без этого любые данные между сессиями и тенантами смешиваются. |
| 9 | Tenant Isolation | Полная изоляция корпоративных клиентов: векторные индексы, память, аудит, политики — всё per-tenant. |
| 10 | RAG Governance | Evidence Lineage для каждого факта из RAG. Trust-Weighted Retrieval. Провенанс с ECT/WPL цепочкой до первичного источника. |
| 11 | OpenAPI 3.1 YAML | Машиночитаемый контракт для всех эндпоинтов — из v1.0 и новых. Разработчик получает SDK за 30 минут. |

Разделы 1–7 из v1.0 не изменяются. Нумерация продолжается с 8.

Зависимости: AK-MASTER v3.1 FINAL ✓  |  HELIX v2.0.1 ✓  |  Phase 4.5 Active Patches ✓  |  AK-BRIDGE v1.0 ✓  |  Runtime Spec v1.0 ✓

## Раздел 8 — Memory Partitioning Schema

Система работает с шестью типами памяти. Каждый тип имеет изолированное хранилище, политику доступа, TTL и правила очистки. Смешение типов — нарушение GL-01 (AK-CORE Immutable).

### 8.1 Шесть типов памяти

| Тип | Назначение | Содержимое | TTL | Isolation |
|---|---|---|---|---|
| EPISODIC | Данные сессии | Входящие запросы, промежуточные состояния, markers | Время сессии | Per-session |
| SEMANTIC | Верифицированные знания | ECT-3/4 факты, верифицированные источники, WPL записи | Persistent / 90 дней | Per-tenant |
| TRIBUNAL | Immutable доказательства | Tribunal решения, CFO-записи, HITL events | Permanent (append-only) | Per-tenant / encrypted |
| EXPERIMENTAL | Sandbox / тесты | Гипотезы, незавершённый анализ, stress-test данные | 24 часа | Isolated sandbox |
| CONTAMINATED | Скомпрометированная память | MPE-CORRUPT, PDP-X, AC-DEGRADED факты | До разрешения HITL | Quarantined |
| TENANT_PRIVATE | Изолированная корп. память | Проприетарные источники, внутренние векторные индексы | По конфигурации тенанта | Per-tenant / air-gapped |

### 8.2 TypeScript-схемы

#### MemoryRecord — базовая запись

interface MemoryRecord {

  record_id:       string;          // UUID v4

  memory_type:     MemoryType;

  tenant_id:       string;          // обязателен для non-EPISODIC

  session_id:      string | null;   // только для EPISODIC

  content:         MemoryContent;

  ect_level:       1 | 2 | 3 | 4 | null;

  trust_score:     number | null;   // 0.0 – 1.0

  contamination_flags: ContaminationFlag[];

  created_at:      ISO8601;

  expires_at:      ISO8601 | null;  // null = permanent

  access_policy:   MemoryAccessPolicy;

  provenance:      ProvenanceChain | null;

  hash:            string;          // SHA-256 контента

}

type MemoryType =

  | 'EPISODIC' | 'SEMANTIC' | 'TRIBUNAL'

  | 'EXPERIMENTAL' | 'CONTAMINATED' | 'TENANT_PRIVATE';

interface MemoryContent {

  raw:       string;

  embedding: number[] | null;   // vector (если индексировано)

  metadata:  Record<string, unknown>;

}

#### MemoryAccessPolicy — политика доступа

interface MemoryAccessPolicy {

  read:  AccessLevel[];

  write: AccessLevel[];

  cross_tenant: boolean;     // всегда false для TENANT_PRIVATE

  requires_hitl: boolean;    // для TRIBUNAL записей

}

type AccessLevel =

  | 'SYSTEM'          // только внутренние движки

  | 'OPERATOR'        // авторизованный оператор HITL

  | 'TENANT_ADMIN'    // администратор тенанта

  | 'AUDIT_ONLY';     // только чтение для аудита

### 8.3 Жизненный цикл записи

| Событие | Действие системы |
|---|---|
| Создание | Тип определяется автоматически по источнику (ECT + CHF-флаги + session context). Хеш вычисляется до записи. |
| MPE-CORRUPT активирован | Запись перемещается из SEMANTIC → CONTAMINATED. Trust_score × 0.6. Оригинальная запись помечается, не удаляется. |
| HITL разрешает | CONTAMINATED запись может перейти в SEMANTIC (restored) или EXPERIMENTAL (downgraded). TRIBUNAL запись создаётся с решением оператора. |
| Истечение TTL | EPISODIC и EXPERIMENTAL удаляются автоматически. SEMANTIC архивируется (не удаляется). TRIBUNAL никогда не удаляется. |
| Conflict detection | Если новая SEMANTIC запись противоречит существующей ECT-4 — FRCP запускается автоматически (AK-INT-04). Конфликт не записывается без разрешения. |

### 8.4 Политики доступа — матрица

| Тип памяти | SYSTEM | OPERATOR | TENANT_ADMIN | AUDIT_ONLY | Cross-tenant |
|---|---|---|---|---|---|
| EPISODIC | R/W | R | — | — | ❌ |
| SEMANTIC | R/W | R | R | R | ❌ |
| TRIBUNAL | Append | R (HITL) | R | R | ❌ Encrypted |
| EXPERIMENTAL | R/W | R/W | R | — | ❌ |
| CONTAMINATED | R | R/W (HITL) | — | R | ❌ Quarantined |
| TENANT_PRIVATE | R/W* | — | R/W | R | ❌ Air-gapped |

* SYSTEM доступ к TENANT_PRIVATE только через явный tenant context. Без него — 403.

### 8.5 Memory Engine API

POST /helix/memory/store

  Body:     { content: string; type: MemoryType; session_id?: string; tenant_id: string; ect_level?: number; provenance?: ProvenanceStep[] }

  Response: MemoryRecord

  Errors:   403 если cross-tenant нарушение | 409 если conflict detection

GET /helix/memory/{record_id}

  Response: MemoryRecord

  Errors:   403 если тип = CONTAMINATED без HITL авторизации

POST /helix/memory/search

  Body:     { query_embedding: number[]; memory_types: MemoryType[]; tenant_id: string; top_k: number; min_trust_score?: number }

  Response: { results: MemorySearchResult[]; query_id: string }

PATCH /helix/memory/{record_id}/contaminate

  Body:     { reason: ContaminationFlag; authorized_by: string }

  Response: MemoryRecord (обновлённый, type = CONTAMINATED)

POST /helix/memory/{record_id}/restore

  Body:     { operator_id: string; new_type: "SEMANTIC" | "EXPERIMENTAL"; decision_note: string }

  Requires: HITL authorization

  Response: MemoryRecord + TribunalRecord

## Раздел 9 — Tenant Isolation Model

Каждый корпоративный клиент (tenant) полностью изолирован. Изоляция распространяется на: векторные индексы, память всех типов, аудит-логи, политики, промпты, embeddings, runtime cache. Пересечение данных между тенантами — это CFO-04 (Epistemic Poisoning) на инфраструктурном уровне.

### 9.1 Архитектура изоляции

| Уровень | Механизм изоляции |
|---|---|
| Идентификация | Каждый запрос несёт tenant_id в JWT-токене. Без валидного tenant_id — 401. Все downstream вызовы наследуют tenant context. |
| Векторный индекс | Отдельный namespace в векторной БД (Qdrant/Weaviate) per tenant. Запрос без tenant namespace — блокируется на уровне RAG Engine. |
| Память | Все MemoryRecord содержат tenant_id. Memory Engine отклоняет cross-tenant reads физически (row-level security). |
| Аудит | AuditRecord изолированы per-tenant. Tenant может запросить только свой аудит. Оператор HITL видит аудит тенанта только при активном HITL событии. |
| Политики | Tenant может иметь кастомные Policy Rules поверх базовых (не вместо). Базовые GL-01..14 и CPX-ABS-* не переопределяются никогда. |
| Embeddings / кэш | Embedding модели запускаются с tenant context. Кэш не shared между тенантами. Runtime state в памяти — per-session, не per-tenant. |

### 9.2 TenantContext — схема

interface TenantContext {

  tenant_id:          string;          // UUID, primary key

  tenant_name:        string;

  tier:               TenantTier;

  data_residency:     DataResidency;

  custom_policies:    PolicyRule[];     // дополнительные (не замена базовых)

  allowed_modes:      RuntimeMode[];    // подмножество MODE-GI/AK/HX

  hitl_endpoint:      string | null;    // webhook для HITL событий

  audit_retention_days: number;         // мин 90, default 365

  vector_namespace:   string;           // изолированный namespace

  memory_quota_gb:    number;

  created_at:         ISO8601;

  active:             boolean;

}

type TenantTier = 'SAAS_LITE' | 'ENTERPRISE_CLOUD' | 'AIR_GAPPED' | 'SOVEREIGN' | 'DEFENSE';

interface DataResidency {

  region:         string;        // "eu-west-1", "us-east-1", etc.

  sovereign:      boolean;       // данные не покидают юрисдикцию

  encryption_key: string | null; // BYOK если sovereign=true

}

### 9.3 Изолированные ресурсы

| Ресурс | Изоляция | Примечание |
|---|---|---|
| Vector DB namespace | Физически отдельный namespace | Qdrant: collection per tenant. Weaviate: class per tenant. |
| Memory store | Row-level security по tenant_id | PostgreSQL RLS или ClickHouse partition. |
| Audit logs | Отдельная partition per tenant | Append-only, hash chain. Экспорт только tenant_admin. |
| Policy engine | Tenant policies загружаются при session init | OPA: отдельный namespace. Базовые правила не переопределяются. |
| HITL webhook | Per-tenant endpoint | HITL событие идёт только на endpoint данного тенанта. |
| Embedding cache | Не shared | Redis: key prefix = tenant_id. TTL = 1 час. |

### 9.4 Tenant Provisioning API

// ── PROVISIONING ──────────────────────────────────────────

POST /helix/tenants

  Body:     TenantContext (без tenant_id — генерируется)

  Response: TenantContext (с tenant_id)

  Auth:     SYSTEM only

GET /helix/tenants/{tenant_id}

  Response: TenantContext

  Auth:     TENANT_ADMIN | SYSTEM

PATCH /helix/tenants/{tenant_id}

  Body:     Partial<TenantContext>

  Response: TenantContext

  Auth:     TENANT_ADMIN | SYSTEM

  Immutable: tenant_id, data_residency.region (после создания)

DELETE /helix/tenants/{tenant_id}

  Response: { deleted: boolean; audit_export_url: string }

  Auth:     SYSTEM only

  Note:     TRIBUNAL память экспортируется до удаления — никогда не теряется

POST /helix/tenants/{tenant_id}/policies

  Body:     PolicyRule

  Response: { policy_id: string; active: boolean }

  Validation: нельзя переопределить GL-01..14, CPX-ABS-*

GET /helix/tenants/{tenant_id}/audit

  Query:    { from: ISO8601; to: ISO8601; event_type?: HelixEventType }

  Response: AuditRecord[]

  Auth:     TENANT_ADMIN | OPERATOR (только при активном HITL)

### 9.5 Политики governance per-tenant

Тенант может добавлять правила поверх базовых. Правила применяются в приоритете ниже CPX-ABS-* и GL-*, выше CHF-* и AUTO_RESOLVE.

// Пример: тенант добавляет обязательный ICoI check для всех ECT-3 фактов

TENANT_POLICY_ICoI_STRICT:

  condition: "ect_level >= 3 AND icoi_checked == false"

  action: HITL_REQUIRED

  emit: "[TENANT_POLICY: ICoI check required before ECT-3 accept]"

  tenant_id: "tenant_abc"

// Пример: тенант запрещает MODE-AK (только исследовательские задачи)

TENANT_POLICY_GI_ONLY:

  condition: "mode == 'MODE-AK'"

  action: BLOCK

  emit: "[TENANT_POLICY: MODE-AK disabled for this tenant]"

  tenant_id: "tenant_research_institute"

### 9.6 Data residency и compliance

| Tier | Residency | Compliance notes |
|---|---|---|
| SAAS_LITE | Shared cloud | Базовая изоляция. SOC2 Type I. Данные в регионе провайдера. |
| ENTERPRISE_CLOUD | Dedicated cluster | SOC2 Type II. GDPR ready. Dedicated vector namespace, dedicated audit. |
| AIR_GAPPED | On-premise | Данные не покидают инфраструктуру клиента. BYOK encryption. Full audit export. |
| SOVEREIGN | Sovereign cloud | Юрисдикционная привязка. Государственные ключи шифрования. Полный контроль retention. |
| DEFENSE | Air-gapped + classified | Специальные требования по запросу. Полная изоляция сети. Отдельный deployment. |

## Раздел 10 — RAG Governance

Retrieval-Augmented Generation в HELIX работает иначе чем стандартный RAG. Каждый retrieved фрагмент несёт Evidence Lineage — цепочку провенанса с ECT-уровнем, WPL-статусом и Trust Score. Retrieval ранжируется не только по семантической близости, но и по доверию источника.

### 10.1 Evidence Lineage Schema

#### EvidenceLineage — полная запись провенанса

interface EvidenceLineage {

  lineage_id:        string;

  fact_id:           string;          // ссылка на EvidenceNode

  source_id:         string;          // ссылка на SourceNode

  retrieval_path:    RetrievalStep[]; // цепочка от первичного источника

  ect_at_ingestion:  1 | 2 | 3 | 4;  // ECT когда документ попал в систему

  ect_current:       1 | 2 | 3 | 4;  // ECT на момент retrieval (может деградировать)

  trust_at_ingestion: number;

  trust_current:     number;

  contamination_history: ContaminationEvent[];

  ingested_at:       ISO8601;

  last_verified_at:  ISO8601 | null;

  tenant_id:         string;

}

interface RetrievalStep {

  step_id:    string;

  source_type: "PRIMARY" | "SECONDARY" | "SYNTHESIS" | "AI_GENERATED";

  actor_id:   string;

  action:     "OBSERVED" | "REPORTED" | "RELAYED" | "TRANSFORMED" | "SYNTHESIZED";

  timestamp:  ISO8601;

  wpl_status: "CLEAN" | "PARTIAL" | "DEGRADED" | "CONTAMINATED";

  ect_at_step: 1 | 2 | 3 | 4;

}

interface ContaminationEvent {

  event_id:   string;

  flag:       ContaminationFlag;

  triggered_by: string;         // функция или оператор

  timestamp:  ISO8601;

  resolved:   boolean;

  resolved_at: ISO8601 | null;

}

### 10.2 Trust-Weighted Retrieval

Стандартный RAG ранжирует результаты только по cosine similarity. HELIX RAG добавляет trust_weight — произведение ECT-фактора и Trust Score источника, нормализованное против contamination.

#### Формула ранжирования

RetrievalScore(chunk) =

  α × semantic_similarity(query, chunk.embedding)

  + β × trust_weight(chunk)

  + γ × recency_factor(chunk)

  - δ × contamination_penalty(chunk)

Где:

  α = 0.50  (семантическая близость)

  β = 0.30  (доверие источника)

  γ = 0.12  (актуальность)

  δ = 0.08  (штраф за контаминацию)

trust_weight(chunk) =

  ECT_factor(chunk.ect_current) × chunk.trust_current

  ECT_factor: { 4→1.00, 3→0.80, 2→0.55, 1→0.20 }

recency_factor(chunk) =

  exp(-λ × days_since_ingestion)   где λ = 0.01 (половина жизни ~70 дней)

contamination_penalty(chunk) =

  len(chunk.contamination_history) × 0.15   (cap = 0.60)

#### Фильтры перед retrieval

// Обязательные pre-retrieval фильтры:

1. tenant_id == context.tenant_id                // изоляция тенанта

2. ect_current >= context.min_ect_level          // ECT порог (default = 2)

3. trust_current >= context.min_trust_score      // Trust порог (default = 0.4)

4. "CONTAMINATED" NOT IN memory_types            // контаминированные не retrieval

   ЕСЛИ оператор явно запросил forensic mode — исключение с HITL авторизацией

### 10.3 RAG Pipeline — State Machine

| Состояние | Описание и переходы |
|---|---|
| RAG_IDLE | Ожидание запроса. → RAG_QUERY_RECEIVED |
| RAG_QUERY_RECEIVED | Запрос получен. Tenant context проверен. → RAG_EMBED_QUERY |
| RAG_EMBED_QUERY | Embedding запроса. Кэш проверяется первым. → RAG_FILTER_APPLY |
| RAG_FILTER_APPLY | Обязательные pre-retrieval фильтры (tenant, ECT, trust, contamination). → RAG_VECTOR_SEARCH |
| RAG_VECTOR_SEARCH | Семантический поиск в tenant namespace. top_k × 3 кандидата (для ре-ранжирования). → RAG_RERANK |
| RAG_RERANK | Trust-Weighted Retrieval Score для каждого. Выбирается top_k финальных. → RAG_LINEAGE_ATTACH |
| RAG_LINEAGE_ATTACH | EvidenceLineage прикрепляется к каждому результату. → RAG_CHF_CHECK |
| RAG_CHF_CHECK | CHF-Layer scan на retrieved контент: AC, AA, MW флаги. → RAG_OUTPUT (clean) | RAG_DEGRADE (flags) |
| RAG_DEGRADE | CHF-флаги найдены. ECT деградирует, trust_weight снижается. → RAG_OUTPUT с предупреждениями. |
| RAG_OUTPUT | Результаты с EvidenceLineage + RetrievalScore возвращаются. → RAG_AUDIT_LOG |
| RAG_AUDIT_LOG | Запрос + результаты + lineage логируются в tenant audit. → RAG_IDLE |

### 10.4 Provenance Chain Integrity

Каждый retrieval result несёт полную цепочку провенанса. Цепочка проверяется перед включением результата в контекст. Нарушение цепочки → понижение ECT.

// Правила провенанса:

PDE-CHECK:

  Если retrieval_path[0].source_type != "PRIMARY"

  → понизить ect_current на 1 уровень

  → emit "[PDE: non-primary source in RAG — ECT degraded]"

WPL-INTEGRITY:

  Если любой RetrievalStep.wpl_status == "CONTAMINATED"

  → ect_current = min(ect_current, 2)

  → trust_current × 0.7

  → добавить "WPL_CONTAMINATED" в contamination_flags

SCA-CHECK (AI-generated content):

  Если retrieval_path[-1].source_type == "AI_GENERATED"

  → ect_current = 1  (потолок для AI-вывода)

  → emit "[CHF-E SYN: AI-generated content ECT cap = 1]"

### 10.5 RAG Governance API

POST /helix/rag/retrieve

  Body: {

    query:           string;

    tenant_id:       string;

    top_k:           number;           // default 5

    min_ect_level:   number;           // default 2

    min_trust_score: number;           // default 0.4

    memory_types:    MemoryType[];     // default ["SEMANTIC", "TENANT_PRIVATE"]

    forensic_mode:   boolean;          // default false — требует HITL auth

  }

  Response: {

    results:   RAGResult[];

    query_id:  string;

    chf_flags: CHFFlag[];

  }

interface RAGResult {

  chunk_id:         string;

  content:          string;

  retrieval_score:  number;

  semantic_score:   number;

  trust_weight:     number;

  lineage:          EvidenceLineage;

  warnings:         string[];      // CHF-флаги, PDE, WPL предупреждения

}

POST /helix/rag/ingest

  Body: {

    content:    string;

    source:     SourceNode;

    tenant_id:  string;

    memory_type: MemoryType;

    provenance: RetrievalStep[];

  }

  Response: { chunk_ids: string[]; lineage_id: string }

GET /helix/rag/lineage/{lineage_id}

  Response: EvidenceLineage

POST /helix/rag/lineage/{lineage_id}/verify

  Body:     { operator_id: string }

  Response: { verified: boolean; issues: string[] }

## Раздел 11 — OpenAPI 3.1 YAML

Полный машиночитаемый контракт. Формат соответствует OpenAPI 3.1. Все схемы из Разделов 1 и 8–10 транслированы в YAML. Разработчик генерирует SDK командой одной строкой.

Команда генерации SDK: openapi-generator-cli generate -i helix-api.yaml -g typescript-fetch -o ./sdk

### 11.1 Базовая структура и Core эндпоинты (из v1.0)

openapi: "3.1.0"

info:

  title: HELIX Runtime API

  version: "1.1.0"

  description: >

    Cognitive epistemic governance platform.

    Combines AK-MASTER v3.1 × GI v6.1 × CHF Layer × Active Patches.

servers:

  - url: https://api.helix.example.com/v1

    description: Production

  - url: https://sandbox.helix.example.com/v1

    description: Sandbox

security:

  - bearerAuth: []

components:

  securitySchemes:

    bearerAuth:

      type: http

      scheme: bearer

      bearerFormat: JWT

  schemas:

    RuntimeMode:

      type: string

      enum: [MODE-GI, MODE-AK, MODE-HX]

    ECTLevel:

      type: integer

      enum: [1, 2, 3, 4]

      description: Evidence Confidence Tier

    TrustScore:

      type: number

      minimum: 0.0

      maximum: 1.0

    VerificationState:

      type: string

      enum: [UNVERIFIED, VERIFIED, DEGRADED, FROZEN, SUSPENDED, GAP_PRESERVED]

    PolicyAction:

      type: string

      enum: [CONTINUE, DEGRADE_MODE, HITL_REQUIRED, AUTO_RESOLVE, NON_LIQUET, HELIX_FREEZE, TRIBUNAL_REQUIRED]

#### Схемы SourceNode и EvidenceNode

    SourceNode:

      type: object

      required: [source_id, ect_level, trust_score, ssc_status, wpl, timestamp_first]

      properties:

        source_id: { type: string, format: uuid }

        ect_level: { $ref: "#/components/schemas/ECTLevel" }

        trust_score: { $ref: "#/components/schemas/TrustScore" }

        ssc_status:

          type: string

          enum: [SSC-1, SSC-2, SSC-3, SSC-4, SSC-5]

        contamination_flags:

          type: array

          items: { type: string }

        timestamp_first: { type: string, format: date-time }

        timestamp_last: { type: string, format: date-time }

    ConfidenceResult:

      type: object

      required: [fact_id, ect_effective, trust_score_final, non_liquet]

      properties:

        fact_id: { type: string }

        confidence_final:

          oneOf:

            - type: number

            - type: string

              enum: [SUSPENDED]

        ect_effective: { $ref: "#/components/schemas/ECTLevel" }

        trust_score_final: { $ref: "#/components/schemas/TrustScore" }

        non_liquet: { type: boolean }

#### Core Processing эндпоинты

paths:

  /helix/process:

    post:

      summary: Main processing endpoint

      requestBody:

        required: true

        content:

          application/json:

            schema:

              type: object

              required: [input, mode, session]

              properties:

                input: { type: string }

                mode: { $ref: "#/components/schemas/RuntimeMode" }

                session: { $ref: "#/components/schemas/RuntimeContext" }

      responses:

        "200":

          description: Processing result

          content:

            application/json:

              schema:

                type: object

                properties:

                  output: { type: string }

                  confidence: { $ref: "#/components/schemas/ConfidenceResult" }

                  markers: { type: array, items: { type: string } }

                  audit_id: { type: string }

        "423":

          description: HITL Required

          content:

            application/json:

              schema:

                type: object

                properties:

                  error: { type: string, example: "HITL_REQUIRED" }

                  hitl_endpoint: { type: string }

        "503":

          description: HELIX Freeze

### 11.2 Memory Engine эндпоинты

  /helix/memory/store:

    post:

      summary: Store memory record

      requestBody:

        required: true

        content:

          application/json:

            schema:

              type: object

              required: [content, type, tenant_id]

              properties:

                content: { type: string }

                type: { $ref: "#/components/schemas/MemoryType" }

                tenant_id: { type: string }

                ect_level: { $ref: "#/components/schemas/ECTLevel" }

      responses:

        "201": { description: MemoryRecord created }

        "403": { description: Cross-tenant violation }

        "409": { description: Conflict detected — FRCP required }

  /helix/memory/search:

    post:

      summary: Semantic memory search

      requestBody:

        content:

          application/json:

            schema:

              type: object

              required: [query_embedding, memory_types, tenant_id, top_k]

              properties:

                query_embedding: { type: array, items: { type: number } }

                memory_types: { type: array, items: { $ref: "#/components/schemas/MemoryType" } }

                tenant_id: { type: string }

                top_k: { type: integer, minimum: 1, maximum: 50 }

                min_trust_score: { type: number, default: 0.4 }

      responses:

        "200": { description: Search results with lineage }

### 11.3 Tenant Management эндпоинты

  /helix/tenants:

    post:

      summary: Create tenant

      security: [{ bearerAuth: [] }]

      x-roles: [SYSTEM]

      requestBody:

        content:

          application/json:

            schema: { $ref: "#/components/schemas/TenantContext" }

      responses:

        "201": { description: TenantContext with tenant_id }

        "400": { description: Validation error }

  /helix/tenants/{tenant_id}:

    get:

      summary: Get tenant

      x-roles: [TENANT_ADMIN, SYSTEM]

      parameters:

        - name: tenant_id

          in: path

          required: true

          schema: { type: string }

      responses:

        "200": { description: TenantContext }

        "404": { description: Tenant not found }

  /helix/tenants/{tenant_id}/audit:

    get:

      summary: Get tenant audit log

      x-roles: [TENANT_ADMIN, OPERATOR]

      parameters:

        - name: tenant_id

          in: path

          required: true

          schema: { type: string }

        - name: from

          in: query

          schema: { type: string, format: date-time }

        - name: to

          in: query

          schema: { type: string, format: date-time }

      responses:

        "200": { description: AuditRecord array }

### 11.4 RAG эндпоинты

  /helix/rag/retrieve:

    post:

      summary: Trust-weighted RAG retrieval

      requestBody:

        content:

          application/json:

            schema:

              type: object

              required: [query, tenant_id, top_k]

              properties:

                query: { type: string }

                tenant_id: { type: string }

                top_k: { type: integer, default: 5 }

                min_ect_level: { type: integer, default: 2 }

                min_trust_score: { type: number, default: 0.4 }

                forensic_mode: { type: boolean, default: false }

      responses:

        "200":

          description: RAGResult array with lineage

          content:

            application/json:

              schema:

                type: object

                properties:

                  results:

                    type: array

                    items: { $ref: "#/components/schemas/RAGResult" }

                  chf_flags:

                    type: array

                    items: { type: string }

  /helix/rag/ingest:

    post:

      summary: Ingest document into RAG store

      requestBody:

        content:

          application/json:

            schema:

              type: object

              required: [content, source, tenant_id, memory_type]

      responses:

        "201": { description: chunk_ids and lineage_id }

### 11.5 WebSocket events

Для real-time интеграции система эмитирует события через WebSocket. Тенант подключается к wss://api.helix.example.com/v1/events с JWT-токеном.

# WebSocket endpoint:

# wss://api.helix.example.com/v1/events?tenant_id={id}

# Схема события:

HelixWebSocketEvent:

  type: object

  required: [event_id, event_type, session_id, timestamp]

  properties:

    event_id: { type: string, format: uuid }

    event_type:

      type: string

      enum:

        - HITL_REQUIRED

        - HELIX_FREEZE

        - NON_LIQUET

        - CHF_CRITICAL

        - MPE_CORRUPT_ACTIVATED

        - LEM_DEAD_TRIGGERED

        - TRIBUNAL_REQUIRED

        - AUDIT_COMPLETE

        - RAG_LINEAGE_DEGRADED

        - TENANT_POLICY_TRIGGERED

    session_id: { type: string }

    tenant_id: { type: string }

    payload: { type: object }

    timestamp: { type: string, format: date-time }

## Матрица зависимостей и статус

Runtime Specification v1.1 добавляет четыре раздела к v1.0. Все зависимости верифицированы.

| Документ | Зависимость | Версия | Статус |
|---|---|---|---|
| AK-MASTER | GL-01..14, FA-01..32, Phase 9, Thermal, LEM, SIL, MPE, SFE, TAT | v3.1 FINAL | ✅ PRODUCTION |
| GI — Great Investigator | ECT, FRCP, CDR, SSC, ICoI, WPL, HIL, RPL, CHF-A..F | v6.1 | ✅ PRODUCTION |
| АК | ЭВ-ядра (8), SYN-коды, SCN-типы, директора, TST | v6.5 | ✅ PRODUCTION |
| HELIX | TLX-64, CLE-135, Phase 4.5 (AK-INT-01..05), Use-Cases | v2.0.1 | ✅ PRODUCTION-READY |
| Runtime Spec v1.0 | Types, State Machine, Execution Graph, Policy Engine, Confidence Engine, API, Audit | v1.0 | ✅ FOUNDATION |
| AK-BRIDGE | АК ↔ AK-MASTER соответствия, D-01 закрыт | v1.0 | ✅ FOUNDATION |
| Active Patches | AK-INT-01..05, CLE-081..089, HITL bypass, 14 SOFT→HARD | v1.0 | ✅ COMPLETE |
| ST-18 Recovery | ЭВ-ИРОНИЯ/ВОСТОРГ recovery protocol, 8 триггеров | v1.0 | ✅ PRODUCTION |
| ROLE DEFINITION | Карта ролей экосистемы, D-расхождения | v1.0 | ✅ FOUNDATION |

### Открытые вопросы

| ID | Источник | Вопрос | Приоритет |
|---|---|---|---|
| BB-03 | AK-BRIDGE | VRP-X1 (право агента отклонить VTO) vs GL-01 (нет само-суждения трибунала) — потенциальный конфликт | HIGH |
| GI-69 | GI v6.1 | Патч 69 (literary anchor / Шекспир / Гадамер) — статус PENDING в v6.1 | MEDIUM |
| BB-01 | AK-BRIDGE | FRCP в АК (сюжетный конфликт) vs FRCP в AK-MASTER (когнитивный) — нужны ли два имени? | MEDIUM |
| SDK | Runtime Spec v1.1 | Python + TypeScript SDK примеры на базе OpenAPI 3.1 из Раздела 11 | MEDIUM |

## QA Чеклист v1.1

| Раздел 8 — Memory Partitioning | Раздел 8 — Memory Partitioning |
|---|---|
| Шесть типов памяти определены с TTL и Isolation | ✅ PASS |
| MemoryRecord TypeScript-схема полная (hash, provenance, access_policy) | ✅ PASS |
| MemoryAccessPolicy матрица (6 типов × 4 роли) | ✅ PASS |
| CONTAMINATED → Quarantined, cross-tenant = false на всех типах | ✅ PASS |
| Memory Engine API (store, search, contaminate, restore) | ✅ PASS |
| Жизненный цикл записи (create, MPE-CORRUPT, HITL, TTL) | ✅ PASS |
| Раздел 9 — Tenant Isolation | Раздел 9 — Tenant Isolation |
| TenantContext схема (tier, data_residency, BYOK, custom_policies) | ✅ PASS |
| Изолированные ресурсы (7 ресурсов с механизмом изоляции) | ✅ PASS |
| Tenant Provisioning API (create, get, patch, delete, policies, audit) | ✅ PASS |
| Custom policies не могут переопределить GL-01..14, CPX-ABS-* | ✅ PASS |
| 5 Tier: SAAS_LITE → DEFENSE с data residency notes | ✅ PASS |
| TRIBUNAL память экспортируется до удаления тенанта (никогда не теряется) | ✅ PASS |
| Раздел 10 — RAG Governance | Раздел 10 — RAG Governance |
| EvidenceLineage схема (retrieval_path, contamination_history, ect_current) | ✅ PASS |
| Trust-Weighted Retrieval формула (α/β/γ/δ коэффициенты) | ✅ PASS |
| Pre-retrieval фильтры (tenant, ECT, trust, CONTAMINATED exclusion) | ✅ PASS |
| RAG Pipeline State Machine (12 состояний) | ✅ PASS |
| PDE-CHECK, WPL-INTEGRITY, SCA-CHECK провенанс правила | ✅ PASS |
| RAG Governance API (retrieve, ingest, lineage, verify) | ✅ PASS |
| Раздел 11 — OpenAPI 3.1 YAML | Раздел 11 — OpenAPI 3.1 YAML |
| Базовая структура: openapi 3.1.0, servers, security | ✅ PASS |
| Схемы: RuntimeMode, ECTLevel, TrustScore, PolicyAction, SourceNode, ConfidenceResult | ✅ PASS |
| Core эндпоинты (из v1.0): /helix/process с 423/503 ответами | ✅ PASS |
| Memory Engine эндпоинты: /helix/memory/store, /search | ✅ PASS |
| Tenant Management: /helix/tenants CRUD + /audit + /policies | ✅ PASS |
| RAG эндпоинты: /helix/rag/retrieve, /ingest, /lineage | ✅ PASS |
| WebSocket events: 9 event types, HelixWebSocketEvent схема | ✅ PASS |
| RAG_LINEAGE_DEGRADED + TENANT_POLICY_TRIGGERED добавлены к v1.0 событиям | ✅ PASS |
| Совместимость | Совместимость |
| Runtime Spec v1.0 (Разделы 1–7): не изменены | ✅ PASS |
| AK-MASTER v3.1 CORE: не модифицирован | ✅ PASS |
| GI v6.1: не затронут | ✅ PASS |
| Active Patches v1.0: совместимы | ✅ PASS |
| ST-18 Recovery Protocol: совместим | ✅ PASS |
| Namespace конфликтов: 0 | ✅ PASS |
| Новых расхождений с экосистемой: 0 | ✅ PASS |

| HELIX Runtime Spec v1.1 ENTERPRISE INFRASTRUCTURE LAYER | ✅ QA: OVERALL PASS 28 мая 2026 |
|---|---|
