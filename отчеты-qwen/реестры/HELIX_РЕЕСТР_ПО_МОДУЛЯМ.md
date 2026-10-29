# HELIX — поэлементный реестр модулей ядра

**Сгенерировано, не написано руками**: `PYTHONUTF8=1 python scripts/реестр_продуктов.py`.
Номера строк — из AST живого кода, назначение — из докстринга самого элемента,
поэтому реестр не устаревает молча: при правке кода его пересобирают той же командой.

Тесты ищутся в двух каталогах — `helix_pipeline/tests/` и корневом `tests/`:
`market_text` и `claude_classifier` зовёт только корневой тест, и поиск
по одному каталогу объявлял их непроверенными.

Сопровождение: `HELIX_ЕДИНЫЙ_ПАСПОРТ.md` (раздел 5 — что за блоки, раздел 2 — масштаб).

Всего **113 модулей**, **38577 строк**, **1963 элементов верхнего уровня**. Без прямого теста — **0**.

---


## ach_matrix

- **путь**: `helix_pipeline/engine/ach_matrix.py`
- **размер**: 363 строк, SHA-256 blob `05d7610f8e0c4b68…`
- **что это**: ach_matrix.py — ACH: анализ конкурирующих гипотез (INT §8 / TRACE §3).
- **зачем**: Закрывает INT-8 в gi62_patch_manifest.yaml (было SPEC_ONLY — раздел спеки без реализации). Канон — INT §8 (HELIX_INTELLIGENCE_v2_1.md, «РАЗДЕЛ 8 — ACH»): единственная версия с посчитываемой формулой (Шаг 4: вес I пропорционален ECT; §8.2: точные множители/бонусы CF). TRACE §3 (HELIX_TRACE_MERGED.md, «РАЗДЕЛ 3 — ACH») описывает тот же метод прозой, без чисел — расхождения нет, INT §8 просто детальнее (тот же принцип, что HMP: канон там, где есть формула). ЧТО ЭТОТ МОДУЛЬ НЕ ДЕЛАЕТ (та же граница, что у risk_index.py). Не реш…
- **спека-якорь**: `HELIX_INTELLIGENCE_v2_1.md`, `HELIX_TRACE_MERGED.md`
- **коды состояний** (10): `ALTERNATIVE`, `CRITICAL`, `FLAG`, `HIGH`, `INSUFFICIENT`, `LOW`, `MAYBE`, `MODERATE`, `NULL`, `PRIMARY`
- **тесты, которые зовут модуль**: 5 — `helix_pipeline/tests/test_ach_matrix.py`, `helix_pipeline/tests/test_intelligence_closing_markers.py`, `helix_pipeline/tests/test_report_structure.py`, `helix_pipeline/tests/test_reproducibility.py`, `helix_pipeline/tests/test_trace_vector.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 48 | константа | `Rating` |  |
| 49 | константа | `HypType` |  |
| 51 | константа | `MIN_HYPOTHESES` |  |
| 52 | константа | `MIN_ECT_FOR_MATRIX` |  |
| 55 | константа | `ECT_I_WEIGHT` | dict, 3 элементов |
| 57 | константа | `CF_START` |  |
| 58 | константа | `CF_APORIA_WARNING` |  |
| 59 | константа | `CF_APORIA_CRITICAL` |  |
| 60 | константа | `CF_MPF_WARNING` |  |
| 61 | константа | `CF_EFR_C` |  |
| 62 | константа | `CF_SSD_PASS_BONUS` |  |
| 63 | константа | `CF_ANI_PASS_BONUS` |  |
| 64 | константа | `CF_MPF_PASS_BONUS` |  |
| 66 | константа | `CF_LEVELS` | tuple, 4 элементов |
| 80 | константа | `CF_MARKER` | dict, 4 элементов |
| 90 | константа | `RED_TEAM_MARKER` | dict, 3 элементов |
| 98 | константа | `RED_TEAM_QUESTIONS` | tuple, 5 элементов |
| 109 | класс | `Hypothesis (0 публичных методов)` |  |
| 117 | класс | `Evidence (0 публичных методов)` |  |
| 127 | функция | `validate_hypotheses(hypotheses)` | INT §8.1: H-NULL обязательна всегда; минимум 3 гипотезы. |
| 142 | класс | `HypothesisScore (0 публичных методов)` |  |
| 148 | функция | `hypothesis_score(cells, evidence_by_id)` | Один ряд матрицы: C/I/N-оценки для одной гипотезы -> I-вес. |
| 175 | функция | `build_ach_scores(hypotheses, evidence, matrix)` | Собрать I-вес для каждой гипотезы. `matrix`: hypothesis_id -> cells. |
| 199 | функция | `rank_hypotheses(scores)` | INT §8.1 Шаг 4: «Гипотеза с наименьшим суммарным I — победитель» — |
| 208 | класс | `ConfidenceFactorResult (0 публичных методов)` |  |
| 215 | функция | `_cf_level(cf)` |  |
| 222 | функция | `confidence_factor()` | INT §8.2 — CF (Confidence Factor). Все входы — уже посчитанные band- |
| 274 | функция | `red_team_applicability()` | INT §8.3: когда Red Team применяется (ANI WARNING+ / NGI HIGH+ / IFM-1+ |
| 290 | класс | `ACHMatrixResult (0 публичных методов)` |  |
| 302 | функция | `compute_ach_matrix()` | Собрать полную ACH-матрицу: I-веса, ранжирование, CF, применимость |

## additive_confidence_score

- **путь**: `helix_pipeline/engine/additive_confidence_score.py`
- **размер**: 327 строк, SHA-256 blob `ae89e9b45dcbdd45…`
- **что это**: additive_confidence_score.py — GOVERNANCE §2 (4 зоны) + §3/§4.15 (H-TYPE-1..8)
- **зачем**: + §5 (аддитивный Confidence Score, 0-100). НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. `governance_math.py` реализует только МУЛЬТИПЛИКАТИВНУЮ (SaaS) версию Confidence Score — §14.2, шкала 0-1, `Confidence = base × Π(1−weight_i) × RPL_Factor`. Спека сама явно называет её ОДНОЙ из двух параллельных версий: «промпт-версия Confidence Score (Раздел 5) использует аддитивную шкалу 0-100. SaaS-версия (Раздел 14.2) — мультипликативную 0-1. Обе корректны: мультипликативная — для API-вычислений, аддитивная — для человекочитаемого от…
- **коды состояний** (5): `CRITICAL`, `HIGH`, `LOW`, `MODERATE`, `VERY_LOW`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_additive_confidence_score.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_report_structure.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 75 | константа | `Zone` |  |
| 76 | константа | `CSLevel` |  |
| 81 | константа | `ZONE_MODIFIER` | dict, 4 элементов |
| 83 | константа | `BASE_SCORE` |  |
| 84 | константа | `VERIFICATION_BONUS_PER_FACT` |  |
| 85 | константа | `VERIFICATION_BONUS_CAP` |  |
| 89 | константа | `_PER_OCCURRENCE_PENALTIES` | dict, 3 элементов |
| 92 | константа | `_ONE_TIME_PENALTIES` | dict, 2 элементов |
| 93 | константа | `HALLUCINATION_PENALTY_FLOOR` |  |
| 96 | константа | `H_TYPE_8_PENALTY` |  |
| 98 | константа | `CHF_SP_FORM_PENALTY` |  |
| 99 | константа | `CHF_MW_TAC_PENALTY` |  |
| 102 | константа | `CHF_A_PENALTY` |  |
| 103 | константа | `CHF_C_PENALTY` |  |
| 104 | константа | `CHF_F_PENALTY` |  |
| 105 | константа | `CHF_PENALTY_FLOOR` |  |
| 108 | константа | `NGI_PENALTY_BY_LEVEL` | dict, 4 элементов |
| 113 | константа | `APORIA_PENALTY_BY_BAND` | dict, 4 элементов |
| 118 | константа | `PRESSURE_DISCOUNT` |  |
| 121 | константа | `CS_LEVELS` | tuple, 5 элементов |
| 136 | константа | `CS_MARKER` | dict, 5 элементов |
| 144 | константа | `OVERLOAD_MARKER_THRESHOLD` |  |
| 148 | класс | `HallucinationOccurrences (0 публичных методов)` | Сколько раз встретился каждый тип за один проход (§5). |
| 159 | класс | `AdditiveConfidenceScoreResult (0 публичных методов)` |  |
| 181 | функция | `zone_for(content_category)` | Классифицировать категорию контента в одну из четырёх зон (§2). |
| 201 | функция | `_level_for(total)` |  |
| 208 | функция | `additive_confidence_score()` | §5 — Confidence Score = сумма компонентов, 0-100. |
| 317 | функция | `additive_confidence_score_summary()` | Сводка — для отчётов о готовности. |

## ai_ani

- **путь**: `helix_pipeline/engine/ai_ani.py`
- **размер**: 137 строк, SHA-256 blob `75df3cb34b6b5498…`
- **что это**: ai_ani.py — GOVERNANCE §4.11: ANI — СОСТЯЗАТЕЛЬНАЯ ИНЪЕКЦИЯ НАРРАТИВА
- **зачем**: (AI-prompt framing), + мост ANI × FA-02. НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ (позиция 26 WORK_PLAN.md, найдено при подключении FA-02 §4.5 в этой же сессии): `ani.py` (GI Патч 47/INT §3.12) и GOVERNANCE §4.11 называются ОДИНАКОВО дословно — «ANI — состязательная инъекция нарратива» — но описывают РАЗНЫЕ признаки. `ani.py` оценивает СТРУКТУРУ ДОКАЗАТЕЛЬСТВ расследования (несовершенство улик, псевдо- независимость источников, синхронизация поступления, избыточная достаточность). GOVERNANCE §4.11 оценивает ФРЕЙМИНГ ПРОМПТА, кото…
- **коды состояний** (3): `CRITICAL`, `MONITOR`, `WARNING`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_ai_ani.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 37 | константа | `AIAniComposite` |  |
| 39 | константа | `_FLAG_MARKERS` | dict, 4 элементов |
| 48 | класс | `AIAniInputs (0 публичных методов)` |  |
| 56 | класс | `AIAniResult (1 публичных методов)` |  |
| 76 | функция | `ai_ani_evaluate(inp)` | §4.11 — 4 признака AI-prompt framing + COMPOSITE (1→MONITOR, |
| 114 | функция | `ani_fa02_bridge(ai_ani_composite, fa02_triggered)` | §4.11: «ANI × FA-02 → [ADVERSARIAL AI DEPLOYMENT: HITL_REQUIRED]». |
| 130 | функция | `ai_ani_summary()` |  |

## ai_icoi

- **путь**: `helix_pipeline/engine/ai_icoi.py`
- **размер**: 145 строк, SHA-256 blob `183cd181c3c897db…`
- **что это**: ai_icoi.py — GOVERNANCE §4.13: конфликт интересов AI-СИСТЕМЫ (не источника).
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ: `icoi_source.py` (INT §3.22/TRACE §4.1) — конфликт интересов ИСТОЧНИКА (человека/организации, дающей показания). GOVERNANCE §4.13 — четвёртая, отдельная ось: конфликт интересов самой AI-СИСТЕМЫ, которая производит вывод. Разные субъекты конфликта, разные числа (Trust Score cap 0.55/0.45/0.60 против icoi_source.py's 0.55 STRUCTURAL/0.45 REPUTATIONAL/0.60 POLITICAL/0.30 MULTI-TYPE — частично похожие числа, разные оси, не смешаны в одну функцию, тот же принцип, что и остальные «похожи…
- **коды состояний** (3): `COMMERCIAL`, `DATA`, `STRUCTURAL`
- **тесты, которые зовут модуль**: 5 — `helix_pipeline/tests/test_ai_icoi.py`, `helix_pipeline/tests/test_chain_diagnostics.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 41 | константа | `AIIcoiType` |  |
| 44 | константа | `TRUST_CAP` | dict, 3 элементов |
| 50 | константа | `_VALID_TYPES` | frozenset(TRUST_CAP) |
| 54 | класс | `AIIcoiResult (1 публичных методов)` |  |
| 75 | функция | `ai_icoi_resolve()` | §4.13 — эффект AI-ICoI на Trust Score + мост с NGI-П. |
| 140 | функция | `ai_icoi_summary()` |  |

## ai_output_governance

- **путь**: `helix_pipeline/engine/ai_output_governance.py`
- **размер**: 598 строк, SHA-256 blob `fea44467113459b6…`
- **что это**: ai_output_governance.py — что HELIX GOVERNANCE говорит об AI-выводе.
- **зачем**: ## ПОЧЕМУ ЭТОТ ФАЙЛ ПОЯВИЛСЯ Найдено 20.08.2026 аудитом контракта возвратов (`helix_contract_audit`). `HELIX_GOVERNANCE_v1_4.md` объявляет адресные маркеры для каждого класса дефекта AI-вывода, и ни один из них не был достижим кодом: AI-ECT-1/2/3 лестница достоверности AI-утверждения (Раздел 2) AI-HALLUCINATION-RISK полоса риска по баллам 0–10 (Раздел 3) семь H-TYPE маркеры конфабуляции, дрейфа, фантомов (Раздел 3) AI-NUMERICAL-DRIFT три новых типа SaaS-таксономии (Раздел 13) AI-LOGIC-INVERSION AI-SEMANTIC-BOUNDARY NGI-Э/П/А/…
- **спека-якорь**: `HELIX_GOVERNANCE_v1_4.md`
- **коды состояний** (8): `COVERED`, `CRITICAL`, `HIGH`, `LOW`, `M6_AI`, `MEDIUM`, `NOT_RUN`, `RAN`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_ai_output_governance.py`, `helix_pipeline/tests/test_chain_diagnostics.py`, `helix_pipeline/tests/test_governance_v14.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 80 | константа | `HType` |  |
| 88 | константа | `HTYPE_MARKER` | dict, 8 элементов |
| 101 | константа | `SAAS_TYPE_MARKER` | dict, 3 элементов |
| 110 | константа | `SAAS_TYPE_CS_PENALTY` | dict, 2 элементов |
| 113 | константа | `H_TYPE_8_PENALTY_MARKER` | строка: «[H-TYPE-8 PENALTY: −40 STANDARD v1.3]» |
| 119 | константа | `RISK_FACTORS` | dict, 6 элементов |
| 129 | константа | `RISK_BANDS` | tuple, 4 элементов |
| 139 | класс | `HallucinationRisk (0 публичных методов)` |  |
| 146 | функция | `hallucination_risk_score()` | Балл риска одного утверждения AI-вывода и его полоса (Раздел 3). |
| 169 | константа | `AI_ECT_MARKER` | dict, 3 элементов |
| 179 | функция | `ai_source_class(source_classes)` | Классы найденных первоисточников утверждения («первичный», «СМИ», …) → буква. |
| 191 | функция | `ai_ect_two_axis(level, source_class)` | Метка v1.4: `[AI-ECT-N: источник X]`. |
| 197 | константа | `AI_ECT4_UNREACHABLE` | строка: «ECT-4 недостижимо через AI: AI — инструмент поиска направления, не ист» |
| 202 | функция | `ai_ect_level()` | Уровень ECT утверждения AI и маркер спеки. |
| 219 | функция | `ngi_ai_markers()` | Четыре измерения NGI для AI-вывода (§4.3), каждое 0–3. |
| 248 | функция | `moffatt_markers()` | Ответственность за client-facing AI-вывод (Раздел 0). |
| 270 | константа | `HIGH_RISK_DOMAINS` | frozenset({'medicine', 'law', 'hiring', 'credit', 'critical_infrastructure', 'ju |
| 275 | константа | `ARTICLE_9_MIN_CS` |  |
| 278 | функция | `eu_ai_act_9()` | Статус соответствия Article 9 для AI-вывода в high-risk области. |
| 301 | константа | `RPL_ECT4_THRESHOLD` |  |
| 304 | функция | `rpl_ect4_block(rpl_factor)` | «Нельзя заявлять абсолютную достоверность в условиях дефицита» (§14). |
| 316 | функция | `manufactured_consensus()` | APORIA CRITICAL + H-TYPE-5 → консенсус изготовлен (§4.8). |
| 329 | функция | `mpf_ai_markers()` | MPF-4/MPF-5 применительно к AI-агенту (§4.6). |
| 344 | функция | `epistemic_lock_ai()` | M6 (SSD × IFM-2) для AI-агентов: замок и его снятие (§4.9). |
| 360 | функция | `sp_form_4_markers(subject)` | SP-FORM-4 Voice/Video Cloning (§11c): у клона есть ПОСТРАДАВШИЙ. |
| 385 | константа | `SAAS_TO_HTYPE_UNAMBIGUOUS` | dict, 3 элементов |
| 387 | константа | `SAAS_TO_HTYPE_AMBIGUOUS` | dict, 3 элементов |
| 395 | константа | `_NOT_OBSERVED_FACTORS_NOTE` | строка: «Разметчик GOVERNANCE не размечает причинность, «консенсус» и точные чи» |
| 402 | функция | `_sec(status)` |  |
| 406 | функция | `_ect_and_risk(labels, human_review, labeler_reason)` | Раздел 2 (лестница AI-ECT) и Раздел 3 (Risk Score) по утверждениям. |
| 463 | функция | `ai_output_governance_for_chain(governance_api)` | Слой «что GOVERNANCE говорит об AI-выводе» над готовым ответом стадии. |

## ai_output_pde

- **путь**: `helix_pipeline/engine/ai_output_pde.py`
- **размер**: 172 строк, SHA-256 blob `d1260901e4e50cd2…`
- **что это**: ai_output_pde.py — GOVERNANCE §4.2: провенанс AI-вывода (когда AI указывает
- **зачем**: источники). НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ: `helix_pipeline/engine/pde.py` (Патч 58, GI v6.2) — это ДРУГОЙ PDE. Тот считает цепочку ДОКУМЕНТОВ («через сколько рук прошёл документ» — copy_distance/origin_status/custody_gaps и т.д.). GOVERNANCE §4.2 — двухэтапная проверка AI-цитирования источника: существует ли источник вообще, и содержит ли он то, что AI утверждает. Разные вопросы, разные модели данных, одно название по случайному совпадению — не смешаны в одну функцию/файл, тот же принцип, что у RPL/ CPX/ICoI/Conf…
- **коды состояний** (3): `CONTENT_MISMATCH`, `PENDING_CONTENT_VERIFICATION`, `VERIFIED`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_ai_output_pde.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 42 | константа | `SERIES_THRESHOLD` |  |
| 44 | константа | `AIOutputPDEStatus` |  |
| 53 | класс | `AIOutputSourceCheck (0 публичных методов)` | Один AI-указанный источник + опциональная цепочка редактур. |
| 64 | класс | `AIOutputPDEResult (1 публичных методов)` |  |
| 87 | функция | `ai_output_pde_evaluate(check)` | §4.2 — двухэтапная проверка AI-указанного источника + правило |
| 164 | функция | `ai_output_pde_summary()` |  |

## ai_sad

- **путь**: `helix_pipeline/engine/ai_sad.py`
- **размер**: 121 строк, SHA-256 blob `fd06c90dde4e06b6…`
- **что это**: ai_sad.py — GOVERNANCE §4.12: SAD — МОЛЧАНИЕ AI КАК ДАННЫЕ (AI-адаптация).
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. `GovernanceRequest.sad_topics` уже существовал и вызывал `gi.sad.analyze()` (`gi_core.py::SADProtocol`, GI Патч 45 — «SAD-SIL», INT/TRACE) — но это ДРУГОЙ протокол, не §4.12. Раздел 0 самой спеки `HELIX_GOVERNANCE_v1_4.md` явно разграничивает два SAD: «SAD-SIL (Silence as Data): Используется в INTELLIGENCE и TRACE. GI v6.1, Патч 45» против «SAD-ADE (Sequential Action Deconstruction): Используется в GOVERNANCE». Но фактический текст §4.12 («AI-SAD-0/1/2», разговор о молчании тем, а не…
- **спека-якорь**: `HELIX_GOVERNANCE_v1_4.md`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_ai_sad.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `AISadType` |  |
| 49 | класс | `AISadTopicInput (0 публичных методов)` | Один топик для AI-SAD анализа AI-вывода (§4.12). |
| 61 | класс | `AISadResult (1 публичных методов)` |  |
| 78 | функция | `ai_sad_evaluate(inp)` | §4.12 — классифицировать молчание AI по теме и решить, нужна ли |
| 115 | функция | `ai_sad_summary()` |  |

## ai_ssd

- **путь**: `helix_pipeline/engine/ai_ssd.py`
- **размер**: 157 строк, SHA-256 blob `3e4b3f69213dfc34…`
- **что это**: ai_ssd.py — GOVERNANCE §4.14: SSD — НЕФАЛЬСИФИЦИРУЕМОСТЬ AI-ВЫВОДА
- **зачем**: (AI-адаптация). НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. `GovernanceRequest.ssd_hypothesis` уже существовал и вызывал `ssd_test()` (`ssd.py`, Патч 51, GI v6.2 блок B4) — тест Поппера над формальной `Hypothesis` (`falsifier`/`falsifier_observable` и три патологических паттерна SSD-P1/P2/P3: поглощение опровержений, молчание-как-подтверждение, отрицание-как-подтверждение). Это протокол для РАССЛЕДОВАНИЯ с явной гипотезой H1, которую вызывающий уже сформулировал. §4.14 описывает ДРУГУЮ проверку — не структурированную гипотезу, а прямо…
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_ai_ssd.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 42 | константа | `AI_SSD_ECT_CEILING` |  |
| 46 | класс | `AISsdCheckInput (0 публичных методов)` | Один AI-вывод, проверяемый на нефальсифицируемость (§4.14). |
| 67 | класс | `AISsdResult (1 публичных методов)` |  |
| 86 | константа | `AI_SSD_1_CANDIDATE` | строка: «[AI-SSD-1: оговорка — кандидат для вопроса Поппера, не провал]» |
| 89 | функция | `ai_ssd_evaluate(inp)` | §4.14 — три языковых паттерна + вопрос Поппера над AI-выводом. |
| 151 | функция | `ai_ssd_summary()` |  |

## ani

- **путь**: `helix_pipeline/engine/ani.py`
- **размер**: 243 строк, SHA-256 blob `5a03087625a8a170…`
- **что это**: ani.py — Патч 47: состязательная инъекция нарратива, ANI (GI v6.2, блок B5).
- **зачем**: Целенаправленная конструкция доказательной среды, эксплуатирующая саму логику верификации. Мысль патча, которую стоит держать в голове при разработке этого продукта: **чем известнее протокол — тем уязвимее к ANI.** Опубликованный стандарт проверки — это и инструкция для того, кто хочет его пройти. 4 ПРИЗНАКА: ANI-1 НАМЕРЕННАЯ НЕСОВЕРШЕННОСТЬ — несоответствия есть, но все периферийны, объяснимы и ни одно не создаёт конфликта FRCP. Слишком удобно. ANI-2 ПСЕВДОНЕЗАВИСИМОСТЬ — источники пришли через одного посредника, вза…
- **коды состояний** (1): `MPF`
- **тесты, которые зовут модуль**: 5 — `helix_pipeline/tests/test_ai_ani.py`, `helix_pipeline/tests/test_aporia_scoa_ani_b5.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_rpl.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `SYNCHRONIZED_ARRIVAL_THRESHOLD` |  |
| 40 | константа | `ANI_RED_TEAM_QUESTION` | строка: «Если бы кто-то хотел, чтобы расследование пришло к H1, что именно он д» |
| 45 | константа | `ANI_WHY` | строка: «Чем известнее протокол — тем уязвимее к ANI.» |
| 48 | класс | `ANIBand (0 публичных методов)` |  |
| 56 | класс | `EvidenceStructure (0 публичных методов)` | Структура доказательной базы — предмет проверки ANI. |
| 79 | класс | `ANIFlag (0 публичных методов)` |  |
| 87 | класс | `ANIResult (2 публичных методов)` |  |
| 113 | функция | `_band_for(composite)` |  |
| 123 | константа | `_ORDER` | list, 4 элементов |
| 127 | функция | `ani_evaluate(e)` | Проверить структуру доказательной базы на признаки инъекции. |
| 233 | функция | `ani_sensitivity_from_mpf(mpf_result)` | Принять запрос моста M3 от MPF и превратить его во вход ANI. |

## anonymity

- **путь**: `helix_pipeline/engine/anonymity.py`
- **размер**: 137 строк, SHA-256 blob `1abf75e7e86a01d9…`
- **что это**: anonymity.py — Патч 37: анонимный vs псевдонимный источник (GI v6.2, B1).
- **зачем**: Разграничение, которое спутывают почти всегда: «анонимный» и «псевдонимный» — не синонимы, и следствия у них противоположные. АНОНИМНЫЙ — личность неизвестна ДАЖЕ СЛЕДОВАТЕЛЮ. P3.5 (Biographical OSINT) невозможен. SAP-2 Independence Vector НЕ верифицируем. Потолок ECT-3. Два анонимных источника могут быть одним лицом. ПСЕВДОНИМНЫЙ — личность известна следователю, защищена от публикации. P3.5 применим полностью, IV верифицируем, Exception Pathway доступен при выполнении условий. Кейс спеки: «Глубокая Глотка» в Уотергейте …
- **коды состояний** (3): `ANONYMOUS`, `IDENTIFIED`, `PSEUDONYMOUS`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_anonymity_sta_dyn_b1.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `ANONYMOUS_ECT_CEILING` |  |
| 33 | константа | `PSEUDONYMOUS_ECT_CEILING` |  |
| 35 | константа | `EXCEPTION_PATHWAY_CONFLICT` | строка: «Патч 37 (v5.7): для анонимного Exception Pathway ЗАБЛОКИРОВАН. Патч 71» |
| 42 | класс | `AnonymityType (0 публичных методов)` |  |
| 49 | класс | `AnonymityAssessment (1 публичных методов)` |  |
| 63 | функция | `classify_anonymity(source_id, anonymity_type)` | Определить следствия типа анонимности для эпистемики источника. |
| 101 | функция | `convert_to_pseudonymous(source_id, reveal_date)` | Правило конвертации: анонимный раскрыл личность следователю. |
| 117 | функция | `independent_source_count(anonymity_types)` | «Два анонимных источника могут быть одним лицом» — поэтому анонимные |

## aporia

- **путь**: `helix_pipeline/engine/aporia.py`
- **размер**: 184 строк, SHA-256 blob `0ec2c64d5d294bf7…`
- **что это**: aporia.py — Патч 43: APORIA CHECK, ложные паттерны (GI v6.2, блок B5).
- **зачем**: Проверка на слишком хороший нарратив. Обязательна ПЕРЕД финализацией ACH-матрицы, EXIT PROTOCOL и любым публичным заявлением. Мысль патча: реальность неопрятна. Настоящее дело содержит периферийный хаос — факты, которые никуда не вписываются, шум, необъяснённые мелочи. Нарратив, где всё сходится, вероятнее сконструирован, чем обнаружен. 4 ТЕСТА: ТЕСТ 1 СИММЕТРИЯ каждый ключевой факт идеально вписан в H1 (≥ 7 фактов без исключений) → FLAG-1 ТЕСТ 2 ПОЛНОТА нет ни одной необъяснённой детали → FLAG-2 ТЕСТ 3 MYTH-COMPATIBILITY н…
- **тесты, которые зовут модуль**: 6 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_aporia_scoa_ani_b5.py`, `helix_pipeline/tests/test_exit_protocol_int9.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 33 | константа | `SYMMETRY_MIN_FACTS` |  |
| 35 | константа | `COINCIDENCE_THRESHOLD` |  |
| 37 | константа | `CF_BY_FLAGS` | dict, 5 элементов |
| 39 | константа | `AK_INT_06` | строка: «AK-INT-06 (ACTIVE_PATCHES v1.0): «ДОПОЛНЕНИЕ к APORIA CHECK: ТЕСТ 4 — » |
| 45 | константа | `APORIA_WHY` | строка: «Нормальный нарратив содержит периферийный хаос. Нарратив, в котором вс» |
| 51 | класс | `AporiaBand (0 публичных методов)` |  |
| 59 | класс | `KeyFact (0 публичных методов)` | Ключевой факт дела и его отношение к гипотезе. |
| 68 | класс | `NarrativeH1 (0 публичных методов)` | Гипотеза-нарратив и то, что о ней известно извне. |
| 82 | класс | `AporiaResult (1 публичных методов)` |  |
| 101 | функция | `aporia_check(narrative, key_facts)` | Прогнать 4 теста и вернуть полосу с множителем CF (чертёж PPC-4). |
| 182 | функция | `apply_aporia_to_confidence(cf, r)` | Применить множитель APORIA к CF. Не уходит ниже нуля. |

## bridges

- **путь**: `helix_pipeline/engine/bridges.py`
- **размер**: 477 строк, SHA-256 blob `366544fd9489ef25…`
- **что это**: bridges.py — Мосты M1–M6 (GI v6.2, блок B8).
- **зачем**: **AK-INT-11 дословно: «Мосты M1–M6 НЕ ОПЦИОНАЛЬНЫ. При срабатывании триггера в любом протоколе — Мост проверяется немедленно. Мосты не требуют явного запроса — система применяет их автономно.»** Поэтому мосты — не «интеграционные удобства», а обязательный слой. Спека называет их прямо: «Это не новые уязвимости — это незакрытые взаимодействия». Каждый протокол по отдельности может дать правильный ответ, а система в целом — неправильный, потому что два верных вывода не встретились. | Мост | Кого связывает | Что закрывает | |---|---|---| | M1 | TIE ↔ C…
- **тесты, которые зовут модуль**: 5 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_bridges_b8.py`, `helix_pipeline/tests/test_gi_coverage_validator.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 30 | константа | `AK_INT_11` | строка: «AK-INT-11 (ACTIVE_PATCHES v1.0): «Мосты M1–M6 не опциональны. При сраб» |
| 36 | константа | `BRIDGES_ARE_NOT_NEW_VULNERABILITIES` | строка: «Спека о мостах: «Это не новые уязвимости — это незакрытые взаимодейств» |
| 43 | константа | `M1_TIE_CONFIDENCE_FACTOR` |  |
| 45 | константа | `M1_CDR_DECAY_THRESHOLD` |  |
| 47 | константа | `M3_THRESHOLD_SHIFT` |  |
| 49 | константа | `M4_REACTIVATION_ECT` |  |
| 51 | константа | `M5_NGI_THRESHOLD` |  |
| 53 | константа | `M5_DECLARATION` | строка: «Данное расследование проводилось по задекларированным стандартам ECT. » |
| 61 | класс | `BridgeResult (1 публичных методов)` |  |
| 78 | функция | `m1_tie_cdr(tie_triggered, source_cdr_decay, window, dyn_change)` | При ЛЮБОМ флаге TIE запросить CDR-статус источников по окну. |
| 140 | функция | `m2_sdf_sca(sdf_triggered, source_id, sca_result, institution_documents)` | SDF-1 (Authority Bias) → ПРИНУДИТЕЛЬНЫЙ полный SCA для источника. |
| 191 | функция | `m3_mpf_ani(mpf_band, ani_composite, ani_band)` | MPF WARNING → пороги ANI снижаются на 1. MPF CRITICAL → Red Team по всем |
| 240 | функция | `m4_telp_ppep(telp_declared, new_evidence_ect, relates_to_telp_question, data_type, filters_passed)` | Порог реактивации TELP: ECT ≥ 3 И прямое отношение к вопросу предела. |
| 296 | функция | `m5_efr_ngi(efr_type, ngi_score)` | EFR-C + NGI ≥ 7 → [EFR×NGI CRITICAL]. |
| 342 | функция | `m6_ssd_ifm(ssd_result, ifm_triggered, ifm_2_approaching)` | SSD FAIL + IFM-2 CRITICAL → [EPISTEMIC LOCK]. |
| 404 | класс | `BridgeContext (0 публичных методов)` | Всё, что нужно шести мостам. Поля необязательны: мост, у которого нет |
| 436 | функция | `apply_all_bridges(ctx)` | Проверить ВСЕ шесть мостов без явного запроса (AK-INT-11). |

## business_rules_prefilter

- **путь**: `helix_pipeline/engine/business_rules_prefilter.py`
- **размер**: 73 строк, SHA-256 blob `a026181336718c4f…`
- **что это**: business_rules_prefilter.py — GOVERNANCE v1.4 §17: правила тенанта проверяются кодом.
- **зачем**: не передаётся вовсе (рассуждающая модель отвечает HTTP 400), поэтому его метки между одинаковыми запросами могут расходиться. Нарушение правила тенанта с явным `pattern` (Раздел 17: «ключевые слова / фраза / regex») — не суждение, а совпадение шаблона. Его проверяет Python, бесплатно и одинаково при каждом вызове.
- **коды состояний** (7): `BLOCK`, `CRITICAL`, `HIGH`, `LOG`, `LOW`, `MEDIUM`, `WARN`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_business_rules_prefilter.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 26 | константа | `MAX_PATTERN_LEN` |  |
| 27 | константа | `MAX_TEXT_LEN` |  |
| 29 | константа | `VALID_SEVERITIES` | set, 4 элементов |
| 30 | константа | `VALID_ACTIONS` | set, 3 элементов |
| 31 | константа | `VALID_TYPES` |  |
| 34 | функция | `check_business_rules(text, rules)` | Проверить AI-вывод по шаблонам правил тенанта. Модель не вызывается. |

## chain_cross_layers

- **путь**: `helix_pipeline/engine/chain_cross_layers.py`
- **размер**: 628 строк, SHA-256 blob `32cc4b5c012daac0…`
- **что это**: chain_cross_layers.py — три слоя поверх уже посчитанных протоколов цепочки.
- **зачем**: исполнялись ни разу:
- **коды состояний** (34): `ANI`, `ANI_SIGNS`, `BEFORE_OR_AT_EVENT`, `CONFIRMED_BY_OTHER_SOURCE`, `CONTRADICTED_BY_OTHER_SOURCE`, `FAILED`, `FIRST_24H`, `FIRST_MONTH`, `FIRST_WEEK`, `HIL`, `HMP`, `IFM`, `INTELLIGENCE`, `LATER`, `MPF`, `NGI`, `NON_LIQUET`, `NOT_RUN`, `NO_EXTERNAL_DATA`, `PDE`, `PDE_KEY_DOCS`, `PPEP`, `RAN`, `RDI`, `RDI_SCORE`, `RPL`, `SAD`, `SSD`, `SSD_FAILED`, `TELP`, `TRACE`, `WPL`, `WPL_CHAIN_DIVERGENCE`, `WPL_DEPTH`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_chain_cross_layers.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 51 | константа | `REPORT_ONLY_NOTE` | строка: «REPORT-ONLY: слой не меняет решение цепочки и не пишет во входные данн» |
| 57 | функция | `_as_dict(x)` |  |
| 61 | функция | `_intel_parts(intel)` | (protocols, labels, причина отсутствия). Принимает слой целиком |
| 75 | функция | `_trace_parts(trace)` | (protocols, trace_api, причина). TraceStageReport → to_api(). |
| 87 | функция | `_gov_parts(gov)` |  |
| 97 | функция | `_ran(p)` |  |
| 101 | функция | `_reason_of(p)` |  |
| 109 | константа | `Side` |  |
| 112 | класс | `_Sides (2 публичных методов)` |  |
| 272 | функция | `_inter_to_dict(x)` |  |
| 277 | функция | `_pde_counts(docs)` |  |
| 283 | функция | `_call_rdi_x_ifm(rdi)` |  |
| 287 | функция | `_call_mpf_to_rdi(mpf, score)` |  |
| 291 | функция | `_call_rdi_non_liquet(rdi, nl)` |  |
| 295 | функция | `_call_rdi_x_pde(rdi)` |  |
| 299 | функция | `_call_pde_entropy(docs)` |  |
| 304 | функция | `_call_hmp_tribunal(hmp)` |  |
| 308 | функция | `_call_wpl_tie(pairs)` |  |
| 319 | функция | `_combo()` |  |
| 323 | функция | `_call_triple_lock(hmp, rdi, ssd_failed)` |  |
| 327 | функция | `_call_ngi_mpf_hmp(ngi, mpf, hmp)` |  |
| 331 | функция | `_call_pde_ani(docs, ani_signs)` |  |
| 339 | константа | `INTERACTIONS` | tuple, 25 элементов |
| 381 | функция | `_normalize_result(r)` |  |
| 389 | функция | `_run_interactions(sides)` |  |
| 439 | константа | `_RELATION_MONTHS_UPPER` | dict, 4 элементов |
| 442 | константа | `_TRACE_SAP6_VERIFIED` | dict, 3 элементов |
| 450 | функция | `_run_trace_revision(sides)` |  |
| 556 | функция | `_run_speed(sides)` |  |
| 596 | функция | `_failed(e)` |  |
| 600 | функция | `cross_layers_for_chain(intel_protocols, trace_data, gov_api)` | TRACE revision, стыки GI v6.2 и Speed Protocols поверх протоколов цепочки. |

## chain_diagnostics

- **путь**: `helix_pipeline/engine/chain_diagnostics.py`
- **размер**: 61 строк, SHA-256 blob `a791b80f204452e2…`
- **что это**: chain_diagnostics.py — диагностика над ГОТОВЫМ ответом цепочки сайта.
- **зачем**: Одна точка входа: `diagnostics_for_chain(chain_response)`, где `chain_response` — словарь `mr_helix/api/main.py::_chain_response`. Два слоя, оба только читают ответ и ничего не перезапрашивают (ни одного вызова модели), решение цепочки не меняют: failure_atlas `mr_helix/engine/failure_atlas.py::diagnose_chain` — каждый SKIPPED/FAILED стадии, сбой провайдера, обрыв по лимиту, сбой разметчика и FA-маркер сводятся к классу Appendix C FA-01..32 с цепочкой восстановления из спеки, либо уходят в «не в атласе». ai_output_governance…
- **коды состояний** (4): `FAILED`, `GOVERNANCE`, `NOT_RUN`, `RAN`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_chain_diagnostics.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 27 | функция | `_layer(fn)` |  |
| 34 | функция | `_not_run(reason)` |  |
| 38 | функция | `diagnostics_for_chain(chain_response)` | {"failure_atlas": {...}, "ai_output_governance": {...}}; никогда не бросает. |

## chf

- **путь**: `helix_pipeline/engine/chf.py`
- **размер**: 309 строк, SHA-256 blob `6c42ab8b66d720a6…`
- **что это**: chf.py — CHF: Современная когнитивная среда (INT §3.16 / TRACE §4.13,
- **зачем**: Appendix E CHF EXTENSION — ТАКТИЧЕСКИЙ СЛОЙ / COMPOUND RULE). НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. Хостильный сквозной аудит четырёх векторов нашёл, что CHF отсутствует полностью — ни модуля, ни формулы нигде в helix_pipeline/engine/. Единственный код с похожим именем — mr_helix/engine/environment_chf_pressure_layer.py — реализует ДРУГУЮ, более грубую формулу («3+ активных модуля → HITL», без весов) для другой спеки и не импортируется ни INTELLIGENCE, ни TRACE. Этот модуль закрывает разрыв. ОБЩАЯ ФОРМУЛА ДЛЯ ДВУХ ПРОДУКТОВ (…
- **спека-якорь**: `HELIX_INTELLIGENCE_v2_1.md`, `HELIX_TRACE_MERGED.md`
- **коды состояний** (7): `ALERT`, `CRITICAL`, `ESCALATION`, `FLAG`, `HIGH`, `MEDIUM`, `WARNING`
- **тесты, которые зовут модуль**: 5 — `helix_pipeline/tests/test_chf.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_mw_defense.py`, `tests/test_ssc_char_classifier.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 78 | константа | `ACIndicator` |  |
| 83 | константа | `AC_INDICATOR_SEVERITY` | dict, 7 элементов |
| 93 | константа | `CHFALevel` |  |
| 97 | константа | `MwTac` |  |
| 101 | константа | `SpForm` |  |
| 104 | константа | `SP_FORM_TRUST_ZERO` | frozenset({'SP-FORM-1', 'SP-FORM-3'}) |
| 108 | константа | `InfIndicator` |  |
| 110 | константа | `Level` |  |
| 113 | константа | `CHF_WEIGHTS` | dict, 6 элементов |
| 124 | константа | `DEFAULT_FLOOR` |  |
| 126 | константа | `MW_QUARANTINE_FLOOR` |  |
| 129 | константа | `COMPOUND_THRESHOLD` |  |
| 132 | функция | `chf_a_evaluate(indicators)` | CHF-A: КРАХ УСТОЙЧИВОГО ВНИМАНИЯ. |
| 155 | функция | `chf_bc_evaluate(active, factor)` | CHF-B (алгоритмическая амплификация) / CHF-C (нарратив как идентичность). |
| 168 | функция | `chf_d_evaluate(tactics)` | CHF-D: МЕМЕТИЧЕСКАЯ ВОЙНА. 1 тактика → WARNING, 2+ → CRITICAL (решение №2). |
| 182 | функция | `chf_e_evaluate(forms)` | CHF-E: СИНТЕТИЧЕСКОЕ УБЕЖДЕНИЕ. |
| 205 | функция | `chf_f_evaluate(indicators)` | CHF-F: ИНФОРМАЦИОННОЕ ИСТОЩЕНИЕ. 1 признак → WARNING, 2+ → CRITICAL (решение №2). |
| 220 | класс | `CHFResult (0 публичных методов)` | Полный результат оценки когнитивной среды по всем шести факторам. |
| 238 | функция | `_weight_for(factor, level)` |  |
| 245 | функция | `chf_compound(trust_base, ac_indicators, b_active, c_active, mw_tactics, sp_forms, inf_indicators)` | CHF COMPOUND RULE (Appendix E) — полный проход по всем шести факторам. |

## claude_classifier

- **путь**: `helix_pipeline/engine/claude_classifier.py`
- **размер**: 40 строк, SHA-256 blob `4fc2129f43a82da9…`
- **что это**: УСТАРЕЛО. Транспорт Anthropic удалён — правило провайдера: только Google.
- **зачем**: Этот файл вызывал `anthropic.Anthropic(...)` с моделью `claude-sonnet-4-6` и требовал `ANTHROPIC_API_KEY`. Правило автора (9 августа 2026, docs/PROVIDER_RULE.md): Всё работает через Google Cloud и Gemini API. Ключи — Google Cloud. Anthropic API — НЕТ и НЕ БУДЕТ НИКОГДА. Замена: `helix_pipeline.engine.governance_classifier.GovernanceClassifierClient`. System prompt (РАЗДЕЛ 16 спецификации) перенесён туда дословно и остаётся единственным источником. Файл не удалён, а превращён в заглушку намеренно: молчаливое исчезновение …
- **тесты, которые зовут модуль**: 1 — `tests/test_provider_rule_google_only.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 26 | константа | `REPLACED_BY` | строка: «helix_pipeline.engine.governance_classifier.GovernanceClassifierClient» |
| 28 | константа | `WHY_REMOVED` | строка: «Правило провайдера: всё через Google Cloud и Gemini API, ключи Google.» |
| 34 | класс | `ClaudeClassifierClient (0 публичных методов)` | Больше не работает. Оставлен, чтобы старый вызов сказал, почему и куда. |

## corporate_fa

- **путь**: `helix_pipeline/engine/corporate_fa.py`
- **размер**: 245 строк, SHA-256 blob `538e2c34b110c417…`
- **что это**: corporate_fa.py — TRACE §4.11: FA — КОРПОРАТИВНЫЕ РЕЖИМЫ ОТКАЗА.
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ: TRACE §4.11 отсутствовал полностью — ни строки в манифесте, ни модуля. ЧИСЛОВАЯ КОЛЛИЗИЯ (ровно то, что и было записано в WORK_PLAN.md как повод не закрывать эту позицию сразу): TRACE §4.11 даёт 8 конкретных FA-номеров (01/03/04/05/09/11/15/19, спека называет их «девять ключевых режимов» — подсчёт самой спеки расходится с явным перечислением на единицу, не исправлено молча, зафиксировано как есть) для корпоративного Red Teaming. GI62 v2.0.1 Appendix C — отдельный, гораздо более широкий каталог…
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_corporate_fa.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 56 | константа | `FA03_DIVERSITY_FLOOR` |  |
| 58 | константа | `FA11_MONOPOLY_SHARE_CEILING` |  |
| 61 | константа | `COLLIDING_NUMBERS` | frozenset({'FA-09', 'FA-11', 'FA-15', 'FA-19'}) |
| 63 | константа | `MATCHING_NUMBERS` | frozenset({'FA-01', 'FA-02', 'FA-03', 'FA-04', 'FA-05'}) |
| 67 | класс | `CorporateFAResult (1 публичных методов)` |  |
| 86 | функция | `fa01_semantic_poisoning(chain_changed_character)` | Ключевой факт заменён на ненадёжный через source contamination. |
| 97 | функция | `fa03_governance_capture(source_diversity)` | Внешний агент монополизирует source set → diversity < 0.3. |
| 124 | функция | `fa04_tribunal_deadlock(tribunal_conflicted)` | Tribunal состоит из участников с конфликтными интересами. |
| 135 | функция | `fa05_synthetic_paranoia(over_flagging_icoi)` | Система видит ICoI везде, заморожены валидные источники. |
| 152 | функция | `fa09_ai_generated_document(sca_flag_count)` | TRACE-содержание — ОТЛИЧАЕТСЯ от Appendix C FA-09 (FORK LINEAGE |
| 168 | функция | `fa11_source_monopolization(single_source_evidence_share)` | TRACE-содержание — ОТЛИЧАЕТСЯ от Appendix C FA-11 (AMBIGUITY |
| 185 | функция | `fa15_institutional_coercion(sources_pressuring_conclusion)` | TRACE-содержание — ОТЛИЧАЕТСЯ от Appendix C FA-15 (NARRATIVE |
| 197 | функция | `fa19_manufactured_consensus(mutual_citation_without_primary_data)` | TRACE-содержание — ОТЛИЧАЕТСЯ от Appendix C FA-19 (JOUISSANCE |
| 212 | функция | `numbering_collision_report()` | Отчёт о коллизии номеров TRACE §4.11 vs GI62 Appendix C — для |
| 233 | функция | `corporate_fa_summary()` |  |

## cpx_int

- **путь**: `helix_pipeline/engine/cpx_int.py`
- **размер**: 333 строк, SHA-256 blob `616b7f6ea63357b6…`
- **что это**: cpx_int.py — CPX: матрица приоритетов конфликтов (INT §3.29).
- **зачем**: ━━━ ОСТОРОЖНО: ЭТО НЕ ТА МАТРИЦА CPX ━━━ В экосистеме ДВЕ разные матрицы с одним именем «CPX T1..T5», и совпадает у них только T1. Коллизию нашёл аудит незакрытых дел; она записана в реестре расхождений и в манифесте, но повторю здесь, потому что читать будут этот файл: тип │ HELIX Phase 7.7 (`mr_helix/tribunal_helix`) │ INT §3.29 (здесь) ────┼────────────────────────────────────────────┼────────────────────────── T1 │ факты против нарратива │ то же — СОВПАДАЕТ T2 │ связность против верификации │ документ против живой памяти T3 │ си…
- **коды состояний** (8): `BOTH`, `CONSENSUS`, `DOCUMENT`, `FACT`, `FRCP_CRITERION_1`, `HISTORICAL_RECORD`, `SINGLE_SOURCE`, `UNDECIDED`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_cpx_int.py`, `helix_pipeline/tests/test_cpx_trace.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 51 | константа | `CPX_INT_IS_NOT_HELIX_CPX` | строка: «Это матрица INT §3.29, а не HELIX Phase 7.7. Совпадает только T1: T2 з» |
| 59 | константа | `CPX_BEFORE_FRCP` | строка: «CPX разрешает конфликты между ТИПАМИ утверждений и применяется ДО FRCP» |
| 66 | константа | `CONSENSUS_IS_NOT_EVIDENCE` | строка: «T4: много источников — не доказательство, если это один источник, повт» |
| 72 | константа | `AI_VERIFICATION_HAS_A_CEILING` | строка: «T3: независимая верификация AI-вывода снимает дисквалификацию, но не д» |
| 80 | константа | `ECHO_CHAMBER_IV` |  |
| 83 | константа | `AI_VERIFIED_ECT_CEILING` |  |
| 86 | константа | `CPX_HIERARCHY` | tuple, 5 элементов |
| 88 | константа | `Winner` |  |
| 93 | класс | `CPXTypeSpec (0 публичных методов)` | Один тип конфликта: о чём он и что предписано. |
| 103 | константа | `CPX_INT_TYPES` | dict, 5 элементов |
| 135 | функция | `cpx_int_type(code)` | Тип конфликта по коду или None. |
| 144 | функция | `_marker(code, text)` |  |
| 148 | функция | `cpx_int_resolve(conflict_type)` | Разрешить конфликт типов утверждений по матрице INT §3.29. |
| 295 | функция | `cpx_int_classify_by_hierarchy(candidates)` | Выбрать тип по иерархии, когда природа конфликта неясна. |
| 321 | функция | `cpx_int_summary()` | Сводка матрицы INT — и предупреждение о коллизии имён. |

## cpx_trace

- **путь**: `helix_pipeline/engine/cpx_trace.py`
- **размер**: 305 строк, SHA-256 blob `0cf36a3a32fe7a5b…`
- **что это**: cpx_trace.py — CPX: разрешение конфликтов (TRACE §4.12).
- **зачем**: ━━━ НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ ━━━ До этого модуля TRACE §4.12 подключался через `cpx_int.py` (INT §3.29) — матрицу, которая сама себя документирует как ДРУГУЮ: имена T1..T5 совпадают только у T1, иерархия и содержание T2-T5 — нет (см. `cpx_int.py`'s `CPX_INT_IS_NOT_HELIX_CPX`). Более раннее сравнение с HELIX Phase 7.7 (`mr_helix/engine/tribunal_helix.py`) показало, что T2-T5 TRACE §4.12 по сути ближе к Phase 7.7 — но Phase 7.7's `CPX_PRIORITY_MATRIX` устроена по режимам MODE-GI/MODE-AK/MODE-HX, специфичным для экосистемы AK-6.7…
- **коды состояний** (5): `AMBIGUITY`, `FACT`, `NON_LIQUET`, `TRIBUNAL`, `UNDECIDED`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_cpx_trace.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 46 | константа | `CPX_TRACE_IS_A_THIRD_MATRIX` | строка: «TRACE §4.12 — третья самостоятельная матрица CPX в экосистеме, не копи» |
| 53 | константа | `Winner` |  |
| 57 | класс | `CPXTraceTypeSpec (0 публичных методов)` |  |
| 64 | константа | `CPX_TRACE_TYPES` | dict, 5 элементов |
| 89 | функция | `cpx_trace_type(code)` |  |
| 104 | константа | `CPX_RULE_ID` | dict, 4 элементов |
| 113 | функция | `_marker(code, text)` |  |
| 118 | функция | `cpx_trace_resolve(conflict_type)` | Разрешить конфликт типов утверждений по матрице TRACE §4.12. |
| 223 | константа | `TRIBUNAL_STEPS` | tuple, 5 элементов |
| 233 | класс | `TribunalStepResult (0 публичных методов)` |  |
| 240 | функция | `tribunal_procedure_trace()` | 5-шаговая процедура TRIBUNAL (TRACE §4.12), вызывается когда СЛОЙ 1 не решил. |
| 283 | функция | `gl06_check(tribunal_members_conflicted)` | GOVERNANCE LOCK GL-06 — Tribunal не судит себя. |
| 298 | функция | `cpx_trace_summary()` | Сводка матрицы — для отчётов о готовности. |

## cross_product_standards

- **путь**: `helix_pipeline/engine/cross_product_standards.py`
- **размер**: 205 строк, SHA-256 blob `0958a0f8186f2f00…`
- **что это**: cross_product_standards.py — межпродуктовые стандарты (INT §10).
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. §10 (OSINT/Financial/Legal/ Multilingual) не имел ни строки в манифесте и был почти полностью не реализован: §10.1 OSINT — нет маппинга тип-источника → PDE-дефолт, нет маркеров [OSINT-STA]/[OSINT-DYN], нет OSINT+ANI мета-провенанс правила; §10.2 Financial — правило «финансовый интерес = ICoI HIGH по умолчанию» есть только в market_math.py (принадлежит вектору MARKET, не INTELLIGENCE), (а)-(г) разбивка финансового анализа нигде не собрана; §10.4 Multilingual — pde.py's плоский штраф TRANSLATED …
- **коды состояний** (3): `HIGH`, `STRUCTURAL`, `UNKNOWN`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_cross_product_standards.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 36 | константа | `OsintSourceType` |  |
| 40 | константа | `_OSINT_PDE_DEFAULTS` | dict, 4 элементов |
| 50 | класс | `OsintResult (0 публичных методов)` |  |
| 59 | функция | `osint_pde_default(source_type)` | §10.1 — PDE-дефолт и STA/DYN-маркеры для OSINT-источника. |
| 85 | функция | `osint_dyn_marker()` | [OSINT-DYN: изменение зафиксировано, дата, механизм] — когда |
| 95 | константа | `FinancialRole` |  |
| 99 | константа | `_FINANCIAL_ROLE_ICOI` | dict, 3 элементов |
| 107 | класс | `FinancialAnalysisResult (0 публичных методов)` |  |
| 115 | функция | `financial_dyn_changed_analysis()` | §10.2 — DYN-CHANGED финансового атрибута форсирует 4-частный анализ |
| 128 | функция | `icoi_financial_default(role)` | §10.2 — «Финансовый интерес = ICoI HIGH по умолчанию» + SDF-2 роли. |
| 151 | константа | `TranslationType` |  |
| 153 | константа | `_TRANSLATION_PDE` | dict, 3 элементов |
| 161 | класс | `TranslationResult (0 публичных методов)` |  |
| 168 | функция | `translation_pde_default(translation_type)` | §10.4 — PDE-дефолт по типу перевода (не плоский штраф pde.py's |
| 184 | функция | `semantic_capture_in_translation_marker()` | §10.4 — CHF-D MW-TAC-2 в переводе: зафиксировать оригинальный термин. |
| 192 | функция | `cultural_context_marker()` | §10.4 — EFR-C для материалов из культурно отличных сред. |
| 197 | функция | `cross_product_standards_summary()` | Сводка — для отчётов о готовности. |

## deep_research

- **путь**: `helix_pipeline/engine/deep_research.py`
- **размер**: 273 строк, SHA-256 blob `4cd8e2d9b204f9e7…`
- **что это**: deep_research.py — агент Google Deep Research через Interactions API.
- **зачем**: Требование владельца 22.08.2026: «чтобы запрос шёл по глубокому исследованию Google, не просто 3.1 pro».
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_deep_research.py`, `helix_pipeline/tests/test_intelligence_extra_layers.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 53 | константа | `БАЗА` | строка: «https://generativelanguage.googleapis.com/v1beta/interactions» |
| 57 | константа | `АГЕНТ_БЫСТРЫЙ` | строка: «deep-research-preview-04-2026» |
| 58 | константа | `АГЕНТ_ПОЛНЫЙ` | строка: «deep-research-max-preview-04-2026» |
| 62 | константа | `ИНТЕРВАЛ_ОПРОСА` |  |
| 63 | константа | `ПРЕДЕЛ_ОЖИДАНИЯ` |  |
| 68 | константа | `ЗАВЕРШЁННЫЕ` | set, 5 элементов |
| 71 | класс | `DeepResearchError (0 публичных методов)` | Агент не смог отработать — с названной причиной, не молча. |
| 75 | функция | `_извлечь(ответ)` | Ответ Interactions API → форма, которую понимает `round_gate`. |
| 160 | функция | `исследовать(запрос)` | Запустить Deep Research и дождаться результата. |
| 272 | константа | `__all__` | list, 6 элементов |

## efr

- **путь**: `helix_pipeline/engine/efr.py`
- **размер**: 188 строк, SHA-256 blob `5a228ba35a02f435…`
- **что это**: efr.py — Патч 50: эпистемическая фрагментация, EFR (GI v6.2, блок B3).
- **зачем**: Активируется, когда несогласие вызвано РАЗНЫМИ СТАНДАРТАМИ ДОКАЗАТЕЛЬСТВА, а не разными данными и не разными выводами из одних данных. Это самый тихий из протоколов: он не ловит ложь, он ловит ситуацию, в которой «доказательство» значит разное для разных сторон — и потому спор не может быть решён данными. ТРИ ТИПА НЕСОГЛАСИЯ (первые два EFR НЕ активируют — важно не путать): EFR-A ФАКТИЧЕСКОЕ разные данные → ECT + FRCP EFR-B ИНТЕРПРЕТАЦИОННОЕ одни данные, разные выводы → ACH-матрица EFR-C ОНТОЛОГИЧЕСКОЕ разные стандарты дока…
- **коды состояний** (2): `CRITICAL`, `HIGH`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_efr_patch50.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_trace_revision.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 40 | константа | `DEFAULT_EPISTEMIC_STANDARD` | строка: «ECT GI v6.2» |
| 42 | константа | `FALSE_BALANCE_LIMIT` | строка: «ОГРАНИЧЕНИЕ спеки: EFR ≠ «дать слово обеим сторонам». False Balance — » |
| 49 | класс | `DisagreementType (0 публичных методов)` |  |
| 56 | класс | `Disagreement (0 публичных методов)` | Что известно о несогласии. |
| 73 | класс | `EFRResult (1 публичных методов)` |  |
| 90 | функция | `classify_disagreement(d)` | Отнести несогласие к EFR-A / EFR-B / EFR-C. |
| 109 | функция | `efr_evaluate(d, epistemic_standard)` | Классифицировать несогласие и, при EFR-C, выдать три предписанных действия. |

## exit_protocol

- **путь**: `helix_pipeline/engine/exit_protocol.py`
- **размер**: 375 строк, SHA-256 blob `bbce6ee47fb3556c…`
- **что это**: exit_protocol.py — EXIT PROTOCOL и ECT-зонирование (INT v2.1, Разделы 9.1–9.2).
- **зачем**: **Это продуктовая граница.** Всё остальное в движке — отдельные проверки; здесь они сходятся в один вопрос: можно ли публиковать. Именно по этому чеклисту измеряется готовность продукта (см. GI62_BUILD_PLAN §7.1), поэтому он собран исполняемым, а не оставлен списком в документе: чеклист, который надо сверять глазами, рано или поздно сверят невнимательно. 6 БЛОКОВ, 19 ПУНКТОВ: 1 Неразрешённые конфликты (3) 2 Нарратив (5) 3 Следователь (3) 4 Безопасность источников (3) 5 Лимиты (3) 6 Постпубликационный (2) ПОПРАВКА К…
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_exit_protocol_int9.py`, `helix_pipeline/tests/test_intelligence_vector.py`, `helix_pipeline/tests/test_trace_vector.py`, `helix_pipeline/tests/test_uc5_ai_preflight.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 35 | константа | `EXIT_PROTOCOL_IS_THE_PRODUCT_BOUNDARY` | строка: «EXIT PROTOCOL — не формальность в конце, а граница продукта: движок по» |
| 42 | константа | `FAIL_IS_A_DIFFERENT_STATE` | строка: «EXIT FAIL — не «много недочётов», а другое состояние: система требовал» |
| 51 | константа | `COERCION_RISK_THRESHOLD` |  |
| 53 | константа | `HIL_LIMIT` |  |
| 56 | константа | `ECT_ZONES` | dict, 4 элементов |
| 62 | константа | `NON_LIQUET_ZONE` | строка: «Ответа нет» |
| 65 | класс | `ExitOutcome (0 публичных методов)` |  |
| 72 | класс | `InvestigationState (0 публичных методов)` | Состояние расследования перед публикацией. |
| 122 | класс | `ChecklistItem (0 публичных методов)` |  |
| 132 | класс | `ExitResult (3 публичных методов)` |  |
| 154 | константа | `_BLOCK_NAMES` | dict, 6 элементов |
| 164 | функция | `exit_protocol(s)` | Прогнать все 19 пунктов чеклиста публикации. |
| 332 | класс | `ZonedFact (0 публичных методов)` |  |
| 339 | функция | `ect_zoning(facts)` | Разложить факты по ECT-зонам для публикации при неполной верификации. |

## fa02_recursive_hallucination

- **путь**: `helix_pipeline/engine/fa02_recursive_hallucination.py`
- **размер**: 124 строк, SHA-256 blob `7120441931edc60b…`
- **что это**: fa02_recursive_hallucination.py — GOVERNANCE §4.5: FA-02, РЕКУРСИВНАЯ
- **зачем**: ГАЛЛЮЦИНАЦИЯ (критический режим отказа, специфичен для AI). НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ: третий закрытый узел позиции 13 WORK_PLAN.md. §4.5 не существовал нигде в коде, хотя упоминается по имени маркера («FA-02 RECURSIVE HALLUCINATION») в нескольких других разделах спеки (Phase 9 MPE-CORRUPT, ANI × FA-02 bridge, §14 штрафная таблица "FA-02: -30 одноразовый, ceil 0", чек-листы §15/§16) — сам протокол, решающий, сработал ли FA-02, отсутствовал. ТРИГГЕР (спека, дословно): «AI-вывод используется как входные данные для др…
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_fa02_recursive_hallucination.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | класс | `FA02Check (0 публичных методов)` |  |
| 50 | класс | `FA02Result (1 публичных методов)` |  |
| 69 | функция | `fa02_check(check)` | §4.5 — решает, разрешено ли Independence Vector быть выше 0 для |
| 118 | функция | `fa02_summary()` |  |

## frcp_gi

- **путь**: `helix_pipeline/engine/frcp_gi.py`
- **размер**: 441 строк, SHA-256 blob `23a9e846627d7328…`
- **что это**: frcp_gi.py — Патч 70: FRCP-GI ЯВНЫЙ ПРОТОКОЛ (GI v6.2, блок B0).
- **зачем**: Проблема, которую закрывает патч (словами спеки): «FRCP упоминается 30+ раз как механизм разрешения, но нигде не определён как явная процедура. NON LIQUET существует как принцип — без правила активации.» Здесь процедура становится явной и детерминированной: 4 критерия Поппера с точными порогами, EPSILON-правило и NON LIQUET как ЛЕГИТИМНЫЙ эпистемический выход, а не отказ системы. ЖЁСТКОЕ РАЗГРАНИЧЕНИЕ (спека, «Межпродуктовые активации запрещены»): FRCP-GI — движок GI, применяется к ФАКТАМ, выход: победитель или NON LIQUET; FRCP-A…
- **коды состояний** (15): `ALL_FOUR_CRITERIA_INCONCLUSIVE`, `BOTH_PHYSICALLY_IMPOSSIBLE`, `CONTAMINATED`, `DIRECT`, `K1_PRIMACY`, `K2_INDEPENDENCE`, `K3_FALSIFIABILITY`, `K4_VERIFIABILITY`, `K_PHYSICAL`, `NON_LIQUET`, `PDE_TIE_BREAKER`, `RELAY`, `RESOLVED`, `UNKNOWN`, `UNVERIFIABLE`
- **тесты, которые зовут модуль**: 6 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_frcp_gi_patch70.py`, `helix_pipeline/tests/test_gi62_audit_regressions.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_s6_формальное_основание.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 30 | константа | `K1_PRIMACY_DELTA` |  |
| 31 | константа | `K2_INDEPENDENCE_DELTA` |  |
| 32 | константа | `K4_VERIFIABILITY_DELTA` |  |
| 33 | константа | `EPSILON_DEFAULT` |  |
| 35 | константа | `FRCP_THRESHOLDS_NOTE` | строка: «K1=0.15, K2=0.20, K4=0.25, EPSILON=0.10 — эвристики Патча 70, не калиб» |
| 48 | константа | `EPSILON_PROFILES` | dict, 2 элементов |
| 54 | константа | `DEFAULT_PROFILE` | строка: «patch70» |
| 56 | константа | `K2_THRESHOLD_DECISION` | строка: «Расхождение №5: Патч 70 (GI v6.2) даёт порог K2 = 0.20, INT v2.1 §3.5 » |
| 70 | константа | `ICOI_STRUCTURAL_IV_FACTOR` |  |
| 71 | константа | `CHF_D_FRAME_IV_FACTOR` |  |
| 72 | константа | `SSC_CHAR_5_IV_FACTOR` |  |
| 73 | константа | `ANI_2_IV_CEILING` |  |
| 74 | константа | `ECHO_CHAMBER_IV_CEILING` |  |
| 75 | константа | `IV_CANNOT_WIN_BELOW` |  |
| 84 | константа | `IV_GUARD_REACHABILITY_NOTE` | строка: «Защита «IV < 0.2 не может победить по Independence» достижима только п» |
| 92 | константа | `INT_ADDITIVE_LAYER` | строка: «INT v2.1 §3.5 содержит материал, которого нет в Патче 70: критерий физ» |
| 101 | класс | `Timing (0 публичных методов)` | Критерий 1 — первичность. Оценки взяты дословно из спеки. |
| 110 | константа | `_TIMING_SCORE` | dict, 4 элементов |
| 118 | класс | `WPLDepth (0 публичных методов)` | Критерий 4 — верифицируемость (WPL × PDE). |
| 126 | константа | `_WPL_SCORE` | dict, 4 элементов |
| 134 | класс | `CrossProductViolation (0 публичных методов)` | GL: межпродуктовые активации FRCP-GI ↔ FRCP-AK запрещены. |
| 139 | класс | `GIFact (7 публичных методов)` | Факт для FRCP-GI. subject='fact' обязателен — нарративные конфликты |
| 249 | класс | `FRCPGIResult (1 публичных методов)` |  |
| 268 | функция | `frcp_resolve(fact_a, fact_b)` | Патч 70 / чертёж PPC-1. Вызывается когда два факта ECT-4 прямо |
| 434 | функция | `_all_scores(a, b)` |  |

## gi_core

- **путь**: `helix_pipeline/engine/gi_core.py`
- **размер**: 1523 строк, SHA-256 blob `49f4893d017d9e06…`
- **что это**: engine/gi_core.py
- **зачем**: ================= HELIX Module 1 — GI v6.2 Core Engine Источник: GI_v6_2_COMPLETE.docx Реализует 7 базовых протоколов которые используют ОБА продукта: GOVERNANCE (через governance_math.py) и INTELLIGENCE (через intelligence_engine.py) Протоколы: P33 — SSC: Source Status Change (смена статуса источника) P34 — FRCP: Fact Reconciliation (разрешение конфликта ECT-4) P35 — CDR: Cascade Downgrade Rules (каскадное понижение ECT) P45 — SAD: Silence As Data (молчание как данные) P46 — NGI: Narrative Gravity Index (нарративная гравитация) P55 — PPS: Protocol Priority Stack (приоритет п…
- **спека-якорь**: `GI_v6_2_COMPLETE.md`, `HELIX_INTELLIGENCE_v2_1.md`
- **коды состояний** (72): `ANI_CRITICAL`, `ANI_MONITOR`, `APORIA_CRITICAL`, `APORIA_MONITOR`, `CDR1_DOWNGRADE`, `CDR3_MONITOR`, `CHF_COMPOUND_HIGH`, `CHF_D_ACTIVE`, `CRITICAL`, `DYN_CHANGED`, `ECT_CONFLICT_UNRESOLVED`, `EFR_NGI_CRITICAL`, `EPISTEMIC_LOCK`, `FRCP_ARBITRATION`, `GL06_VIOLATION`, `HIGH`, `HIL_ATTACHED`, `HIL_FUSED`, `HIL_LOCKED`, `HITL_RESOLVED`, `HITL_SLA_BREACH`, `HITL_TICKET_CREATED`, `IFM1_FLAG`, `IFM2_CRITICAL`, `IFM3_WARNING`, `IFM4_CRITICAL`, `IFM5_CRITICAL`, `LOW`, `MODERATE`, `MPF_CRITICAL`, `MPF_MONITOR`, `MPF_WARNING`, `NGI_CRITICAL`, `NGI_HIGH`, `NGI_MODERATE`, `ORANGE`, `P55`, `PDE_DECAY`, `PDPX_CRITICAL`, `PDPX_MONITOR`, `PPS_EVALUATION`, `PRE_LOCK_MONITOR`, `RDI_DD_RISING`, `RDI_DL_FORCED_CLOSURE`, `RDI_DL_RISING`, `RED`, `RISK_INDEX_CATASTROPHIC`, `RISK_INDEX_CRITICAL`, `RISK_INDEX_MODERATE`, `RPL_DEGRADED`, `SAD2_STRATEGIC`, `SCOA2_PLUS_SCOA4`, `SDF1_FLAG`, `SDF2_FLAG`, `SDF3_FLAG`, `SDF4_FLAG`, `SSC1_RECANTATION`, `SSC2_COERCION`, `SSC3_DEATH`, `SSC4_HIDDEN_LINK`, `SSD_FAIL`, `ST18_INITIATED`, `TELP_DECLARED`, `TIE1_IMPOSSIBLE_WINDOW`, `UC5_FAIL_P1`, `V61_CHAIN_DEGRADATION`, `V61_PERSONAL_LOCK`, `V61_RESOURCE_TELP`, `V61_STRATEGIC_DESTRUCTION`, `V61_TRIPLE_EXHAUSTION`, `WPL_CRITICAL`, `YELLOW`
- **тесты, которые зовут модуль**: 39 — `helix_pipeline/tests/test_additive_confidence_score.py`, `helix_pipeline/tests/test_ai_sad.py`, `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_anonymity_sta_dyn_b1.py`, `helix_pipeline/tests/test_aporia_scoa_ani_b5.py`, `helix_pipeline/tests/test_bridges_b8.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 42 | класс | `ECTLevel (2 публичных методов)` | Evidence Confidence Threshold. |
| 65 | константа | `ECT_FROZEN` | строка: «ECT-FROZEN» |
| 70 | класс | `SSCType (0 публичных методов)` |  |
| 87 | класс | `Source (0 публичных методов)` | Источник в расследовании. |
| 98 | класс | `SSCEvent (0 публичных методов)` | Событие смены статуса источника (P33). |
| 108 | класс | `SSCResult (0 публичных методов)` | Результат применения SSC-протокола к источнику. |
| 121 | класс | `SSCProtocol (1 публичных методов)` | P33 — Протокол смены статуса источника. |
| 196 | класс | `Fact (0 публичных методов)` | Факт в расследовании. |
| 207 | класс | `FRCPResult (0 публичных методов)` | Результат арбитража конфликта ECT-4 (P34). |
| 218 | класс | `FRCPProtocol (1 публичных методов)` | P34 — Протокол разрешения конфликта ECT-4. |
| 331 | класс | `CDRType (0 публичных методов)` |  |
| 339 | класс | `CDRResult (0 публичных методов)` | Результат каскадного понижения (P35). |
| 350 | класс | `CDRProtocol (1 публичных методов)` | P35 — Каскадное понижение ECT. |
| 463 | класс | `SADType (0 публичных методов)` |  |
| 470 | класс | `SADResult (0 публичных методов)` | Результат анализа молчания (P45). |
| 481 | класс | `SADProtocol (1 публичных методов)` | P45 — Silence As Data. |
| 593 | класс | `NGIAction (0 публичных методов)` | Обязательные действия по уровню NGI (P46). |
| 602 | константа | `NGI_ACTIONS` | dict, 4 элементов |
| 638 | функция | `get_ngi_actions(ngi_level)` | Получить обязательные действия для данного NGI-уровня. |
| 683 | класс | `PPSLevel (0 публичных методов)` |  |
| 690 | константа | `PPS_TRIGGER_MAP` | dict, 60 элементов |
| 763 | константа | `PPS_OVERLOAD_THRESHOLD` |  |
| 767 | класс | `PPSResult (0 публичных методов)` | Результат расстановки приоритетов (P55). |
| 778 | функция | `pps_prioritize(active_triggers)` | P55 — Расставить приоритеты при множественных триггерах. |
| 819 | класс | `OASRecord (0 публичных методов)` | Единица журнала аудита (P56). |
| 842 | класс | `OASJournal (6 публичных методов)` | P56 — Журнал аудита решений. |
| 938 | класс | `GICore (5 публичных методов)` | GI v6.2 Core — фасад над всеми протоколами. |

## gi_coverage_validator

- **путь**: `helix_pipeline/engine/gi_coverage_validator.py`
- **размер**: 192 строк, SHA-256 blob `34e7c88b59b0f034…`
- **что это**: gi_coverage_validator.py — учёт сборки GI v6.2 «Великий Расследователь».
- **зачем**: Ш-0 плана сборки. По образцу `/101 engine/coverage_validator.py`, который дал 13 ENFORCED-блоков: отделяет «символ есть в коде» от «поведение проверено». Почему это первый шаг, а не последний: враждебный аудит плана (ошибка О-3) показал, что реализованность, измеренная по ИМЕНАМ, — завышенная оценка. Здесь ENFORCED требует behavior_tests, поэтому «8 патчей готово» честно превращается в PARTIAL до поведенческой верификации. Статусы: SPEC_ONLY → PARTIAL → ENFORCED (+ DOC_ANCHOR / BLUEPRINT для недоказуемых слоёв, как БЛОК 1…
- **коды состояний** (8): `BLUEPRINT`, `DECISION_ENFORCED`, `DECISION_UNVERIFIED`, `DOC_ANCHOR`, `ENFORCED`, `PARTIAL`, `RPL`, `SPEC_ONLY`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_gi_coverage_validator.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_helix_contract_audit.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 23 | константа | `ROOT` |  |
| 24 | константа | `MANIFEST` |  |
| 25 | константа | `ENGINE_DIR` |  |
| 26 | константа | `TESTS_DIR` |  |
| 30 | класс | `PatchCoverage (1 публичных методов)` |  |
| 47 | класс | `GICoverageValidator (2 публичных методов)` | Считает статус каждого патча GI v6.2 по коду и тестам, не по декларации. |

## gl_locks

- **путь**: `helix_pipeline/engine/gl_locks.py`
- **размер**: 214 строк, SHA-256 blob `a0f8daa1b88d6f21…`
- **что это**: gl_locks.py — GOVERNANCE §4.7 (GL-GI-01..05, GL-01/02/06/07 AK) и §4.16
- **зачем**: (GL-08..14): GOVERNANCE LOCKS для AI-систем — неизменяемые правила. НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ: пятый закрытый узел позиции 13 WORK_PLAN.md. 16 замков (5 GL-GI + 4 AK в §4.7, 7 GL-08..14 в §4.16) существовали только как текст спеки. §4.16 явно ссылается на протоколы, уже построенные в этой же сессии (FA-02, LEM/MPE/SFE — Phase 9) — этот модуль их не переопределяет, только проверяет соблюдение правила использования их результатов. ДВЕ ГРУППЫ ПО ХАРАКТЕРУ: §4.7 (GL-GI-01..05, GL-01/02/06/07) — «кто имеет право приня…
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_gl_locks.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_oas_цепочка_sha256.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 41 | константа | `DecisionMaker` |  |
| 45 | класс | `GLLocksInput (0 публичных методов)` | Все поля опциональны — проверяется только то, что передано (P0-6: |
| 73 | класс | `GLLockViolation (0 публичных методов)` |  |
| 79 | класс | `GLLocksResult (1 публичных методов)` |  |
| 96 | функция | `gl_locks_check(inp)` |  |
| 198 | функция | `oas_tampered_from_chain(verify_result)` | GL-02 из проверки цепочки SHA-256 (`OASJournal.verify_provenance()`). |
| 208 | функция | `gl_locks_summary()` |  |

## governance_classifier

- **путь**: `helix_pipeline/engine/governance_classifier.py`
- **размер**: 454 строк, SHA-256 blob `f530e199b6e4be48…`
- **что это**: HELIX Module 2b — классификатор GOVERNANCE через Google (Gemini / Vertex AI).
- **зачем**: ПРАВИЛО ПРОВАЙДЕРА (автор, 9 августа 2026, см. docs/PROVIDER_RULE.md): Всё работает через Google Cloud и Gemini API. Ключи — Google Cloud. Anthropic API — НЕТ и НЕ БУДЕТ НИКОГДА. Прежняя версия (`claude_classifier.py`) вызывала `anthropic.Anthropic(...)` с моделью `claude-sonnet-4-6` и требовала `ANTHROPIC_API_KEY`. Это была ЕДИНСТВЕННАЯ LLM-зависимость всего движка журналистики — и она требовала ключ, которого у автора нет и не будет. То есть продукт не мог работать в принципе, и заметно это стало не сразу: `helix_p…
- **спека-якорь**: `HELIX_GOVERNANCE_v1_4.md`
- **коды состояний** (3): `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `PROVIDER_NOT_CONFIGURED`
- **тесты, которые зовут модуль**: 11 — `helix_pipeline/tests/test_chain_diagnostics.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_v14.py`, `helix_pipeline/tests/test_injection_guard.py`, `helix_pipeline/tests/test_temporal_grounding.py`, `helix_pipeline/tests/test_trace_classifier.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 50 | константа | `GOVERNANCE_CLASSIFIER_SYSTEM_PROMPT` | строка: «Ты — HELIX Governance Classifier.
Твоя задача: анализировать AI-вывод » |
| 110 | константа | `PROVIDER` | строка: «google» |
| 164 | константа | `INJECTION_GUARD_NOTE` | строка: «СЛУЖЕБНАЯ СПРАВКА ОТ СИСТЕМЫ (не часть анализируемого текста).
Всё, чт» |
| 180 | константа | `TEMPORAL_GROUNDING_NOTE` | строка: «СЛУЖЕБНАЯ СПРАВКА ОТ СИСТЕМЫ (не часть анализируемого текста).
Текущая» |
| 205 | константа | `TYPE_DEFINITIONS_NOTE` | строка: «СЛУЖЕБНАЯ СПРАВКА ОТ СИСТЕМЫ (не часть анализируемого текста).
Типы по» |
| 240 | константа | `FETCHED_SOURCES_NOTE` | строка: «СЛУЖЕБНАЯ СПРАВКА ОТ СИСТЕМЫ (не часть анализируемого текста).
Эти ист» |
| 254 | функция | `источники_справка(sources, предел)` |  |
| 264 | константа | `WHY_GOOGLE_ONLY` | строка: «Правило автора: всё работает через Google Cloud и Gemini API, ключи — » |
| 269 | константа | `NOT_CONFIGURED_MESSAGE` | строка: «Ключ Google не настроен на бэкенде. Классификация не выполнена. Пустой» |
| 277 | константа | `GOOGLE_KEY_ENV_NAMES` | tuple, 2 элементов |
| 280 | класс | `ClassifierNotConfigured (0 публичных методов)` | Ключа Google нет. Отдельный тип, чтобы вызывающий отличил это от сбоя сети. |
| 288 | класс | `ClassifierCallFailed (0 публичных методов)` | Google ответил отказом или пустым текстом. |
| 292 | функция | `today_utc_iso()` | Текущая дата UTC, ISO 8601. Единственный источник «сейчас» для обоих |
| 317 | константа | `CLASSIFIER_TEMPERATURE` |  |
| 320 | функция | `google_key_present()` | Есть ли у сервера провайдер для классификатора. |
| 336 | функция | `_caller_for(api_key)` | Собрать вызов классификатора, при наличии — с ключом ПОЛЬЗОВАТЕЛЯ. |
| 354 | функция | `_default_caller(system, prompt, max_tokens)` | Прежняя точка входа без ключа — оставлена: на неё ссылаются тесты. |
| 360 | класс | `GovernanceClassifierClient (1 публичных методов)` | Тонкая обёртка над Google для HELIX Governance Classifier. |

## governance_cognitive_labeler

- **путь**: `helix_pipeline/engine/governance_cognitive_labeler.py`
- **размер**: 554 строк, SHA-256 blob `cb390e76f0835408…`
- **что это**: governance_cognitive_labeler.py — ОТДЕЛЬНЫЙ разметочный вызов для
- **зачем**: возвращает только TYPE-1..7, NGI 0–3, EU-tier и нарушения правил; его системный промпт — дословный текст §16 и не редактируется. Входы §2 (зона каждого утверждения), §4.1 SCA, §4.2 PDE, §4.5 FA-02, §4.8 APORIA, §4.9 MPF, §4.11 ANI, §4.12 AI-SAD, §4.13 AI-ICoI, §4.14 AI-SSD-2/3 из его ответа не выводятся — поэтому раньше эти протоколы на сайте оставались NOT_RUN. Этот модуль — второй, самостоятельный вызов со своим промптом.
- **коды состояний** (4): `COMMERCIAL`, `DATA`, `PROVIDER_NOT_CONFIGURED`, `STRUCTURAL`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_chain_diagnostics.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 53 | константа | `LABELS` | tuple, 3 элементов |
| 54 | константа | `ZONES` | tuple, 4 элементов |
| 55 | константа | `SOURCE_KINDS` | tuple, 2 элементов |
| 56 | константа | `AI_ICOI_TYPES` | tuple, 3 элементов |
| 61 | константа | `FORBIDDEN_KEYS` | frozenset({'score', 'scores', 'confidence', 'confidence_score', 'cs', 'weight',  |
| 69 | константа | `MAX_CLAIMS` |  |
| 70 | константа | `MAX_SOURCES` |  |
| 71 | константа | `DEFAULT_ATTEMPTS` |  |
| 74 | константа | `TEXT_LABELS` | dict, 16 элементов |
| 94 | константа | `CLAIM_LABELS` | tuple, 3 элементов |
| 97 | константа | `COGNITIVE_LABELER_SYSTEM_PROMPT` | строка: «Ты — HELIX Governance Cognitive Labeler.
Ты РАЗМЕЧАЕШЬ текст AI-вывода» |
| 195 | класс | `LabelerNotConfigured (0 публичных методов)` | Провайдера нет — разметка не выполнялась (не «разметка пуста»). |
| 199 | класс | `LabelerCallFailed (0 публичных методов)` | Провайдер ответил отказом или пустым текстом. |
| 203 | класс | `LabelerResponseError (0 публичных методов)` | Ответ нарушил контракт разметчика (не JSON, запрещённое поле, число). |
| 208 | класс | `Label (3 публичных методов)` |  |
| 228 | класс | `ClaimLabels (1 публичных методов)` |  |
| 251 | класс | `CitedSourceLabels (1 публичных методов)` |  |
| 269 | класс | `CognitiveLabels (1 публичных методов)` | Нормализованная, проверенная разметка. Только метки и цитаты. |
| 293 | функция | `_norm(s)` |  |
| 297 | функция | `_quote_in(quote, haystack)` |  |
| 302 | функция | `_scan_forbidden(node, path)` | Запрещённые ключи — на любом уровне; числа — только в claims[].zone. |
| 325 | функция | `_label(raw, where, haystack, rejections)` |  |
| 345 | функция | `parse_labeler_response(raw)` | Строгая проверка ответа разметчика. Нарушение контракта → исключение; |
| 490 | функция | `_sources_digest(sources)` |  |
| 495 | класс | `GovernanceCognitiveLabeler (2 публичных методов)` | Разметчик когнитивного слоя. Возвращает `CognitiveLabels` или бросает |

## governance_hitl

- **путь**: `helix_pipeline/engine/governance_hitl.py`
- **размер**: 188 строк, SHA-256 blob `f41dfbbbf9b211ea…`
- **что это**: governance_hitl.py — GOVERNANCE §6: HITL_REQUIRED / HITL_ADVISORY.
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. `GovernanceDecision` (governance_math.py) знает только четыре состояния: PASS/WARN/BLOCK/HITL_REQUIRED — ни одного ADVISORY. `governance_service.py`'s когнитивный слой риска (построен раньше в этой же сессии) уже умеет поднимать решение до HITL_REQUIRED, но нет второго, более мягкого класса: авто-действие + лог, система продолжает — именно то, что §6 явно требует для 12 из 20 названных условий. Тот же принцип, что у `hitl_matrix.py` (INT/TRACE): два класса, а не один, потому что если рекомен…
- **коды состояний** (5): `ADVISORY`, `HITL_ADVISORY`, `HITL_NONE`, `HITL_REQUIRED`, `REQUIRED`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_hitl.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `GOVERNANCE_HITL_REQUIRED` | dict, 8 элементов |
| 45 | константа | `GOVERNANCE_HITL_ADVISORY` | dict, 12 элементов |
| 60 | константа | `_overlap` |  |
| 79 | константа | `CONDITION_ALIASES` | dict, 2 элементов |
| 85 | функция | `_normalise(s)` |  |
| 90 | функция | `governance_hitl_classify(conditions)` | Развести сработавшие условия GOVERNANCE §6 на REQUIRED/ADVISORY/unknown. |
| 133 | функция | `governance_hitl_summary()` | Сводка — для отчётов о готовности. |
| 146 | константа | `ALL_GOVERNANCE_HITL_CONDITIONS` |  |
| 150 | функция | `summarize_condition_evaluation(evaluations)` | Свести оценку условий §6, выведенную из протоколов ОДНОГО прохода. |

## governance_live_inputs

- **путь**: `helix_pipeline/engine/governance_live_inputs.py`
- **размер**: 725 строк, SHA-256 blob `b6f5ac1a46d2a8a4…`
- **что это**: governance_live_inputs.py — входы когнитивного слоя GOVERNANCE, которые
- **зачем**: живая цепочка (`mr_helix/engine/vector_orchestrator.py`) может вывести САМА, ничего не выдумывая. НАЙДЕНО АУДИТОМ 06.10.2026. Цепочка сайта строила `GovernanceRequest(ai_output=...)` — и только. Все опциональные входы `GovernanceService._run_cognitive_risk_layer` оставались NOT_RUN, а §5 (аддитивный Confidence Score) и §6 (8 REQUIRED + 12 ADVISORY условий) с сайта не исполнялись никогда. Этот модуль — разбор того, что из них можно получить из данных, которые у цепочки уже есть (текст ответа INTELLIGENCE, список реально пол…
- **коды состояний** (5): `APORIA`, `FAILED`, `NOT_RUN`, `PRESSURE`, `RAN`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_вырождение_текста.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 69 | константа | `AI_SSD_1_SPEC_PHRASES` | tuple, 2 элементов |
| 71 | константа | `_WORD` | строка: «а-яёa-z0-9» |
| 72 | константа | `_AI_SSD_1_RE` | re.compile(f'(?<![{_WORD}])(данные\\s+свидетельствуют\|как\\s+правило)(?![{_WORD} |
| 76 | константа | `_AI_SSD_2_FIRST` | re.compile(f'(?<![{_WORD}])с\\s+одной\\s+стороны(?![{_WORD}])', re.I) |
| 77 | константа | `_AI_SSD_2_SECOND` | re.compile(f'(?<![{_WORD}])с\\s+другой(?![{_WORD}])', re.I) |
| 79 | константа | `_CYRILLIC` | re.compile('[а-яё]', re.IGNORECASE) |
| 80 | константа | `_LATIN` | re.compile('[a-z]', re.IGNORECASE) |
| 81 | константа | `_URL` | re.compile('https?://[^\\s<>\\"\'()\\[\\]«»]+', re.IGNORECASE) |
| 83 | константа | `MAX_EVIDENCE` |  |
| 87 | константа | `NOT_RUN_REASONS` | dict, 19 элементов |
| 136 | функция | `_context(text, start, end, radius)` |  |
| 141 | функция | `ai_ssd_check_from_text(ai_output)` | §4.14 по литеральным фразам спеки. Возвращает (вход или None, справка). |
| 200 | функция | `_norm_url(url)` |  |
| 209 | функция | `source_crosscheck(ai_output, sources)` | Справка: какие URL, названные в тексте, есть среди реально |
| 232 | функция | `build_live_governance_request(ai_output)` | `GovernanceRequest` для живой цепочки: всё выводимое — передано, |
| 289 | константа | `AGGREGATION_RULE` | строка: «РЕШЕНИЕ ВЛАДЕЛЬЦА 07.10.2026 (спека правила свода не даёт): CS §5 счит» |
| 299 | константа | `VERIFIED_FACTS_NOTE` | строка: «Проверенным считается утверждение, на которое ссылаются два и более ис» |
| 308 | функция | `_norm(s)` |  |
| 312 | функция | `_домен(url)` | Регистрируемый домен: www.finance.yahoo.com → yahoo.com, bbc.co.uk → bbc.co.uk. |
| 328 | константа | `EXACT_DATA_RULE` | строка: ««точные данные» §4.2 = (автор И год) ЛИБО точный URL в тексте (решение» |
| 332 | константа | `TAXONOMY_CONFLICT` | строка: «ТАКСОНОМИЯ TYPE-n: с 07.10.2026 классификатор получает определения §13» |
| 338 | константа | `_LABELER_NOT_RUN` | строка: «когнитивная разметка не выполнена: {reason}» |
| 341 | функция | `_aporia_band_for(n)` |  |
| 346 | функция | `labels_to_request_fields(labels)` | Метки → (поля GovernanceRequest, not_run_reasons, provenance, notes). |
| 628 | функция | `build_full_governance_request(ai_output)` | `build_live_governance_request` + всё, что даёт разметка. Без меток — |
| 677 | функция | `governance_full_for_chain(text, sources, raw_classifier_output)` | Точка входа для оркестратора: полный аудит GOVERNANCE одного текста. |

## governance_math

- **путь**: `helix_pipeline/engine/governance_math.py`
- **размер**: 573 строк, SHA-256 blob `7b0de0942690cc7f…`
- **что это**: engine/governance_math.py
- **зачем**: ========================= HELIX Module 0 — Детерминированный математический движок. Источник: HELIX_GOVERNANCE_v1_4.md, Раздел 14–15 Zero third-party ML. Только Python stdlib + typing. CVE-2026-45758: никаких PyPI ML-пакетов. Архитектурный принцип: модель-разметчик (LLM) → возвращает семантические сигналы (текст, метки, 4 NGI-числа) HelixGovernanceMath → считает всё числовое детерминированно Никогда наоборот. Порядок в pipeline: [1] классификатор-модель → JSON с hallucinations + ngi_dimensions + eu_ai_act_signals [2] calculate_rpl_factor() → RPL_Factor [3] calculate_c…
- **спека-якорь**: `HELIX_GOVERNANCE_v1_4.md`
- **коды состояний** (19): `ABOVE_HITL_THRESHOLD`, `ADVERSARIAL_DEPLOYMENT`, `BLOCK`, `CIRI_THRESHOLD`, `COMPLIANT`, `CRITICAL`, `EU_AI_ACT`, `HALLUCINATION_BLOCK_RULE`, `HIGH`, `HITL_REQUIRED`, `LOW`, `LOW_CONFIDENCE`, `MEDIUM`, `MODERATE`, `NGI_ADVISORY`, `NGI_THRESHOLD`, `NON_COMPLIANT`, `PARTIAL`, `WARN`
- **тесты, которые зовут модуль**: 11 — `helix_pipeline/tests/test_additive_confidence_score.py`, `helix_pipeline/tests/test_governance_math.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_governance_v14.py`, `helix_pipeline/tests/test_ngi.py`, `helix_pipeline/tests/test_outcome_matrix.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 33 | константа | `HALLUCINATION_WEIGHTS` | dict, 4 элементов |
| 40 | константа | `NGI_THRESHOLDS` | dict, 4 элементов |
| 49 | константа | `CIRI_WEIGHTS` | dict, 3 элементов |
| 54 | константа | `CIRI_HALLUCINATION_WEIGHT` |  |
| 57 | константа | `ARTICLE9_WEIGHTS` | dict, 8 элементов |
| 72 | константа | `ADVERSARIAL_TYPE` | строка: «TYPE-8» |
| 76 | константа | `RISK_WORDS_NOTE` | строка: «эвристика триажа, не калибрована: слово следует из решения и тяжести н» |
| 81 | константа | `RPL_BLOCK_THRESHOLD` |  |
| 84 | константа | `CIRI_WARN_THRESHOLD` |  |
| 87 | константа | `CONFIDENCE_HITL_THRESHOLD` |  |
| 92 | константа | `NGI_HITL_THRESHOLD` |  |
| 95 | константа | `NGI_ADVISORY_THRESHOLD` |  |
| 101 | класс | `Hallucination (0 публичных методов)` | Одна обнаруженная галлюцинация (из классификатора-модели). |
| 111 | класс | `NGIResult (0 публичных методов)` | Результат расчёта Narrative Gravity Index. |
| 122 | класс | `CIRIResult (0 публичных методов)` | Composite Integrity Risk Index. |
| 132 | класс | `Article9Result (0 публичных методов)` | EU AI Act Article 9 compliance. |
| 140 | класс | `GovernanceDecision (0 публичных методов)` | Финальное решение движка. |
| 148 | класс | `GovernanceResult (0 публичных методов)` | Полный результат одного прохода через HelixGovernanceMath. |
| 167 | класс | `HelixGovernanceMath (10 публичных методов)` | Детерминированный математический движок HELIX GOVERNANCE. |

## governance_service

- **путь**: `helix_pipeline/engine/governance_service.py`
- **размер**: 1522 строк, SHA-256 blob `5e1ba7e24d1a618c…`
- **что это**: engine/governance_service.py
- **зачем**: ============================= HELIX Module 2 — Governance Service. Связывает три слоя: 1. JSON от Claude-классификатора (РАЗДЕЛ 16 спецификации GOVERNANCE v1.3) 2. HelixGovernanceMath (Module 0) — детерминированная математика 3. GICore / OASJournal (Module 1) — журнал аудита решений Это первый слой который реально ПРОИЗВОДИТ governance-результат из сырого ответа Claude, а не просто содержит формулы. Контракт входного JSON (строго по РАЗДЕЛ 16): { "hallucinations": [ {"type": "TYPE-1".."TYPE-7", "severity_signal": "CRITICAL|HIGH|MEDIUM|LOW", "description": str, "evi…
- **коды состояний** (20): `ADVISORY`, `BLOCK`, `BUSINESS_RULE`, `COGNITIVE_RISK_LAYER`, `CONTENT_MISMATCH`, `CRITICAL`, `GOVERNANCE_DECISION`, `HIGH`, `HITL`, `HITL_REQUIRED`, `INSTITUTION`, `LOW`, `M6_AI`, `MEDIUM`, `NOT_CALIBRATED`, `NOT_RUN`, `RAN`, `REQUIRED`, `WARN`, `WARNING`
- **тесты, которые зовут модуль**: 9 — `helix_pipeline/tests/test_business_rules_prefilter.py`, `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_primary_output.py`, `helix_pipeline/tests/test_governance_service.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 126 | класс | `ClassifierResponseError (0 публичных методов)` | Классификатор вернул невалидный JSON или нарушил контракт РАЗДЕЛ 16. |
| 131 | класс | `SadTopicInput (0 публичных методов)` | Один топик для SAD-анализа (P45) — см. `gi.sad.analyze()`. |
| 143 | класс | `GovernanceRequest (0 публичных методов)` | Входные данные для одного прохода governance-аудита. |
| 335 | класс | `CognitiveRiskLayerResult (0 публичных методов)` | Результаты подключённых протоколов §4 — по одному полю на протокол. |
| 378 | класс | `GovernanceServiceResult (0 публичных методов)` | Полный результат сервиса — то что возвращает API наружу. |
| 399 | константа | `REQUIRED_TOP_KEYS` | set, 4 элементов |
| 403 | константа | `VALID_TYPES` |  |
| 404 | константа | `VALID_SEVERITIES` | set, 4 элементов |
| 405 | константа | `VALID_EU_TIERS` | set, 4 элементов |
| 408 | функция | `parse_classifier_response(raw)` | Парсит и валидирует JSON от Claude-классификатора. |
| 524 | функция | `hallucinations_from_classifier(data)` | Конвертирует блок 'hallucinations' классификатора в List[Hallucination]. |
| 540 | класс | `GovernanceService (2 публичных методов)` | Оркестрирует один governance-проход: классификатор JSON → математика → OAS. |
| 1355 | константа | `_LIST_PROTOCOLS` | tuple, 5 элементов |
| 1356 | константа | `_DICT_PROTOCOLS` | tuple, 15 элементов |
| 1361 | функция | `additive_confidence_summary(crl)` | §5 одним объектом: score/level/breakdown/per_claim/aggregation_rule. |
| 1384 | функция | `hitl_summary(crl)` | §6: status, required[], advisory[], not_evaluated[]. |
| 1406 | функция | `_result_label(value)` |  |
| 1414 | функция | `protocol_statuses(crl)` | Протокол → {status: RAN\|NOT_RUN, result, reason, note}. |
| 1453 | функция | `_violation_profile(result)` | Нарушения по типам: TYPE-N классификатора §16 (+ H-TYPE, где соответствие |
| 1480 | функция | `_two_axis(result)` | Класс источника A–D × AI-ECT по утверждениям — тем же правилом, что |
| 1501 | функция | `primary_output_summary(result)` | {violation_profile, two_axis, decision, scores_reference} — только чтение. |

## helix_contract_audit

- **путь**: `helix_pipeline/engine/helix_contract_audit.py`
- **размер**: 456 строк, SHA-256 blob `64590de2e93c07b4…`
- **что это**: helix_contract_audit.py — сверка КОНТРАКТА ВОЗВРАТОВ HELIX.
- **зачем**: `gi_coverage_validator` объявляет свой контракт сам:
- **спека-якорь**: `GI_v6_2_COMPLETE.md`, `HELIX_INTELLIGENCE_v2_1.md`, `HELIX_TRACE_MERGED.md`, `HELIX_GOVERNANCE_v1_4.md`, `HELIX_CORE_v2_5.md`, `HELIX_MARKET_v1_0.md`
- **коды состояний** (1): `BENCHMARK`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_helix_contract_audit.py`, `tests/test_form_agent.py`, `tests/test_читай_первым_не_протух.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 55 | константа | `ROOT` |  |
| 56 | константа | `SPEC_DIR` |  |
| 57 | константа | `CODE_DIRS` | tuple, 2 элементов |
| 64 | константа | `CONTRACT_SPECS` | tuple, 5 элементов |
| 76 | константа | `EXCLUDED_SPECS` | dict, 18 элементов |
| 125 | константа | `EXCLUDED_SECTIONS` | dict, 3 элементов |
| 163 | константа | `NOT_A_STATE` | dict, 6 элементов |
| 199 | класс | `SpecContract (1 публичных методов)` |  |
| 212 | функция | `_py_files()` |  |
| 221 | функция | `code_string_literals()` | Все строковые литералы HELIX, включая статические части f-строк. |
| 239 | функция | `code_status_patterns()` | f-строки кода как ШАБЛОНЫ: подстановки → «что угодно». |
| 275 | функция | `identifier_patterns(patterns)` | Шаблоны, обрезанные до ИДЕНТИФИКАТОРА — до первого двоеточия. |
| 295 | константа | `_TOKEN_RE` | re.compile('\\[([A-Z][^\\]\\n]{1,70})\\]') |
| 296 | константа | `_ENUM_RE` | re.compile('enum:\\s*\\[([^\\]\\n]+)\\]') |
| 297 | константа | `_STATE_RE` | re.compile('^[A-Z][A-Z0-9_\\-→×]*(?:[ /][A-Z0-9_\\-→×]+)*$') |
| 300 | функция | `state_head(token)` | Ведущий идентификатор: `AI-ECT-2: частичная верификация` → `AI-ECT-2`. |
| 312 | функция | `strip_excluded_sections(spec_name, text)` | Вырезать разделы, названные в EXCLUDED_SECTIONS, до следующего |
| 334 | функция | `spec_states(text)` | Имя состояния → пример его написания в спеке. |
| 365 | функция | `is_reachable(head, code, patterns, id_patterns)` | Умеет ли код вообще выдать состояние с таким именем. |
| 388 | функция | `_sep_neutral(text)` | Пробел, дефис и подчёркивание внутри имени сведены к одному знаку. |
| 393 | функция | `audit()` |  |
| 432 | функция | `main()` |  |

## hil

- **путь**: `helix_pipeline/engine/hil.py`
- **размер**: 335 строк, SHA-256 blob `17afd7ca6235775d…`
- **что это**: hil.py — Патч 66: замок идентичности гипотезы, HIL (GI v6.2, блок B6).
- **зачем**: ПРИНЦИП: **когда следователь становится гипотезой — расследование заканчивается.** ━━━ РАЗГРАНИЧЕНИЕ HMP / HIL (спека требует понять сразу) ━━━ HMP (Патч 59) внешняя, социальная, экономическая природа. «Кто потеряет лицо, если H1 окажется ложной?» → обходится СМЕНОЙ СЛЕДОВАТЕЛЯ. HIL (Патч 66) внутренняя, психологическая, экзистенциальная природа. «Кем станет следователь, если H1 окажется ложной?» → СЛЕДУЕТ ЗА СЛЕДОВАТЕЛЕМ. HMP: «моя карьера зависит от H1». HIL: «я — это H1, без неё меня нет». Пример спеки: журналист 5 лет р…
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_exit_protocol_int9.py`, `helix_pipeline/tests/test_hmp_hil_b6.py`, `helix_pipeline/tests/test_intelligence_closing_markers.py`, `helix_pipeline/tests/test_s1_calibrated_and_codes.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 51 | константа | `W_PUBLIC_ID` |  |
| 52 | константа | `W_TIME` |  |
| 53 | константа | `W_NARRATIVE_SELF` |  |
| 54 | константа | `W_COUNTER_REACTION` |  |
| 55 | константа | `W_ISOLATION` |  |
| 56 | константа | `W_EXISTENTIAL` |  |
| 57 | константа | `HIL_MAX` |  |
| 60 | константа | `EXIT_PROTOCOL_HIL_LIMIT` |  |
| 62 | константа | `HIL_SCALE_CONFLICT` | строка: «Расхождение №10: Патч 66 (GI v6.2) даёт HIL-шкалу 0–100 с весовой табл» |
| 70 | константа | `HIL_VS_HMP` | строка: «HMP спрашивает «кто потеряет лицо, если H1 ложна?» — и обходится смено» |
| 77 | класс | `HILBand (0 публичных методов)` |  |
| 85 | константа | `FUSION_STAGES` | dict, 4 элементов |
| 104 | константа | `EARLY_WARNING_MARKERS` | dict, 4 элементов |
| 113 | класс | `InvestigatorIdentity (0 публичных методов)` | Отношение следователя к H1 — вход HIL. Все шкалы из спеки. |
| 142 | класс | `HILResult (1 публичных методов)` |  |
| 167 | функция | `hil_evaluate(i)` | Патч 66: балл замка идентичности 0–100 по весовой таблице спеки. |
| 240 | константа | `_HIL_BAND_RANGES` | dict, 4 элементов |
| 248 | функция | `hil_score_compressed(result)` | Производная шкала 0–10 для маркеров INT §3.13 и пункта EXIT PROTOCOL. |
| 261 | функция | `exit_protocol_hil_pass(result)` | Ответ на пункт EXIT PROTOCOL (INT §9.1, БЛОК 3): «HIL score < 6?». |
| 283 | функция | `hil_and_hmp_are_different_locks(hil, hmp_band)` | Свести два замка и НЕ смешать их. |
| 307 | функция | `hil_extra_markers(hil)` | Дополнительные маркеры HIL из GI v6.2 П66 (INT §3.16, конец раздела). |

## hitl_matrix

- **путь**: `helix_pipeline/engine/hitl_matrix.py`
- **размер**: 418 строк, SHA-256 blob `d5fe5f8cb9e3fd5c…`
- **что это**: hitl_matrix.py — HITL Threshold Matrix: REQUIRED против ADVISORY (AK-INT-05).
- **зачем**: ━━━ ЧТО БЫЛО НЕ ТАК ━━━ Флаг `hitl_required` возвращают PDE, SCA, PDP-X, FRCP-GI, SAP и другие — но разделения на два класса в коде не было. Один класс на всё. Практическое следствие опаснее, чем кажется. Если рекомендация посмотреть человеку и обязательная остановка выглядят одинаково, происходит одно из двух: система встаёт там, где хватило бы записи в лог — или, что хуже, от привычки к частым остановкам её проигнорируют в тот единственный раз, когда останавливаться обязательно. Обесценивание остановки — не мелочь:…
- **спека-якорь**: `HELIX_INTELLIGENCE_v2_1.md`, `HELIX_TRACE_MERGED.md`
- **коды состояний** (6): `ADVISORY`, `HITL_ADVISORY`, `HITL_NEEDS_FACT`, `HITL_NONE`, `HITL_REQUIRED`, `REQUIRED`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_hitl_matrix.py`, `helix_pipeline/tests/test_intelligence_vector.py`, `tests/test_читай_первым_не_протух.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 80 | константа | `DATA_FILE` |  |
| 81 | константа | `SPEC_RELATIVE` | строка: «helix_pipeline/docs/specs/HELIX_INTELLIGENCE_v2_1.md» |
| 83 | константа | `TRACE_DATA_FILE` |  |
| 84 | константа | `TRACE_SPEC_RELATIVE` | строка: «helix_pipeline/docs/specs/HELIX_TRACE_MERGED.md» |
| 86 | константа | `Phase` |  |
| 87 | константа | `Product` |  |
| 89 | константа | `WHY_TWO_CLASSES` | строка: «Если рекомендация и обязательная остановка выглядят одинаково, система» |
| 96 | константа | `OVERLAP_RULE` | строка: «Шесть условий стоят в обоих списках спеки. Побеждает строгость — REQUI» |
| 103 | константа | `PHASE_IS_NOT_GUESSED` | строка: «`phase` обязателен и не имеет значения по умолчанию. Уточнения спеки (» |
| 116 | константа | `PHASE_QUALIFIED` | dict, 1 элементов |
| 127 | константа | `FACT_QUALIFIED` | dict, 1 элементов |
| 136 | функция | `_repo_root()` |  |
| 140 | функция | `_normalise(line)` |  |
| 144 | функция | `_base_condition(raw)` | Условие без уточнения и без авто-действия. |
| 156 | функция | `extract_hitl_matrix(text)` | Оба списка AK-INT-05 из спеки продукта. |
| 186 | функция | `_trace_base_condition(raw)` | Как `_base_condition`, плюс два формата Приложения E/Раздела 7: |
| 207 | функция | `extract_trace_hitl_matrix(text)` | TRACE-матрица: объединение РАЗДЕЛА 7 (краткая версия) и ПРИЛОЖЕНИЯ E |
| 260 | функция | `hitl_matrix(product)` | Матрица из committed JSON (тест сверяет её со спекой). `product` |
| 272 | функция | `overlapping_conditions(product)` | Условия, стоящие в обоих списках. |
| 282 | функция | `hitl_classify(conditions)` | Развести сработавшие условия на REQUIRED и ADVISORY. |
| 406 | функция | `hitl_matrix_summary(product)` | Сводка матрицы — для отчётов и проверки полноты. |

## hitl_queue

- **путь**: `helix_pipeline/engine/hitl_queue.py`
- **размер**: 208 строк, SHA-256 blob `b686e5b76d2c02fe…`
- **что это**: hitl_queue.py — GOVERNANCE §18.2: HITL-очередь тикетов + SLA-тайминги.
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ: §18.2 существовал только как текст спеки — ни очереди тикетов, ни SLA-таймингов, ни RESOLVE-решений нигде в репозитории не было. `governance_hitl.py` (§6) классифицирует, требуется ли HITL вообще (REQUIRED/ADVISORY) — но что происходит ПОСЛЕ этого решения (тикет, дедлайн, эскалация, resolve) не существовало. СОСТОЯНИЕ, НЕ ЧИСТАЯ ФУНКЦИЯ. В отличие от большинства модулей `engine/` этой сессии, очередь тикетов принципиально держит состояние между вызовами (SLA считается от времени создания…
- **коды состояний** (10): `APPROVE_RELEASE`, `BREACHED`, `CRITICAL`, `ESCALATE`, `HIGH`, `MODIFY`, `NORMAL`, `OPEN`, `REJECT`, `RESOLVED`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_hitl_queue.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 43 | константа | `Priority` |  |
| 44 | константа | `ResolveDecision` |  |
| 45 | константа | `TicketStatus` |  |
| 48 | константа | `SLA_HOURS` | dict, 3 элементов |
| 52 | константа | `AUTO_CREATE_TYPES` | frozenset({'TYPE-7', 'TYPE-1', 'TYPE-8'}) |
| 54 | константа | `_VALID_DECISIONS` | frozenset({'APPROVE_RELEASE', 'REJECT', 'MODIFY', 'ESCALATE'}) |
| 55 | константа | `_VALID_PRIORITIES` | frozenset({'CRITICAL', 'HIGH', 'NORMAL'}) |
| 59 | класс | `HITLTicket (0 публичных методов)` |  |
| 73 | класс | `HITLQueue (9 публичных методов)` | §18.2 — очередь HITL-тикетов с SLA. Одна очередь на расследование, |

## hitl_threshold_matrix

- **путь**: `helix_pipeline/engine/hitl_threshold_matrix.py`
- **размер**: 386 строк, SHA-256 blob `62df557c9a510740…`
- **что это**: hitl_threshold_matrix.py — §4.1 HITL THRESHOLD MATRIX.
- **зачем**: ПОСТРОЕНО 24.08.2026 — реализация `HELIX_Final_Stabilization_MERGED.md`, PHASE 4 §4.1, единственного пункта, который сам файл `ЧИТАЙ_ПЕРВЫМ.md` (раздел 7) называет «самым важным открытым местом» во всей системе. ЕДИНЫЙ ЭТАЛОН (23.10.2026). Раньше §4.1 жила в двух независимых копиях — здесь и в `mr_helix/engine/hitl_threshold_matrix.py` — с разным поведением на краях (критерий анонимного источника, исход HITL-TIER-UNDETERMINED). Логика теперь одна: `classify_hitl_tier()` ниже; `mr_helix` её реэкспортирует, а `классифицировать()` — прежний р…
- **коды состояний** (13): `ANONYMOUS`, `CRITICAL`, `DRAW`, `HELIX_FREEZE`, `HIGH`, `LOW`, `MEDIUM`, `NAMED`, `NO_RESOLUTION`, `PSEUDONYMOUS`, `RESOLVED`, `RULE_AVAILABLE`, `WARNING`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_hitl_threshold_matrix.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 55 | класс | `Stake (0 публичных методов)` |  |
| 61 | класс | `ChfStatus (0 публичных методов)` | Худший статус среди активных модулей CHF-A..F (см. PACK 02). |
| 68 | класс | `PriorityMatrixResult (0 публичных методов)` | Итог §7.7 CPX Priority Matrix для данного конфликта. |
| 75 | класс | `SourceType (0 публичных методов)` | Тип источника по HELIX-таксономии, используемый именно в §4.1. |
| 82 | класс | `Tier (0 публичных методов)` |  |
| 88 | функция | `classify_hitl_tier()` | §4.1. Классифицировать конфликт CPX по трём уровням HITL. |
| 221 | функция | `_tier_result(tier, reasons, stake, types, chf_status, session_conflict_count, priority_matrix_result)` | Собрать действие, маркер и Phase 7 маршрут для найденного TIER — |
| 279 | функция | `hitl_tier_summary_table()` | Сводная таблица §4.1 — перенесена построчно, для справки и тестов |
| 294 | константа | `TIER_AUTO` | строка: «TIER-AUTO» |
| 295 | константа | `TIER_RECOMMEND` | строка: «TIER-RECOMMEND» |
| 296 | константа | `TIER_MANDATORY` | строка: «TIER-MANDATORY» |
| 299 | константа | `СТАВКИ` | tuple, 3 элементов |
| 301 | константа | `УРОВНИ_CHF` | tuple, 3 элементов |
| 303 | константа | `PRIORITY_MATRIX` | tuple, 3 элементов |
| 307 | класс | `HITLThresholdInput (0 публичных методов)` | Сигналы, из которых §4.1 вычисляет TIER. Все — известные вызывающему |
| 350 | класс | `HITLThresholdResult (0 публичных методов)` |  |
| 359 | функция | `классифицировать(вход)` | Прежний русский интерфейс поверх единого эталона `classify_hitl_tier()`. |

## hmp

- **путь**: `helix_pipeline/engine/hmp.py`
- **размер**: 356 строк, SHA-256 blob `e9593997f66b4d4d…`
- **что это**: hmp.py — Патч 59: протокол рынка гипотез, HMP (GI v6.2, блок B6).
- **зачем**: ПРИНЦИП: гипотезы конкурируют СОЦИАЛЬНО, а не только доказательно. Слепое пятно, которое закрывает патч: ACH-матрица оценивает гипотезу по доказательствам. HMP оценивает, **сколько стоит отказ от неё тем, кто в неё вложился**. Ответ определяет, насколько вероятно, что пересмотр реально произойдёт — даже когда доказательства его требуют. Пример спеки: расследование 3 года, прокуратура публично объявила H1 обоснованной, выдан ордер на арест, институт вложил репутацию, политик — карьеру. Появляется конфликт FRCP, доказательная сила…
- **коды состояний** (6): `FRCP_EXPLAINED_AS_COVERUP`, `FREE`, `LOCKED`, `PRESTIGE_CAPTURE`, `RED_TEAM_DISMISSED`, `SSD_FAIL_NOT_ADDRESSED`
- **тесты, которые зовут модуль**: 7 — `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_exit_protocol_int9.py`, `helix_pipeline/tests/test_hmp_hil_b6.py`, `helix_pipeline/tests/test_intelligence_protocol_inputs.py`, `helix_pipeline/tests/test_s1_calibrated_and_codes.py`, `helix_pipeline/tests/test_trace_questionnaire_and_labels.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `SC_INTERNAL_ONLY` |  |
| 46 | константа | `SC_MEDIA_PUBLICATIONS` |  |
| 47 | константа | `SC_OFFICIAL_DOCUMENTS` |  |
| 48 | константа | `SC_LEGAL_ACTIONS` |  |
| 49 | константа | `INSTITUTIONAL_DEPTH` | dict, 4 элементов |
| 55 | константа | `PA_EXPERTS` |  |
| 56 | константа | `PA_POLITICAL` |  |
| 57 | константа | `PCL_WEIGHT` |  |
| 58 | константа | `REVERSAL_COST` | dict, 3 элементов |
| 59 | константа | `HMP_MAX` |  |
| 62 | константа | `IFM_FREQ_ABOVE_50` |  |
| 63 | константа | `IFM_FREQ_ABOVE_75` |  |
| 65 | константа | `ACH_CONFIRMATION_WEIGHT_FACTOR` |  |
| 67 | константа | `LOCK_SIGNALS_REQUIRED` |  |
| 69 | константа | `HMP_SCALE_CONFLICT` | строка: «Расхождение №9: Патч 59 (GI v6.2) даёт HMP-шкалу 0–100 с весовой табли» |
| 78 | константа | `HMP_VS_HIL` | строка: «HMP (Патч 59) — внешняя, социальная цена отказа от H1: «кто потеряет л» |
| 85 | константа | `HYPOTHESIS_ECONOMY_TABLE` | dict, 8 элементов |
| 104 | класс | `HMPBand (0 публичных методов)` |  |
| 112 | класс | `HypothesisMarket (0 публичных методов)` | Инвестиции в гипотезу — вход HMP. |
| 152 | класс | `HMPResult (1 публичных методов)` |  |
| 179 | функция | `hmp_evaluate(m)` | Патч 59: балл рынка гипотез 0–100 по весовой таблице спеки. |
| 270 | константа | `_HMP_BAND_RANGES` | dict, 4 элементов |
| 278 | функция | `hmp_score_compressed(result)` | Производная шкала 0–10 для маркеров INT §3.15. |
| 293 | класс | `HypothesisLockCheck (0 публичных методов)` | Вход детектора захвата (`hmp_lock_detection`). |
| 304 | функция | `hmp_lock_detection(c)` | Детектор захвата гипотезы. Вызывается при HMP ≥ 51 + конфликт FRCP/SSD. |
| 348 | функция | `apply_hmp_to_ach_weight(confirmation_weight, r)` | HMP ↔ ACH: при LOCK RISK и выше вес подтверждающих фактов × 0.85. |

## icoi_source

- **путь**: `helix_pipeline/engine/icoi_source.py`
- **размер**: 225 строк, SHA-256 blob `20af9dc1142613e8…`
- **что это**: icoi_source.py — ICoI: конфликт интересов источника (INT §3.22 / TRACE §4.1).
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. До этого модуля существовал только `ICOI_STRUCTURAL_TRUST_CAP = 0.40` внутри SAP-3 (sap_protocol.py) — один тип из пяти, без формул для PARTIAL/HIGH/UNKNOWN, без правила «2+ типов → cap 0.30», без бриджей ANI×ICoI и ICoI×NGI. `frcp_gi.py` применял IV×0.75 только по булеву флагу `icoi_structural`, не по остальным типам. ДВЕ СПЕКИ ОПИСЫВАЮТ ICoI ПО-РАЗНОМУ, И ЭТО НЕ ОДНА И ТА ЖЕ ОСЬ: INT §3.22 — 5 ТИРОВ СТРОГОСТИ (одна шкала, каждый следующий тир строже): NONE < PARTIAL < HIGH < STR…
- **коды состояний** (8): `CRITICAL`, `FINANCIAL`, `HIGH`, `PARTIAL`, `POLITICAL`, `REPUTATIONAL`, `STRUCTURAL`, `UNKNOWN`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_cross_product_standards.py`, `helix_pipeline/tests/test_icoi_source.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 52 | константа | `IcoiIntType` |  |
| 55 | константа | `ICOI_INT_TRUST_CAP` | dict, 5 элементов |
| 60 | константа | `ICOI_INT_TRUST_MULTIPLIER` | dict, 5 элементов |
| 64 | константа | `ICOI_INT_ECT_CEILING` | dict, 5 элементов |
| 68 | константа | `ICOI_INT_IV_MULTIPLIER_IN_FRCP` | dict, 5 элементов |
| 73 | константа | `MULTI_TYPE_TRUST_CAP` |  |
| 75 | константа | `NGI_HIGH_PLUS_LEVELS` | frozenset({'HIGH', 'CRITICAL'}) |
| 77 | константа | `ICOI_NGI_BRIDGE_MULTIPLIER` |  |
| 80 | функция | `_int_marker(type_, source_id, extra)` |  |
| 85 | функция | `icoi_int_resolve()` | INT §3.22 — эффект ICoI на Trust Score/ECT/FRCP для одного источника. |
| 155 | константа | `IcoiTraceCategory` |  |
| 159 | функция | `icoi_trace_resolve()` | TRACE §4.1 — эффект ICoI по категории (не по тиру строгости — см. |
| 216 | функция | `icoi_source_summary()` | Сводка — для отчётов о готовности. |

## ifm

- **путь**: `helix_pipeline/engine/ifm.py`
- **размер**: 231 строк, SHA-256 blob `a0a9c090aef0afe3…`
- **что это**: ifm.py — Патч 42: усталость следователя, IFM (GI v6.2, блок B2).
- **зачем**: ICoI (Патч 38) фиксирует НАЧАЛЬНЫЕ условия следователя. IFM отслеживает их ДЕГРАДАЦИЮ в процессе работы. Это единственный протокол, направленный не на источник и не на документ, а на того, кто расследует. Реализовано по чертежу PPC-5 (`ifm_checklist`) из Патча 54 — псевдокод спеки взят как логика, а не как вдохновение. 5 ИНДИКАТОРОВ: IFM-1 ТУННЕЛЬНОЕ ЗРЕНИЕ Competing Hypothesis Review > 7 дней IFM-2 РЕКУРСИВНАЯ ПАРАНОЙЯ > 30 % записей с фразами-маркерами паранойи IFM-3 SUNK COST > 3 месяцев И неразрешённый FRCP IFM-4 ЭМОЦ. ВОВЛЕЧ…
- **коды состояний** (5): `CRITICAL`, `FLAG`, `FORCED_CLOSURE`, `HIGH`, `RISING`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_ifm_patch42.py`, `helix_pipeline/tests/test_ssd_mpf_telp_b4.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 37 | константа | `IFM1_CHR_DAYS` |  |
| 39 | константа | `IFM2_PARANOID_RATIO` |  |
| 41 | константа | `IFM3_MONTHS` |  |
| 43 | константа | `IFM5_SEARCH_WINDOW` |  |
| 45 | константа | `CHECKLIST_DAYS_DEFAULT` |  |
| 46 | константа | `CHECKLIST_DAYS_ACCELERATED` |  |
| 48 | константа | `AK_INT_02` | строка: «AK-INT-02 (ACTIVE_PATCHES v1.0): «H-NULL не проверялась > 7 дней → IFM» |
| 55 | класс | `IFMSeverity (0 публичных методов)` |  |
| 61 | класс | `InvestigatorState (0 публичных методов)` | Что известно о следователе и расследовании на момент прогона чеклиста. |
| 77 | класс | `IFMIndicator (0 публичных методов)` |  |
| 86 | класс | `IFMResult (1 публичных методов)` |  |
| 107 | функция | `checklist_frequency_days(state)` | 14 дней по умолчанию; 7 при NGI HIGH+ (Патч 46) или RDI RISING+ (Патч 60). |
| 120 | функция | `ifm_checklist(state)` | Прогнать чеклист IFM. Возвращает сработавшие индикаторы и предписания. |
| 219 | функция | `ifm_checklist_questions()` | Чеклист словами — для человека, а не для машины (Патч 42 + INT §3.10). |

## independence_vector

- **путь**: `helix_pipeline/engine/independence_vector.py`
- **размер**: 168 строк, SHA-256 blob `6d58d0331b46e1c7…`
- **что это**: independence_vector.py — SAP-2: Independence Vector, полные компоненты
- **зачем**: IV-A/B/C/D (TRACE Appendix A, «полные компоненты из v1.1»). НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. `sap_protocol.py`'s `sap_2_independence()` принимает уже готовое число `independence_vector: float` — раскладки на четыре компонента (IV-A информационная / IV-B мотивационная / IV-C сетевая / IV-D темпоральная независимость) не было, как и четырёх именованных «корпоративных ловушек», которые спека даёт с конкретными числовыми последствиями, а не общими словами. Appendix A прямо помечен как расширение краткой версии: «v1.2 содерж…
- **коды состояний** (4): `DEPENDENT`, `FULL`, `PARTIAL`, `ZERO`
- **тесты, которые зовут модуль**: 9 — `helix_pipeline/tests/test_frcp_gi_patch70.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_independence_vector.py`, `helix_pipeline/tests/test_market_math.py`, `helix_pipeline/tests/test_s1_calibrated_and_codes.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 28 | константа | `IVBand` |  |
| 31 | константа | `IV_FULL` |  |
| 32 | константа | `IV_PARTIAL_FLOOR` |  |
| 33 | константа | `IV_DEPENDENT_CEILING` |  |
| 35 | константа | `IV_FRCP_WIN_FLOOR` |  |
| 37 | константа | `TRAP4_IV_D_VALUE` |  |
| 41 | класс | `IVComponents (0 публичных методов)` | Четыре компонента Independence Vector (Appendix A), каждый 0.0-1.0. |
| 50 | класс | `CorporateTraps (0 публичных методов)` | Четыре именованные ловушки (Appendix A) — булевы флаги наблюдения. |
| 59 | класс | `IndependenceVectorResult (0 публичных методов)` |  |
| 70 | функция | `_clamp01(name, value)` |  |
| 76 | функция | `apply_corporate_traps(components, traps)` | Ловушки ПЕРЕЗАПИСЫВАЮТ соответствующий компонент, а не усредняются с |
| 99 | функция | `_band_for(iv)` | Спека даёт шкалу с двумя непокрытыми промежутками: (0.3, 0.6) и |
| 115 | функция | `independence_vector_compute(source_id, components, traps)` | IV = МИНИМУМ из IV-A/B/C/D после ловушек (Appendix A). Ревизия 22.10.2026: |
| 158 | функция | `independence_vector_summary()` | Сводка — для отчётов о готовности. |

## intelligence_extra_layers

- **путь**: `helix_pipeline/engine/intelligence_extra_layers.py`
- **размер**: 499 строк, SHA-256 blob `9b8b3c0a84a308f4…`
- **что это**: intelligence_extra_layers.py — научный (SL-1..SL-8) и литературный
- **зачем**: `literary_layer.py` и `deep_research.py` написаны и покрыты тестами, но с сайта не исполнялись. Здесь — одна точка подключения для оркестратора (`extra_layers_for_chain`) и разбор режима исследования (`research_mode_for_chain`). Модуль НЕ делает вызовов моделей: он работает поверх того, что цепочка уже получила, — результата `IntelligenceVector.investigate()` и слоя протоколов (`research["protocols_layer"]`, один вызов разметчика).
- **коды состояний** (15): `ABSENT`, `EXTRA_LAYERS_KEY`, `EXTRA_LAYERS_PROMPT_ADDENDUM`, `FAILED`, `HYPNOSIS`, `LEADING_QUESTIONS`, `NGI`, `NOT_APPLICABLE`, `NOT_RUN`, `RAN`, `REPEATED_INSISTENT_SESSIONS`, `SSC`, `SSD`, `SUGGESTIVE_PRESSURE`, `THERAPEUTIC_TEMPLATES`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_intelligence_extra_layers.py`, `helix_pipeline/tests/test_intelligence_protocol_inputs.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 71 | константа | `EXTRA_LAYERS_KEY` | строка: «extra_layers» |
| 75 | константа | `SUGGESTIVE_PRESSURE` | tuple, 4 элементов |
| 78 | константа | `_TRI_KEYS` | tuple, 3 элементов |
| 80 | константа | `_STR_KEYS` | tuple, 1 элементов |
| 81 | константа | `_LIST_KEYS` | dict, 2 элементов |
| 85 | константа | `EXTRA_LAYER_KEYS` | frozenset(_TRI_KEYS + _STR_KEYS + tuple(_LIST_KEYS) + ('suggestive_pressure',)) |
| 88 | константа | `EXTRA_LAYERS_PROMPT_ADDENDUM` | строка: «
ДОПОЛНИТЕЛЬНО (научный и литературный слои GI). Верни поле верхнего у» |
| 107 | класс | `ExtraLayerLabelsError (0 публичных методов)` | Метки extra_layers нарушили контракт — отвергаются целиком. |
| 111 | функция | `_tri(v, path)` |  |
| 116 | функция | `parse_extra_layer_labels(raw)` | Строгая проверка `extra_layers`. None → None (меток нет). |
| 158 | функция | `_rule_ran(res, inputs)` | RAN: правило вычислено. `res` — SLResult/LLResult, список или None |
| 170 | функция | `_rule_not_run(reason)` |  |
| 176 | функция | `_rule_na(reason)` |  |
| 182 | функция | `_layer(rules, sources, empty_reason)` |  |
| 198 | функция | `_failed(e)` |  |
| 206 | функция | `_inputs(rr, labels)` | Метки и выполненные протоколы. |
| 236 | функция | `_no_layer_reason(inp)` |  |
| 243 | константа | `_EXTRA_MISSING` | строка: «метка extra_layers.{0} не получена: разметчик INTELLIGENCE её пока не » |
| 247 | функция | `_extra_field(inp, name)` |  |
| 253 | функция | `_science(inp)` |  |
| 348 | функция | `_per_item_rule(items, tri_key, fn, field_name, none_reason)` |  |
| 375 | функция | `_literary(rr, inp)` |  |
| 425 | функция | `extra_layers_for_chain(research_result)` | Научный и литературный слои над результатом INTELLIGENCE. |
| 455 | функция | `research_mode_for_chain(research_mode)` | Проверить режим до запуска и назвать цену. Не бросает, не звонит. |
| 497 | константа | `__all__` | list, 7 элементов |

## intelligence_protocol_inputs

- **путь**: `helix_pipeline/engine/intelligence_protocol_inputs.py`
- **размер**: 1363 строк, SHA-256 blob `846092fce508b7fc…`
- **что это**: intelligence_protocol_inputs.py — протоколы INTELLIGENCE §3 на живом пути.
- **зачем**: `IntelligenceVector.investigate()` + `round_gate` + научные базы. Протоколы §3 (SAP, WPL, PDE, NGI, ANI, SSD, APORIA, MPF, EFR, TIE, SDF, SAD, CHF, ICoI…) написаны и покрыты тестами, но с сайта не запускались ни разу; процедура §4–§9 (`IntelligenceVector.prioritize/classify_hitl/compile_report/ check_exit`) — тоже. Причина та же, что у TRACE до `trace_classifier.py`: протоколы принимают УЖЕ классифицированные признаки, а классификатора из сырого текста не было.
- **спека-якорь**: `HELIX_INTELLIGENCE_v2_1.md`
- **коды состояний** (111): `AGGREGATOR_UNVERIFIED`, `AI_OUTPUT`, `AMPLIFIED`, `ANI`, `ANI_CRITICAL`, `ANI_MONITOR`, `ANNOTATED`, `ANONYMITY`, `ANONYMOUS`, `APORIA`, `APORIA_CRITICAL`, `APORIA_MONITOR`, `BEFORE_OR_AT_EVENT`, `CDR`, `CDR3_MONITOR`, `CHF`, `CHF_COMPOUND_HIGH`, `CHF_D_ACTIVE`, `CLEAN`, `COERCIVE`, `COMPRESSED`, `COMPROMISED`, `CONFIRMED_BY_OTHER_SOURCE`, `CONTRADICTED_BY_OTHER_SOURCE`, `CRITICAL`, `DIRECT`, `DOCUMENT`, `EFR`, `EFR_NGI_CRITICAL`, `EMOTIONAL`, `EXCERPTED`, `EXPERT`, `EXTANT`, `FAILED`, `FINANCIAL`, `FIRST_24H`, `FIRST_MONTH`, `FIRST_WEEK`, `FRCP`, `HIGH`, `HIL`, `HMP`, `IDENTIFIED`, `IFM`, `INHERITED`, `INSTITUTIONAL`, `INT`, `INTERPRETED`, `LATER`, `LOST`, `MODERATE`, `MPF`, `NEUTRAL`, `NGI`, `NODES_3_5`, `NOT_ASSESSED`, `NOT_RUN`, `NO_EXTERNAL_DATA`, `OFFICIAL_STATEMENT`, `ONE_TO_SIX_MONTHS`, `OVER_TWO_YEARS`, `PARTIAL`, `PDE`, `PDE_DECAY`, `POLITICAL`, `PPEP`, `PRE_LOCK_MONITOR`, `PRIMARY`, `PROVIDER_NOT_CONFIGURED`, `PROXIMATE`, `PSEUDONYMOUS`, `RAN`, `RDI`, `RECONSTRUCTED`, `RECOVERED`, `REDACTED`, `REFRAMED`, `RELATIONAL`, `RELAY`, `REPUTATIONAL`, `RPL`, `SAD`, `SAD2_STRATEGIC`, `SDF`, `SECONDARY`, `SECONDARY_REPORT`, `SECURE`, `SIX_MONTHS_TO_TWO_YEARS`, `SKIPPED`, `SOCIAL`, `SSC`, `SSD`, `SSD_FAIL`, `STRUCTURAL`, `TELP`, `TEMPORAL`, `TIE`, `TIE1_IMPOSSIBLE_WINDOW`, `TRANSLATED`, `UNCERTAIN`, `UNCLEAR`, `UNDER_WEEK`, `UNKNOWN`, `UNVERIFIED`, `UNVERIFIED_NODES`, `VERIFIED`, `VERIFIED_1_2`, `WEEK_TO_MONTH`, `WITNESS`, `WPL`, `WPL_CRITICAL`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_intelligence_extra_layers.py`, `helix_pipeline/tests/test_intelligence_protocol_inputs.py`, `helix_pipeline/tests/test_две_оси.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 50 | константа | `IDENTITY` | tuple, 4 элементов |
| 51 | константа | `SOURCE_KIND` | tuple, 7 элементов |
| 53 | константа | `PRIMACY` | tuple, 3 элементов |
| 54 | константа | `DATE_RELATION` | tuple, 6 элементов |
| 56 | константа | `ICOI_TIER` | tuple, 5 элементов |
| 57 | константа | `MOTIVES` | tuple, 5 элементов |
| 58 | константа | `EXTERNAL_CHECK` | tuple, 3 элементов |
| 60 | константа | `FIRSTHAND` | tuple, 5 элементов |
| 61 | константа | `INHERITANCE` | tuple, 5 элементов |
| 62 | константа | `TEMPORAL_DELAY` | tuple, 5 элементов |
| 64 | константа | `CONTAMINATION` | tuple, 5 элементов |
| 65 | константа | `ORIGIN_STATUS` | tuple, 6 элементов |
| 67 | константа | `ARCHIVE` | tuple, 5 элементов |
| 68 | константа | `EDITORIAL` | tuple, 7 элементов |
| 70 | константа | `TRANSMISSION` | tuple, 4 элементов |
| 71 | константа | `REHOSTING` | tuple, 5 элементов |
| 73 | константа | `AC_INDICATORS` | tuple((f'AC-I-0{i}' for i in range(1, 8))) |
| 74 | константа | `MW_TACTICS` | tuple((f'MW-TAC-{i}' for i in range(1, 7))) |
| 75 | константа | `SP_FORMS` | tuple((f'SP-FORM-{i}' for i in range(1, 6))) |
| 83 | константа | `ALLOWED_COUNT_KEYS` | frozenset({'index', 'source_indices', 'months_after_event', 'relay_depth', 'stat |
| 91 | константа | `ORDINAL_0_3_KEYS` | frozenset({'emotional', 'political', 'archetypal', 'industry'}) |
| 95 | константа | `FORBIDDEN_KEYS` | frozenset({'score', 'scores', 'confidence', 'band', 'verdict', 'level', 'risk',  |
| 105 | константа | `FORBIDDEN_PREFIXES` | tuple, 6 элементов |
| 106 | константа | `FORBIDDEN_SUFFIXES` | tuple, 7 элементов |
| 108 | константа | `STATE_FIELDS` | tuple, 4 элементов |
| 113 | константа | `INTELLIGENCE_LABELS_SYSTEM_PROMPT` | строка: «Ты — HELIX INTELLIGENCE Protocol Labeler.
Прочитай итоговый текст расс» |
| 248 | константа | `PROVIDER` | строка: «google» |
| 249 | константа | `CLASSIFIER_MAX_TOKENS` |  |
| 250 | константа | `DEFAULT_ATTEMPTS` |  |
| 252 | константа | `NOT_CONFIGURED_MESSAGE` | строка: «Провайдер не настроен на бэкенде (ни ключа Google/Gemini, ни Azure). Р» |
| 258 | класс | `IntelligenceLabelsNotConfigured (0 публичных методов)` | Нет провайдера — лечится настройкой, не повтором. |
| 262 | класс | `IntelligenceLabelsCallFailed (0 публичных методов)` | Провайдер не ответил / ответил пустым текстом. |
| 266 | класс | `IntelligenceLabelsError (0 публичных методов)` | Ответ нарушил контракт: не JSON, запрещённое поле, число вне |
| 273 | функция | `_caller_for(api_key)` | Вызов через `api.provider_gateway.шлюз_для_поиска` — решение владельца |
| 287 | функция | `_default_caller(system, prompt, max_tokens)` | Шов для тестов (монкипатч), как в trace/governance классификаторах. |
| 292 | функция | `_sources_block(sources)` |  |
| 301 | класс | `IntelligenceProtocolClassifier (2 публичных методов)` | Разметка итогового текста INTELLIGENCE для протоколов §3. |
| 374 | функция | `_forbidden_key(key)` |  |
| 380 | функция | `_walk_numbers(node, path, parent_key)` | Запрещённые ключи и числа вне разрешённого — по всему дереву. |
| 419 | функция | `_check_enum(value, allowed, path, nullable)` |  |
| 428 | функция | `_check_enum_list(value, allowed, path)` |  |
| 437 | функция | `_check_tri(value, path)` |  |
| 442 | константа | `TOP_LEVEL_KEYS` | tuple, 12 элементов |
| 449 | константа | `_WITNESS_ENUMS` | dict, 3 элементов |
| 451 | константа | `_DOCUMENT_ENUMS` | dict, 5 элементов |
| 454 | константа | `SDF_BOOL_LABELS` | tuple, 17 элементов |
| 467 | функция | `parse_labels(raw)` | JSON модели → провалидированная разметка. Любое нарушение — исключение, |
| 548 | функция | `_plain(obj)` | Датакласс/enum → JSON-совместимое. |
| 561 | функция | `_not_run(reason)` |  |
| 567 | функция | `_missing(block, fields)` |  |
| 573 | функция | `_per_item(protocol, ran, skipped, feeds, no_items_reason)` |  |
| 587 | функция | `_source_meta(research_result, idx)` |  |
| 599 | константа | `SAP4_SCORE` | dict, 4 элементов |
| 604 | функция | `_sap4_score(relation, months)` | «Позже (–0.05 за месяц): score ≤ 0.6». Читается как 0.7 − 0.05·месяцы, |
| 616 | функция | `_run_source_protocols(rr, src_labels, ngi_level, ani_warning)` |  |
| 801 | функция | `_run_claims_sap6(rr, claims)` |  |
| 827 | функция | `_run_global_protocols(lab)` | NGI → SSD → MPF → (M3) → ANI → APORIA → EFR(M5) → CHF → TIE → SAD. |
| 1026 | константа | `NOT_RUN_FROM_TEXT` | dict, 26 элементов |
| 1061 | функция | `_collect_triggers(p)` | PPS-триггеры и HITL-условия — ТОЛЬКО из результатов выполненных |
| 1133 | константа | `_HITL_KEEP` | tuple, 10 элементов |
| 1137 | константа | `_EXIT_UNSUPPLIED` | tuple, 12 элементов |
| 1153 | функция | `_run_procedure(rr, protocols, phase)` |  |
| 1278 | функция | `run_intelligence_protocols(research_result, labels)` | Чистая функция: метки → протоколы §3 → процедура §4–§9. |
| 1327 | функция | `intelligence_protocols_for_chain(research_result)` | Точка вызова из оркестратора после INTELLIGENCE. НИКОГДА не бросает. |

## intelligence_sap

- **путь**: `helix_pipeline/engine/intelligence_sap.py`
- **размер**: 287 строк, SHA-256 blob `137d36a2057607f5…`
- **что это**: intelligence_sap.py — SAP §3.1 из HELIX_INTELLIGENCE_v2_1: аутентификация
- **зачем**: источника для расследования. ## ЭТО НЕ ДУБЛИКАТ sap_protocol.py. НОМЕРА СОВПАДАЮТ, ПРОТОКОЛЫ РАЗНЫЕ. Найдено 20.08.2026 аудитом контракта возвратов. Две спеки называют своими именами РАЗНЫЕ проверки под одними номерами: номер GI v6.2 (Патч 71) HELIX_INTELLIGENCE §3.1 ───── ──────────────────── ──────────────────────────── SAP-4 временная оценка, число темпоральная близость: полосы PRIMARY / DELAYED / CRITICAL SAP-5 Exception Pathway внутренняя согласованность: (PASS/FAIL → ECT-4) PASS / FLAG / CENTRAL FLAG / FAIL SAP-6 д…
- **спека-якорь**: `HELIX_INTELLIGENCE_v2_1.md`
- **коды состояний** (18): `ANON`, `CLEAN`, `COERCIVE`, `CRITICAL`, `DELAYED`, `FAILED`, `FINANCIAL`, `FLAG`, `HIGH`, `LOW`, `NEUTRAL`, `PARTIAL`, `POLITICAL`, `PRIMARY`, `RELATIONAL`, `REPUTATIONAL`, `VERIFIED`, `ZERO`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_helix_contract_audit.py`, `helix_pipeline/tests/test_intelligence_sap.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 46 | константа | `IdentityType` |  |
| 48 | константа | `CONTINUITY_PASS` |  |
| 49 | константа | `CONTINUITY_PARTIAL_FLOOR` |  |
| 50 | константа | `COERCION_PASS_MAX` |  |
| 51 | константа | `WPL_UNVERIFIED_DEPTH` |  |
| 55 | класс | `SAPVerdict (0 публичных методов)` |  |
| 63 | функция | `sap_1_identity()` | Кто именно этот источник — не что он говорит (§3.1 SAP-1). |
| 99 | константа | `IV_HIGH_FLOOR` |  |
| 100 | константа | `IV_DEPENDENT_CEIL` |  |
| 101 | константа | `IV_FRCP_FLOOR` |  |
| 104 | функция | `sap_2_independence()` | IV = МИНИМУМ четырёх компонентов (ревизия 22.10.2026, реестр INTELLIGENCE). |
| 145 | константа | `MOTIVE_TYPES` | tuple, 5 элементов |
| 147 | константа | `COERCION_MODERATE` |  |
| 148 | константа | `COERCION_HIGH` |  |
| 149 | константа | `COERCION_CRITICAL` |  |
| 150 | константа | `ICOI_STRUCTURAL_TRUST_CAP` |  |
| 153 | функция | `sap_3_motivation()` | Мотив ≠ ложь, но повышает стандарт верификации на 1 уровень ECT. |
| 197 | константа | `TEMPORAL_PDP_X_FLOOR` |  |
| 198 | константа | `TEMPORAL_ECT_PENALTY_FLOOR` |  |
| 201 | функция | `sap_4_temporal()` | Насколько источник близок к событию по времени (§3.1 SAP-4). |
| 228 | функция | `sap_5_internal_consistency()` | Противоречит ли источник сам себе (§3.1 SAP-5 у INTELLIGENCE). |
| 259 | константа | `DetailResult` |  |
| 262 | функция | `sap_6_detail()` | Подтверждается ли конкретная деталь внешними данными (§3.1 SAP-6). |

## intelligence_vector

- **путь**: `helix_pipeline/engine/intelligence_vector.py`
- **размер**: 998 строк, SHA-256 blob `09c021d893f1f2a8…`
- **что это**: intelligence_vector.py — собирающая точка входа вектора INTELLIGENCE.
- **зачем**: имя заранее — `helix_pipeline.engine.intelligence_vector.IntelligenceVector` — чтобы проверка `vector_is_available()` была честной: искала то, что должно быть, и до сих пор не находила. Протоколы GI v6.2 написаны (33-71 + мосты M1-M6, INT-6 отчёт, INT-9 EXIT PROTOCOL) и уже собраны фасадом `GICore` (`используется как GOVERNANCE, так и INTELLIGENCE» — см. её docstring), но ни одна не-тестовая точка входа с ИМЕНЕМ вектора не существовала: оркестратор не мог найти INTELLIGENCE и, значит, не мог его вызвать.
- **коды состояний** (8): `FAILED`, `HELIX_RESEARCH_PIPELINE`, `HELIX_SCHOLAR_SEARCH`, `NGI_HIGH`, `NOT_RUN`, `OFF`, `RAN`, `SSC1_RECANTATION`
- **тесты, которые зовут модуль**: 16 — `helix_pipeline/tests/test_deep_research.py`, `helix_pipeline/tests/test_hitl_matrix.py`, `helix_pipeline/tests/test_intelligence_extra_layers.py`, `helix_pipeline/tests/test_intelligence_vector.py`, `helix_pipeline/tests/test_investigate_rework_loop.py`, `helix_pipeline/tests/test_report_structure.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 52 | константа | `DEFAULT_RESEARCH_ROUNDS` |  |
| 58 | константа | `MAX_RESEARCH_ROUNDS` |  |
| 62 | константа | `RESEARCH_MAX_OUTPUT_TOKENS` |  |
| 69 | константа | `RESEARCH_ANSWER_DEFAULT_ECT_NOTE` | строка: «AI-вывод (синтезированный ответ) получает ECT-1 по умолчанию (INT §3.1» |
| 77 | константа | `_SYSTEM_INSTRUCTION` |  |
| 115 | константа | `_ПОДМЕНА_ЛИЧНОСТИ` | строка: «Ты — исследовательский модуль HELIX INTELLIGENCE.» |
| 117 | константа | `_ВЕКТОР_ЛИЧНОСТИ` | строка: «Ниже — метод твоего вектора INTELLIGENCE. Ты остаёшься Mr. Helix: голо» |
| 166 | константа | `_ГОЛОС_MR_HELIX` | строка: «6. Итоговый текст пишет Mr. Helix — живой следователь, а не отчёт сист» |
| 202 | функция | `_gateway_call_for(api_key)` | Собрать вызов шлюза, при наличии — с ключом ПОЛЬЗОВАТЕЛЯ (BYOK). |
| 227 | функция | `_default_gateway_call(system, prompt, max_tokens)` | Прежняя точка входа без ключа — оставлена: на неё ссылаются тесты. |
| 240 | функция | `конвейер_включён()` |  |
| 244 | функция | `режим_конвейера()` | "gemini" — обе роли у Gemini (ищейка и судья); "gemini_azure" — |
| 259 | функция | `_провайдер_роли()` | Провайдер этого разбора (новости сравниваются по провайдерам); иначе Gemini. |
| 265 | функция | `_судья_gemini(system, prompt, max_tokens)` |  |
| 270 | функция | `_поиск_gemini(system, prompt, max_tokens)` |  |
| 275 | функция | `_судья_azure(system, prompt, max_tokens)` |  |
| 281 | константа | `_ОТКАЗ` | re.compile("^\\W*(i['’]?m sorry\|i am sorry\|sorry,\|i can(?:no\|['’])t (?:help\|assi |
| 287 | функция | `_это_отказ_модели(текст)` | Короткий ответ, начинающийся с формулы отказа. Длинный текст, где |
| 294 | константа | `_ПУБЛИЦИСТИКА` | re.compile('опровергнуть (?:это \|факт )?можно (?:только\|лишь)\|не оставляет (?:ни |
| 300 | функция | `проверить_форму(текст)` | Форма отчёта судьи — числами: пометки уровней, объяснения к ним, |
| 322 | класс | `ResearchError (0 публичных методов)` | Исследование нельзя безопасно выполнить (нет ключа/провайдер отказал). |
| 326 | класс | `IntelligenceVector (7 публичных методов)` | Точка входа вектора INTELLIGENCE (см. модульный docstring). |

## investigator_icoi

- **путь**: `helix_pipeline/engine/investigator_icoi.py`
- **размер**: 195 строк, SHA-256 blob `b28ec77ffc3ebf2e…`
- **что это**: investigator_icoi.py — Патч 38: конфликт интересов СЛЕДОВАТЕЛЯ (GI v6.2, B2).
- **зачем**: ВАЖНОЕ РАЗГРАНИЧЕНИЕ (см. `ICOI_NAME_COLLISION`): аббревиатура ICoI занята в спеках дважды и означает РАЗНОЕ. Патч 38 (этот файл) — ICoI СЛЕДОВАТЕЛЯ: декларация из 4 пунктов, статусы PASS / PARTIAL / HIGH CONFLICT. Предмет — тот, кто расследует. INT v2.1 §3.22 — ICoI ИСТОЧНИКА: 5 типов с потолками Trust Score. Живёт в `sap_protocol.py` как SAP-3. Предмет — тот, о ком или от кого информация. Это не дублирование правила, а два разных правила под одним именем. Поэтому модуль назван `investigator_icoi`, а не `icoi`: имя …
- **коды состояний** (2): `DIRECT`, `INDIRECT`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_investigator_icoi_patch38.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 29 | константа | `ICOI_NAME_COLLISION` | строка: «ICoI означает разное в двух спеках: Патч 38 (GI v6.2) — конфликт интер» |
| 38 | класс | `ICoIStatus (0 публичных методов)` |  |
| 44 | класс | `ICoILevel (0 публичных методов)` | Уровень по одному пункту декларации. |
| 52 | класс | `InvestigatorDeclaration (0 публичных методов)` | 4 пункта декларации Патча 38. Заполняются при инициации расследования. |
| 85 | класс | `ICoIPoint (0 публичных методов)` | Результат по одному пункту. |
| 93 | класс | `ICoIResult (1 публичных методов)` |  |
| 108 | функция | `_classify_point(name, direct, indirect, direct_detail, indirect_detail)` |  |
| 117 | функция | `declare_investigator_icoi(d)` | Провести декларацию Патча 38 и выдать статус. |
| 193 | функция | `icoi_update_required(ifm_triggered)` | v5.9-интеграция Патча 38: «ICoI обновляется при IFM-4 CRITICAL». |

## language_mode

- **путь**: `helix_pipeline/engine/language_mode.py`
- **размер**: 211 строк, SHA-256 blob `5830854fb7cf2a8d…`
- **что это**: language_mode.py — языковой режим вывода (AK-INT-13).
- **зачем**: Правило спеки целиком: «Язык вывода = язык входного текста. Смешанный текст → основной язык текста определяет язык вывода. Маркеры (ECT, FRCP, SAP, etc.) = латиница всегда, независимо от языка. Объяснения, оценки, рекомендации = язык вывода.» ━━━ ПОЧЕМУ ЭТО НЕ КОСМЕТИКА ━━━ Отчёт на чужом языке читают хуже, а читают его люди, принимающие решение о публикации. Но опаснее другое: если переводить МАРКЕРЫ, они перестают быть опознаваемыми. `[ECT-4]` — это код, по которому две системы и человек понимают друг друга; «[ДКУ-4]» не поймёт никто, вкл…
- **коды состояний** (34): `ANI`, `APORIA`, `CDR`, `CHF`, `CLE`, `CPX`, `DYN`, `ECT`, `EFR`, `EXIT`, `FRCP`, `HIL`, `HITL`, `HMP`, `IFM`, `MPF`, `NGI`, `OAS`, `PDE`, `PPEP`, `PPS`, `RDI`, `RPL`, `SAD`, `SAP`, `SCA`, `SDF`, `SSC`, `SSD`, `STA`, `TELP`, `TIE`, `TLX`, `WPL`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_ak_int_patches.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 41 | константа | `AK_INT_13` | строка: «AK-INT-13: язык вывода = язык входного текста; смешанный текст — по ос» |
| 47 | константа | `WHY_MARKERS_STAY_LATIN` | строка: «Маркер — код, по которому две системы и человек понимают друг друга. П» |
| 54 | константа | `DOES_NOT_TRANSLATE` | строка: «Модуль определяет язык и защищает маркеры, но НЕ переводит. Определени» |
| 63 | константа | `DOMINANCE_THRESHOLD` |  |
| 67 | константа | `ALPHABETS` | dict, 3 элементов |
| 75 | константа | `MARKER_PREFIXES` | tuple, 50 элементов |
| 84 | константа | `_MARKER_RE` | re.compile('\\[([^\\[\\]]+)\\]') |
| 85 | константа | `_CYRILLIC` | re.compile('[а-яёА-ЯЁ]') |
| 88 | функция | `detect_language(text)` | Определить язык входного текста по долям алфавитов. |
| 149 | функция | `is_marker(token)` | Является ли содержимое квадратных скобок маркером системы. |
| 155 | функция | `markers_in(text)` | Все маркеры системы, найденные в тексте. |
| 161 | функция | `check_markers_untranslated(text)` | Проверить, что маркеры остались латиницей. |
| 185 | функция | `output_language_for(text)` | На каком языке писать отчёт по этому входу. |

## literary_layer

- **путь**: `helix_pipeline/engine/literary_layer.py`
- **размер**: 165 строк, SHA-256 blob `60b8bc1a7ea347f1…`
- **что это**: literary_layer.py — LL-1..LL-5: пять правил из литературы (Патч 62).
- **зачем**: Метод спеки назван прямо: «сжатая аналитическая экстракция — не цитирование». Из каждого автора взята не мысль и не цитата, а
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_intelligence_extra_layers.py`, `helix_pipeline/tests/test_literary_layer_and_oas.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 39 | константа | `LL_SOURCES` | dict, 5 элементов |
| 48 | константа | `LL2_NGI_THRESHOLD` |  |
| 50 | константа | `LL4_GROUP_TRUST` |  |
| 54 | класс | `LLResult (0 публичных методов)` |  |
| 61 | функция | `ll_1_confession()` | Признание — не финал расследования (Достоевский). |
| 76 | функция | `ll_2_blind_review()` | Остранение: читать материалы, не зная текущей H1 (Шкловский). |
| 93 | функция | `ll_3_ante_factum()` | Объяснял ли нарратив событие ДО того, как оно произошло (Талеб). |
| 110 | функция | `ll_4_systemic_pressure()` | Вся группа источников под системным давлением (Солженицын). |
| 140 | константа | `IMPERSONAL_OPERATORS` | frozenset({'', 'система', 'система решила', 'system', 'auto', 'автоматически', ' |
| 146 | функция | `ll_5_named_operator()` | Каждая OAS-запись обязана иметь именного автора (Арендт). |

## market_math

- **путь**: `helix_pipeline/engine/market_math.py`
- **размер**: 479 строк, SHA-256 blob `f945355c1b1ca5d5…`
- **что это**: market_math.py — детерминированный Math Engine вектора MARKET.
- **зачем**: ИСТОЧНИК. `HELIX_MARKET_v1_0.md` описывает MARKET как ОТДЕЛЬНЫЙ продукт («Создан как отдельный продукт. Не часть MR_HELIX», Раздел 15) со своей инфраструктурой (PostgreSQL, Neo4j, Redis, GPT-4o, Docker-compose, `helix_market/` как отдельный пакет) — та же ситуация, что была с «Частью II» TRACE (`risk_index.py`): отдельный, не построенный здесь backend, а не альтернативное правило для того же расчёта. Что реализовано здесь — только Раздел 8 (MATH ENGINE) плюс формулы разделов 3 (CAG), 4 (CNM), 5 (SAD), 6 (ICoI), 9 (HITL) — детермини…
- **спека-якорь**: `HELIX_MARKET_v1_0.md`
- **коды состояний** (16): `ADVISORY`, `CEO`, `CFO`, `CLEAR`, `CRITICAL`, `HIGH`, `HITL`, `HITL_REQUIRED`, `H_NULL`, `LOW`, `MEDIUM`, `MODERATE`, `NON_LIQUET`, `PARTIAL`, `REQUIRED`, `STRUCTURAL`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_cross_product_standards.py`, `helix_pipeline/tests/test_market_math.py`, `helix_pipeline/tests/test_market_vector.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 72 | константа | `SECTION_WEIGHTS` | dict, 6 элементов |
| 80 | константа | `DEFAULT_SECTION_WEIGHT` |  |
| 82 | константа | `EvidenceSourceType` |  |
| 85 | константа | `_EVIDENCE_POINTS` | dict, 4 элементов |
| 92 | класс | `EvidenceItem (0 публичных методов)` |  |
| 96 | функция | `compute_declared_confidence()` | §3: `raw = claim_count / max(1, word_count); return min(1, raw*weight*intensity)`. |
| 109 | функция | `compute_evidence_support(evidence_items)` | §3: сумма очков по типу источника, потолок 1.0. |
| 115 | константа | `CAG_LEVELS` | tuple, 5 элементов |
| 121 | функция | `compute_cag()` | §3: `CAG = declared_confidence - evidence_support`, зажато в [0, 1]. |
| 130 | функция | `cag_level(cag)` |  |
| 139 | константа | `CnmType` |  |
| 140 | константа | `CnmSeverity` |  |
| 142 | константа | `CNM_SEVERITY_WEIGHTS` | dict, 4 элементов |
| 143 | константа | `CNM_TYPE_MULTIPLIERS` | dict, 7 элементов |
| 147 | константа | `MANIPULATION_RISK_CAP` |  |
| 151 | класс | `CnmMarker (0 публичных методов)` |  |
| 157 | функция | `compute_manipulation_risk(cnm_markers)` | §4/§8: `sum(severity_weight × type_multiplier)`, потолок 25. |
| 178 | константа | `DocumentType` |  |
| 181 | константа | `EXPECTED_TOPICS` | dict, 7 элементов |
| 201 | константа | `SAD_TOPIC_RISK` | dict, 10 элементов |
| 208 | константа | `SAD_RISK_POINTS` | dict, 3 элементов |
| 209 | константа | `SAD_RISK_CAP` |  |
| 213 | класс | `SadResult (0 публичных методов)` |  |
| 218 | функция | `expected_topics_for(document_type)` |  |
| 225 | функция | `sad_topic_risk_for(topic)` |  |
| 229 | функция | `compute_missing_topics()` | §4 CNM-7 / §5: темы, ожидаемые для типа документа, но не найденные. |
| 235 | функция | `compute_sad_risk(sad_results)` | §5/§8: HIGH×6 + MEDIUM×3 + LOW×1, потолок 20. CRITICAL не входит в |
| 242 | функция | `critical_sad_count(sad_results)` |  |
| 248 | константа | `IcoiActorRole` |  |
| 251 | константа | `ICOI_RULES` | dict, 7 элементов |
| 268 | константа | `ICOI_TYPE_RISK_POINTS` | dict, 4 элементов |
| 269 | константа | `ICOI_RISK_CAP` |  |
| 272 | функция | `icoi_rule_for(actor_role)` |  |
| 279 | функция | `apply_track_record_modifier(base_cap, accurate_rate)` | §6: история точности прогнозов модифицирует trust_cap. `None` — нет |
| 293 | функция | `compute_icoi_risk(actor_roles)` | §6/§8: балл по типу ICoI, максимум среди всех источников документа — |
| 302 | функция | `has_structural_icoi(actor_roles)` |  |
| 306 | константа | `INDEPENDENCE_VECTOR_FLOOR` |  |
| 309 | функция | `compute_independence_vector()` | §6: `raw = unique_origins/len(sources); adjusted = raw*(1-cascade_factor)`, |
| 331 | константа | `BASE_RISK_CAP` |  |
| 332 | константа | `INDEPENDENCE_RISK_CAP` |  |
| 333 | константа | `MARKET_RISK_TOTAL_CAP` |  |
| 335 | константа | `RISK_LEVELS` | tuple, 5 элементов |
| 341 | класс | `MarketRiskBreakdown (1 публичных методов)` |  |
| 356 | функция | `compute_base_risk()` | §8: «ECT-1 × 3pts, ECT-2 × 1pt, ECT-4 × -1pt, max 20» — тот же принцип, |
| 363 | функция | `get_risk_level(index)` |  |
| 370 | функция | `compute_market_risk_index()` | §8: пять компонентов -> 0–100. Детерминировано — GPT-4o не вызывается. |
| 394 | константа | `AchWinner` |  |
| 395 | константа | `MIN_VERIFIED_CLAIMS` |  |
| 398 | функция | `determine_ach_winner()` | §7: победитель — детерминированная функция CAG и Market Risk Index, |
| 415 | константа | `SSD_UNFALSIFIABLE_PATTERNS` | tuple, 7 элементов |
| 421 | функция | `ssd_test(claim)` | §7: тест Поппера — нефальсифицируемые корпоративные шаблоны. |
| 431 | константа | `HitlStatus` |  |
| 432 | константа | `CRITICAL_SAD_HITL_THRESHOLD` |  |
| 433 | константа | `STRUCTURAL_ICOI_INDEPENDENCE_FLOOR` |  |
| 437 | класс | `HitlResult (0 публичных методов)` |  |
| 442 | функция | `determine_hitl_status()` | §9: REQUIRED останавливает публикацию; ADVISORY публикует с флагом. |

## market_text

- **путь**: `helix_pipeline/engine/market_text.py`
- **размер**: 22 строк, SHA-256 blob `736ff9e5b798aa9d…`
- **что это**: market_text.py — MARKET в HELIX по обычному тексту.
- **зачем**: Раньше HELIX принимал только готовую корпоративную анкету (`market_vector`), а разметчик текста жил только у Мистера Хеликса. Здесь — тот же разметчик (одна модель, Python проверяет цитаты и считает по HELIX_MARKET_v1_0), подключённый к HELIX без своей копии формул
- **спека-якорь**: `HELIX_MARKET_v1_0.md`
- **коды состояний** (1): `RAN`
- **тесты, которые зовут модуль**: 1 — `tests/test_helix_market_text.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 14 | функция | `разобрать_текст(текст, адреса, вызов)` |  |

## market_vector

- **путь**: `helix_pipeline/engine/market_vector.py`
- **размер**: 166 строк, SHA-256 blob `9b55a41cf001b520…`
- **что это**: market_vector.py — собирающая точка входа вектора MARKET.
- **зачем**: путь заранее — `helix_pipeline.engine.market_vector.MarketVector` — тем же приёмом, что и у TRACE/INTELLIGENCE. В отличие от них, MARKET не оборачивает `GICore`: его протоколы (CNM, SAD, ICoI-роли, Independence Vector) — самостоятельные, не переиспользуют GI v6.2 напрямую (см. `market_math.py`, Раздел 0 докстринга — CAG/CNM/ICoI-роли MARKET не совпадают по вокабуляру с ICoI-тирами GI-core). Общая точка — сама архитектура (ECT-веса, детерминизм,
- **спека-якорь**: `HELIX_MARKET_v1_0.md`
- **коды состояний** (2): `CEO`, `HIGH`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_market_vector.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 46 | константа | `DISCLAIMER` | строка: «This is not financial advice. This is a corporate narrative risk audit» |
| 51 | класс | `MarketAnalysisResult (0 публичных методов)` |  |
| 64 | класс | `MarketVector (1 публичных методов)` | Точка входа вектора MARKET (см. модульный docstring). |

## mpf

- **путь**: `helix_pipeline/engine/mpf.py`
- **размер**: 218 строк, SHA-256 blob `59f13e656fec98eb…`
- **что это**: mpf.py — Патч 52: фильтр моральной паники, MPF (GI v6.2, блок B4).
- **зачем**: паники свидетели, следователи и СМИ могут быть ПОЛНОСТЬЮ ИСКРЕННИМИ — и при этом системно производить ложные результаты. Ни IFM, ни PDP-X этого не обнаружат: они смотрят на индивидуальный уровень, а дефект здесь коллективный.
- **коды состояний** (1): `HITL`
- **тесты, которые зовут модуль**: 8 — `helix_pipeline/tests/test_aporia_scoa_ani_b5.py`, `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_exit_protocol_int9.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 36 | константа | `MPF_NGI_BOOST` |  |
| 38 | константа | `MPF_WHY` | строка: «В условиях моральной паники свидетели, следователи и СМИ могут быть по» |
| 45 | класс | `MPFBand (0 публичных методов)` |  |
| 53 | класс | `PanicContext (0 публичных методов)` | Контекст расследования по пяти критериям Коэна. |
| 76 | класс | `MPFCriterion (0 публичных методов)` |  |
| 84 | класс | `MPFResult (2 публичных методов)` |  |
| 110 | функция | `mpf_evaluate(c)` | Посчитать composite по 5 критериям и выдать предписания полосы. |

## mw_defense

- **путь**: `helix_pipeline/engine/mw_defense.py`
- **размер**: 178 строк, SHA-256 blob `f0e0ea78044a3dd0…`
- **что это**: mw_defense.py — MW-Defense Protocol: защитные процедуры против MW-TAC-1..6
- **зачем**: (INT §3.16 / TRACE Appendix E CHF EXTENSION). НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. `chf.py` (построен в этом же заходе) детектирует и эскалирует MW-TAC-1..6 (CHF-D фактор), но сама спека для каждой тактики даёт ещё и ЗАЩИТНУЮ ПРОЦЕДУРУ — что именно делать, а не только какой маркер поставить. Этих процедур не было нигде как структурированных данных/функций, только как маркеры детекции. ШЕСТЬ ПРОЦЕДУР (дословно из спеки, INT §3.16): MW-TAC-1 EPISTEMIC FLOODING → Criteria Triage: верифицировать 3 ключевых утверждения, не р…
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_mw_defense.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 40 | класс | `CriteriaTriageResult (0 публичных методов)` | MW-TAC-1: EPISTEMIC FLOODING → Criteria Triage. |
| 47 | функция | `criteria_triage(claims)` | Верифицировать первые `top_n` заявленных ключевых утверждений (порядок |
| 65 | класс | `TermLockResult (0 публичных методов)` | MW-TAC-2: SEMANTIC CAPTURE → зафиксировать оригинальное определение. |
| 73 | функция | `lock_term_definition(term, operational_definition, source_document)` | Зафиксировать операциональное определение термина ДО использования — |
| 89 | класс | `PreemptiveInoculationDefenseResult (0 публичных методов)` | MW-TAC-3: PRE-EMPTIVE INOCULATION → Red Team обязателен. |
| 96 | функция | `preemptive_inoculation_defense()` | Red Team всегда обязателен при обнаружении MW-TAC-3 — не условно. |
| 104 | класс | `GishListResult (0 публичных методов)` | MW-TAC-4: GISH GALLOP → Gish List. |
| 111 | функция | `gish_list(arguments)` | Записать ВСЕ аргументы, выбрать `top_n` наиболее сильных (порядок |
| 128 | класс | `NormalizationTimelineResult (0 публичных методов)` | MW-TAC-5: NORMALIZATION CREEP → задокументировать timeline сдвига. |
| 134 | функция | `document_normalization_timeline(events)` | Спека не даёт для MW-TAC-5 отдельной 'MW-Defense:' процедуры (в |
| 149 | класс | `LiarsDividendDefenseResult (0 публичных методов)` | MW-TAC-6: LIAR'S DIVIDEND → независимая SCA + PDE для каждого доказательства. |
| 157 | функция | `liars_dividend_defense(evidence_ids)` | Независимая SCA и PDE обязательны для КАЖДОГО доказательства без |
| 171 | функция | `mw_defense_summary()` | Сводка — для отчётов о готовности. |

## ngi

- **путь**: `helix_pipeline/engine/ngi.py`
- **размер**: 111 строк, SHA-256 blob `bb56432b94148a88…`
- **что это**: ngi.py — NGI: нарративная гравитация (GI v6.2 / INT §3.15 / TRACE §4.3).
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. Расчёт NGI (4 измерения 0-3 → сумма 0-12 → уровень LOW/MODERATE/HIGH/CRITICAL) существовал только внутри `HelixGovernanceMath.calculate_ngi_score()` (governance_math.py) — GOVERNANCE-специфичного класса, который ни `IntelligenceVector`, ни `TraceVector` не импортируют. `gi_core.py` даёт только `get_ngi_actions()` — обязательные действия для УЖЕ ИЗВЕСТНОГО уровня, но нет пути от сырых NGI-Э/П/А/М измерений до уровня внутри самого TRACE/INTELLIGENCE вектора. Пороги здесь ДОСЛОВНО совпада…
- **коды состояний** (4): `CRITICAL`, `HIGH`, `LOW`, `MODERATE`
- **тесты, которые зовут модуль**: 9 — `helix_pipeline/tests/test_chain_diagnostics.py`, `helix_pipeline/tests/test_efr_patch50.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_math.py`, `helix_pipeline/tests/test_governance_service.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 33 | константа | `NGILevel` |  |
| 37 | константа | `NGI_THRESHOLDS` | dict, 4 элементов |
| 41 | константа | `_LEVEL_ORDER` | tuple, 4 элементов |
| 45 | константа | `NGI_CORP_TRIGGER_VALUE` |  |
| 49 | класс | `NGIScoreResult (0 публичных методов)` |  |
| 61 | функция | `_validate_dim(name, value)` |  |
| 67 | функция | `_level_for_total(total)` |  |
| 74 | функция | `ngi_score(emotional, political, archetypal, industry)` | 4 измерения → сумма 0-12 → уровень, плюс NGI-CORP WARNING (TRACE §4.3). |
| 105 | функция | `ngi_summary()` | Сводка — для отчётов о готовности. |

## oas

- **путь**: `helix_pipeline/engine/oas.py`
- **размер**: 225 строк, SHA-256 blob `497222af6e6db12a…`
- **что это**: oas.py — Патч 56: Operational Audit System, журнал решений расследования.
- **зачем**: ## ПОЧЕМУ ЭТОТ ФАЙЛ ПОЯВИЛСЯ Найдено 20.08.2026 аудитом контракта возвратов. На OAS ссылаются четыре разных механизма — LL-5 (именная ответственность, Арендт), MOFFATT-SHIELD (журнал как юридическая защита), Article 9 EU AI Act (audit log как доказательство должной осторожности), предпубликационный аудит перед EXIT PROTOCOL, — и самого журнала в движке не было. Ссылались на то, чего нет. Это худший вид пробела: каждый отдельный механизм выглядит построенным, потому что называет своё требование к журналу, а требование нек…
- **коды состояний** (29): `ACTIVE`, `ANI_CRITICAL`, `APORIA_CRITICAL`, `APORIA_WARNING`, `APPEALED`, `CDR_CASCADE`, `CONFIRMED`, `ECT_DOWNGRADE`, `ECT_UPGRADE`, `EPISTEMIC_LOCK`, `EXIT_PROTOCOL`, `FRCP_RESOLVED`, `FRCP_UNRESOLVED`, `HITL_TRIGGERED`, `ICOI_CONFLICT`, `IFM_2_CRITICAL`, `IFM_4_CRITICAL`, `IFM_5_CRITICAL`, `MPF_CRITICAL`, `NON_LIQUET`, `PPS_ORANGE`, `PPS_RED`, `PRE_LOCK_MONITOR`, `SOURCE_DEGRADED`, `SSD_FAIL`, `SSD_PASS`, `SUPERSEDED`, `TELP_DECLARED`, `TELP_REACTIVATED`
- **тесты, которые зовут модуль**: 9 — `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_gi_core.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_hitl_queue.py`, `helix_pipeline/tests/test_literary_layer_and_oas.py`, `tests/test_activation_map_last_steps.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 40 | константа | `Status` |  |
| 44 | константа | `OAS_EVENT_CATALOG` | dict, 25 элементов |
| 63 | константа | `HITL_REQUIRED_EVENTS` | frozenset({'FRCP_UNRESOLVED', 'SSD_FAIL', 'APORIA_CRITICAL', 'IFM_2_CRITICAL', ' |
| 70 | константа | `DEFAULT_APPEAL_CONDITION` | строка: «при появлении контрдоказательства ECT-3+» |
| 73 | константа | `IMPERSONAL_OPERATORS` | frozenset({'', 'система', 'система решила', 'system', 'auto', 'автоматически', ' |
| 80 | класс | `OASRecord (1 публичных методов)` |  |
| 104 | класс | `OASJournal (3 публичных методов)` | Журнал решений одного расследования. |

## oas_provenance

- **путь**: `helix_pipeline/engine/oas_provenance.py`
- **размер**: 235 строк, SHA-256 blob `788b3a251f111f78…`
- **что это**: oas_provenance.py — журнал решений переживает рестарт процесса.
- **зачем**: списке в памяти. В `helix_pipeline/api/main.py` это записано прямым текстом как долг:
- **коды состояний** (2): `AK_DATA_DIR`, `HELIX_PROVENANCE_DIR`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_oas_provenance.py`, `helix_pipeline/tests/test_oas_цепочка_sha256.py`, `tests/test_v16_tail_closure.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 54 | константа | `ENV_DIR` | строка: «HELIX_PROVENANCE_DIR» |
| 55 | константа | `DEFAULT_DIR` |  |
| 58 | константа | `GENESIS` |  |
| 59 | константа | `_ПОЛЯ_ЦЕПИ` | tuple, 2 элементов |
| 62 | функция | `chain_hash(prev, запись)` | SHA-256 от хеша предыдущей записи и канонического JSON этой (без полей цепи). |
| 69 | функция | `provenance_dir()` | Каталог журналов. Читается при каждом вызове, а не один раз при |
| 76 | функция | `_serialise(значение)` | Привести к тому, что понимает json. Datetime — в ISO 8601 с зоной. |
| 99 | класс | `ProvenanceWriter (6 публичных методов)` | Дописывает записи журнала в файл. Один файл на расследование. |
| 213 | функция | `_безопасное_имя(investigation_id)` | id расследования приходит снаружи и попадает в имя файла. |
| 225 | функция | `list_investigations(каталог)` | Какие расследования есть в журнале на диске. |
| 233 | функция | `load(investigation_id)` | Прочитать журнал расследования, записанный в прошлой жизни процесса. |

## outcome_matrix

- **путь**: `helix_pipeline/engine/outcome_matrix.py`
- **размер**: 331 строк, SHA-256 blob `75b0aa4c3ab37ff4…`
- **что это**: outcome_matrix.py — каркас матрицы исходов: пропуски и ложные тревоги
- **зачем**: У продукта есть вердикт — PASS / WARN / BLOCK / HITL_REQUIRED, — и нет измерения, сколько раз этот вердикт ошибся В КАЖДУЮ СТОРОНУ. Пока считается одно общее «прошло / не прошло», две противоположные ошибки складываются в одно число и взаимно маскируются: инструмент, который блокирует ВСЁ, и инструмент, который пропускает ВСЁ, могут показать одинаковую «точность».
- **коды состояний** (15): `APPROVAL`, `BLOCK`, `CLEAN`, `DEFERRED`, `DEFERRED_TO_HUMAN`, `FLAWED`, `FLAWED_APPROVAL`, `FLAWED_BLOCK`, `GATE_A_AND_SYSTEM_FAILURES`, `HITL_REQUIRED`, `NO_GROUND_TRUTH`, `UNKNOWN`, `VALIDATED_APPROVAL`, `VALIDATED_BLOCK`, `WARN`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_outcome_matrix.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 52 | константа | `ВЕРДИКТЫ` | tuple, 4 элементов |
| 55 | класс | `Действие (0 публичных методов)` | Во что вердикт превращается для читателя. |
| 74 | константа | `ДЕЙСТВИЕ_ПО_ВЕРДИКТУ` | dict, 4 элементов |
| 84 | класс | `Истина (0 публичных методов)` | Независимая разметка случая. НЕ вычисляется этим модулем. |
| 94 | класс | `Корзина (0 публичных методов)` |  |
| 107 | константа | `РЕШЁННЫЕ` | tuple, 4 элементов |
| 124 | константа | `ПРИЧИНА_ОТКЛОНЕНИЯ_ОТ_ОБРАЗЦА` |  |
| 128 | класс | `Случай (1 публичных методов)` | Один прогон: что подали, что система сказала, что было на самом деле. |
| 186 | функция | `_доля(числитель, знаменатель)` | Доля или `None`. НИКОГДА не ноль при пустом знаменателе. |
| 197 | класс | `МатрицаИсходов (8 публичных методов)` | Накопитель случаев. Считает только то, что есть чем считать. |
| 328 | константа | `__all__` | list, 8 элементов |

## pde

- **путь**: `helix_pipeline/engine/pde.py`
- **размер**: 279 строк, SHA-256 blob `c8dca403732e3095…`
- **что это**: pde.py — Патч 58: PDE, движок деградации происхождения (GI v6.2, блок B1).
- **зачем**: ПРИНЦИП спеки: «Подлинность ≠ Целостность происхождения». Слепое пятно, которое закрывает патч: документ может быть ПОДЛИННЫМ, а его доказательная сила — уничтоженной тем, что с ним случилось по дороге (переиздание, редактура, смена хранителя, репостинг через агрегатор). SAP этого не видит, CDR не видит. Канонический пример спеки: оригинал 1943 → уничтожен 1945 → пересъёмка 1944 (плёнка утеряна) → книга 1967 без источника → сборник 1991 «по материалам» → сайт 2003 «архивный документ» → ECT-4 в 2026. Отличие от WPL (Патч…
- **коды состояний** (20): `ANNOTATED`, `BROKEN_CHAIN`, `COMPROMISED`, `CONFIRMED_PROVENANCE`, `EXCERPTED`, `EXTANT`, `LOST`, `PARTIAL`, `PARTIAL_PROVENANCE`, `PDE_ENTROPY_CRITICAL`, `RECONSTRUCTED`, `RECOVERED`, `REDACTED`, `SECURE`, `TRANSLATED`, `UNCERTAIN`, `UNKNOWN`, `UNKNOWN_PROVENANCE`, `UNVERIFIED`, `VERIFIED`
- **тесты, которые зовут модуль**: 7 — `helix_pipeline/tests/test_cross_product_standards.py`, `helix_pipeline/tests/test_gi62_audit_regressions.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_pde_patch58.py`, `helix_pipeline/tests/test_s1_calibrated_and_codes.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `PDE_STABLE_FLOOR` |  |
| 33 | константа | `PDE_WARNING_FLOOR` |  |
| 34 | константа | `PDE_CRITICAL_FLOOR` |  |
| 35 | константа | `ENTROPY_CRITICAL_FAILED_DOCS` |  |
| 38 | класс | `OriginStatus (0 публичных методов)` |  |
| 47 | класс | `ArchiveUncertainty (0 публичных методов)` |  |
| 55 | класс | `EditorialIntervention (0 публичных методов)` |  |
| 65 | класс | `TransmissionIntegrity (0 публичных методов)` |  |
| 72 | класс | `RehostingClass (0 публичных методов)` |  |
| 81 | константа | `_COPY_DISTANCE` | dict, 5 элементов |
| 82 | константа | `_ORIGIN` | dict, 6 элементов |
| 87 | константа | `_CUSTODY` | dict, 3 элементов |
| 88 | константа | `_ARCHIVE` | dict, 5 элементов |
| 93 | константа | `_EDITORIAL` | dict, 7 элементов |
| 99 | константа | `_TRANSMISSION` | dict, 4 элементов |
| 103 | константа | `_REHOSTING` | dict, 5 элементов |
| 111 | класс | `ProvenanceChain (0 публичных методов)` | Восемь полей модели происхождения (Раздел I спеки). |
| 128 | класс | `PDEResult (1 публичных методов)` |  |
| 155 | функция | `_validate(doc)` | Бессмысленный вход не имеет права давать уверенный результат. |
| 173 | функция | `pde_evaluate(doc)` | PDE Score = 100 − Σ(штрафы). Вызывается при входе каждого документа |
| 249 | константа | `_BAND_CATEGORY` | dict, 4 элементов |
| 254 | константа | `CATEGORY_CODES` | dict, 4 элементов |
| 258 | функция | `_category(band, unverified_claim)` |  |
| 264 | функция | `pde_entropy_check(results)` | Патч 61 (кросс-линки): ≥2 документа FAILED → PDE ENTROPY CRITICAL, |

## pdp_x

- **путь**: `helix_pipeline/engine/pdp_x.py`
- **размер**: 253 строк, SHA-256 blob `fe0b0843157c586b…`
- **что это**: pdp_x.py — Патч 41: PDP-X, дрейф памяти источника (GI v6.2, блок B1).
- **зачем**: MEMORY PRESSURE DRIFT PROTOCOL. Активируется НЕ при грубых SSC-событиях, а при накопленных факторах, медленно деформирующих достоверность показаний источника, который по критериям SSC остаётся «активным». Ключевая оговорка спеки, вынесенная в поведение модуля: «PDP-X ≠ SAP-7 FAILED. PDP-X фиксирует УСЛОВИЯ деградации, не доказывает ложь.» Поэтому модуль возвращает условия и рекомендованные действия (свежее интервью, когнитивное интервью, аудит транскриптов) — и никогда не выносит вердикт о правдивости источника. Отличие от P…
- **спека-якорь**: `GI_v6_2_COMPLETE.md`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_gi62_audit_regressions.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_pdp_x_patch41.py`, `helix_pipeline/tests/test_s1_calibrated_and_codes.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `MDP1_CONTACT_THRESHOLD` |  |
| 39 | константа | `MDP4_PATTERN_THRESHOLD` |  |
| 40 | константа | `TRUST_PENALTY_TWO_FLAGS` |  |
| 41 | константа | `TRANSCRIPT_AUDIT_INTERVIEWS` |  |
| 44 | константа | `MDP6_IDENTIFICATION_TRUST_MULTIPLIER` |  |
| 47 | класс | `MDP (0 публичных методов)` |  |
| 57 | класс | `SourceInterviewHistory (0 публичных методов)` | Накопленные условия вокруг источника (входы, а не суждения). |
| 76 | класс | `MDPFlag (1 публичных методов)` |  |
| 88 | класс | `PDPXResult (1 публичных методов)` |  |
| 112 | функция | `pdp_x_evaluate(h)` | Оценить дрейф памяти источника по пяти факторам MDP. |

## phase9_runtime

- **путь**: `helix_pipeline/engine/phase9_runtime.py`
- **размер**: 233 строк, SHA-256 blob `e790239ead0e894c…`
- **что это**: phase9_runtime.py — GOVERNANCE §4.6: Phase 9 Runtime, когнитивные
- **зачем**: состояния AI-агента (LEM/MPE/SFE/SIL). НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ: четвёртый закрытый узел позиции 13 WORK_PLAN.md. Phase 9 упоминается по имени в нескольких местах пакета (risk_index.py's докстринг прямо говорит «нет phase9.py», governance_service.py's докстринг — «Phase 9 отсутствует полностью», report_structure.py включает `"phase9"` в опциональный список §7 GOVERNANCE- отчёта) — сам протокол отсутствовал. ЧЕТЫРЕ ДВИЖКА (спека §4.6, применяются к выводу AI-агента): LEM — Low Energy Mode, 5 состояний (BORE/DRIFT/RITUA…
- **коды состояний** (18): `BORE`, `CORRUPT`, `DEAD`, `DRIFT`, `ETHICAL`, `EXHAUST`, `FIXATE`, `INSTITUTION`, `MEME`, `PREGNANT`, `RITUAL`, `SHAME`, `SUPPRESS`, `TACTICAL`, `TEMPORAL`, `THERMAL`, `TRAUMA`, `VACUUM`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_phase9_runtime.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `LemState` |  |
| 46 | константа | `MpeSignal` |  |
| 47 | константа | `SfeSignal` |  |
| 48 | константа | `SilType` |  |
| 50 | константа | `_VALID_LEM` | frozenset({'BORE', 'DRIFT', 'RITUAL', 'EXHAUST', 'DEAD'}) |
| 51 | константа | `_VALID_MPE` | frozenset({'THERMAL', 'TEMPORAL', 'SUPPRESS', 'FIXATE', 'CORRUPT'}) |
| 52 | константа | `_VALID_SFE` | frozenset({'MEME', 'SHAME', 'INSTITUTION'}) |
| 53 | константа | `_VALID_SIL` | frozenset({'TACTICAL', 'ETHICAL', 'TRAUMA', 'VACUUM', 'PREGNANT'}) |
| 56 | константа | `SIL_VACUUM_SAD2_THRESHOLD` |  |
| 59 | функция | `_check_subset(values, valid, label)` |  |
| 67 | класс | `LEMResult (0 публичных методов)` |  |
| 73 | функция | `lem_evaluate(active_states)` |  |
| 85 | класс | `MPEResult (0 публичных методов)` |  |
| 92 | функция | `mpe_evaluate(active_signals)` |  |
| 108 | класс | `SFEResult (0 публичных методов)` |  |
| 113 | функция | `sfe_evaluate(active_signals)` |  |
| 124 | класс | `SILResult (0 публичных методов)` |  |
| 133 | функция | `sil_evaluate(active_types)` |  |
| 172 | класс | `Phase9Result (1 публичных методов)` |  |
| 196 | функция | `phase9_evaluate()` | §4.6 — четыре движка разом. Каждый параметр независим: пустой/не |
| 225 | функция | `phase9_summary()` |  |

## ppep

- **путь**: `helix_pipeline/engine/ppep.py`
- **размер**: 296 строк, SHA-256 blob `e39ab5ff6e9c6406…`
- **что это**: ppep.py — Патч 39: постпубликационные доказательства, PPEP (GI v6.2, B7).
- **зачем**: Единственный протокол, работающий ПОСЛЕ публикации. Всё остальное решает, можно ли публиковать; PPEP решает, что делать, когда материал уже вышел, а доказательство появилось потом. ПРИНЦИП ПАТЧА, ради которого он существует: **Признание ошибки при PPE-1 = методологическая добросовестность. Отказ обработать PPE-1 = нарушение Блока 4.** То есть отказ рассматривать новое доказательство — не осторожность, а дефект. 4 ТИПА СОБЫТИЙ: PPE-1 НОВОЕ ДОКАЗАТЕЛЬСТВО → SAP-цикл → ECT → FRCP с оригинальным выводом PPE-2 ДИСКВАЛИФИКАЦИЯ…
- **коды состояний** (2): `NON_LIQUET`, `RESOLVED`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_cross_product_standards.py`, `helix_pipeline/tests/test_ppep_patch39.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `CORRECTION_ECT_THRESHOLD` |  |
| 40 | константа | `PPEP_PRINCIPLE` | строка: «Признание ошибки при PPE-1 = методологическая добросовестность. Отказ » |
| 45 | константа | `COURT_STANDARD_NOTE` | строка: «Судебный стандарт ≠ журналистский стандарт. Противоположный приговор Н» |
| 52 | класс | `PPEType (0 публичных методов)` |  |
| 59 | класс | `PublicationOutcome (0 публичных методов)` |  |
| 68 | класс | `PostPublicationEvent (0 публичных методов)` | Событие после публикации. |
| 96 | класс | `PPEPResult (1 публичных методов)` |  |
| 115 | функция | `ppep_evaluate(e)` | Обработать постпубликационное событие по типу PPE-1..4. |
| 158 | функция | `_ppe_1(e, res)` | Новое доказательство: SAP → ECT → FRCP → решение по публикации. |
| 205 | функция | `_ppe_2(e, res)` | Дисквалификация источника: CDR-каскад по всем зависимым фактам. |
| 231 | функция | `_ppe_3(e, res)` | Контекстуальное изменение: вывод верен, но вводит в заблуждение. |
| 248 | функция | `_ppe_4(e, res)` | Процессуальное событие: суд решил по тем же фактам. |
| 273 | функция | `ppep_triggers_for_exit_protocol(publication_id, triggers, review_date)` | Пункт EXIT PROTOCOL, БЛОК 6: «PPEP-триггеры определены? Контрольная дата |

## protocol_interactions

- **путь**: `helix_pipeline/engine/protocol_interactions.py`
- **размер**: 397 строк, SHA-256 blob `57eaee946be81479…`
- **что это**: protocol_interactions.py — что происходит, когда протоколы GI встречаются.
- **зачем**: ## ПОЧЕМУ ЭТОТ ФАЙЛ ПОЯВИЛСЯ Найдено 20.08.2026 аудитом контракта возвратов. Спека GI v6.2 отводит взаимодействиям отдельные разделы (`RPL ↔ SAD`, `RDI ↔ TELP`, `PDE ↔ PPEP`, «КРИТИЧЕСКИЕ КОМБИНАЦИИ»), даёт каждому точное условие и свой маркер. В коде не было почти ничего: сами протоколы построены и покрыты тестами, а их СТЫКИ жили только как проза. Стык — не украшение. Главная его работа в том, что он отличает **находку от артефакта**: PDE WARNING при RPL DEGRADED — деградация провенанса или просто не было денег её про…
- **спека-якорь**: `GI_v6_2_COMPLETE.md`
- **коды состояний** (1): `HITL`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_protocol_interactions.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 43 | класс | `Interaction (0 публичных методов)` |  |
| 49 | функция | `rpl_x_sad()` | RPL ↔ SAD (Патч 45): третья причина молчания. |
| 67 | функция | `rpl_x_pde()` | RPL ↔ PDE (Патч 58): деградация провенанса или невозможность проверки. |
| 84 | функция | `rpl_x_wpl()` | RPL ↔ WPL (Патч 65): цепочка длинная — или денег хватило только на неё. |
| 98 | функция | `rpl_x_telp()` | RPL ↔ TELP (Патч 53): предел познаваемости или предел кошелька. |
| 123 | функция | `rpl_x_hil()` | RPL ↔ HIL (Патч 66): изоляция ускоряет слияние. |
| 138 | функция | `rpl_to_ani()` | RPL → ANI (Патч 47): истощение как состязательная атака. |
| 155 | константа | `RDI_IFM_CHECKLIST_DAYS` | dict, 3 элементов |
| 160 | функция | `rdi_x_ifm()` | RDI ↔ IFM (Патч 42): давление ускоряет все паттерны истощения. |
| 169 | функция | `rdi_x_telp()` | RDI ↔ TELP (Патч 53): «Мы не можем сказать что не знаем — нас ждут». |
| 186 | функция | `mpf_to_rdi()` | MPF → RDI (Патч 52): паника прибавляет к давлению +15. |
| 199 | функция | `rdi_x_non_liquet()` | RDI ↔ NON LIQUET: честный ответ под давлением. |
| 217 | функция | `rdi_x_pde()` | RDI ↔ PDE (Патч 58): «у нас нет времени проверять цепочку». |
| 238 | константа | `PDE_ENTROPY_CRITICAL_MIN` |  |
| 239 | константа | `PDE_ENTROPY_WARNING_MIN` |  |
| 242 | функция | `pde_entropy()` | Системная деградация доказательной базы (Патч 58). |
| 259 | функция | `pde_x_ppep()` | PDE ↔ PPEP (Патч 39): чем можно и чем нельзя пересмотреть ECT-4. |
| 274 | функция | `pde_to_telp2()` | PDE → TELP-2 (Патч 53): документальная невосполнимость. |
| 284 | функция | `hmp_x_telp()` | HMP ↔ TELP (Патч 53): «слишком много вложено, чтобы сказать не знаем». |
| 295 | функция | `hmp_x_tribunal()` | HMP ↔ Tribunal: при высокой цене отказа выводы пересматривает чужой. |
| 304 | функция | `hil_x_ifm()` | HIL ↔ IFM (Патч 66→42): слияние запускает каскад истощения. |
| 318 | функция | `hil_fusion_risk()` | Ранняя диагностика слияния по числу признаков (Патч 66). |
| 326 | функция | `wpl_chain_degradation()` | Дисторсия нарастает по ВСЕЙ цепочке, а не в одном звене (Патч 65). |
| 338 | функция | `wpl_x_tie()` | WPL ↔ TIE (Патч 48): каждый ретранслятор — точка temporal stitching. |
| 358 | функция | `critical_combinations()` | Пять критических комбинаций Патча 61. Каждая требует HITL. |

## rdi

- **путь**: `helix_pipeline/engine/rdi.py`
- **размер**: 531 строк, SHA-256 blob `ef899aa722b9a108…`
- **что это**: rdi.py — Патч 60: индекс долга разрешения (GI v6.2, блок B2).
- **зачем**: ЧТО ЭТО ЛОВИТ. Расследование идёт 18 месяцев. Семьи ждут ответа. Пресса спрашивает «когда результат?» каждую неделю. Бюджет истекает через 3 месяца. Доказательная база — ECT-3, вывода нет. NON LIQUET честен. И система начинает производить вывод не потому, что данные его требуют, а потому что ВРЕМЯ его требует. Это Resolution Debt — и ни IFM, ни HMP, ни TELP его не покрывают: следователь может быть свеж, институт — не заинтересован, предела познания ещё нет. Давит само ожидание. ━━━ ТРИ ПРОТОКОЛА ПОД ОДНИМ ИМЕНЕМ (см. `RDI_NAME_COLLI…
- **коды состояний** (1): `RDI_PRESSURE_LOG`
- **тесты, которые зовут модуль**: 9 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_exit_protocol_int9.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_intelligence_protocol_inputs.py`, `helix_pipeline/tests/test_rdi_patch60.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 39 | константа | `RDI_NAME_COLLISION` | строка: «Три разных вычисления называются RDI: Патч 60 (GI v6.2) — индекс давле» |
| 48 | константа | `DURATION_SCORE` | tuple, 4 элементов |
| 49 | константа | `DURATION_SCORE_MAX` |  |
| 50 | константа | `W_MEDIA` |  |
| 51 | константа | `W_INSTITUTIONAL` |  |
| 52 | константа | `W_STAKEHOLDER` |  |
| 53 | константа | `W_POLITICAL` |  |
| 54 | константа | `W_ANALYST` |  |
| 56 | константа | `W_BUDGET` |  |
| 57 | константа | `RDI_MAX` |  |
| 60 | класс | `RDIBand (0 публичных методов)` |  |
| 68 | класс | `InvestigationPressure (0 публичных методов)` | 7 переменных Патча 60. Уровни 0–4 — шкалы из спеки. |
| 93 | класс | `RDIResult (1 публичных методов)` |  |
| 117 | функция | `_duration_component(months)` |  |
| 126 | константа | `RESOLUTION_DEBT_TABLE` | dict, 7 элементов |
| 144 | функция | `rdi_evaluate(p)` | Патч 60: индекс долга разрешения 0–100. |
| 248 | класс | `FalseFinalityResult (0 публичных методов)` |  |
| 257 | функция | `false_finality_check(ect_current, ect_baseline_without_pressure)` | SHIELD-4: сравнить ECT под давлением с ECT, который был бы без давления. |
| 293 | функция | `rdi_pressure_log_entry(source, pressure_type, timestamp)` | SHIELD-2: запись внешнего запроса о сроках. |
| 311 | класс | `RDIDDBand (0 публичных методов)` |  |
| 319 | класс | `RDIDDResult (1 публичных методов)` |  |
| 336 | функция | `rdi_dd_evaluate(unresolved_ect_conflicts, skipped_hitl, closing_under_external_pressure)` | RDI-DD: долг неразрешённых конфликтов и пропущенных HITL (INT §3.24). |
| 389 | класс | `RDIDLBand (0 публичных методов)` |  |
| 396 | константа | `DL_COMPONENTS` | tuple, 6 элементов |
| 404 | константа | `DL_MAX` |  |
| 408 | класс | `RDIDLResult (1 публичных методов)` |  |
| 425 | функция | `rdi_dl_evaluate(levels)` | RDI-DL: давление дедлайнов, 6 компонентов по 0–5, сумма 0–30. |
| 476 | функция | `rdi_parallel_shields(dd, dl)` | AK-INT-09: при активных обоих протоколах SHIELD применяются ПАРАЛЛЕЛЬНО. |
| 503 | функция | `triple_lock_check(rdi_dd, hmp_lock_risk, ssd_result)` | INT §3.24: [TRIPLE LOCK: HMP + RDI-DD + SSD] → ST-18 Recovery Protocol. |

## report_structure

- **путь**: `helix_pipeline/engine/report_structure.py`
- **размер**: 353 строк, SHA-256 blob `e905079dcdc4f4a6…`
- **что это**: report_structure.py — структура выходного отчёта (INT §6 / TRACE §8).
- **зачем**: ━━━ НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ (TRACE-аудит) ━━━ До этой правки модуль знал только одну структуру — заголовок «HELIX INTELLIGENCE — ЭПИСТЕМИЧЕСКИЙ ОТЧЁТ» и восемь разделов INT §6 — и `TraceVector.compile_report()` пропускал через неё TRACE-отчёты тоже, хотя TRACE §8 задаёт СВОЙ заголовок («HELIX TRACE — RED TEAM АУДИТ»), свою версию формата (1.0, не 2.0) и другую разбивку B/C/D/E/G/H (INT: Анализ источников/Анализ фактов/Анализ нарратива/Конфликты и пределы/Карта доверия/Действия; TRACE: ICoI AUDIT/ACH-матрица/Факти…
- **коды состояний** (13): `ANI`, `APORIA`, `CHF`, `COMPLETE`, `EFR`, `HIL`, `HMP`, `INCOMPLETE`, `MPF`, `NGI`, `RDI`, `RPL`, `SAD`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_report_structure.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 66 | константа | `Product` |  |
| 68 | константа | `REPORT_TITLE` | строка: «HELIX INTELLIGENCE — ЭПИСТЕМИЧЕСКИЙ ОТЧЁТ» |
| 69 | константа | `TRACE_REPORT_TITLE` | строка: «HELIX TRACE — RED TEAM АУДИТ» |
| 70 | константа | `GOVERNANCE_REPORT_TITLE` | строка: «HELIX GOVERNANCE — AI COGNITIVE AUDIT REPORT» |
| 75 | константа | `REPORT_FORMAT_VERSION` | строка: «2.0» |
| 76 | константа | `TRACE_REPORT_FORMAT_VERSION` | строка: «1.0» |
| 77 | константа | `GOVERNANCE_REPORT_FORMAT_VERSION` | строка: «1.1» |
| 79 | константа | `ONE_DOCUMENT_RULE` | строка: «Всегда один документ. Маркеры ВСТРОЕНЫ в объяснение и не выносятся в о» |
| 86 | константа | `BUILDER_DOES_NOT_ASSESS` | строка: «Сборщик не анализирует и не оценивает: он раскладывает готовые результ» |
| 94 | класс | `SectionSpec (0 публичных методов)` | Один раздел отчёта: что в нём обязательно, а что по применимости. |
| 105 | константа | `REPORT_SECTIONS` | tuple, 8 элементов |
| 132 | константа | `BY_APPLICABILITY` | tuple, 2 элементов |
| 136 | константа | `TRACE_REPORT_SECTIONS` | tuple, 8 элементов |
| 159 | константа | `TRACE_BY_APPLICABILITY` | tuple, 1 элементов |
| 165 | константа | `GOVERNANCE_REPORT_SECTIONS` | tuple, 6 элементов |
| 185 | константа | `GOVERNANCE_BY_APPLICABILITY` | tuple, 1 элементов |
| 187 | константа | `_MARKER_RE` | re.compile('\\[[^\\[\\]]+\\]') |
| 191 | класс | `ReportInput (0 публичных методов)` | Готовые результаты протоколов. Сборщик их не считает, только раскладывает. |
| 202 | функция | `_fmt(value)` |  |
| 208 | функция | `_is_present(value)` | Отличить «не передано» от «передан честный ноль/False/пустая строка». |
| 228 | константа | `_PRODUCT_STRUCTURE` | dict, 3 элементов |
| 238 | функция | `build_report(inp)` | Собрать отчёт из разделов продукта (`inp.product` — восемь у |
| 311 | функция | `markers_are_embedded_not_listed(report)` | Проверить главное правило: маркеры внутри объяснений, не отдельным списком. |
| 341 | функция | `report_structure_summary(product)` | Сводка структуры — для отчётов о готовности. `product` — см. `ReportInput.product`. |

## reproducibility

- **путь**: `helix_pipeline/engine/reproducibility.py`
- **размер**: 322 строк, SHA-256 blob `ae5321692dcef4f8…`
- **что это**: reproducibility.py — замер воспроизводимости: один вход, много прогонов,
- **зачем**: Плавающий вердикт между двумя одинаковыми запросами здесь уже ловили вживую и лечили: `CLASSIFIER_TEMPERATURE = 0.0` в `governance_classifier.py`. **Правка есть, замера нет.** То есть до сих пор неизвестно, помогла ли она и насколько — а «мы это починили» без замера есть ровно то утверждение без проверки, которое продукт ловит у чужих текстов.
- **коды состояний** (8): `ALTERNATIVE`, `CRITICAL`, `HIGH`, `MEDIUM`, `NULL`, `PRIMARY`, `PYTHONHASHSEED`, `PYTHONPATH`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_reproducibility.py`, `tests/test_zenodo_deposit.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 50 | функция | `канон(значение)` | Устойчивое текстовое представление результата для сравнения. |
| 78 | класс | `ЗамерПовторов (5 публичных методов)` | Итог одного замера: сколько раз гоняли, сколько разных исходов вышло. |
| 133 | функция | `замерить(имя, вызов, повторов)` | Вызвать `вызов()` `повторов` раз и посчитать разные исходы. |
| 161 | функция | `замерить_в_отдельных_процессах(имя, код, повторов)` | То же, но каждый прогон — свой процесс Python. |
| 197 | класс | `ОтчётВоспроизводимости (4 публичных методов)` |  |
| 240 | функция | `замерить_детерминированные_части(повторов)` | Прогнать одинаковый вход через реальные движки продукта. |
| 308 | функция | `главная()` |  |
| 318 | константа | `__all__` | list, 7 элементов |

## research_discipline

- **путь**: `helix_pipeline/engine/research_discipline.py`
- **размер**: 184 строк, SHA-256 blob `cbbe58fa283343f1…`
- **что это**: research_discipline.py — дисциплина расследования, отдаваемая модели.
- **зачем**: Требование владельца 22.08.2026: «чтобы запуск был на этот конструкт
- **спека-якорь**: `HELIX_INTELLIGENCE_v2_1.md`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_research_discipline.py`, `helix_pipeline/tests/test_шкала_доверия.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `СПЕКА` |  |
| 50 | константа | `ШКАЛА_ECT` | строка: «ECT-4: ОЧЕНЬ ВЫСОКАЯ УВЕРЕННОСТЬ
  Факт задокументирован несколькими н» |
| 77 | константа | `ИСКЛЮЧЕНИЕ_ECT4` | строка: «Факт может получить ECT-4 при наличии ≥3 полностью независимых источни» |
| 86 | функция | `дисциплина_для_промпта()` | Блок дисциплины, вставляемый в системную инструкцию расследования. |
| 117 | функция | `_блок_из_спеки()` | Шкала, вырезанная из живого файла спецификации. |
| 163 | константа | `МОДЕЛЬ_РАССЛЕДОВАНИЯ` | строка: «gemini-3.1-pro-preview» |
| 166 | константа | `МОДЕЛЬ_ЗАПАСНАЯ` | строка: «gemini-2.5-pro» |
| 171 | константа | `ИНСТРУМЕНТ_ПОИСКА` | dict, 1 элементов |
| 174 | константа | `РЕЖИМЫ` | tuple, 2 элементов |
| 177 | функция | `модели_расследования()` | Порядок предпочтения моделей. Первая — та, что просит владелец. |
| 182 | константа | `__all__` | list, 10 элементов |

## risk_index

- **путь**: `helix_pipeline/engine/risk_index.py`
- **размер**: 256 строк, SHA-256 blob `5681e2bd06f81032…`
- **что это**: risk_index.py — Risk Index 0–100 (TRACE §5 / INT §3.30).
- **зачем**: ОБЩАЯ ФОРМУЛА ДЛЯ ДВУХ ПРОДУКТОВ. Заголовок INT §3.30 сам это объявляет: «Risk Index 0–100 · из MR. HELIX TRACE / Product Layer · только v2.1» — формула пришла из TRACE, INTELLIGENCE её переиспользует. Закрывает сразу два долга: TRACE Risk Index (новый, раздел спеки не имел вообще никакой реализации) и `int_layer` INT-3.30 в gi62_patch_manifest.yaml (был SPEC_ONLY: «символов в коде нет» — из-за этого report_structure.py печатает Раздел F с пометкой «[RISK INDEX: НЕ РЕАЛИЗОВАН — INT-3.30]» вместо чисел). РАСХОЖДЕНИЕ СПЕК (зафиксировано, н…
- **спека-якорь**: `HELIX_TRACE_MERGED.md`
- **коды состояний** (7): `CATASTROPHIC`, `CRITICAL`, `HIGH`, `LOW`, `MODERATE`, `PARTIAL`, `STRUCTURAL`
- **тесты, которые зовут модуль**: 11 — `helix_pipeline/tests/test_gi_core.py`, `helix_pipeline/tests/test_intelligence_protocol_inputs.py`, `helix_pipeline/tests/test_intelligence_vector.py`, `helix_pipeline/tests/test_market_math.py`, `helix_pipeline/tests/test_report_structure.py`, `helix_pipeline/tests/test_reproducibility.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 69 | константа | `Spec` |  |
| 70 | константа | `IcoiTier` |  |
| 72 | константа | `BASE_RISK_CAP` |  |
| 73 | константа | `ICOI_RISK_CAP` |  |
| 74 | константа | `HYPOTHESIS_RISK_CAP` |  |
| 75 | константа | `PRESSURE_RISK_CAP` |  |
| 76 | константа | `MANIPULATION_RISK_CAP` |  |
| 77 | константа | `TOTAL_CAP` |  |
| 80 | константа | `_HMP_HIGH_BANDS` | set, 2 элементов |
| 81 | константа | `_HMP_LOCK_BAND` | строка: «HMP LOCK RISK» |
| 83 | константа | `RDI_BAND_POINTS` | dict, 4 элементов |
| 86 | константа | `ANI_BAND_POINTS` | dict, 4 элементов |
| 90 | константа | `RISK_LEVELS` | tuple, 5 элементов |
| 105 | константа | `RISK_MARKER` | dict, 5 элементов |
| 115 | константа | `PPS_OVERLOAD_TRIGGER_COUNT` |  |
| 119 | класс | `RiskIndexResult (1 публичных методов)` |  |
| 143 | функция | `base_risk()` | BASE RISK (0–30): ECT-1 ×3 + ECT-2 ×1 − ECT-4 ×1, зажато в диапазон. |
| 149 | константа | `_ICOI_TIER_POINTS` | dict, 4 элементов |
| 152 | функция | `icoi_risk()` | ICoI RISK (0–20). Комбо-условие +20 различается по спеке — см. докстринг модуля. |
| 163 | функция | `hypothesis_risk()` | HYPOTHESIS RISK (0–20). «HMP HIGH»/«HMP LOCK» — см. докстринг модуля |
| 178 | функция | `pressure_risk()` | PRESSURE RISK (0–15): полоса RDI напрямую задаёт балл. |
| 186 | функция | `manipulation_risk()` | MANIPULATION RISK (0–15). `combo_trigger` — уже определённое вызывающим |
| 201 | функция | `risk_level(total)` |  |
| 210 | функция | `compute_risk_index()` | Собрать все пять компонентов в итоговый Risk Index 0–100. |

## round_gate

- **путь**: `helix_pipeline/engine/round_gate.py`
- **размер**: 650 строк, SHA-256 blob `5b74db71dce54ffc…`
- **что это**: round_gate.py — гейт между раундами: выдумка не доживает до следующего раунда.
- **зачем**: Найдено владельцем 22.08.2026. Цикл поиска склеивал в промпт следующего раунда ПОЛНЫЙ ТЕКСТ всех предыдущих (`intelligence_vector._round_prompt`):
- **коды состояний** (8): `ACCEPTED`, `DERIVED`, `EMPTY`, `GROUNDED`, `HYPOTHESIS`, `NFKC`, `REWORK`, `UNGROUNDED`
- **тесты, которые зовут модуль**: 8 — `helix_pipeline/tests/test_deep_research.py`, `helix_pipeline/tests/test_intelligence_vector.py`, `helix_pipeline/tests/test_round_gate.py`, `helix_pipeline/tests/test_round_gate_ect.py`, `helix_pipeline/tests/test_конвейер_gemini_azure.py`, `helix_pipeline/tests/test_починка_06_10.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 61 | класс | `Класс (0 публичных методов)` | Чем утверждение является — и это НЕ одно и то же. |
| 94 | класс | `Вердикт (0 публичных методов)` | Что гейт говорит о раунде. |
| 112 | константа | `МИН_УВЕРЕННОСТЬ` |  |
| 116 | константа | `ПУСТЫХ_РАУНДОВ_ДО_ОСТАНОВКИ` |  |
| 121 | константа | `_НЕ_ФАКТ` | re.compile('^(?:[01]\|20\\d\\d)$') |
| 129 | константа | `_НЕ_ФАКТ_ПРЕФИКС` | re.compile('(?:\\barxiv\\s*:?\|\\b(?:стать[яи]\|ст\\.\|article\|art\\.\|§\|пункт[а-я]* |
| 138 | константа | `_ЗАГОЛОВОК_ПЕРЕД_ЧИСЛОМ` | re.compile('\\s*#{1,6}\\s*$') |
| 141 | функция | `_номер_пункта_списка(текст, начало, конец)` | «2. Текст» или «3) Текст» в начале строки — номер пункта, не факт. |
| 150 | функция | `_после_заголовка(текст, начало)` |  |
| 160 | константа | `_МАРКЕРЫ_ГИПОТЕЗЫ` | re.compile('\\b(?:верси\|гипотез\|предполож\|вероятн\|возможно\|похоже\|по\\s+оценк\|оц |
| 170 | константа | `_МАРКЕРЫ_ВЫВОДА` | re.compile('\\b(?:следовательн\|значит\|отсюда\|итого\|в\\s+сумме\|разница\|расхождени |
| 177 | класс | `Утверждение (1 публичных методов)` | Одно атомарное утверждение, извлечённое из текста раунда. |
| 199 | класс | `ПроверкаРаунда (6 публичных методов)` | Итог гейта по одному раунду. |
| 260 | константа | `_ШАБЛОНЫ` | tuple, 5 элементов |
| 276 | функция | `_нормализовать(s)` | Одинаковое написание для сравнения: неразрывные пробелы, регистр. |
| 286 | константа | `_СОКРАЩЕНИЕ_ПЕРЕД_ТОЧКОЙ` | re.compile('(?:^\|[\\s(«\\"$€£₽~≈\\d])(?:тыс\|млн\|млрд\|трлн\|руб\|долл\|коп\|ок\|др\|пр\| |
| 293 | константа | `_НОМЕР_ПУНКТА` | re.compile('(?:^\\s*(?:#{1,6}\\s*\|[-*]\\s*)?\|[.!?]\\s+)\\d{1,3}$') |
| 296 | функция | `_границы_предложений(текст)` | Позиции начала каждого предложения. |
| 323 | функция | `_предложение_вокруг(текст, начало)` | Предложение, в которое попадает КОНКРЕТНОЕ вхождение — по позиции |
| 345 | функция | `извлечь_утверждения(текст)` | Разобрать текст на атомарные утверждения, требующие источника. |
| 399 | функция | `_подкреплённые_куски(supports, источники)` | (нормализованный текст куска, uri источника) для каждого подкрепления. |
| 419 | функция | `_содержит(текст, значение)` | Значение входит в текст ЦЕЛЫМ числом: «3» не подкреплено куском |
| 428 | функция | `проверить_раунд(номер, ответ)` | Главная функция модуля: пропустить раунд через гейт. |
| 493 | функция | `_предложений(n)` |  |
| 501 | функция | `очистить_текст(текст, неподкреплённые)` | Убрать из текста предложения с неподкреплёнными утверждениями. |
| 563 | константа | `_ПОМЕТКА_ГЕЙТА` | re.compile('\\n*\\[(?:СНЯТО ГЕЙТОМ\|ОТВЕТ РАУНДА ОБОРВАН ЛИМИТОМ ДЛИНЫ):[^\\]]*\\ |
| 567 | функция | `текст_для_аудита(текст)` | Текст ответа без служебных пометок гейта — то, что аудирует GOVERNANCE. |
| 578 | функция | `задание_на_доработку(проверка)` | Что сказать следователю в следующем раунде. |
| 646 | константа | `__all__` | list, 10 элементов |

## rpl

- **путь**: `helix_pipeline/engine/rpl.py`
- **размер**: 229 строк, SHA-256 blob `6922ea669f9ded46…`
- **что это**: rpl.py — RPL: слой ресурсного давления (Патч 67, GI v6.2 Раздел XXII).
- **зачем**: НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ. До этого модуля существовал только непрерывный `RPL_Factor` в governance_math.py (`calculate_rpl_factor`) — и это ДРУГАЯ формула для ДРУГОГО протокола: HELIX_GOVERNANCE_v1_4.md §14.2 определяет RPL_Factor как `1 − (deficit/required_hours × penalty_weight)`, вход — часы на аудит, назначение — единственный порог 0.70 для блокировки ECT-4 в GOVERNANCE. Патч 67 GI v6.2 (этот модуль) — семиполевая модель 0–100 с четырьмя именованными полосами и отдельным подпротоколом RPL-ANI (намеренное исто…
- **спека-якорь**: `HELIX_GOVERNANCE_v1_4.md`
- **коды состояний** (6): `CONSTRAINED`, `CRITICAL`, `DEGRADED`, `MONITOR`, `STABLE`, `WARNING`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_governance_math.py`, `helix_pipeline/tests/test_intelligence_closing_markers.py`, `helix_pipeline/tests/test_rpl.py`, `helix_pipeline/tests/test_s1_calibrated_and_codes.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 42 | константа | `RPLBand` |  |
| 45 | константа | `RPL_FIELD_WEIGHTS` | dict, 7 элементов |
| 55 | константа | `RPL_NORMALIZATION_DENOMINATOR` |  |
| 58 | константа | `RPL_BANDS` | tuple, 4 элементов |
| 71 | константа | `RPL_MARKER` | dict, 4 элементов |
| 80 | класс | `RPLInputs (0 публичных методов)` | Семь полей модели RPL (Патч 67, Раздел I) — каждое 0–5. |
| 92 | класс | `SkippedVerification (0 публичных методов)` | Одна пропущенная из-за ресурсов верификация (для RPL AUDIT). |
| 100 | класс | `RPLResult (0 публичных методов)` |  |
| 112 | функция | `_validate_field(name, value)` |  |
| 117 | функция | `rpl_evaluate(inputs)` | RPL Score 0-100 + полоса + предписанные действия (Патч 67, Раздел II). |
| 149 | функция | `rpl_audit(skipped)` | RPL AUDIT (Раздел V) — что не проверено из-за ресурсных ограничений. |
| 173 | константа | `RplAniIndicator` |  |
| 175 | константа | `RPL_ANI_LABELS` | dict, 4 элементов |
| 182 | константа | `RplAniLevel` |  |
| 186 | класс | `RplAniResult (0 публичных методов)` |  |
| 195 | функция | `rpl_ani_check(indicators)` | RPL-ANI COMPOSITE (Раздел IV): 1 признак MONITOR, 2 WARNING+ANI WARNING, |
| 220 | функция | `rpl_summary()` | Сводка — для отчётов о готовности. |

## sap_protocol

- **путь**: `helix_pipeline/engine/sap_protocol.py`
- **размер**: 411 строк, SHA-256 blob `06b16bd08a59adeb…`
- **что это**: sap_protocol.py — Патч 71: SAP ПОЛНЫЙ ПРОТОКОЛ (SAP-1..9), GI v6.2, блок B0.
- **зачем**: Проблема, которую закрывает патч (словами спеки): «SAP-1..9 упоминаются фрагментарно. SAP-1, SAP-3, SAP-4, SAP-5 существуют только в ссылках без определений.» Проверка кодом подтвердила: 0 из 9 в реализации. ВАЖНОЕ НАБЛЮДЕНИЕ О ПРИРОДЕ ПАТЧА (уточнение плана, найдено при сборке): SAP-1..9 — не «лист», а АГРЕГАТОР. Часть подпротоколов самодостаточна и реализуется здесь полностью, часть по спеке ДЕЛЕГИРУЕТ другим патчам: самодостаточные (реализованы): SAP-1, SAP-2, SAP-3, SAP-4, SAP-5 делегирующие: SAP-6 → SDF (Патч 49,…
- **коды состояний** (19): `ADVERSARIAL_AI_SUSPECT`, `AI_OUTPUT`, `ANON`, `CAP`, `COERCION_EXTREME`, `COERCION_HIGH`, `FLAGGED`, `FULL`, `HITL`, `ICOI_PRESENT`, `ICOI_STRUCTURAL`, `NOT_APPLICABLE`, `NOT_DEFINED`, `PARTIAL`, `PROTOCOL_UNAVAILABLE`, `SCOA_DETECTED`, `SDF_APPLIED`, `SOCIAL_CAPTURE`, `STRUCTURAL`
- **тесты, которые зовут модуль**: 12 — `helix_pipeline/tests/test_aporia_scoa_ani_b5.py`, `helix_pipeline/tests/test_gi62_audit_regressions.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_gi_core.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_icoi_source.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `ICOI_STRUCTURAL_TRUST_CAP` |  |
| 33 | константа | `CONTINUITY_PASS` |  |
| 34 | константа | `CONTINUITY_PARTIAL_FLOOR` |  |
| 42 | константа | `COERCION_HIGH` |  |
| 43 | константа | `COERCION_EXTREME` |  |
| 46 | константа | `COERCION_LOW` |  |
| 47 | константа | `SAP5_COERCION_MAX` |  |
| 48 | константа | `ECHO_CHAMBER_IV` |  |
| 49 | константа | `SINGLE_PRIMARY_IV` |  |
| 52 | класс | `Identity (0 публичных методов)` |  |
| 60 | класс | `WPLClass (0 публичных методов)` |  |
| 67 | класс | `SourceProfile (0 публичных методов)` | Вход SAP-цикла. Значения, которые по спеке приходят из других патчей |
| 98 | класс | `SAPStep (1 публичных методов)` |  |
| 111 | функция | `sap_1_identity(p)` |  |
| 159 | функция | `sap_2_independence(p)` |  |
| 172 | функция | `sap_3_motivation(p)` |  |
| 199 | константа | `_TEMPORAL` | dict, 4 элементов |
| 203 | функция | `sap_4_temporal(p)` |  |
| 217 | функция | `sap_5_exception(p)` | Анонимный источник может подняться выше потолка — при всех 4 условиях. |
| 247 | функция | `_unavailable(step, patch, block)` |  |
| 254 | функция | `sap_6_sdf(p)` | SAP-6 = слот SDF (по таблице SAP-1..9 патча 71). Разблокирован в B3. |
| 299 | функция | `sap_7_ssc_char(p)` | Единственный делегат, доступный уже сейчас: Патч 69 собран. |
| 312 | функция | `sap_8_sca(p)` | Делегат к SCA (Патч 36). Протокол собран в блоке B1 — вызывающий может |
| 341 | функция | `sap_9_scoa(p)` | SAP-9 = слот SCoA (Патч 44). Разблокирован в B5. |
| 379 | функция | `sap_full_cycle(p)` | Прогон SAP-1..9. Возвращает шаги, итоговый ECT и Trust CAP. |

## sca

- **путь**: `helix_pipeline/engine/sca.py`
- **размер**: 166 строк, SHA-256 blob `3be49f0fc74be934…`
- **что это**: sca.py — Патч 36: SAP-8 / SCA, аудит синтетического контента (GI v6.2, B1).
- **зачем**: SYNTHETIC CONTENT AUDIT. Применяется ко ВСЕМ входящим документам и медиафайлам. Контринтуитивное ядро патча (SCA-1): «Слишком чистый документ — подозрителен». Настоящие документы несут следы человеческого производства — опечатки, форматные артефакты, случайные неровности. Их отсутствие — не признак качества, а признак машинного происхождения. Разблокирует SAP-8 в агрегаторе `sap_protocol` (до этого патча делегат честно возвращал PROTOCOL_UNAVAILABLE). Агрегация из спеки: 0 флагов → SCA PASS ECT без ограничений 1 флаг →…
- **тесты, которые зовут модуль**: 11 — `helix_pipeline/tests/test_aporia_scoa_ani_b5.py`, `helix_pipeline/tests/test_bridges_b8.py`, `helix_pipeline/tests/test_gi62_audit_regressions.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_governance_cognitive_labeler.py`, `helix_pipeline/tests/test_governance_live_inputs.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 25 | константа | `MIN_VERIFIED_REFERENCES` |  |
| 28 | класс | `SCATest (0 публичных методов)` |  |
| 36 | класс | `SCADocument (0 публичных методов)` | Входящий документ или медиафайл. |
| 56 | класс | `SCAFlag (1 публичных методов)` |  |
| 66 | класс | `SCAResult (1 публичных методов)` |  |
| 80 | функция | `sca_evaluate(doc)` | Четыре теста SCA + агрегация (Патч 36). |
| 161 | константа | `SCA_HUMAN_FLAG` | строка: «[SCA FLAG: требуется проверка человеком]» |
| 164 | функция | `sca_flags_for_sap8(result)` | Список кодов флагов в формате, который потребляет SAP-8 (Патч 71). |

## sca_trace

- **путь**: `helix_pipeline/engine/sca_trace.py`
- **размер**: 88 строк, SHA-256 blob `abb7fa032179de92…`
- **что это**: sca_trace.py — SCA: корпоративные комбинации (TRACE Приложение C).
- **зачем**: ━━━ НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ ━━━ `sca.py` (Патч 36, разделяемый с INTELLIGENCE) реализует четыре теста SCA и их базовую агрегацию (0/1/2+ флагов) — уже сверено и подтверждено верным. TRACE Приложение C добавляет к тем же четырём тестам два КОРПОРАТИВНЫХ правила, которых не было нигде в коде: SCA DUAL FLAG: SCA-1 (тест идеальности) + SCA-2 (тест метаданных) сработали ОДНОВРЕМЕННО → сильный сигнал AI, все факты документа → ECT-2 max + углублённая верификация. Это НЕ то же самое, что общая агрегация «2+ флага → AI-VERIF…
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_sca_trace.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 41 | класс | `ScaDualFlagResult (0 публичных методов)` |  |
| 48 | функция | `sca_dual_flag(triggered_tests)` | TRACE Приложение C: SCA-1 + SCA-2 одновременно → сильный сигнал AI. |
| 67 | класс | `BackdatedDocumentResult (0 публичных методов)` |  |
| 74 | функция | `backdated_document_check()` | TRACE Приложение C: «задним числом» — SCA-2 (создан после события, |

## scientific_layer

- **путь**: `helix_pipeline/engine/scientific_layer.py`
- **размер**: 189 строк, SHA-256 blob `99edc072c6ef19f4…`
- **что это**: scientific_layer.py — SL-1..SL-8: восемь правил из академических
- **зачем**: Затем, что расследование, которое понижает доверие к опознанию, обязано уметь сказать ПОЧЕМУ — и ответ «так решил алгоритм» не годится. Ответ «субъективная уверенность свидетеля не равна объективной точности, Deffenbacher & Loftus, 1982» — годится, и он же защищает вывод, когда его оспорят. Маркер SL и есть эта ссылка.
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_intelligence_extra_layers.py`, `helix_pipeline/tests/test_scientific_layer.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 43 | константа | `SL_SOURCES` | dict, 8 элементов |
| 55 | константа | `SL6_SUGGESTIVE_MARKERS_MIN` |  |
| 57 | константа | `SL1_INTUITION_MULTIPLIER` |  |
| 58 | константа | `SL8_PHYSICAL_EVIDENCE_ECT_MULTIPLIER` |  |
| 62 | класс | `SLResult (0 публичных методов)` |  |
| 69 | функция | `sl_1_cognitive_overload()` | Истощение Системы 2 блокирует Систему 1 (Kahneman 2011). |
| 95 | функция | `sl_2_substitution_check()` | Отвечаю ли я на поставленный вопрос или на более простой (Kahneman). |
| 115 | функция | `sl_3_ad_hoc()` | Граница Поппера между допустимой и недопустимой вспомогательной |
| 133 | функция | `sl_6_suggestive_contamination(markers_present)` | Суггестивное давление обнуляет Trust, а не понижает (Loftus & Ketcham). |
| 150 | функция | `sl_7_spiral_filter()` | Медийная частотность — сигнал спирали девиации, не измерение (Cohen). |
| 166 | функция | `sl_8_blind_decontextualization()` | Улики уходят эксперту без контекста дела (Dror). |

## scoa

- **путь**: `helix_pipeline/engine/scoa.py`
- **размер**: 235 строк, SHA-256 blob `8bb42d6498cc417b…`
- **что это**: scoa.py — Патч 44: социальный каскад, SCoA / SAP-9 (GI v6.2, блок B5).
- **зачем**: Диффузная контаминация через внешнюю информационную среду. Отличие от Echo Effect: тот работает с ПРЯМЫМИ связями между источниками, а SCoA — с косвенной синхронизацией через медиапространство. Источники могут не знать друг друга и всё равно говорить одно, потому что все читали одно и то же. Живой пример спеки: **Салемские процессы (1692)** — SCoA-2 + SCoA-4, 20 человек казнены, все впоследствии реабилитированы. ━━━━━━ РАСХОЖДЕНИЕ СПЕК №8 ━━━━━━ Номера SCoA означают в двух спеках разное: | № | GI v6.2, Патч 44 | INT v2.1, §…
- **коды состояний** (3): `CONFORMITY_CHANGE`, `MEDIA_SPECIFIC_DETAILS`, `RETROSPECTIVE_RECONSTRUCTION`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_aporia_scoa_ani_b5.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `TS_DELTA_PRE_EXPOSURE` |  |
| 40 | константа | `TS_DELTA_AFFECT_MILD` |  |
| 41 | константа | `TS_DELTA_AFFECT_STRONG` |  |
| 43 | константа | `TS_CEILING_PANIC` |  |
| 45 | константа | `LEXICAL_SYNC_MIN_SOURCES` |  |
| 47 | константа | `PANIC_COVERAGE_HOURS` |  |
| 49 | константа | `SCOA_NUMBERING_CONFLICT` | строка: «Номера SCoA-1/2/3/4 означают разное в GI v6.2 Патч 44 и в INTELLIGENCE» |
| 58 | константа | `SALEM_CASE` | строка: «Салемские процессы (1692): SCoA-2 + SCoA-4 → HITL перед ECT-4 EXCEPTIO» |
| 65 | класс | `SocialContext (0 публичных методов)` | Контекст получения показаний — предмет проверки SCoA. |
| 85 | класс | `SCoAFlag (0 публичных методов)` |  |
| 95 | класс | `SCoAResult (2 публичных методов)` |  |
| 115 | функция | `scoa_audit(c)` | 4 теста Патча 44 + три именованных паттерна INT. |
| 212 | функция | `apply_scoa_to_trust(trust, r)` | Применить последствия SCoA к Trust Score. |
| 225 | функция | `scoa_flags_for_sap9(r)` | Сводка для слота SAP-9 (таблица SAP-1..9 патча 71). |

## sdf

- **путь**: `helix_pipeline/engine/sdf.py`
- **размер**: 339 строк, SHA-256 blob `8740d7930601a8b7…`
- **что это**: sdf.py — Патч 49: статусное искажение, SDF (GI v6.2 + INT v2.1, блок B3).
- **зачем**: ПРИНЦИП: **статус ≠ ECT.** Один факт = один уровень верификации, независимо от того, кто источник — министр или бездомный, лауреат или обвиняемый. Отступление от единообразия документируется явно. ━━━━━━ РАСХОЖДЕНИЕ СПЕК №7 (самое серьёзное из найденных) ━━━━━━ Номера SDF означают РАЗНОЕ в двух спеках. Это не разные формулировки одного правила — это разные правила под одинаковыми номерами: | № | GI v6.2, Патч 49 | INTELLIGENCE v2.1, §3.21 | |---|---|---| | SDF-1 | Authority Bias | Authority Bias (совпадает) | | SDF-2 | P…
- **коды состояний** (3): `CHECK`, `POVERTY_SKEPTICISM`, `REPUTATIONAL_SHIELDING`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_aporia_scoa_ani_b5.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_sdf_patch49.py`, `helix_pipeline/tests/test_trace_questionnaire_and_labels.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `SDF_NUMBERING_CONFLICT` | строка: «Номера SDF-2/3/5/6 означают разное в GI v6.2 Патч 49 и в INTELLIGENCE » |
| 54 | константа | `AK_INT_10` | строка: «AK-INT-10 (ACTIVE_PATCHES v1.0): «SDF-7 (Эффект Дрора) добавлен к сист» |
| 63 | класс | `SubjectStatus (0 публичных методов)` | Что известно о статусе источника/субъекта и как с ним обошлись. |
| 104 | класс | `SDFFlag (0 публичных методов)` |  |
| 115 | класс | `SDFResult (2 публичных методов)` |  |
| 140 | функция | `sdf_audit(s)` | Полный SDF-аудит: 7 типов + 2 подтипа + 2 паттерна Патча 49. |
| 318 | функция | `sdf_trust_cap_for_sap6(result)` | Что SDF передаёт в слот SAP-6 (по таблице SAP-1..9 патча 71). |
| 330 | функция | `sdf_flags_for_sap6(result)` | Сводка SDF для SAP-6: чем именно слот заполнен. |

## ssc_char

- **путь**: `helix_pipeline/engine/ssc_char.py`
- **размер**: 177 строк, SHA-256 blob `51851ab7e9c7d782…`
- **что это**: ssc_char.py — Патч 69: SSC-CHAR Character Reliability Status (GI v6.2, B0).
- **зачем**: ГРАНИЦА С /101 (ревизия кросс-репо, урок ошибки О-6 враждебного аудита). SSC-CHAR — «межпродуктовый стандарт AK-MASTER v3.1 / HELIX» (слова самого `/101 engine/ssc_char_classifier.py`). Реализации уже существуют: /101 ssc_char_classifier.py — КЛАССИФИКАЦИЯ типа надёжности нарратора; /101 cortex_vi_router.py — диспетчеризация по типу; /101 block13_tracker.py — главо-скоупные переходы состояния. Проверено грепом: **таблицы эпистемических ПОСЛЕДСТВИЙ (Trust ×0.6 / CAP 0.60, ECT-эффект, SAP-7, SIL-WITHHOLD) нет ни в одном …
- **коды состояний** (4): `FAILED`, `NOT_APPLICABLE`, `NOT_DEFINED`, `PARTIAL`
- **тесты, которые зовут модуль**: 9 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_gi62_audit_regressions.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_s1_calibrated_and_codes.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 30 | константа | `TRUST_MPE_FACTOR` |  |
| 31 | константа | `TRUST_CAP_CONCEALMENT` |  |
| 32 | константа | `HITL_TRUST_FLOOR` |  |
| 35 | класс | `SSCCharStatus (0 публичных методов)` |  |
| 44 | константа | `_NAMES` | dict, 4 элементов |
| 53 | класс | `SSCCharConsequence (1 публичных методов)` | Последствия статуса для эпистемики следователя (таблица Патча 69). |
| 74 | функция | `ssc_char_evaluate(status)` | Патч 69 / вызывается SAP-7. Детерминированно, без LLM. |

## ssd

- **путь**: `helix_pipeline/engine/ssd.py`
- **размер**: 251 строк, SHA-256 blob `a92eae362861c011…`
- **что это**: ssd.py — Патч 51: самозапечатывающаяся система, SSD (GI v6.2, блок B4).
- **зачем**: Гипотеза нефальсифицируема, если ЛЮБОЙ результат — и подтверждающий, и опровергающий — читается как её поддержка. Это не ошибка в данных: данные могут быть безупречны. Это ошибка в форме гипотезы. ТЕСТ SSD — ВОПРОС ПОППЕРА, дословно из спеки: «Какое наблюдаемое событие убедило бы нас отказаться от H1?» Ответ существует И операционализируем → [SSD PASS: фальсификатор: {событие}] Ответа нет → [SSD FAIL: CF ×0.50, потолок ECT-3] H1 остаётся в матрице, но не выше ECT-3 до разрешения — гипотеза не выбрасывается, она перестаёт п…
- **тесты, которые зовут модуль**: 10 — `helix_pipeline/tests/test_ach_matrix.py`, `helix_pipeline/tests/test_ai_ssd.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_intelligence_closing_markers.py`, `helix_pipeline/tests/test_s6_формальное_основание.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 39 | константа | `SSD_FAIL_CF_MULTIPLIER` |  |
| 41 | константа | `SSD_FAIL_ECT_CEILING` |  |
| 43 | константа | `P1_COERCION_EXPLANATIONS` |  |
| 45 | константа | `COERCION_RESOLUTIONS` | tuple, 3 элементов |
| 47 | константа | `SSD_THRESHOLDS_NOTE` | строка: «CF ×0.50, потолок ECT-3 и порог P1 = 3 — эвристики триажа, не калибров» |
| 53 | константа | `POPPER_QUESTION` | строка: «Какое наблюдаемое событие убедило бы нас отказаться от H1?» |
| 54 | константа | `P3_QUESTION` | строка: «При каком ответе субъекта мы понизили бы уверенность?» |
| 56 | константа | `SSD_PRINCIPLE` | строка: «Расследование, производящее нефальсифицируемые выводы, перестаёт быть » |
| 63 | класс | `Hypothesis (0 публичных методов)` | Гипотеза H1 и то, что о её проверяемости известно. |
| 74 | класс | `FRCPResolution (0 публичных методов)` | Запись из журнала FRCP: как был закрыт конфликт. |
| 81 | класс | `SourceResponse (0 публичных методов)` | Ответ источника и как его классифицировали. |
| 89 | класс | `SSDResult (2 публичных методов)` |  |
| 120 | функция | `ssd_test(h, recent_frcp_log, source_responses)` | Тест Поппера + три патологических паттерна (чертёж PPC-2). |
| 214 | функция | `epistemic_lock_outcome()` | Чем кончился эпистемический замок (INT §3.18, конец раздела). |
| 239 | функция | `apply_ssd_to_confidence(cf, r)` | Применить множитель SSD к уверенности. CF не уходит ниже нуля. |
| 244 | функция | `falsifier_exists_but_unobservable(h)` | Условие TELP-3: фальсификатор существует, но наблюдать его нельзя. |

## st18_recovery

- **путь**: `helix_pipeline/engine/st18_recovery.py`
- **размер**: 275 строк, SHA-256 blob `cfdc1ac2d7fa2a64…`
- **что это**: st18_recovery.py — ST-18 Recovery Protocol (INT §3.31): выход из тройной блокировки.
- **зачем**: Закрывает INT-3.31 в gi62_patch_manifest.yaml (было SPEC_ONLY). ST-18 — не провал системы, а структурированный выход из состояния, когда расследование одновременно заблокировано с трёх независимых сторон (доказательной, институциональной и личной/феноменологической). ТРИ ОПРЕДЕЛЕНИЯ TRIPLE LOCK — РАЗНОЕ ПРАВИЛО СРАБАТЫВАНИЯ ДЛЯ КАЖДОГО. Спека даёт три альтернативных набора условий и одно общее правило ШАГА 0: «подтвердить наличие ≥2 из трёх условий TRIPLE LOCK». Это правило дословно описывает только первый наб…
- **коды состояний** (4): `FREEZE`, `PRIORITY`, `REBUILD`, `VERIFY`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_st18_recovery.py`, `tests/test_ev_sequence_monitor.py`, `tests/test_v161_audit_response.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 46 | константа | `_COMBO_A_LABELS` | dict, 3 элементов |
| 51 | константа | `COMBO_A_MIN_CONDITIONS` |  |
| 55 | класс | `TripleLockInputs (0 публичных методов)` | Вход ШАГА 0 — уже посчитанные результаты других протоколов. |
| 71 | класс | `TripleLockDiagnosis (0 публичных методов)` |  |
| 79 | функция | `diagnose_triple_lock(inp)` | ШАГ 0 — ДИАГНОСТИКА. Возвращает, сработал ли TRIPLE LOCK и какое Комбо. |
| 103 | класс | `St18State (0 публичных методов)` | Вход шагов 1–7. Каждый шаг — свой `_done`, см. докстринг модуля. |
| 142 | класс | `St18StepResult (0 публичных методов)` |  |
| 151 | класс | `St18Result (0 публичных методов)` |  |
| 162 | функция | `run_st18(triple_lock, state)` | Провести ST-18 по уже переданным данным шагов 1–7. |

## sta_dyn

- **путь**: `helix_pipeline/engine/sta_dyn.py`
- **размер**: 193 строк, SHA-256 blob `a78b122440eab9cc…`
- **что это**: sta_dyn.py — Патч 40: устаревший vs изменившийся факт (GI v6.2, блок B1).
- **зачем**: Различение, без которого расследование либо выбрасывает верные факты, либо пропускает улику: STA — СТАТИЧЕСКИЙ УСТАРЕВШИЙ ФАКТ: был истинным, мог стать ложным из-за смены реестра или времени. Действие: проверить актуальность. DYN — ДИНАМИЧЕСКИЙ ИЗМЕНИВШИЙСЯ ФАКТ: изменился, и САМО ИЗМЕНЕНИЕ является частью расследования (смена владельца за неделю до сделки — это не «устаревшие данные», это улика). КЛЮЧЕВОЙ ПРИНЦИП СПЕКИ: **ИСТОРИЧЕСКИЙ ECT ≠ УСТАРЕВШИЙ ECT.** Факт «Субъект владел X в 2019 году» остаётся ECT-4 навсегда, д…
- **коды состояний** (3): `CURRENT`, `DYN`, `STA`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_ak_int_patches.py`, `helix_pipeline/tests/test_anonymity_sta_dyn_b1.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 29 | константа | `AK_INT_04` | строка: «AK-INT-04 (ACTIVE_PATCHES v1.0, HELIX INTELLIGENCE v2.1 Раздел 11): «П» |
| 38 | константа | `STA_FORCED_AGE_MONTHS` |  |
| 40 | константа | `SAP6_SLOT_CONFLICT` | строка: «Патч 40 (v5.7) озаглавлен «SAP-6 РАСШИРЕНИЕ: STA/DYN», но таблица SAP-» |
| 47 | класс | `FactTemporalStatus (0 публичных методов)` |  |
| 54 | класс | `FactTemporalProfile (0 публичных методов)` | Вход: что известно о факте и его изменении. |
| 71 | класс | `STADYNResult (1 публичных методов)` |  |
| 88 | функция | `_parse_ym(value)` | Прочитать «YYYY», «YYYY-MM» или «YYYY-MM-DD» как (год, месяц). |
| 107 | функция | `timestamp_age_in_months(stamp, as_of)` | Возраст временной метки в месяцах. None — метку прочитать не удалось. |
| 120 | функция | `classify_fact_temporal_status(f)` | Отнести факт к CURRENT / STA / DYN и выдать предписанные действия. |
| 190 | функция | `historical_ect_is_preserved(before, result)` | Проверка ключевого принципа: ИСТОРИЧЕСКИЙ ECT ≠ УСТАРЕВШИЙ ECT. |

## streaming_interceptor

- **путь**: `helix_pipeline/engine/streaming_interceptor.py`
- **размер**: 119 строк, SHA-256 blob `3c0f219458502a7c…`
- **что это**: streaming_interceptor.py — GOVERNANCE §18.1: перехват потока токенов до
- **зачем**: отправки клиенту. НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ: §18.1 существовал только как текст спеки — `stream_intercept()` не было нигде в репозитории. Реализовано по псевдокоду секции почти буквально: буферизация по `buffer_size` токенов, блокировка при TYPE-1 CRITICAL / TYPE-7, безопасная замена текста, честный fallthrough при недоступности анализатора (не блокировать прод молча). ЧТО ОСТАЁТСЯ ЗА ВЫЗЫВАЮЩИМ. `analyze` — функция классификации буфера («какая галлюцинация, если есть»), передаётся параметром: это классификатор, …
- **коды состояний** (2): `BLOCKED`, `CRITICAL`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_hitl_queue.py`, `helix_pipeline/tests/test_streaming_interceptor.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `DEFAULT_BUFFER_SIZE` |  |
| 35 | константа | `SAFE_REPLACEMENTS` | dict, 3 элементов |
| 44 | константа | `_BLOCKING_TYPES` | frozenset({'TYPE-7', 'TYPE-1'}) |
| 47 | функция | `get_safe_replacement(analysis_type)` |  |
| 51 | функция | `_should_block(analysis)` |  |
| 60 | функция | `stream_intercept(token_stream, analyze)` | §18.1 — буферизует токены, анализирует каждый полный буфер, блокирует |
| 112 | функция | `streaming_interceptor_summary()` | Сводка — для отчётов о готовности. |

## telp

- **путь**: `helix_pipeline/engine/telp.py`
- **размер**: 234 строк, SHA-256 blob `74113bde15e5ea80…`
- **что это**: telp.py — Патч 53: терминальный эпистемический предел, TELP (GI v6.2, B4).
- **зачем**: **TELP ≠ NON LIQUET.** Различение, которое и есть весь смысл патча: NON LIQUET → временная неопределённость: данных нет, ждём. TELP → терминальная неопределённость: новых данных принципиально не ожидается. «Мы никогда не узнаем» — и это честный результат. ТРИ УСЛОВИЯ АКТИВАЦИИ (все три обязательны): TELP-1 ОНТОЛОГИЧЕСКОЕ ИСТОЩЕНИЕ ИСТОЧНИКОВ — все прямые показания недоступны, поиск новых кандидатов не даёт TS > 0.40. TELP-2 ДОКУМЕНТАЛЬНАЯ НЕВОСПОЛНИМОСТЬ — ключевые документы уничтожены (SAD-1 подтверждён) или не существ…
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_ppep_patch39.py`, `helix_pipeline/tests/test_ssd_mpf_telp_b4.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `NON_LIQUET_DAYS_REQUIRED` |  |
| 40 | константа | `NEW_CANDIDATE_TS_THRESHOLD` |  |
| 42 | константа | `NGI_IFM_CONTINUES` |  |
| 44 | константа | `TELP_VS_NON_LIQUET` | строка: «NON LIQUET — временная неопределённость: ждём новых данных. TELP — тер» |
| 50 | константа | `TELP_PROTECTIVE_PRINCIPLE` | строка: «Ложный вывод ≠ справедливость для жертв. [TELP DECLARED] защищает от л» |
| 55 | константа | `NEED_FOR_CLOSURE_NOTE` | строка: «Потребность в завершённости будет давить на производство вывода. TELP » |
| 62 | класс | `InvestigationLimit (0 публичных методов)` | Состояние расследования на момент проверки предела. |
| 91 | класс | `TELPResult (1 публичных методов)` |  |
| 110 | функция | `telp_evaluate(inv)` | Проверить, достигнут ли терминальный предел (чертёж PPC-3). |
| 203 | функция | `telp_partial_marker(unresolved_question, resolved_question, resolved_ect)` | [TELP PARTIAL]: один вопрос неразрешим, другой установлен. |
| 214 | функция | `telp_reactivate(new_data_ect, date)` | Новые данные после TELP: реактивация или подтверждение предела. |

## tie

- **путь**: `helix_pipeline/engine/tie.py`
- **размер**: 247 строк, SHA-256 blob `9c516fe692430fbd…`
- **что это**: tie.py — Патч 48: темпоральная целостность, TIE (GI v6.2, блок B3).
- **зачем**: TIE верифицирует не отдельные факты, а ХРОНОЛОГИЧЕСКИЕ ОТНОШЕНИЯ между ними. Каждый факт по отдельности может быть ECT-4 — и вся последовательность при этом невозможна. Ни один другой протокол этого не видит: они смотрят на источник, на документ, на память, но не на интервал между двумя событиями. ТРИ РЕЖИМА: TIE-1 ВРЕМЕННЫ́Е ОКНА В1: физически/логистически возможен интервал? Нет → IMPOSSIBLE WINDOW, факт аннулируется даже при ECT-4, FRCP немедленно. В2: процессуальный минимум соблюдён? Нарушен → PROCESS VIOLATION, ECT −1. В3:…
- **коды состояний** (5): `CONFLICT`, `FLAG`, `IMPOSSIBLE`, `UNCERTAIN`, `VIOLATION`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_tie_patch48.py`, `helix_pipeline/tests/test_tie_trace.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 47 | константа | `TA1_IS_INPUT_NOT_DERIVED` | строка: «Спека Патча 48 называет TA-1 «нереалистичной плотностью», но не даёт ч» |
| 55 | класс | `TIESeverity (0 публичных методов)` |  |
| 64 | класс | `TemporalSequence (0 публичных методов)` | Последовательность «событие A → событие B» и что о ней известно. |
| 87 | класс | `TIEFlag (0 публичных методов)` |  |
| 96 | класс | `TIEResult (2 публичных методов)` |  |
| 118 | функция | `tie_evaluate(s)` | Прогнать все три режима TIE по одной последовательности. |
| 243 | функция | `chronology_map_row(event, timestamp, source, ect_status)` | Строка хронологической карты: событие × метка × источник × ECT-статус. |

## tie_trace

- **путь**: `helix_pipeline/engine/tie_trace.py`
- **размер**: 207 строк, SHA-256 blob `79cc144a52abfa41…`
- **что это**: tie_trace.py — TIE: темпоральная целостность документа (TRACE §4.19).
- **зачем**: ━━━ НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ ━━━ `trace_vector.py` заявляет, что «большинство протоколов TRACE §4 — это те же протоколы GI v6.2, уже собранные GICore... TRACE их не переопределяет». Для TIE это неверно ровно в той части, где TRACE даёт СВОЮ нумерацию: GI v6.2 Патч 48 / INT §3.17 (`tie.py`, `gi.tie`): TIE-1 = вопрос 1 (физическая возможность) + вопрос 3 (согласие источников по длительности) объединены под одним кодом TIE-1 PROCESS VIOLATION = вопрос 2 (процессуальный минимум) TIE-2 = причинность (TC-1/2/3, Post Hoc…
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_tie_trace.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 56 | константа | `TIE_TRACE_NUMBERING_NOTE` | строка: «TRACE §4.19 задаёт СВОЮ нумерацию TIE-1..4, отличную от GI v6.2 Патча » |
| 65 | константа | `_PDE_CRITICAL_BANDS` | tuple, 2 элементов |
| 68 | класс | `TieTraceCode (0 публичных методов)` |  |
| 76 | класс | `DocumentTemporalProfile (0 публичных методов)` | Что известно о документе для TRACE §4.19 (входы, не суждения). |
| 95 | класс | `TieTraceFlag (1 публичных методов)` |  |
| 106 | класс | `TieTraceResult (2 публичных методов)` |  |
| 123 | функция | `tie_trace_evaluate(d)` | Прогнать TIE-1..4 TRACE §4.19 по одному документу. |
| 201 | функция | `tie_trace_summary()` | Сводка — для отчётов о готовности. |

## trace_classifier

- **путь**: `helix_pipeline/engine/trace_classifier.py`
- **размер**: 846 строк, SHA-256 blob `17a5232f6e3a463b…`
- **что это**: trace_classifier.py — TRACE-классификатор из сырого текста (WORK_PLAN.md:
- **зачем**: `TraceVector.compute_risk_index()` принимает уже КЛАССИФИЦИРОВАННЫЕ структуры (ICoI-тир, SSD PASS/FAIL, полосы HMP/RDI/ANI), а не сырой текст — классификатора, который получает эти структуры ИЗ ответа `IntelligenceVector.investigate()`, в кодовой базе не было ни regex, ни LLM. Этот модуль — часть ответа, тем же транспортом и той же дисциплиной, что `governance_classifier.py` (Google/Gemini через `api/provider_gateway`, LLM отдаёт ТОЛЬКО семантические сигналы, математику считают уже существующие протоколы — `icoi_source.py`/`ssd.py`/`ani.py`/`ngi.py`).
- **коды состояний** (10): `CRITICAL`, `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `HIGH`, `INVALID`, `MISSING`, `PARTIAL`, `PROVIDER_NOT_CONFIGURED`, `STRUCTURAL`, `UNKNOWN`
- **тесты, которые зовут модуль**: 8 — `helix_pipeline/tests/test_temporal_grounding.py`, `helix_pipeline/tests/test_trace_classifier.py`, `helix_pipeline/tests/test_trace_questionnaire_and_labels.py`, `helix_pipeline/tests/test_trace_живые_сбои_07_10.py`, `tests/test_byok_reaches_engine.py`, `tests/test_classifier_determinism.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 92 | константа | `TRACE_CLASSIFIER_SYSTEM_PROMPT` | строка: «Ты — HELIX TRACE Content Classifier.
Твоя задача: прочитать текст расс» |
| 280 | константа | `PROVIDER` | строка: «google» |
| 282 | константа | `NOT_CONFIGURED_MESSAGE` | строка: «Ключ Google не настроен на бэкенде. TRACE-классификация текста не выпо» |
| 288 | константа | `GOOGLE_KEY_ENV_NAMES` | tuple, 2 элементов |
| 292 | константа | `_ICOI_UNKNOWN_MAPPED_TO` | строка: «HIGH» |
| 293 | константа | `_ICOI_SEVERITY_ORDER` | tuple, 4 элементов |
| 294 | константа | `_VALID_ICOI_TIERS_FROM_CLASSIFIER` | set, 5 элементов |
| 297 | класс | `TraceClassifierNotConfigured (0 публичных методов)` | Ключа Google нет — не то же самое, что «сбой сети», лечится по-разному. |
| 301 | класс | `TraceClassifierCallFailed (0 публичных методов)` | Google ответил отказом, пустым текстом, или после всех попыток. |
| 305 | класс | `TraceClassifierResponseError (0 публичных методов)` | Ответ классификатора невалиден или нарушил контракт (не JSON, |
| 310 | функция | `google_key_present()` | Есть ли у сервера провайдер для классификатора. |
| 326 | функция | `_caller_for(api_key)` | Собрать вызов классификатора, при наличии — с ключом ПОЛЬЗОВАТЕЛЯ. |
| 344 | функция | `_default_caller(system, prompt, max_tokens)` | Прежняя точка входа без ключа — оставлена: на неё ссылаются тесты. |
| 350 | класс | `TraceClassifierClient (1 публичных методов)` | Транспорт TRACE-классификатора. Парсинг — в `parse_classifier_response()` |
| 409 | функция | `classify_with_retries(client, ai_output)` | До `attempts` попыток вызова классификатора при транзиентном сбое. |
| 442 | функция | `classify_and_parse(client, ai_output)` | Вызов с повторами + разбор; ответ, нарушивший контракт, спрашивается заново. |
| 469 | константа | `_VALID_SEVERITIES_NOT_ALLOWED` | tuple, 13 элементов |
| 480 | функция | `parse_classifier_response(raw)` | Парсит и валидирует JSON от TRACE-классификатора. |
| 566 | константа | `_SECTION_SCHEMAS` | dict, 8 элементов |
| 613 | константа | `TRACE_PROTOCOL_SECTIONS` | tuple(_SECTION_SCHEMAS) |
| 614 | константа | `_FACT_FIELDS` | dict, 4 элементов |
| 618 | функция | `_is_int(v)` |  |
| 622 | константа | `_ECT_STR` | re.compile('^\\s*(?:ECT[\\s_-]*)?([1-4])\\s*$', re.IGNORECASE) |
| 625 | функция | `_ect_as_int(v)` | Живой прогон 07.10: модель вернула ECT строкой `'3'`, и §4.12 CPX упал |
| 637 | функция | `_check(kind, v)` |  |
| 697 | функция | `_check_obj(obj, fields)` |  |
| 716 | функция | `parse_trace_protocol_labels(data)` | Проверить раздел `trace_protocols` по разделам. |
| 746 | класс | `TraceContentSignals (0 публичных методов)` | Результат разрешения классификации: только content-derivable поля |
| 768 | функция | `_resolve_icoi_tier(icoi_items)` | Худший тир среди сообщённых источников. UNKNOWN -> HIGH, см. докстринг |
| 791 | функция | `resolve_trace_content_signals(data)` | Провалидированный JSON классификатора -> content-derivable поля |

## trace_full_run

- **путь**: `helix_pipeline/engine/trace_full_run.py`
- **размер**: 642 строк, SHA-256 blob `918a35529e335fa3…`
- **что это**: trace_full_run.py — полный прогон TRACE §4.1–§4.25 + Risk Index §5 + ACH §3.
- **зачем**: `hmp_band`/`rdi_band` она целиком уходила в SKIPPED, хотя большинству протоколов TRACE полосы HMP/RDI не нужны вовсе. Владелец 06.10.2026: «я вижу только два вектора запущенные». Здесь каждый протокол получает свой статус:
- **коды состояний** (18): `ACTIVATED`, `CHECK`, `CHF_COMPOUND_HIGH`, `CHF_D_ACTIVE`, `CRITICAL`, `EPISTEMIC_LOCK`, `FAILED`, `HIGH`, `HITL_REQUIRED`, `HMP`, `MISSING`, `MODERATE`, `NOT_RUN`, `RAN`, `RDI`, `SAD2_STRATEGIC`, `SOURCE_MONOPOLY`, `SSD_FAIL`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_chain_cross_layers.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 60 | константа | `NOT_RUN_REASONS` | dict, 19 элементов |
| 110 | константа | `_REDIRECT_HOSTS` | tuple, 1 элементов |
| 111 | константа | `_DOMAIN_RE` | re.compile('^[a-z0-9-]+(\\.[a-z0-9-]+)+$', re.IGNORECASE) |
| 114 | функция | `_p(status)` |  |
| 120 | функция | `source_actor(src)` | Домен источника. Для переадресации grounding — заголовок, если он |
| 133 | класс | `TraceStageReport (6 публичных методов)` | Данные стадии TRACE. Обратно совместим с `RiskIndexResult` по тем |
| 178 | функция | `_resolve_hmp(manual, q)` |  |
| 211 | функция | `_resolve_rdi(manual, q, inv_id)` |  |
| 243 | функция | `_run_sad(labels)` |  |
| 266 | константа | `_SDF_LABEL_FIELDS` | tuple, 19 элементов |
| 281 | функция | `_run_sdf(labels)` |  |
| 304 | функция | `_run_corporate_fa(labels)` |  |
| 315 | функция | `_run_cpx(labels)` |  |
| 328 | функция | `_run_chf(labels)` |  |
| 348 | функция | `_run_aporia(labels)` |  |
| 363 | функция | `_run_mpf(labels, inv_id, ssd_result)` |  |
| 372 | функция | `run_trace_full()` | Прогнать всё, что можно, и честно пометить остальное. |

## trace_questionnaire

- **путь**: `helix_pipeline/engine/trace_questionnaire.py`
- **размер**: 270 строк, SHA-256 blob `b78f4333f88b67a7…`
- **что это**: trace_questionnaire.py — анкета человека для TRACE §4.5 HMP и §4.6 RDI.
- **зачем**: `trace_classifier.py` их осознанно НЕ извлекает из текста (см. его докстринг и
- **спека-якорь**: `GI_v6_2_COMPLETE.md`, `HELIX_TRACE_MERGED.md`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_trace_questionnaire_and_labels.py`, `tests/test_mr_helix_chain_api.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 63 | класс | `QuestionnaireError (0 публичных методов)` | Анкета заполнена неверно: недостающее/лишнее поле, значение вне шкалы. |
| 67 | функция | `_bool_q(field, label, spec)` |  |
| 73 | функция | `_scale_q(field, label, spec, labels)` |  |
| 80 | константа | `_RDI_SCALE_SPEC` | строка: «GI_v6_2_COMPLETE.md, Патч 60, «Переменные RDI»» |
| 81 | константа | `_HMP_SPEC` | строка: «GI_v6_2_COMPLETE.md, Патч 59, «Поля модели HMP» и весовая таблица» |
| 84 | константа | `HMP_QUESTIONS` | tuple, 11 элементов |
| 140 | константа | `RDI_QUESTIONS` | tuple, 7 элементов |
| 178 | функция | `_questions(kind)` |  |
| 182 | функция | `questionnaire_needed(kinds)` | Описание формы для фронтенда: что спросить, как подписать, что допустимо. |
| 206 | функция | `_check_value(q, value)` |  |
| 223 | функция | `validate_part(kind, answers)` | Проверить одну часть анкеты. Возвращает чистый словарь или бросает |
| 249 | функция | `validate_questionnaire(q)` | Вся анкета `{hmp?: {...}, rdi?: {...}}`. |
| 261 | функция | `evaluate_hmp(answers, hypothesis_id)` | Ответы → `hmp_evaluate` (Патч 59). Балл и полосу считает формула. |
| 267 | функция | `evaluate_rdi(answers, investigation_id)` | Ответы → `rdi_evaluate` (Патч 60). Балл и полосу считает формула. |

## trace_revision

- **путь**: `helix_pipeline/engine/trace_revision.py`
- **размер**: 221 строк, SHA-256 blob `d415f6b4d457befa…`
- **что это**: trace_revision.py — что делает TRACE ПОСЛЕ закрытия аудита.
- **зачем**: ## ТРЕТЬЯ КОЛЛИЗИЯ ИМЁН МЕЖДУ СПЕКАМИ. ЭТО НЕ ДУБЛИКАТ efr.py. Найдено 20.08.2026 аудитом контракта возвратов — тем же способом, что коллизия SAP (см. `intelligence_sap.py`) и коллизия SSD-P1..P3. буквы HELIX_INTELLIGENCE §3 HELIX_TRACE §4.14б ───── ────────────────────── ───────────────────────────── EFR-A терминологическое НОВЫЕ ДАННЫЕ: появились факты несогласие ECT≥3 против вывода EFR-B методологическое ИЗМЕНЕНИЕ КОНТЕКСТА: вывод несогласие формально верен, но вводит в заблуждение EFR-C онтологическое: спорят КОНКУРИРУЮЩИЙ ВЫВОД: …
- **коды состояний** (3): `ANI`, `MPF`, `SDF`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_chain_cross_layers.py`, `helix_pipeline/tests/test_trace_revision.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 39 | константа | `EFR_NGI_BRIDGE_THRESHOLD` |  |
| 43 | класс | `RevisionResult (0 публичных методов)` |  |
| 51 | функция | `efr_a_new_data()` | Появились факты ECT≥3, противоречащие закрытому выводу (§4.14б). |
| 61 | функция | `efr_b_context_changed()` | Вывод формально верен, но в новом контексте вводит в заблуждение. |
| 74 | функция | `efr_c_competing_finding()` | Другой аналитик или суд на ТЕХ ЖЕ данных пришёл к другому выводу. |
| 97 | функция | `ppep_reactivation()` | Мост M4: PPEP + новые данные ECT≥3 после закрытия (§4.11). |
| 130 | функция | `rdi_ppep_downgrade()` | Вывод, сделанный под давлением дедлайна, пересматривается с |
| 144 | функция | `moffatt_trace_audit()` | Moffatt v. Air Canada применительно к аудиту (§Раздел 0, TRACE). |
| 178 | константа | `TRACE_SAP4_FLAG_MONTHS` |  |
| 179 | константа | `TRACE_SAP4_MINIMAL_DRIFT_HOURS` |  |
| 182 | функция | `trace_sap_2_independence()` | Два источника через одного посредника = один источник (§4.14). |
| 196 | функция | `trace_sap_4_temporal()` | Темпоральная близость в редакции аудитора (§4.14). |
| 211 | функция | `trace_sap_6_detail()` | Верификация детали (§4.14): имена, даты, суммы, должности. |

## trace_vector

- **путь**: `helix_pipeline/engine/trace_vector.py`
- **размер**: 206 строк, SHA-256 blob `e87fb3ba3ee6d08e…`
- **что это**: trace_vector.py — собирающая точка входа вектора TRACE.
- **зачем**: имя заранее — `helix_pipeline.engine.trace_vector.TraceVector` — тем же способом, что и для INTELLIGENCE (см. `intelligence_vector.py`, тот же приём, тот же автор решения). Большинство протоколов TRACE §4 (4.1–4.25) — это те же протоколы GI v6.2, уже собранные `GICore` (ICoI, SSD, NGI, ANI, APORIA, MPF,
- **коды состояний** (2): `HIGH`, `LOW`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_hitl_matrix.py`, `helix_pipeline/tests/test_ngi.py`, `helix_pipeline/tests/test_report_structure.py`, `helix_pipeline/tests/test_trace_vector.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 72 | класс | `TraceVector (7 публичных методов)` | Точка входа вектора TRACE (см. модульный docstring). |

## uc5_ai_preflight

- **путь**: `helix_pipeline/engine/uc5_ai_preflight.py`
- **размер**: 242 строк, SHA-256 blob `1a657114f994e192…`
- **что это**: uc5_ai_preflight.py — UC-5 AI Preflight/Postflight Protocol (INT §3.32).
- **зачем**: Закрывает INT-3.32 в gi62_patch_manifest.yaml (было SPEC_ONLY). Применяется, когда анализируемый материал создан AI, или когда сам следователь (как AI) генерирует аналитический текст в рамках расследования. БАЗОВОЕ ПРАВИЛО (буквально из спеки, не смягчается ничем ниже): AI-вывод = ECT-1 по умолчанию, всегда, без исключений. GL-06: AI не верифицирует AI — Independence Vector двух AI = 0. Это ЖЁСТКОЕ правило, а не «много недочётов»: как EXIT FAIL в exit_protocol.py, GL-06 VIOLATION форсирует общий FAIL независимо от того, с…
- **коды состояний** (3): `HIGH`, `LOW`, `MEDIUM`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_uc5_ai_preflight.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 35 | константа | `AI_OUTPUT_DEFAULT_ECT` |  |
| 37 | константа | `CRITICALITY_LEVELS` | tuple, 3 элементов |
| 41 | класс | `ChecklistItem (0 публичных методов)` |  |
| 49 | класс | `PreflightState (0 публичных методов)` | БЛОК A — вход для 4 под-блоков по 3 пункта каждый. |
| 71 | класс | `PreflightResult (0 публичных методов)` |  |
| 78 | функция | `run_preflight(state)` |  |
| 120 | класс | `VerifiedPart (0 публичных методов)` |  |
| 127 | класс | `PostflightState (0 публичных методов)` | БЛОК B — вход для 5 под-блоков по 3 пункта каждый. |
| 155 | константа | `SCA3_MIN_VERIFIED_FACTS` |  |
| 159 | класс | `PostflightResult (0 публичных методов)` |  |
| 168 | функция | `run_postflight(state)` |  |

## v61_critical_combinations

- **путь**: `helix_pipeline/engine/v61_critical_combinations.py`
- **размер**: 241 строк, SHA-256 blob `a06afc0e4eacbab9…`
- **что это**: v61_critical_combinations.py — v6.1 критические комбинации (INT §3.33).
- **зачем**: Закрывает INT-3.33 в gi62_patch_manifest.yaml (было SPEC_ONLY) — ЧЕТЫРЕ именованные комбинации из заголовка патча: CHAIN DEGRADATION, STRATEGIC DESTRUCTION, PERSONAL LOCK, RESOURCE-TELP. Раздел спеки (§3.33) вдобавок описывает набор ДОПОЛНИТЕЛЬНЫХ маркеров для WPL/HIL/FRCP (6-й критерий FRCP по WPL-приоритету, [HIL REINFECTION RISK], [HIL→EPISTEMIC LOCK] и т.д.) — это НЕ реализовано здесь и не покрыто закрытием INT-3.33: та часть требует изменения уже протестированных `frcp_gi.py`/`wpl.py`/`hil.py`, а не нового модуля-агре…
- **спека-якорь**: `GI_v6_2_COMPLETE.md`
- **коды состояний** (1): `CRITICAL`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_intelligence_closing_markers.py`, `helix_pipeline/tests/test_rpl.py`, `helix_pipeline/tests/test_v61_critical_combinations.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 43 | константа | `CHAIN_DEGRADATION_ECT_CEILING` |  |
| 47 | класс | `ChainDegradationInputs (0 публичных методов)` |  |
| 54 | класс | `ChainDegradationResult (0 публичных методов)` |  |
| 61 | функция | `check_chain_degradation(inp)` | Цепочка, документ и память деградированы полностью — все три сразу |
| 73 | константа | `_ANI_WARNING_PLUS` | tuple, 2 элементов |
| 77 | класс | `StrategicDestructionInputs (0 публичных методов)` |  |
| 89 | класс | `StrategicDestructionResult (0 публичных методов)` |  |
| 97 | функция | `check_strategic_destruction(inp)` | Признак целенаправленного разрушения расследования — RPL-ANI + |
| 114 | константа | `HIL_LOCKED_COMPRESSED_MIN` |  |
| 115 | константа | `HMP_HIGH_COMPRESSED_MIN` |  |
| 119 | класс | `PersonalLockInputs (0 публичных методов)` |  |
| 128 | класс | `PersonalLockResult (0 публичных методов)` |  |
| 135 | функция | `check_personal_lock(inp)` | Следователь, расследование и публичная позиция полностью заблокированы. |
| 155 | класс | `ResourceTelpInputs (0 публичных методов)` |  |
| 165 | класс | `ResourceTelpResult (0 публичных методов)` |  |
| 172 | функция | `check_resource_telp(inp)` | РАЗЛИЧЕНИЕ КРИТИЧНО (спека): RPL CRITICAL = ресурсы исчерпаны |
| 199 | функция | `check_ngi_hmp()` | Нарратив соблазнителен И дорог в отказе (§3.15). |
| 213 | функция | `check_ssc_char_pdp_x()` | Нарратор ненадёжен И память деградировала (§3.26). |
| 227 | функция | `check_chf_d_ssc_char_5()` | Меметическое давление И ненадёжный нарратор (§3.27). |

## wpl

- **путь**: `helix_pipeline/engine/wpl.py`
- **размер**: 255 строк, SHA-256 blob `b264568185d80c9c…`
- **что это**: wpl.py — Патч 65: WPL, слой провенанса свидетеля (GI v6.2, блок B1).
- **зачем**: ПРИНЦИП: «Подлинность свидетеля ≠ Целостность линии передачи показаний». Третье слепое пятно источниковой целостности, которое не закрывают предыдущие: PDE (58) — «Через сколько РУК прошёл документ?» объект: документ PDP-X (41) — «Что стало с памятью этого человека?» объект: источник WPL (65) — «Через сколько ЛЮДЕЙ прошло свидетельство?» объект: показание Пример спеки: A был очевидцем → рассказал B → B через 3 года рассказал C → C рассказал следователю, добавив интерпретацию. SAP верифицирует C (Trust 0.80), PDP-X проверяет п…
- **коды состояний** (19): `AMPLIFIED`, `CLEAN`, `COMPRESSED`, `CRITICAL`, `DIRECT`, `EMOTIONAL`, `HIGH`, `INHERITED`, `INSTITUTIONAL`, `INTERPRETED`, `LOW`, `MODERATE`, `POLITICAL`, `PROXIMATE`, `REFRAMED`, `RELAY`, `SOCIAL`, `TEMPORAL`, `UNKNOWN`
- **тесты, которые зовут модуль**: 8 — `helix_pipeline/tests/test_gi62_audit_regressions.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_intelligence_closing_markers.py`, `helix_pipeline/tests/test_intelligence_protocol_inputs.py`, `helix_pipeline/tests/test_s1_calibrated_and_codes.py`, `helix_pipeline/tests/test_wpl_doc.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 44 | константа | `WPL_DIRECT_FLOOR` |  |
| 45 | константа | `WPL_RELAY_FLOOR` |  |
| 46 | константа | `WPL_CONTAMINATED_FLOOR` |  |
| 47 | константа | `DEPTH_WARNING` |  |
| 48 | константа | `DEPTH_CRITICAL` |  |
| 49 | константа | `MEMORY_RELAY_MONTHS` |  |
| 52 | класс | `FirsthandStatus (0 публичных методов)` |  |
| 60 | класс | `TestimonyInheritance (0 публичных методов)` |  |
| 68 | класс | `ContaminationVector (0 публичных методов)` |  |
| 76 | класс | `TemporalDelay (0 публичных методов)` |  |
| 85 | константа | `_FIRSTHAND` | dict, 5 элементов |
| 90 | константа | `_DEPTH` | dict, 4 элементов |
| 91 | константа | `_INHERITANCE` | dict, 5 элементов |
| 96 | константа | `_DELAY` | dict, 5 элементов |
| 101 | константа | `_VECTORS` | dict, 3 элементов |
| 104 | функция | `hearsay_band(pct)` | ПОЛЕ 5: доля утверждений без атрибуции конкретному очевидцу. |
| 116 | класс | `WitnessProvenance (0 публичных методов)` | Девять полей модели провенанса свидетеля (Раздел I). |
| 131 | класс | `WPLResult (1 публичных методов)` |  |
| 154 | функция | `wpl_evaluate(w)` | WPL Score = 100 − Σ(штрафы). Вызывается при входе каждого источника |
| 228 | функция | `wpl_additional_markers(result)` | Дополнительные маркеры WPL из GI v6.2 П65 (INT §3.13, конец раздела). |
| 253 | функция | `apply_wpl_to_trust(trust_score, result)` | Применить множитель полосы WPL к Trust Score источника. |

## wpl_doc

- **путь**: `helix_pipeline/engine/wpl_doc.py`
- **размер**: 160 строк, SHA-256 blob `f07391a944c7f655…`
- **что это**: wpl_doc.py — WPL-DOC: цепочка передачи документа (TRACE §4.18).
- **зачем**: ━━━ НАЙДЕНО СВЕРКОЙ СПЕКИ С РЕАЛИЗАЦИЕЙ ━━━ Третий протокол с корнем «WPL» в экосистеме, и каждый — про другой объект: WPL (Патч 65, `wpl.py`) — цепочка ПОКАЗАНИЙ: через сколько ЛЮДЕЙ прошло свидетельство до следователя. PDE (Патч 58, `pde.py`) — цепочка ДОКУМЕНТА в целом: происхождение, custody gaps, редактура, рехостинг — восьмикомпонентная модель, 100→0. WPL-DOC (TRACE §4.18, здесь) — конкретно ГЛУБИНА ПЕРЕДАЧИ документа (depth 0/1-2/3+/сломана) плюс четыре КОРПОРАТИВНЫЕ точки риска (юротдел, PR, внутренняя версия, реакционный …
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_wpl_doc.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 46 | константа | `DEPTH_DIRECT` |  |
| 47 | константа | `DEPTH_RELAY_MAX` |  |
| 48 | константа | `DEPTH_CONTAMINATED_MIN` |  |
| 51 | константа | `_PDE_WARNING_PLUS` | tuple, 3 элементов |
| 54 | класс | `WPLDocBand (0 публичных методов)` |  |
| 62 | класс | `DocumentTransmissionChain (0 публичных методов)` | Что известно о передаче документа до следователя (TRACE §4.18). |
| 79 | класс | `WPLDocResult (1 публичных методов)` |  |
| 93 | константа | `_CORPORATE_RISK_LABELS` | tuple, 4 элементов |
| 105 | функция | `wpl_doc_evaluate(c, pde_band)` | Полоса WPL-DOC по глубине передачи + корпоративные точки риска. |

## вырождение_текста

- **путь**: `helix_pipeline/engine/вырождение_текста.py`
- **размер**: 88 строк, SHA-256 blob `322facdf5afc4b95…`
- **что это**: вырождение_текста.py — Phase 9 GOVERNANCE кодом: признаки вырождения текста модели.
- **зачем**: названия-метафоры, но за ними стоит измеримое явление: при декодировании с максимизацией правдоподобия текст скатывается в повторы и пресность (Holtzman et al. 2020, «The Curious Case of Neural Text Degeneration», arXiv 1904.09751). До этого модуля признаки не мерились ничем.
- **коды состояний** (7): `HIGHLY_COMPRESSIBLE`, `LOW_DIVERSITY`, `MAX_TOKENS`, `NOT_RUN`, `RAN`, `REPETITION`, `TRUNCATED`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_helix_sensor.py`, `helix_pipeline/tests/test_вырождение_текста.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 30 | константа | `MIN_TOKENS` |  |
| 32 | константа | `ПОРОГ_SEQ_REP_4` |  |
| 33 | константа | `ПОРОГ_DISTINCT_2` |  |
| 34 | константа | `ПОРОГ_СЖАТИЯ` |  |
| 35 | константа | `ПОРОГ_СЖАТИЯ_ДЛИНА` |  |
| 36 | константа | `ПОРОГИ_ПОМЕТКА` | строка: «пороги эвристические, не калиброваны на размеченных данных» |
| 38 | константа | `_СЛОВО` | re.compile('\\w+', re.UNICODE) |
| 39 | константа | `_КОНЕЦ` | re.compile('[.!?…»\\")\\]]\\s*$') |
| 42 | функция | `_нграммы(токены, n)` |  |
| 46 | функция | `seq_rep(токены, n)` |  |
| 51 | функция | `distinct(токены, n)` |  |
| 56 | функция | `сжатие(текст)` |  |
| 61 | функция | `признаки_вырождения(текст, finish_reason)` | Признаки Phase 9 по тексту. Модель не вызывается; результат детерминирован. |

## две_оси

- **путь**: `helix_pipeline/engine/две_оси.py`
- **размер**: 112 строк, SHA-256 blob `7b9e633ff45d4f9e…`
- **что это**: Д-5. Две оси до конца: уровень сведения (ECT) и уверенность вывода (23.10.2026).
- **зачем**: STANAG 2511 / AJP-2.1 оценивает источник и сведение НЕЗАВИСИМО: ненадёжный источник может сообщить подтверждённое. ICD 203 говорит о другом — об уверенности в ВЫВОДЕ: вывод на одном анонимном источнике не бывает высокоуверенным. Оба правила верны, но про разные величины, поэтому их две: ect — уровень сведения: первоисточник, независимые подтверждения, сверка со страницей (`конвейер_расследования.потолок_уровня`). Не меняется. conclusion_ect — уверенность вывода: min(ect, потолки от свойств источника). Потолок по с…
- **коды состояний** (6): `ANONYMITY`, `NOT_RUN`, `PDE`, `RAN`, `SOURCE`, `WPL`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_две_оси.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 28 | константа | `ОСЬ_ПОТОЛКА` | dict, 5 элементов |
| 36 | константа | `ПРИЧИНА` | dict, 5 элементов |
| 45 | функция | `_потолок(результат)` |  |
| 53 | функция | `потолки_источников(protocols)` | uri источника → потолки оси вывода от протоколов, которые по нему отработали. |
| 70 | функция | `две_оси(research_result, protocols)` | По каждому доказательству конвейера: уровень сведения и уверенность вывода. |
| 100 | функция | `раздел_отчёта(сводка)` | Короткий раздел для отчёта: только там, где вывод слабее сведения. |

## диагностичность_ach

- **путь**: `helix_pipeline/engine/диагностичность_ach.py`
- **размер**: 130 строк, SHA-256 blob `cda0e4729e1b4622…`
- **что это**: Диагностичность Хейера и построчная расшифровка счёта гипотез (ICD 203, LOGIC).
- **зачем**: Источник: Мастер-ТЗ HELIX-CORE v2.5, модуль 1.3 (21.10.2026). Замер по прогону 4: счёт гипотез (0 / −14 / −46) выведен без слагаемых, а «0 у H1» говорит лишь об отсутствии опровержений, не о силе различающих доказательств. ФОРМУЛЫ ТЗ D(F) = |{H : R=−1}| / K, если 0 < |I| < K, иначе 0 диагностичность факта (ревизия 22.10.2026; по ТЗ было 1 − |{H : R=+1}| / K — N считалось опровержением); W(F) = E(F) · D(F) диагностический вес; C(H) = − Σ E(F) по R(F,H) = −1 штраф противоречий (как INT §8.1); S(H) = Σ R(F,H) · E(F) ·…
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_мастер_тз_v25.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `_R` | dict, 3 элементов |
| 41 | функция | `диагностичность(оценки)` | D(F) по оценкам факта {гипотеза: C\|I\|N}. |
| 54 | функция | `разложение(гипотезы, доказательства)` | Таблица вкладов. `доказательства`: [{id, ect, ach: {H: C\|I\|N}}]. |
| 85 | функция | `множество_разворота(доказательства, лидер, соперник, домены)` | Heuer, гл. 8, шаг 6 — минимальный набор доказательств, без которого лидер теряет |
| 121 | функция | `таблица_markdown(разл, гипотезы)` | Таблица для отчёта: читатель складывает столбцы сам и получает итоговый счёт. |

## калибровка_пометка

- **путь**: `helix_pipeline/engine/калибровка_пометка.py`
- **размер**: 12 строк, SHA-256 blob `443f5eb1c37c9a98…`
- **что это**: калибровка_пометка.py — одна пометка «не калибровано» для выдачи модулей с порогами.
- **зачем**: полос в HMP, RDI, WPL, HIL, RPL, PDE, PDP-X и SSC-CHAR взяты из спецификаций и нигде не проверены на размеченных данных (пометка П в реестрах). Ревизия
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_governance_primary_output.py`, `helix_pipeline/tests/test_helix_sensor.py`, `helix_pipeline/tests/test_pde_patch58.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 10 | константа | `NOT_CALIBRATED` | строка: «не калибровано: веса, множители и пороги полос взяты из спецификации и» |

## канонизация_фактов

- **путь**: `helix_pipeline/engine/канонизация_фактов.py`
- **размер**: 265 строк, SHA-256 blob `e4accead1c946d12…`
- **что это**: Канонизация фактов: слияние дублей между подвопросами (Мастер-ТЗ v2.5, модуль 1.2).
- **зачем**: Прогон 4 (Луна): снимки LRO извлечены 9 раз, приём сигналов в Бохуме 6, отражатели 4–8; дубли раздувают отстойник и делят источники одного утверждения между копиями. ВЕРСИЯ 2 (21.10.2026). Первая версия («≥ 2 общих заглавных слова, числа не спорят») на настоящих 65 фактах прогона 4 дала 18 слияний, из них группа из девяти разных фактов (отчёт SP-214 + лазерная локация + …): узел брал текст самого длинного члена и цепочкой притягивал следующие. Падежи («Аполлона»/«Аполлон») не сводились, служебная метка «ECT-4» …
- **коды состояний** (3): `ENTITY_CANON_MERGED`, `F71`, `NO_DUPLICATES`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_мастер_тз_v25.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `ПОРОГ` |  |
| 47 | константа | `ДОПУСК_ЧИСЕЛ` |  |
| 49 | константа | `_СЛОВО` | re.compile('[A-Za-zА-Яа-яЁё][A-Za-zА-Яа-яЁё\\-]*') |
| 50 | константа | `_СЛУЖЕБНОЕ` | re.compile('\\[(?:ECT-\\d\|ГАЛЛЮЦИНАЦИЯ)[^\\]]*\\]\|\\bECT-\\d\\b\|\\b[FQE]\\d+\\b' |
| 51 | константа | `_СТОП` | set, 59 элементов |
| 57 | константа | `_ГОД` | re.compile('(?<!\\d)(1[89]\\d\\d\|20\\d\\d)(?!\\d)') |
| 67 | функция | `_лемма(слово)` |  |
| 74 | функция | `_чистый(текст)` |  |
| 78 | функция | `леммы(текст)` |  |
| 87 | функция | `годы(текст)` |  |
| 91 | функция | `_числа(текст)` |  |
| 96 | функция | `_близко(a, b)` |  |
| 100 | функция | `конфликт(a, b)` | Годы не пересекаются или числа одной единицы разошлись сверх допуска. |
| 114 | класс | `_Веса (0 публичных методов)` | IDF по набору фактов одного прогона: частое слово (Apollo, Луна) почти ничего не весит. |
| 130 | функция | `сходство(a, b, вес)` |  |
| 138 | функция | `канонизировать(факты, порог)` | `факты`: [{id, text, sources?: [url…], subquestion?}] → канонические узлы. |
| 172 | функция | `можно_слить(a, b, порог)` | Пара без контекста набора: веса слов равные. |
| 180 | функция | `оценить(узлы, строгие, допустимые)` | Точность и полнота по парам против разметки. |
| 199 | константа | `ПОЛ_ПЕРЕКРЫТИЯ` |  |
| 201 | константа | `ИНСТРУКЦИЯ_РАЗМЕТКИ` | строка: «Ты размечаешь дубли. Дубль — два факта, утверждающие ОДНО И ТО ЖЕ (оди» |
| 209 | функция | `проверить_группы(факты, группы)` | Группы модели → группы, принятые кодом. |
| 236 | функция | `канонизировать_со_смыслом(факты, разметить)` | `разметить(инструкция, текст) -> {"groups": [...]}` — вызов модели без поиска. |

## каскад_источников

- **путь**: `helix_pipeline/engine/каскад_источников.py`
- **размер**: 420 строк, SHA-256 blob `aa4c099bce4087cc…`
- **что это**: каскад_источников.py — гейт «тема источника» и бесплатный каскад для нечитаемых страниц.
- **зачем**: страницах, которые код не прочитал: 403 издательств, заглушка платной книги, PDF без текста. У научных работ часто есть открытая копия. Но найденный по DOI документ может оказаться посторонним: у факта F37 DOI 10.2514/3.28972 вёл на статью 1967 г. о краске «Сервейера», а факт — о защите командного модуля. Читать такой PDF бесполезно, а сверять по нему числа вредно. Поэтому порядок такой: найти документ → пройти гейт темы → только потом числа.
- **коды состояний** (3): `DOI`, `OPENALEX_API_KEY`, `TOPIC_MISMATCH_REJECTED`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_каскад_источников.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 47 | константа | `ПОРОГ_ПОКРЫТИЯ` |  |
| 49 | константа | `ПОРОГ_ЗАГЛУШКИ` |  |
| 51 | константа | `ЧИСЛО_КАНДИДАТОВ` |  |
| 53 | константа | `СТАТУС_ОТКАЗА` | строка: «TOPIC_MISMATCH_REJECTED» |
| 55 | константа | `API_OPENALEX` | строка: «https://api.openalex.org» |
| 56 | константа | `API_CROSSREF` | строка: «https://api.crossref.org» |
| 57 | константа | `NTRS` | строка: «https://ntrs.nasa.gov» |
| 58 | константа | `ТАЙМАУТ` | httpx.Timeout(10.0) |
| 59 | константа | `ЗАГОЛОВКИ_API` | dict, 1 элементов |
| 61 | константа | `Http` |  |
| 62 | константа | `Загрузчик` |  |
| 65 | функция | `_http_json(url, params)` | JSON-ответ или None (любая ошибка, код не 200). |
| 77 | константа | `_СЛОВО` | re.compile('[A-Za-zА-Яа-яЁё][A-Za-zА-Яа-яЁё\\-]*') |
| 78 | константа | `_КИРИЛЛИЦА` | re.compile('[А-Яа-яЁё]') |
| 79 | константа | `_РИМ` | dict, 3 элементов |
| 81 | константа | `_КОД` | re.compile('\\b([A-ZА-ЯЁ][A-Za-zА-Яа-яЁё]{2,})[ \\-]?(\\d{1,3}\|[IVX]{1,5})\\b') |
| 83 | константа | `_КОД_ПРИБОРА` | re.compile('\\b([A-Z]{2,6})-?(\\d{1,4})\\b') |
| 85 | константа | `_СТОП` | frozenset('\nкоторые который которая которое которых которому этого этот эта это |
| 94 | константа | `_ТРАНС_ЗВОНКОСТЬ` | str.maketrans({'b': 'p', 'd': 't', 'g': 'k', 'v': 'f', 'z': 's', 'j': 's'}) |
| 97 | функция | `_римское(с)` |  |
| 107 | функция | `_номер(с)` |  |
| 111 | функция | `_скелет(слово)` | Согласный скелет слова любого алфавита; звонкие и глухие объединены. |
| 117 | функция | `_основа(слово)` |  |
| 121 | функция | `_предложения_с_начала(текст)` | Позиции первых слов предложений (там заглавная буква ничего не значит). |
| 129 | функция | `_якоря_факта(факт)` | (имена, коды): имена — основа или скелет слова; коды — (скелет имени, номер). |
| 153 | функция | `_слова_документа(текст)` | (основы, скелеты, коды) документа. |
| 169 | функция | `_знаменательные(факт)` |  |
| 178 | константа | `_СТОП_НОРМ` | frozenset((с.replace('ё', 'е') for с in _СТОП)) |
| 181 | функция | `_алфавит_слова(слово)` |  |
| 185 | функция | `покрытие_слов(факт, документ)` | Доля знаменательных слов факта (по основе из 5 букв), которые есть в документе. |
| 211 | функция | `сверить_тему_источника(факт, заголовок, текст)` | Тот ли это документ, о котором факт? Не сверяет числа — только тему. |
| 238 | константа | `_ОШИБКИ_ДОСТУПА` | re.compile('HTTP (401\|403\|429)\\b') |
| 239 | константа | `_PDF_ПУСТО` | tuple, 4 элементов |
| 242 | функция | `нужен_каскад(стр)` | Обычная загрузка дала 401/403/429, заглушку или PDF без текста, и замены ещё нет. |
| 256 | функция | `_ключ_openalex()` |  |
| 260 | функция | `_аннотация(инд)` |  |
| 266 | функция | `_слова_названия(т)` |  |
| 270 | функция | `_похоже(а, б)` |  |
| 275 | функция | `_из_openalex(w)` |  |
| 283 | функция | `_openalex(http, doi, название)` |  |
| 295 | функция | `_результаты(данные)` |  |
| 300 | функция | `_crossref(http, doi, название)` | Название и аннотация; открытой копии Crossref не даёт, но ссылки из `link` берутся. |
| 325 | функция | `_ntrs(http, запрос)` | NASA NTRS: поиск, затем /api/citations/{id}/downloads (полный текст .txt, иначе PDF). |
| 348 | функция | `_запрос_ntrs(факт, адрес, найденные)` | Название найденной работы; иначе слова адреса NASA; иначе латинские слова факта. |
| 366 | функция | `каскад(факт, адрес, загрузчик)` | Открытая версия недоступной страницы. Гейт темы — до того, как документ вернётся. |

## конвейер_расследования

- **путь**: `helix_pipeline/engine/конвейер_расследования.py`
- **размер**: 1972 строк, SHA-256 blob `f2c420718d5b7b76…`
- **что это**: конвейер_расследования.py — расследование HELIX по ролям (19.10.2026).
- **зачем**: конструкт — давай улучшим так, чтобы он сработал как ты и больше, чем ты».
- **коды состояний** (28): `AK_DATA_DIR`, `ALTERNATIVE`, `BOUND`, `CONTRADICTED`, `CONTRADICTS`, `CORE_BOUND_AUX_PRUNED`, `EMPTY_RESPONSE`, `FAILED`, `HELIX_CANON`, `HELIX_MEMORY`, `HELIX_MEMORY_DIR`, `HELIX_PAGES`, `HELIX_RECOVERY`, `HELIX_SEARCH_TIMEOUT`, `HELIX_THREADS`, `HELIX_WIKI_BASELINE`, `NEEDS_RECOVERY`, `NOT_RUN`, `NO_NUMBERS`, `NULL`, `NUMBERS`, `PRIMARY`, `QUOTE`, `RAN`, `SEARCH_CALL_TIMEOUT`, `STOP`, `UNKNOWN`, `WORDS`
- **тесты, которые зовут модуль**: 6 — `helix_pipeline/tests/test_каскад_источников.py`, `helix_pipeline/tests/test_конвейер_расследования.py`, `helix_pipeline/tests/test_мёртвая_зона_и_домены.py`, `helix_pipeline/tests/test_опора_кеш_и_полярность.py`, `helix_pipeline/tests/test_открытые_версии.py`, `helix_pipeline/tests/test_склейка_перепечаток.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 73 | константа | `ПОТОЛОК_ПОДВОПРОСОВ` |  |
| 74 | константа | `ПОТОЛОК_ВГЛУБЬ` |  |
| 78 | константа | `ПОТОКОВ` | int(os.getenv('HELIX_THREADS', '8') or 8) |
| 82 | константа | `ПОТОЛОК_ВЫЗОВА` | float(os.getenv('HELIX_SEARCH_TIMEOUT', '150') or 150) |
| 83 | константа | `ПАМЯТЬ_ПОТОЛОК` |  |
| 84 | константа | `_ВЫХОД` |  |
| 100 | константа | `_ПЕРВИЧНЫЕ_ДОМЕНЫ` | tuple, 78 элементов |
| 118 | константа | `_СПРАВОЧНИКИ` | tuple, 45 элементов |
| 132 | константа | `_СМИ` | tuple, 84 элементов |
| 150 | функция | `домен(источник)` | Домен источника. У Gemini адрес — переадресация Vertex, домен лежит в |
| 160 | функция | `класс_источника(д)` |  |
| 177 | функция | `потолок_уровня(источники)` | Высший допустимый уровень по типу источников, с причиной словами. |
| 206 | функция | `json_из_текста(текст)` | JSON из ответа модели: снять ```json, взять от первой { до последней }. |
| 219 | функция | `_норм(т)` |  |
| 223 | константа | `_ФАКТ` | re.compile('^\\s*(?:[-*•]\|\\d+[.)])?\\s*\\**ФАКТ\\**:\\s*(.+)$', re.M) |
| 224 | константа | `_НЕ_НАЙДЕНО` | re.compile('^\\s*(?:[-*•])?\\s*\\**НЕ НАЙДЕНО\\**:\\s*(.+)$', re.M) |
| 227 | функция | `факты_из(текст)` |  |
| 244 | функция | `_источники_строки(строка, ответ)` | Какие найденные поиском страницы подкрепляют ЭТУ строку: опоры |
| 268 | функция | `_папка_памяти()` |  |
| 281 | функция | `ключ_темы(тема)` |  |
| 285 | функция | `память_прочесть(тема)` |  |
| 296 | функция | `память_записать(тема, доказательства)` |  |
| 320 | константа | `ЗАДАНИЕ_ИЩЕЙКЕ` | строка: «

ТВОЯ РОЛЬ — ПОИСК, А НЕ ОТЧЁТ. Отчёт напишет другой шаг. Верни не ме» |
| 344 | функция | `_сегодня()` | Дата прогона словами — модель иначе судит по дате своего обучения (вопрос |
| 353 | функция | `_строки_опоры(пункты)` |  |
| 357 | функция | `_промпт_плана(тема, память, потолок, опора)` |  |
| 437 | функция | `_промпт_ищейки(тема, вопрос, гипотезы, память, опора, научные)` |  |
| 464 | константа | `ПРЕДЕЛ_ДОМЕНОВ_В_ТАБЛИЦЕ` |  |
| 467 | функция | `_таблица_фактов(факты)` |  |
| 480 | функция | `_промпт_вглубь(тема, факты, вопросы, потолок)` |  |
| 509 | функция | `_промпт_судьи(тема, гипотезы, вопросы, факты, не_найдено, непокрыто, снято, опора)` |  |
| 599 | функция | `_вызвать_без_поиска(iv, prompt)` | Вызов судьи (без поиска) с одним повтором, если JSON не разобрался. |
| 609 | функция | `_искать(iv, prompt)` |  |
| 622 | функция | `_с_потолком(функция, аргумент, секунд, контекст)` | Вызов в своём потоке: через `секунд` перестаём ждать (поток-сирота доживает сам — |
| 645 | функция | `_параллельно_с_потолком(функция, задания, секунд)` | ЭТАП 1: волна вызовов поиска, ПОТОКОВ одновременно, у каждого свой потолок времени. |
| 657 | функция | `_параллельно(функция, задания)` | Каждое задание — в копии контекста вызывающего потока. Без этого переменные |
| 668 | константа | `_ПРЕДЕЛ_СЫРОГО` |  |
| 671 | функция | `_причина_остановки(raw)` |  |
| 682 | функция | `_телеметрия_судьи(режим, raw, данные, секунд, входных_знаков)` | Одна попытка судьи: что вернул провайдер и чем кончилось. Текст хранится только у |
| 699 | функция | `_вызов_судьи(iv, режим, prompt, попытки)` |  |
| 707 | функция | `_слить_ответы_судьи(части)` | Пакеты судьи → один ответ. Штраф гипотезы — сумма по доказательствам, поэтому |
| 722 | функция | `_судья_цепочкой(iv, тема, гипотезы, вопросы, факты, не_найдено, опора, попытки)` | Судья с запасными путями; каждая попытка записана в `попытки`. |
| 760 | функция | `_план(iv, тема, память, потолок, опора)` |  |
| 800 | функция | `провести(iv, тема)` | Расследование конвейером. Возвращает тот же словарь, что |
| 1100 | функция | `_слить_дубли(iv, факты)` | Факты-дубли → канонические. Каноническим остаётся первый по номеру факт группы, |
| 1147 | константа | `ДОБОР_ФАКТОВ` |  |
| 1148 | константа | `ДОБОР_ПАЧКА` |  |
| 1149 | константа | `_ВАЖНОСТЬ_ВИДА` | dict, 5 элементов |
| 1150 | константа | `_НОМЕР_В_ФАКТЕ` | re.compile('^\\s*\\[?\\s*(F\\d+)\\s*\\]?\\s*[:.\\-—]?\\s*(.*)$') |
| 1153 | константа | `_ЛАТИНСКОЕ_ИМЯ` | re.compile('\\b[A-Z][A-Za-z0-9\\-]{2,}(?:\\s+(?:of\|and\|the\|[A-Z][A-Za-z0-9\\-]+) |
| 1154 | константа | `_ЧИСЛО_С_ЕДИНИЦЕЙ` | re.compile('\\d[\\d\\s.,]*\\s?(?:%\|рад\|мЗв\|км\|кг\|г\|м\|МГц\|ГГц\|КБ\|мм\|см\|rad\|km\|kg\| |
| 1155 | константа | `_ЗАМЕНА_ФОРМ` | dict, 4 элементов |
| 1158 | функция | `точный_запрос(текст, редкие)` | ЭТАП 2: запрос в кавычках по самому редкому в факте — латинским именам (отчёт, |
| 1172 | функция | `_добрать(iv, тема, факты, вопросы, ответы_добора)` | Факт без источника → отдельный поиск первоисточника. Модель повторяет номер факта |
| 1258 | константа | `_ЧИСЛА_СОШЛИСЬ` | tuple, 3 элементов |
| 1261 | функция | `_вес_страницы(найдена)` | Какая страница лучше: сперва та, где подтвердилось число, затем — не справочник. |
| 1269 | функция | `_числа_с_цитатой(ф, р)` | Цитата найдена на странице дословно, а число страницей не подтвердилось (формат записи |
| 1280 | функция | `_сверить_со_страницами(факты, страницы)` | Факт без источника ищется на страницах своего поиска; у факта с неподтверждённым |
| 1359 | функция | `_пустые_подвопросы(данные, доказательства, вопросы)` | Подвопросы без вывода, прошедшего гейт, и без явного «не найдено» судьи. |
| 1368 | функция | `_все_опоры(вызовы, факты)` | Источники и опоры всех вызовов + сами факты, подкреплённые поиском: |
| 1389 | функция | `_число_в_фактах(значение, факты)` | Число стоит в строке одного из фактов, на которые ссылается вывод; |
| 1398 | функция | `_собрать_доказательства(данные, факты, вопросы, источники, опоры)` |  |
| 1489 | константа | `_ГОД` | re.compile('(1[6-9]\|20)\\d{2}(-?[ехя]\|-?х годах\|s)?') |
| 1494 | константа | `СТАТУСЫ_ОПОРЫ` | tuple, 5 элементов |
| 1495 | константа | `_СТАТУСЫ_СУДЬИ` | tuple, 4 элементов |
| 1498 | функция | `d_page(д)` | Вывод держится на странице, прочитанной кодом, и источник не справочник. |
| 1503 | функция | `_невключённые_факты_пунктов(опора, вопросы, факты, использованные)` | Пункт опоры → факты его подвопроса, которые поиск нашёл, а судья в выводы не включил |
| 1522 | функция | `_сверка_с_опорой(опора, данные, доказательства, невключённые)` | Каждый пункт Википедии — со статусом судьи и доказательствами, прошедшими |
| 1576 | функция | `_ach(гипотезы, доказательства, страницы, склеивать_перепечатки)` | Счёт гипотез по INT §8 — кодом. CF не считается: у конвейера нет |
| 1611 | функция | `_чувствительность(гип, доказательства, матрица, счёт, ничья, страницы, склеивать_перепечатки)` | Heuer, гл. 8, шаг 6: минимальный набор доказательств, без которого лидер теряет |
| 1639 | функция | `_склеить_домены(доказательства, домены, страницы)` | Домены перепечаток заменяются доменом-представителем кластера. Возвращает новые |
| 1666 | функция | `_мн(n, одно, два, пять)` |  |
| 1671 | функция | `_класс_надёжности(источники)` | Ось «источник» по аналогии с Admiralty Code (STANAG 2511 оценивает источник отдельно |
| 1688 | функция | `_уверенность(счёт, ничья, чувствительность)` | Уверенность в выводе словами ICD 203 («high / moderate / low confidence»). |
| 1711 | функция | `_точка(т)` |  |
| 1716 | функция | `_строка_доказательства(д)` |  |
| 1753 | функция | `_строка_опоры(сверка)` | Одна строка под итогом: на что опирался разбор и что с этим стало. |
| 1767 | функция | `_строка_галлюцинации(х)` |  |
| 1771 | константа | `_СВЕРКА_СЛОВАМИ` | dict, 4 элементов |
| 1775 | функция | `_что_не_сошлось(н)` | «: на странице iaea.org вместо 31 стоит 30» — точное место ошибки; пусто, если страница не читалась. |
| 1787 | функция | `_строка_факта(ф)` |  |
| 1813 | функция | `_разложение_счёта(ach, доказательства)` | Каждое слагаемое счёта гипотез (ICD 203, LOGIC): читатель складывает столбец |
| 1835 | функция | `_отчёт(данные, вопросы, гипотезы, доказательства, ach, снято, факты_вне, не_найдено, сверка, сверка_страниц, канон, добор)` | Отчёт собирает код — из проверенных частей, поэтому он не рвётся. |

## научная_статистика

- **путь**: `helix_pipeline/engine/научная_статистика.py`
- **размер**: 257 строк, SHA-256 blob `de3e9d1105ce4a70…`
- **что это**: научная_статистика.py — что научные работы говорят ЧИСЛАМИ, и чего нет в Википедии.
- **зачем**: Решение владельца 24.10.2026: «научный метод — статистика». Модель здесь не зовётся ни разу: всё ниже — регулярки и арифметика по тексту аннотаций, которые уже скачаны из PubMed и OpenAlex (`научные_базы.py`). ТРИ ВЕЩИ. 1. Вид исследования — по признакам, а не по ярлыку. Метаанализ и когорта весят больше отдельного случая; отозванная статья не идёт в отчёт вовсе (OpenAlex `is_retracted`, PubMed «Retracted Publication»). Аннотация — заявление авторов, а не проверенный факт: «спин» в аннотациях задокументирован (…
- **коды состояний** (7): `CIXC`, `CIXCV`, `EAR`, `ERR`, `IRR`, `SIR`, `SMR`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_научная_статистика.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 34 | константа | `РАНГ_ВИДА` | dict, 7 элементов |
| 37 | константа | `_ПРИЗНАКИ` | list, 6 элементов |
| 45 | константа | `_ВИДЫ_PUBMED` | dict, 4 элементов |
| 49 | функция | `вид_исследования(работа)` | Вид работы: сперва по типам публикации PubMed, затем по словам заголовка и аннотации. |
| 61 | функция | `отозвана(работа)` |  |
| 67 | константа | `_ЧИСЛО` | строка: «[-−–]?(?<![\d.,])\d+(?:[.,]\d+)?(?![\d])» |
| 70 | константа | `_ПОДПИСЬ_ИНТЕРВАЛА` | re.compile('\\(?\\b(9[05])\\s*%\\s*(?:confidence intervals?\|CI\|ДИ\|доверительн\\w |
| 72 | константа | `_МЕТКА` | dict, 2 элементов |
| 73 | константа | `_МЕРА` | re.compile(f'(?<![\\wа-яё])(?P<мера>ERR\|EAR\|RR\|HR\|OR\|SMR\|SIR\|IRR\|aHR\|aOR\|aRR\|exc |
| 82 | константа | `_КОД_МЕРЫ` | dict, 12 элементов |
| 87 | константа | `_ОТНОШЕНИЯ` | set, 9 элементов |
| 91 | константа | `_ЧИСЛЕННОСТЬ` | re.compile('(?<![\\d.,])(?P<n>\\d{1,3}(?:[ ,]\\d{3})+\|\\d{3,})(?P<тыс>\\s*thousa |
| 98 | функция | `_f(т)` |  |
| 102 | функция | `меры_эффекта(текст)` | Меры эффекта с интервалом из текста аннотации; значимость — по интервалу. |
| 124 | функция | `численность(текст)` | Численность группы, если в аннотации она названа одна. |
| 141 | константа | `_DOI` | re.compile('10\\.\\d{4,9}/[^\\s\\"\'<>&?#]+', re.I) |
| 142 | константа | `_PMID` | re.compile('(?:pubmed\\.ncbi\\.nlm\\.nih\\.gov/\|ncbi\\.nlm\\.nih\\.gov/pubmed/\|p |
| 145 | функция | `ключи_ссылок(ссылки)` | DOI (в нижнем регистре) и «pmid:N» из внешних ссылок статьи Википедии. |
| 157 | функция | `ссылки_википедии(статьи, запрос)` | Ключи DOI/PMID из списков литературы статей опоры (API Википедии, extlinks). |
| 185 | функция | `в_википедии(работа, ключи)` |  |
| 193 | функция | `разобрать(работы, ключи_вики)` | Строки таблицы по работам с аннотацией: вид, численность, меры эффекта, есть ли в Википедии. |
| 215 | функция | `_эффект_строкой(э)` |  |
| 221 | функция | `раздел_отчёта(разбор, предел)` | Два раздела Markdown: таблица статистики и «сверх Википедии». |

## научные_базы

- **путь**: `helix_pipeline/engine/научные_базы.py`
- **размер**: 703 строк, SHA-256 blob `9bdf7a9fd2b5252b…`
- **что это**: научные_базы.py — поиск научных работ для вектора INTELLIGENCE.
- **зачем**: «Хочу, чтобы он работал через Google, через Bing, через другие поисковые системы… сравнить, посмотреть источники, научные работы». Первым шагом выбраны научные базы: они бесплатны, а поиск в сети через Azure (Bing) уже есть. Так у одного факта появляется второй, независимый от поисковика путь подтверждения: статья в журнале с автором, годом и DOI.
- **коды состояний** (11): `CONCLUSION`, `DOI`, `ERROR`, `FINDING`, `HELIX_SCHOLAR_QUERIES`, `HELIX_SCHOLAR_QUERIES_SLOW`, `LIMIT`, `NCBI_API_KEY`, `OPENALEX_API_KEY`, `RESULT`, `SEMANTIC_SCHOLAR_API_KEY`
- **тесты, которые зовут модуль**: 4 — `helix_pipeline/tests/test_научные_базы.py`, `helix_pipeline/tests/test_научные_базы_пределы.py`, `helix_pipeline/tests/test_открытые_версии.py`, `helix_pipeline/tests/test_починка_06_10.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 49 | константа | `РАБОТ_НА_БАЗУ` |  |
| 50 | константа | `ТАЙМАУТ` |  |
| 53 | константа | `ПОЧТА` | строка: «denis@helixcom.net» |
| 54 | константа | `ПОЛЬЗОВАТЕЛЬ` | dict, 1 элементов |
| 56 | константа | `Работа` |  |
| 59 | константа | `_S2_ЗАМОК` | threading.Lock() |
| 62 | константа | `_S2_ИНТЕРВАЛ` |  |
| 63 | константа | `_S2_ИНТЕРВАЛ_С_КЛЮЧОМ` |  |
| 64 | константа | `_S2_ПОСЛЕДНИЙ` | list, 1 элементов |
| 66 | константа | `_спать` |  |
| 69 | функция | `_ключ(имя)` |  |
| 73 | функция | `_отказ(ответ)` |  |
| 80 | функция | `_doi(значение)` |  |
| 88 | функция | `openalex(запрос)` |  |
| 119 | константа | `ДЛИНА_АННОТАЦИИ` |  |
| 122 | функция | `аннотация_openalex(индекс)` | OpenAlex отдаёт аннотацию «перевёрнутым индексом» {слово: [позиции]} — собрать текст. |
| 135 | функция | `openalex_китай(запрос)` | Китайская наука: работы с китайскими организациями и работы на китайском. |
| 168 | функция | `s2_get(путь, params)` | Один запрос к Semantic Scholar Graph API под общим замком процесса. |
| 198 | функция | `semantic_scholar(запрос)` |  |
| 221 | функция | `crossref(запрос)` |  |
| 247 | константа | `_ATOM` | dict, 2 элементов |
| 250 | функция | `arxiv(запрос)` |  |
| 279 | константа | `_NCBI_ЗАМОК` | threading.Lock() |
| 280 | константа | `_NCBI_ПОСЛЕДНИЙ` | list, 1 элементов |
| 281 | константа | `NCBI_ПАУЗА` |  |
| 284 | функция | `_ncbi_get(url, params)` |  |
| 297 | константа | `ПРЕФИКС_PUBMED` | строка: «pubmed:» |
| 300 | константа | `ФИЛЬТР_ДОКАЗАТЕЛЬНЫХ` | строка: «(cohort studies[mh] OR meta-analysis[pt] OR systematic review[pt] OR c» |
| 302 | константа | `РАБОТ_PUBMED` |  |
| 305 | функция | `_esearch(общие, запрос, сколько)` |  |
| 321 | функция | `pubmed(запрос)` |  |
| 380 | функция | `аннотации_pubmed(xml)` | PMID → текст аннотации из ответа efetch (разделы BACKGROUND/RESULTS склеиваются). |
| 403 | константа | `ПРЕФИКС_RU` | строка: «ru:» |
| 404 | константа | `РУССКИЕ_БАЗЫ` | set, 2 элементов |
| 407 | функция | `киберленинка(запрос)` | Русскоязычные научные статьи: КиберЛенинка (открытый поиск, аннотации, журналы ВАК |
| 435 | константа | `БАЗЫ` | dict, 7 элементов |
| 448 | функция | `_ключ_работы(р)` |  |
| 454 | константа | `_МЕДЛЕННЫЕ` | set, 2 элементов |
| 457 | функция | `_предел(имя, по_умолчанию)` |  |
| 464 | функция | `найти_работы(запросы, базы)` | Спросить все базы по всем запросам параллельно и склеить дубли. |
| 601 | константа | `_СТОП` | set, 35 элементов |
| 608 | функция | `_значимые_слова(текст)` |  |
| 615 | функция | `запросы_из_поиска(тема, поисковые_запросы, заголовки_источников)` | Запросы для научных баз: английские запросы, которые модель уже |
| 659 | константа | `АННОТАЦИЯ_В_ПРОМПТЕ` |  |
| 662 | функция | `блок_для_промпта(найдено, предел)` | Список работ для следующего раунда — чтобы модель могла на них |
| 693 | константа | `_ПРИЗНАКИ_НОВОСТИ` | re.compile('новост\|\\bсми\\b\|публикаци[яи]\\s+(?:в\|из)\|пресс-релиз\|журналист\|\\b |
| 700 | функция | `новостная_тема(тема)` | Тема — проверка новости/публикации СМИ, а не научный вопрос. |

## опора_википедия

- **путь**: `helix_pipeline/engine/опора_википедия.py`
- **размер**: 235 строк, SHA-256 blob `b15bc397eb567555…`
- **что это**: Опора: сначала то, что люди уже собрали, — потом проверка и дополнение.
- **зачем**: До этого дня план разбора строила модель по памяти. Замер по Луне (прогон 4, `docs/HELIX_ЛУНА_ЧЕСТНЫЙ_ВЕРДИКТ_ПРОГОН_4.md`): пять пунктов, которые есть в Википедии (Кубрик, следы и пыль, стёртые плёнки, задержка связи, перекрестия), в план не попали вовсе — модель их «не вспомнила». С опорой охват не ниже статьи по устройству, а работа движка — проверить каждый её пункт по первоисточникам, найти ошибки и добавить то, чего в статье нет.
- **коды состояний** (2): `AK_DATA_DIR`, `HELIX_WIKI_CACHE_DIR`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_конвейер_расследования.py`, `helix_pipeline/tests/test_опора_кеш_и_полярность.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 50 | константа | `АДРЕС` | строка: «https://{язык}.wikipedia.org/w/api.php» |
| 52 | константа | `ЗАГОЛОВКИ` | dict, 1 элементов |
| 53 | константа | `ПРЕДЕЛ_СТАТЕЙ` |  |
| 54 | константа | `ПРЕДЕЛ_ЗНАКОВ_СТАТЬИ` |  |
| 55 | константа | `ПРЕДЕЛ_ПУНКТОВ` |  |
| 56 | константа | `_ПОЛЯРНОСТИ` | tuple, 2 элементов |
| 59 | константа | `_ШТАМП_ECT` | re.compile('\\s*\\[ECT-[^\\]]*\\].*$', re.S) |
| 62 | функция | `_без_штампа(текст)` |  |
| 64 | константа | `_НОМЕР` | re.compile('[ОO](\\d{1,3})\\b') |
| 67 | функция | `_промпт_статей(тема)` |  |
| 78 | функция | `_промпт_пунктов(тема, статьи)` |  |
| 98 | функция | `_запрос(язык, параметры)` |  |
| 106 | функция | `скачать(язык, заголовок)` | Полный текст статьи; нет такой — первая из поиска по заголовку. |
| 134 | функция | `_папка_кеша()` |  |
| 140 | функция | `_ключ_темы(тема)` |  |
| 144 | функция | `_ревизии_актуальны(статьи)` | Версии статей те же, что при разборе. Нет сети или нет revid — кеш не берём. |
| 160 | функция | `_из_кеша(тема)` | Замороженный разбор: пока версии статей не изменились, пункты не пересоздаются |
| 176 | функция | `_в_кеш(тема, итог)` |  |
| 187 | функция | `собрать(тема, вызвать)` | Опора по теме. `вызвать(промпт) → (данные JSON, сырой ответ)` — тот же вызов |
| 233 | функция | `номера(текст)` | Номера пунктов опоры, упомянутые в тексте: «О3, О7» (кириллица или латиница). |

## открытые_версии

- **путь**: `helix_pipeline/engine/открытые_версии.py`
- **размер**: 190 строк, SHA-256 blob `a9ae025b5667f6ff…`
- **что это**: открытые_версии.py — закрытая страница научной работы → открытая версия через OpenAlex.
- **зачем**: упали на нечитаемых страницах: 403 издательств (aiaa, aanda, researchgate), таймауты,
- **коды состояний** (2): `DOI`, `OPENALEX_API_KEY`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_открытые_версии.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 41 | константа | `API` | строка: «https://api.openalex.org» |
| 42 | константа | `CROSSREF` | строка: «https://api.crossref.org» |
| 43 | константа | `ТАЙМАУТ` | httpx.Timeout(10.0) |
| 44 | константа | `_DOI` | re.compile('(10\\.\\d{4,9}/[^\\s?#]+)', re.I) |
| 45 | константа | `_RG` | re.compile('researchgate\\.net/publication/\\d+_([^/?#]+)', re.I) |
| 46 | константа | `_СЛОВО` | re.compile('[a-z0-9]+') |
| 49 | функция | `doi_из_адреса(адрес)` |  |
| 57 | функция | `название_из_адреса(адрес)` |  |
| 62 | функция | `_аннотация(инд)` |  |
| 69 | функция | `_слова(т)` |  |
| 73 | функция | `_похоже(а, б)` |  |
| 78 | функция | `_crossref(клиент, doi, название)` | Запасной путь: название и аннотация по DOI (или по названию) из Crossref. |
| 100 | константа | `_S2_ПОЛЯ` | строка: «title,abstract,openAccessPdf,externalIds» |
| 103 | функция | `_semantic_scholar(doi, название)` | Название, аннотация и открытый PDF из Semantic Scholar (общий замок S2). |
| 124 | функция | `найти_работу(адрес)` | Работа по адресу страницы: OpenAlex → Semantic Scholar → Crossref; иначе None. |
| 168 | функция | `открытая_версия(адрес, загрузчик)` | Страница-замена для недоступного адреса: аннотация + открытая копия, если есть. |

## отчёт_документом

- **путь**: `helix_pipeline/engine/отчёт_документом.py`
- **размер**: 340 строк, SHA-256 blob `6d8837d67af7055c…`
- **что это**: Отчёт HELIX документом — Markdown или Word.
- **зачем**: Просьба владельца 06.10.2026: «устал копировать и вставлять для анализа, нужно, чтобы сайт выводил документ». Отчёт собирается из ответа цепочки (`/api/mr_helix/chain/jobs/{id}` → `result`) — того же JSON, что видит экран, — поэтому документ не может разойтись с экраном по содержанию. Порядок разделов: вопрос → вердикт → итог (последний раунд) → источники → найденные выдумки → этапы → предыдущие раунды. Первым идёт то, ради чего открывают документ; рабочие раунды — приложением. Документ ничего не пересчитывает и не добавляет от себя: только переносит…
- **коды состояний** (11): `BLOCK`, `FAILED`, `GOVERNANCE`, `HITL_REQUIRED`, `INTELLIGENCE`, `MARKET`, `NOT_RUN`, `RAN`, `REVIEW`, `SKIPPED`, `TRACE`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_отчёт_документом.py`, `helix_pipeline/tests/test_шкала_доверия.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 25 | константа | `_ЭТАПЫ` | dict, 4 элементов |
| 31 | константа | `_СТАТУСЫ` | dict, 3 элементов |
| 32 | константа | `_РЕШЕНИЯ` | dict, 4 элементов |
| 38 | константа | `_ТИПЫ` | dict, 7 элементов |
| 48 | константа | `_ЛАТЕКС` | tuple, 16 элементов |
| 58 | функция | `_без_формул(текст)` | Формулы LaTeX → обычный текст: в документе для чтения код не нужен. |
| 67 | функция | `_решение(слово)` |  |
| 72 | функция | `_раунды(intel)` |  |
| 78 | константа | `_ПРОПУСК` | set, 3 элементов |
| 81 | функция | `_протоколы(заголовок, протоколы)` | Таблица протоколов: что выполнилось, с каким исходом; что нет — почему. |
| 104 | функция | `собрать_markdown(result)` | Ответ цепочки → Markdown. |
| 265 | константа | `_ЖИРНЫЙ` | re.compile('\\*\\*(.+?)\\*\\*') |
| 266 | константа | `_ССЫЛКА` | re.compile('\\[([^\\]]*)\\]\\(([^)]*)\\)') |
| 269 | функция | `_абзац_с_разметкой(абзац, текст)` |  |
| 282 | функция | `markdown_в_docx(md)` | Markdown отчёта → .docx: заголовки, списки, таблицы, цитаты, жирный. |
| 337 | функция | `имя_файла(result, расширение)` |  |

## привязка_чисел

- **путь**: `helix_pipeline/engine/привязка_чисел.py`
- **размер**: 1034 строк, SHA-256 blob `0ed48bb8eef4c764…`
- **что это**: NUMBER-BINDER: четыре класса привязки числа факта к тексту источника.
- **зачем**: Источник: Мастер-ТЗ HELIX-CORE v2.5, модуль 1.1 (21.10.2026). Замер по прогону 4 (Луна): 21 факт с найденными первичными источниками выброшен в «галлюцинацию» потому, что одно число из 3–5 не нашлось буква в букву в коротком сниппете (F8: 1,14 рад подтверждено, «579 страниц» — нет); «26 % тяги» понижено при диапазоне 10–60 % в отчёте миссии. КЛАССЫ EXACT_MATCH число есть в тексте источника (запись тысяч и запятая/точка нормализованы); RANGE_MATCH число внутри заданного в источнике диапазона [a, b]; DERIVED число получено из …
- **коды состояний** (18): `ATOMIC_NUMBER_PARTIAL_PASS`, `BOUND`, `CITATION_RECOVERY_TRIGGERED`, `COMPARISON_MATCH`, `CONTRADICTED`, `CORE`, `CORE_BOUND_AUX_PRUNED`, `DECORATIVE`, `DERIVED`, `EXACT_MATCH`, `NEEDS_RECOVERY`, `NO_NUMBERS`, `NUMBER_CONTRADICTS_SOURCE`, `NUMBER_RANGE_BOUND`, `RANGE_MATCH`, `ROUNDED_MATCH`, `SCALED_MATCH`, `UNVERIFIABLE`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_helix_sensor.py`, `helix_pipeline/tests/test_мастер_тз_v25.py`, `helix_pipeline/tests/test_привязка_чисел.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 30 | константа | `_ЕДИНИЦЫ` | dict, 90 элементов |
| 52 | константа | `_МАСШТАБ` | dict, 17 элементов |
| 57 | константа | `_СОКР_МАСШТАБ` | dict, 7 элементов |
| 60 | константа | `_ПРОПИСЬЮ` |  |
| 68 | константа | `_БОЛЬШЕ` | строка: «(?:more than\|over\|above\|greater than\|higher than\|larger than\|bigger th» |
| 69 | константа | `_МЕНЬШЕ` | строка: «(?:less than\|fewer than\|lower than\|smaller than\|under\|below\|at most\|up» |
| 72 | константа | `_СЛОВО` | строка: «(?<![\w])» |
| 73 | константа | `_ВРЕМЕННОЕ` | re.compile('^(?:after\|before\|prior to\|earlier than\|later than\|since\|после\|позже\| |
| 75 | константа | `_ПОРЯДОК_ИЛИ_ЧАС` | re.compile("(?:st\|nd\|rd\|th)\\b\|-?(?:й\|го\|м\|е)\\b\|\\s*(?:a\\.?\\s?m\\.?\|p\\.?\\s? |
| 77 | константа | `_СРАВНЕНИЕ` | re.compile(f'{_СЛОВО}(?:(?P<gt>{_БОЛЬШЕ})\|(?P<lt>{_МЕНЬШЕ}))\\s+(?:the\\s+\|a\\s+ |
| 79 | константа | `_СРАВНЕНИЕ_ДАТЫ` | re.compile(f'{_СЛОВО}(?:(?P<gt>{_БОЛЬШЕ})\|(?P<lt>{_МЕНЬШЕ}))\\s+(?:\\d{{1,2}}\\s |
| 86 | константа | `_ИЗМЕНЕНИЕ_ДО` | re.compile('(?:снизил\|снижа\|сократил\|сокраща\|уменьшил\|уменьша\|упал\|упад\|опустил\| |
| 91 | константа | `_СТРОГО` | re.compile('^(?:at least\|не менее\|не ранее\|не раньше\|at most\|up to\|no more than\| |
| 93 | константа | `_СЛОВО_ЧИСЛО` | re.compile('\\b(' + '\|'.join(sorted(_ПРОПИСЬЮ, key=len, reverse=True)) + ')\\b', |
| 96 | константа | `_ПЕРЕСЧЁТ` | dict, 24 элементов |
| 103 | константа | `_НЕ_ТОЖДЕСТВО` | set, 2 элементов |
| 105 | константа | `_ЧИСЛО` | строка: «\d{1,3}(?:\.\d{3}){2,}(?:,\d+)?\|\d{1,3}(?:[ \u00a0\u202f,]\d{3})+(?:[.» |
| 106 | константа | `_ЕД` | строка: «(?:\s?(?P<u>%\|°\s?[CFСcfс](?![\w])\|[A-Za-zА-Яа-яёЁµ]+\.?))?» |
| 107 | константа | `_ДИАПАЗОН` | re.compile(f'(?P<a>{_ЧИСЛО})\\s?(?:[–—\\-]\|to\|до)\\s?(?P<b>{_ЧИСЛО}){_ЕД}', re.I |
| 110 | константа | `_ДАТА` | re.compile('(?<![\\d.])(?P<d>[0-3]?\\d)\\.(?P<m>[01]?\\d)\\.(?P<y>(?:1[89]\|20)\\ |
| 112 | константа | `_МЕТКА_ИДЕНТИФИКАТОРА` | re.compile('(?:ISSN\|ISBN\|DOI\|No\|№)\\W{0,3}$', re.I) |
| 113 | константа | `_ОДНО` | re.compile(f'(?<![\\w.])(?P<n>{_ЧИСЛО}){_ЕД}', re.I) |
| 117 | константа | `_ВАЛЮТА` | re.compile('([$€£¥₽])\\s?$') |
| 122 | константа | `_МЕСЯЦЫ` | tuple, 24 элементов |
| 125 | константа | `_ИМЯ_ПЕРЕД` | re.compile('(?:\\b(?:[A-Z][A-Za-z]+\|ISO)[\\s\\-\\u2011]?\|\\b[A-ZА-ЯЁ]{1,10}[\\-\ |
| 131 | константа | `_НЕ_ИМЯ` | frozenset({'in', 'on', 'at', 'by', 'of', 'for', 'from', 'to', 'around', 'about', |
| 141 | константа | `_ДЕКОР` | re.compile('^\\s*(?:страниц\\w*\|стр\\.\|pages?\|pp\\.?\|слов\\w*\|words?\|строк\\w*\|l |
| 144 | функция | `_ложный_диапазон(a, b, перед, ед)` | «0360–4918» (ISSN), «71–38646» (номер выпуска), «ISBN 5–7…» — коды, а не меры. |
| 154 | функция | `_варианты(строка)` | Прочтения записи числа. Неоднозначное «1,234» / «1.234» — оба: 1,234 и 1234. |
| 172 | функция | `_разбор(строка)` |  |
| 176 | функция | `_единица(u)` |  |
| 182 | константа | `_ПОСТФИКС` | re.compile('\\s*(?:[^\\s\\d.,;:]+\\.?\\s+){0,3}?(?:(?P<ge>и более\|и больше\|и выш |
| 185 | константа | `_ЗНАК_МИНУС` | re.compile('(?:(?:^\|[\\s(\\[:=])[-\\u2212]\|\\u2212\|(?<![\\w])минус\\s)$', re.I) |
| 186 | константа | `_ВРЕМЯ` | re.compile('(?<![\\d:.,])(?:[01]?\\d\|2[0-3]):[0-5]\\d(?::[0-5]\\d)?(?![\\d:])') |
| 191 | константа | `_ОСТАТОК` | re.compile('(?<![\\w])(?:осталь\\w*\|остал\\w*\|оставш\\w*\|остающ\\w*\|остаё\\w*\|ос |
| 194 | константа | `_НЕ_ОСТАТОК` | re.compile('^(?:united\|unrelated\|underlined\|undated\|unified\|unlimited\|need\|newed |
| 199 | константа | `_ПРОТИВОПОЛОЖНОСТИ` | list, 9 элементов |
| 208 | функция | `_окно(текст, сырое, слов_до, слов_после)` | Слова вокруг первого вхождения числа в тексте (для одной стороны сверки). |
| 221 | функция | `_есть_остаток(окно)` |  |
| 225 | функция | `_процент(сырое)` |  |
| 230 | функция | `_окрестность(факт, источник, привязки)` | Два решения по словам рядом с числом, без модели. |
| 260 | функция | `извлечь(текст)` | Числа и диапазоны текста: {value, values, lo, hi, unit, kind, raw, decorative, start}. |
| 377 | функция | `_равны(a, b)` |  |
| 381 | функция | `_округление(v)` | Полшага последнего знака числа, как оно напечатано (1,14 → 0,005). |
| 388 | функция | `_год(v)` |  |
| 392 | функция | `_диапазон_лет(с)` |  |
| 396 | функция | `_знаков(v)` |  |
| 401 | функция | `_совместимы(u1, u2)` |  |
| 405 | функция | `_выполнено(оп, x, y)` | Утверждение «оп x» про величину, которая в источнике равна y. |
| 410 | функция | `_дробное_прочтение(сырое, v)` | «1,000» и «5,400» прочитаны как 1,0 и 5,4 — дробное прочтение неоднозначной записи. |
| 416 | функция | `_пара_допустима(ч, x, с, y)` | Дробное прочтение «1,000» не сверяется с целым без разделителя («one», «1», «5 %»): AggreFact 25.10 — |
| 427 | функция | `привязать_число(число, источник)` |  |
| 472 | константа | `_СОСТАВНОЕ` | re.compile('\\b(twenty\|thirty\|forty\|fifty\|sixty\|seventy\|eighty\|ninety)[\\s\\-](o |
| 476 | функция | `_прописью(текст)` | Числа прописью источника («three moons»): только кандидаты для привязки, не меры факта. |
| 496 | константа | `_СЛОВО` | re.compile('[A-Za-zА-Яа-яЁё]{4,}') |
| 497 | константа | `_СТОП` | set, 21 элементов |
| 501 | функция | `_якорь(текст, начало, длина)` | Слова в окне вокруг числа (по 40 знаков), обрезанные до 5 букв: грубая основа. |
| 507 | функция | `_противоречие(н, факт, источник, текст)` | Источник говорит о ТОМ ЖЕ другое число: тот же род числа и общее слово рядом. |
| 550 | функция | `_календарное(с, текст)` | Год или день месяца («March 23», «23 March 2020») — не величина для сравнения. |
| 558 | функция | `_сравнить(н, факт, источник, текст)` | «more than 70/100» против «79/100»: неравенство проверяется, а не равенство. |
| 620 | функция | `_лучи_не_пересекаются(оп1, x, оп2, y)` | Два неравенства противоположных направлений («< x» и «> y») несовместимы, если нет |
| 629 | функция | `_голова(текст, ч)` | Первое содержательное слово после числа («17 reviews» → «revie»): о чём число. |
| 639 | функция | `_пара(xs, ys)` | Прочтения «1,500» (1.5 или 1500) выбираются ПАРОЙ: утверждение и источник говорят |
| 656 | константа | `_НОМЕР_МЕСЯЦА` |  |
| 666 | константа | `_МЕС_СЛОВА` | '\|'.join(sorted(_НОМЕР_МЕСЯЦА, key=len, reverse=True)) |
| 667 | константа | `_ДАТА_СЛОВАМИ` | re.compile(f'\\b(?:(?P<m1>{_МЕС_СЛОВА})\\.?\\s+(?P<d1>\\d{{1,2}})\\s?,?\\s?(?P<y |
| 671 | константа | `_ДО_ДАТЫ` | re.compile('(?<![\\w])(?:(?P<lt>before\|prior to\|earlier than\|не позднее\|не позже |
| 675 | функция | `_даты_словами(текст)` | Даты с годом: «April 20, 2020», «20 April 2020», «April 2020». Без года не берём. |
| 688 | функция | `_сверить_даты(факт, текст)` | «before April 20, 2020» при единственной подходящей дате источника «May 22, 2020». |
| 727 | константа | `_ДАТА_БЕЗ_ГОДА` | re.compile(f'\\b(?:(?P<m1>{_МЕС_СЛОВА})\\.?\\s+(?P<d1>\\d{{1,2}})(?:st\|nd\|rd\|th) |
| 732 | функция | `_сверить_даты_без_года(факт, текст)` | «before November 30» (года нет) при единственной дате источника «December 28, 2018». |
| 759 | функция | `_смена_ролей(н, факт, источник, текст)` | «45 пациентов старше 60 лет» против «60 пациентов, средний возраст 45 лет» (боевая пара 10, |
| 793 | константа | `_МНОЖИТЕЛЬ_ПЕРЕД` | re.compile('\\d[\\d.,]*\\s*(?:[A-Za-z°%]{1,4})?\\s*[x×*]\\s*$') |
| 795 | константа | `_ОБОЗНАЧЕНИЕ` | re.compile('^\\s*(?:[A-Za-z°%]{1,4})?\\s*[x×*]\\s*\\d') |
| 799 | константа | `_РАЗДЕЛИТЕЛЬ` | re.compile('[x×*]') |
| 802 | функция | `_множители_источника(текст)` | Все составные величины источника: [(число после «x», образец), …]. |
| 822 | функция | `_потеря_множителя(н, факт, текст, множители)` | Составной множитель источника потерян в пересказе: «85g x 300g» → «300 g». |
| 879 | функция | `_диапазон_факта(д, факт, источник, текст)` | «от 12 до 15 МПа» в факте против одного числа той же единицы в источнике (боевые пары |
| 903 | константа | `_СЧЁТ` | re.compile('(?<![\\d.,:/-])(\\d{1,2})\\s?[-–]\\s?(\\d{1,2})(?![\\d%]\|[.,:/-]\\d\| |
| 905 | константа | `_СПОРТ` | re.compile('\\b(?:beat\|beats\|beaten\|won\|win\|wins\|winning\|lost\|lose\|loses\|losing\| |
| 911 | константа | `_СЧЁТ_СЛОВАМИ` | re.compile('\\b(?:\\d{1,2}\|one\|two\|three\|four\|five\|six\|seven\|eight\|nine\|ten\|nil) |
| 915 | функция | `_счета(текст, спорт)` | Счёт матча «3-1»: (a, b, начало, конец, запись). При спорт=True — только рядом со спортивным |
| 931 | функция | `_сверить_счёт(факт, текст, числа)` | «beat Newcastle 2-0» — одна величина, а не числа 2 и 0 по отдельности (AggreFact 24.10, H3). |
| 960 | функция | `привязать(факт, текст_источника)` | Привязать все числа факта к тексту страницы и вынести вердикт. |

## сверка_страниц

- **путь**: `helix_pipeline/engine/сверка_страниц.py`
- **размер**: 552 строк, SHA-256 blob `8be523f664dbade4…`
- **что это**: Сверка факта с ТЕКСТОМ найденной страницы (Мастер-ТЗ v2.5, модули 1.1 и 1.1.4).
- **зачем**: Прогон 4 (Луна): из 81 факта поиска 56 ушли в «галлюцинацию». 35 — «поиск не нашёл источника»: разметка Gemini (`supports`) не связала строку факта ни с одной страницей, хотя страницы этого же поиска найдены. 21 — «число не подтверждено»: страница есть, а разметка не покрыла именно число. Разметка — свойство поиска Google; у Qwen её нет вовсе. Поэтому проверка, не зависящая от провайдера: открыть страницу и посмотреть, стоит ли там факт.
- **коды состояний** (10): `BOUND`, `CONTRADICTED`, `CONTRADICTS`, `CORE`, `CORE_BOUND_AUX_PRUNED`, `GET`, `NO_NUMBERS`, `NUMBERS`, `QUOTE`, `WORDS`
- **тесты, которые зовут модуль**: 6 — `helix_pipeline/tests/test_каскад_источников.py`, `helix_pipeline/tests/test_конвейер_расследования.py`, `helix_pipeline/tests/test_мёртвая_зона_и_домены.py`, `helix_pipeline/tests/test_опора_кеш_и_полярность.py`, `helix_pipeline/tests/test_открытые_версии.py`, `helix_pipeline/tests/test_склейка_перепечаток.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 44 | константа | `ПОТОКОВ` |  |
| 45 | константа | `ТАЙМАУТ` | httpx.Timeout(connect=6.0, read=8.0, write=8.0, pool=6.0) |
| 48 | константа | `ПРЕДЕЛ_ОДНОЙ_СТРАНИЦЫ` |  |
| 50 | константа | `ПРЕДЕЛ_БАЙТ` |  |
| 51 | константа | `ПРЕДЕЛ_ЗНАКОВ` |  |
| 53 | константа | `ПРЕДЕЛ_СТРАНИЦ` |  |
| 54 | константа | `ПРЕДЕЛ_ВРЕМЕНИ` |  |
| 56 | константа | `ПОЛ_СЛОВ` |  |
| 58 | константа | `ПОЛ_СЛОВ_БЕЗ_ЧИСЕЛ` |  |
| 60 | константа | `СЛОВ_ЦИТАТЫ_ПОДРЯД` |  |
| 62 | константа | `ЗАГОЛОВКИ` | dict, 3 элементов |
| 67 | класс | `_Текст (3 публичных методов)` |  |
| 90 | класс | `_Ссылки (1 публичных методов)` |  |
| 103 | константа | `ПРЕДЕЛ_ССЫЛОК` |  |
| 106 | функция | `ссылки_из_html(разметка, база)` | Абсолютные http(s)-ссылки страницы без дублей и без ссылок на её же домен (граф |
| 132 | функция | `html_в_текст(разметка)` |  |
| 144 | константа | `ПРЕДЕЛ_СТРАНИЦ_PDF` |  |
| 147 | функция | `текст_pdf(тело)` | (текст, причина отказа). Обрезанный файл (предел байт) честно назван. |
| 170 | константа | `ЗАГОЛОВКИ_ВИКИМЕДИА` | dict, 2 элементов |
| 173 | константа | `ЗАГОЛОВКИ_БРАУЗЕР` | dict, 4 элементов |
| 178 | константа | `_ПОВТОР_ПО_КОДАМ` | set, 4 элементов |
| 181 | функция | `_заголовки_для(адрес)` |  |
| 187 | функция | `_получить(адрес, заголовки, конец)` | Одна попытка: {final_url, domain, status, type, body, encoding, error}. |
| 214 | функция | `_википедия_через_api(адрес)` | Страницы *.wikipedia.org сервер Викимедиа режет по отпечатку клиента (403 «robot policy»), |
| 233 | функция | `загрузить(адрес)` | {url, final_url, domain, text, error}. Никогда не бросает. |
| 276 | класс | `Страницы (3 публичных методов)` | Кэш страниц на один прогон. `загрузчик` подменяется в тестах. |
| 353 | константа | `_СЛОВО` | re.compile('[\\wё]+', re.I) |
| 356 | функция | `_слова(т)` |  |
| 360 | функция | `_значимые(т)` |  |
| 364 | функция | `доля_слов(факт, страница)` | Доля значимых слов факта (первые 6 букв — грубое снятие окончаний), стоящих на странице. |
| 373 | функция | `цитата_на_странице(цитата, страница)` |  |
| 385 | константа | `_КИР` | re.compile('[а-яё]', re.I) |
| 386 | константа | `_ЛАТ_СЛОВО` | re.compile('\\b[A-Za-z][A-Za-z\\-]{2,}\\b') |
| 389 | функция | `_кириллица(т, предел)` |  |
| 395 | функция | `доля_латиницы(факт, страница)` | Для русского факта и нерусской страницы: доля латинских имён факта (Apollo, LRO, |
| 410 | константа | `_МЕС_РУ` | dict, 12 элементов |
| 412 | константа | `_МЕС_EN` | dict, 24 элементов |
| 416 | константа | `_ДАТА_РУ` | re.compile('\\b(\\d{1,2})\\s+(' + '\|'.join(_МЕС_РУ) + ')\\s+(\\d{4})', re.I) |
| 417 | константа | `_ДАТА_EN1` | re.compile('\\b(\\d{1,2})(?:st\|nd\|rd\|th)?\\s+(?:of\\s+)?([A-Za-z]{3,9})\\.?,?\\s |
| 418 | константа | `_ДАТА_EN2` | re.compile('\\b([A-Za-z]{3,9})\\.?\\s+(\\d{1,2})(?:st\|nd\|rd\|th)?,?\\s+(\\d{4})') |
| 419 | константа | `_МЕС_DE` | dict, 13 элементов |
| 421 | константа | `_ДАТА_DE` | re.compile('\\b(\\d{1,2})\\.?\\s+(' + '\|'.join(_МЕС_DE) + ')\\s+(\\d{4})', re.I) |
| 422 | константа | `_ДАТА_ЧИСЛА` | re.compile('(?<![\\d.])(\\d{1,2})\\.(\\d{1,2})\\.(\\d{4})(?![\\d.])') |
| 425 | функция | `полные_даты(текст)` | Даты «20 июля 1969», «July 20, 1969», «20 July 1969», «20.07.1969» → (день, месяц, год). |
| 444 | константа | `_ТРАНСЛИТ_РУ` | dict, 20 элементов |
| 449 | функция | `_скелет_ру(слово)` |  |
| 453 | функция | `_скелет_лат(слово)` |  |
| 461 | константа | `_ЗАГЛАВНОЕ_РУ` | re.compile('(?<![.!?]\\s)(?<!^)\\b([А-ЯЁ][а-яё]{3,})') |
| 464 | функция | `имя_факта_на_странице(факт, страница)` | Хотя бы одно имя собственное факта (Бохум, Камински, Джодрелл-Бэнк) стоит на странице |
| 476 | константа | `_СТОП_ЛАТ` | set, 9 элементов |
| 479 | функция | `работа_по_теме(факт, работа)` | Научная работа (название + аннотация) относится к факту? |
| 498 | функция | `_сильное(б)` | Число, которое на странице той же темы случайно не совпадёт: не год и не «Apollo 14», |
| 507 | функция | `сверить(факт, цитата, страница)` | Стоит ли факт на этой странице. status: QUOTE \| NUMBERS \| WORDS \| CONTRADICTS \| NONE. |

## склейка_перепечаток

- **путь**: `helix_pipeline/engine/склейка_перепечаток.py`
- **размер**: 174 строк, SHA-256 blob `ee18522d52352185…`
- **что это**: Склейка перепечаток: страницы, переписавшие один источник, считаются ОДНИМ голосом.
- **зачем**: Зачем. Пять изданий, переписавших один пресс-релиз, в `потолок_уровня` и в «независимых источниках» набора разворота давали пять доменов. Это не пять свидетельств, а одно, пересказанное пять раз. Модуль детерминированно склеивает такие страницы в кластеры; без модели, без сети. Две страницы попадают в один кластер, если выполнено ЛЮБОЕ из: (а) общая дословная цитата из >= 7 подряд идущих слов (шинглы по словам, регистр и пунктуация сняты) — кроме шинглов, которые есть у >= 40 % страниц (колонтитулы, cookie- бан…
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_склейка_перепечаток.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 34 | константа | `ДЛИНА_ШИНГЛА` |  |
| 35 | константа | `ДЛИНА_ТРОЙКИ_ЧИСЕЛ` |  |
| 36 | константа | `ДОЛЯ_ШАБЛОНА` |  |
| 37 | константа | `МИН_СТРАНИЦ_ДЛЯ_ШАБЛОНА` |  |
| 38 | константа | `ПРИМЕЧАНИЕ` | строка: «Пороги (7 слов подряд, 3 числа подряд, 40 % страниц как шаблон, миниму» |
| 41 | константа | `_СЛОВО` | re.compile('\\w+', re.UNICODE) |
| 44 | функция | `_слова(текст)` |  |
| 48 | функция | `_шинглы(текст)` |  |
| 53 | функция | `_год(v)` |  |
| 57 | функция | `_тройки_чисел(текст)` |  |
| 70 | функция | `_адрес(url)` | Адрес для сравнения ссылок: без схемы, www, якоря и хвостового слэша. |
| 80 | класс | `_Союз (2 публичных методов)` |  |
| 96 | функция | `_общие(признаки, шаблонных_нет)` | признак → страницы, где он есть; шаблонные (>= 40 % страниц) выброшены. |
| 108 | функция | `cluster_reprints(pages)` | pages: [{url, domain, text, links?}]. Возвращает |
| 155 | функция | `канон_доменов(pages, result)` | домен → домен-представитель его кластера (наименьший по алфавиту). Домены без склейки |

## статистика_аудит

- **путь**: `helix_pipeline/engine/статистика_аудит.py`
- **размер**: 286 строк, SHA-256 blob `6ed74ebdc026cd06…`
- **что это**: HELIX-STAT-AUDIT v2.0: статистическая криминалистика, только детерминированный код.
- **зачем**: Источник: «Мастер-ТЗ HELIX-CORE v2.5 & HELIX-DISCOVERY v2.0», часть 3, модуль 2.1 (присланы владельцем 21.10.2026). Модель только читает и извлекает кортеж (тип теста, статистика, степени свободы, заявленное p); числа и вердикты — здесь. Без scipy: сервис его не ставит. Хватает `math`: p для t и F — через регуляризованную неполную бету, для хи-квадрат — через неполную гамму; в p-кривых df всегда чётное, и там замкнутая форма. ГДЕ Я РАСХОЖУСЬ С ТЕКСТОМ ТЗ (проверено счётом, см. тесты): * штраф за выбывание `floo…
- **коды состояний** (20): `BLOCK`, `HETEROGENEITY`, `INADEQUATE_POWER`, `INSUFFICIENT_K`, `LEFT_SKEW`, `LONGITUDINAL_DECAY_BLOCK`, `NO_FINAL_POINT_DATA`, `PREREGISTERED_PASS`, `ROUND_FLOOR`, `STAT_PCURVE_HETEROGENEITY_DETECTED`, `STAT_PCURVE_INADEQUATE_POWER`, `STAT_PCURVE_K_TOO_SMALL`, `STAT_PCURVE_LEFT_SKEW`, `STAT_PCURVE_TRUE_EFFECT`, `STAT_P_DECISION_ERROR`, `STAT_P_MISMATCH_BLOCK`, `STAT_P_NUMERIC_DRIFT`, `TRANSIENT_NOISE_OR_ATTRITION`, `TRUE_EFFECT`, `WARN`
- **тесты, которые зовут модуль**: 2 — `helix_pipeline/tests/test_мастер_тз_v25.py`, `helix_pipeline/tests/test_статистика_аудит_односторонний.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 25 | константа | `ПОРОГ` |  |
| 30 | функция | `_betacf(a, b, x)` | Цепная дробь Лентца для неполной беты. |
| 57 | функция | `betainc(a, b, x)` | Регуляризованная неполная бета I_x(a, b). |
| 71 | функция | `gammaincc(a, x)` | Регуляризованная верхняя неполная гамма Q(a, x). |
| 104 | функция | `p_t(t, df)` | Двустороннее p критерия Стьюдента. |
| 109 | функция | `p_f(f, df1, df2)` |  |
| 113 | функция | `p_chi2(x, df)` |  |
| 117 | функция | `p_z(z)` |  |
| 121 | функция | `p_r(r, n)` | Двустороннее p коэффициента корреляции при n наблюдениях. |
| 131 | функция | `пересчитать_p(тип, значение, df1, df2, n)` |  |
| 148 | функция | `statcheck(тип, значение, p_заявлено)` | Пересчёт p с интервалом округления опубликованной статистики. |
| 205 | класс | `ПредусловиеНезависимости (0 публичных методов)` | Повторные измерения одной когорты: p-кривую считать нельзя — в продольный шлюз. |
| 209 | функция | `_sf_chi2_even(x, k)` | P(χ²(2k) > x), замкнутая форма для чётных степеней свободы. |
| 219 | функция | `p_кривая(p_значения, когорты)` | Четыре режима по Симонсону и др. (2014), k ≥ 3 независимых значимых тестов. |
| 250 | функция | `продольный_шлюз(точки, t_финал, предзарегистрированные, скорректированный_порог)` | Промежуточные значимости при проваленной предрегистрированной финальной точке. |
| 274 | функция | `ect_после_выбывания(ect_raw, m_rate, post_hoc)` | max(1, ECT_raw − ⌊5·max(0, m−0,15)⌋ − 2·I_post-hoc), всегда в 1..4. |

## статистика_форензика

- **путь**: `helix_pipeline/engine/статистика_форензика.py`
- **размер**: 362 строк, SHA-256 blob `9b30b229f04b4e2e…`
- **что это**: Форензика сводных статистик: GRIM, GRIMMER, Стоуффер по базовым p, сверка с ClinicalTrials.gov.
- **зачем**: Только стандартная библиотека, без сети, детерминированно. Все результаты — ФЛАГИ ДЛЯ РУЧНОЙ ПРОВЕРКИ: «несогласовано» означает «эти сводные числа невозможны при заданных допущениях», а не «автор ошибся/подделал». Причин много: другой способ округления, пропуски в данных, дробные баллы, шкала с несколькими пунктами, опечатка. ИСТОЧНИКИ (каждый открыт при написании, 2026-10-23): * GRIM: Brown N.J.L., Heathers J.A.J. (2017) Soc. Psychol. Personal. Sci. 8(4):363-369, doi:10.1177/1948550616673876 (запис…
- **коды состояний** (10): `BLOCK`, `GRIMMER_OK`, `GRIM_OK`, `HITL_ADVISORY`, `INCONCLUSIVE`, `PRIMARY`, `STAT_CARLISLE_BASELINE_ANOMALY`, `STAT_GRIMMER_PARITY_FAIL`, `STAT_GRIMMER_SD_UNREACHABLE`, `STAT_GRIM_IMPOSSIBLE_MEAN`
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_статистика_форензика.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 41 | константа | `СОГЛАСОВАНО` | строка: «СОГЛАСОВАНО» |
| 42 | константа | `НЕСОГЛАСОВАНО` | строка: «НЕСОГЛАСОВАНО» |
| 43 | константа | `НЕОПРЕДЕЛЕНО` | строка: «НЕОПРЕДЕЛЕНО» |
| 45 | константа | `РЕЖИМЫ_ОКРУГЛЕНИЯ` | tuple, 3 элементов |
| 46 | константа | `ПРЕДЕЛ_КАНДИДАТОВ_СУММЫ` |  |
| 51 | функция | `_разобрать(значение)` | Напечатанное число -> (целое в единицах последнего знака, число знаков D). |
| 69 | функция | `_интервал(единицы, знаков, режим)` | Множество x, которое при округлении до `знаков` даёт `единицы`: (lo, hi, lo_вкл, hi_вкл). |
| 84 | функция | `_в(x, lo, hi, lo_в, hi_в)` |  |
| 88 | функция | `округлить_половина_вверх(x, знаков)` | round-half-up (к +∞ на ничьей), точно; для тестов и справки. |
| 96 | функция | `grim(среднее, n)` | Существует ли целая сумма S, для которой round(S/n, D) == среднее (D — знаки в записи). |
| 119 | функция | `grimmer(среднее, sd, n)` | Совместимы ли среднее, выборочное SD (знаменатель n−1) и n для ЦЕЛЫХ данных. |
| 173 | константа | `_ОГОВОРКИ_КАРЛАЙЛ` | tuple, 5 элементов |
| 187 | функция | `стоуффер_базовых_p(p_значения)` | Объединить p базовых переменных методом Стоуффера: Z = Σ Φ⁻¹(p_i) / √k. |
| 221 | функция | `_путь(d)` |  |
| 229 | функция | `_токены(s)` |  |
| 233 | функция | `_похожесть(a, b)` |  |
| 238 | функция | `_число_p(s)` |  |
| 243 | функция | `сверить_с_реестром(статья, запись)` | Сравнить числа статьи с уже загруженной записью ClinicalTrials.gov API v2. |
| 306 | функция | `код_состояния(результат)` | Свести результат `grim` / `grimmer` к кодам таблицы ТЗ. |
| 324 | функция | `p_уэлча(m1, s1, n1, m2, s2, n2)` | Двустороннее p критерия Уэлча по сводным статистикам группы 1 и группы 2. |
| 337 | функция | `карлайл_по_таблице(строки)` | Метод Карлайла по сводным статистикам Таблицы 1 (формула ТЗ): p_k по Уэлчу для каждой |

## шкала_доверия

- **путь**: `helix_pipeline/engine/шкала_доверия.py`
- **размер**: 176 строк, SHA-256 blob `18620b4a59a8de50…`
- **что это**: шкала_доверия.py — шкала ECT словами для человека.
- **зачем**: Владелец 17.10.2026, со слов программиста, которому показывали HELIX: «доверие три, доверие четыре — никто ничего не понимает. Пусть в начале будет понятно, что такое доверие, на чём оно основано, почему три, а не два, почему не десять». Шкала в движке есть (`research_discipline.ШКАЛА_ECT`, дословно из спеки), но человеку её не показывали: в отчёте стояли голые «[ECT-3]». Здесь — та же шкала простыми словами, для трёх мест, где отчёт видит человек: экран, выгрузка, копия для озвучки. СМЫСЛ НЕ ПЕРЕСКАЗЫВАЕТСЯ ЗАНОВО. Каждая строка легенды — сжа…
- **тесты, которые зовут модуль**: 1 — `helix_pipeline/tests/test_шкала_доверия.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 23 | константа | `СЛОВА` | dict, 3 элементов |
| 33 | константа | `ОСНОВАНИЯ` | dict, 3 элементов |
| 66 | константа | `ЗАГОЛОВОК` | dict, 3 элементов |
| 69 | константа | `ПОЧЕМУ_ЧЕТЫРЕ` | dict, 3 элементов |
| 84 | константа | `_ЧИСЛА_ВСЛУХ` | dict, 4 элементов |
| 87 | функция | `_язык(язык)` |  |
| 91 | функция | `легенда_markdown(язык)` | Блок для выгрузки отчёта: заголовок, четыре строки, почему четыре. |
| 101 | функция | `легенда_для_озвучки()` | Та же легенда без разметки и цифрами словами — для диктора. |
| 111 | константа | `_МАРКЕР` | re.compile('\\[ECT-([1-4])([^\\]]*)\\]') |
| 114 | функция | `со_словами(текст, язык)` | «[ECT-3]» → «[ECT-3 · надёжно, но есть пробел]». Пояснение модели |
| 142 | константа | `_СЛЕДОМ` | re.compile('(причин\|основани\|огранич\|почему\|reason\|basis\|limit)', re.IGNORECASE) |
| 143 | константа | `_ССЫЛКА` | re.compile('https?://\|\\]\\(\|\\bdoi\\b', re.IGNORECASE) |
| 144 | константа | `_ОБЪЯСНЕНИЕ` | re.compile('почему\|потому что\|поскольку\|так как\|основани\|не хватает\|недостаёт\|ну |
| 154 | функция | `выводы_без_причины(текст)` | Сколько маркеров ECT стоят совсем без основания: без ссылки, без |

