# AK-MASTER — поэлементный реестр модулей движка

**Сгенерировано, не написано руками**: `PYTHONUTF8=1 python scripts/реестр_продуктов.py`.
Тот же генератор, что и для HELIX: номера строк из AST, назначение из докстринга.

Тесты ищутся в корневом `tests/` и в `helix_pipeline/tests/`.
Если модуль не зовёт ни один тест, строка «откуда достижим» показывает,
кто его импортирует: `api/service.py`, `api/router.py` или другой модуль
пакета, у которого тесты есть. Это **путь в коде, а не проверка поведения**,
и так он и подписан.

Канон AK-MASTER (14 блоков, 13 ENFORCED + 1 DOC_ANCHOR) считает штатный
`python -m engine.coverage_validator`; этот реестр — про код, а не про канон.
Граница продуктов соблюдена: `engine/` не импортирует `helix_pipeline/` и `mr_helix/`
(`ЧИТАЙ_ПЕРВЫМ.md`, раздел 1).

Всего **161 модулей**, **36165 строк**, **1430 элементов верхнего уровня**. Без прямого теста — **4**, из них достижимы косвенно (через `api/` или другой модуль с тестами) — **4**, без пути вообще — **0**.

---


## ak_discipline_cli

- **путь**: `engine/ak_discipline_cli.py`
- **размер**: 31 строк, SHA-256 blob `0158e35bd341247c…`
- **тесты, которые зовут модуль**: 1 — `tests/test_ak_discipline_cli.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 8 | функция | `main()` |  |

## anaphora_den_arbuza

- **путь**: `engine/anaphora_den_arbuza.py`
- **размер**: 26 строк, SHA-256 blob `df528c48b495b62b…`
- **что это**: anaphora_den_arbuza.py — intentional-anaphora registry for «День Арбуза».
- **зачем**: Editable data. These openings repeat ON PURPOSE — rhetorical anaphora and system-message litanies — so the construction-echo detector skips them. Everything it still surfaces after this list is a candidate accidental opening-echo (e.g. a run of «Он… Он… Он…»), which the author judges. This registry is the intentional-anaphora hook that later feeds the TTS-checklist mechanism
- **тесты, которые зовут модуль**: 1 — `tests/test_construction_echo.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 12 | константа | `INTENTIONAL_ANAPHORA` | list, 8 элементов |

## antagonist_logic_gate

- **путь**: `engine/antagonist_logic_gate.py`
- **размер**: 150 строк, SHA-256 blob `b059a4d43cda67fd…`
- **что это**: antagonist_logic_gate.py — hostile force / antagonist interior logic gate.
- **зачем**: This is the old useful heuristic formerly misnamed LawShadowDetector. It is not AK v6.7 Law of Shadow. It checks whether antagonist/system/hostile force is reduced to a flat evil function without internal necessity
- **коды состояний** (7): `ANTAGONIST_DEMONIZING_LEXIS`, `ANTAGONIST_FLAT_FUNCTION`, `ANTAGONIST_NO_INTERIOR_LOGIC`, `HIGH`, `LOW`, `MEDIUM`, `WARN`
- **тесты, которые зовут модуль**: 7 — `tests/test_lemma_migration_antagonist.py`, `tests/test_lemma_migration_residuals.py`, `tests/test_llm_judge_antagonist_logic.py`, `tests/test_negation_utils.py`, `tests/test_v13_lawz_dr_shadow_scr.py`, `tests/test_v14_issue_closure_pack.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 26 | константа | `ANTAGONIST_RE` | re.compile('\\b(антагонист\|враг\|злодей\|монстр\|система\|регулятор\|корпорац\|алгорит |
| 27 | константа | `ANTAGONIST_LEMMAS` | set, 2 элементов |
| 28 | константа | `DEMONIZE_RE` | re.compile('\\b(злой\|злобн\|безумн\|чудовищн\|омерзительн\|мерзк\|абсолютн\\w*\\s+зл\ |
| 29 | константа | `INTERIOR_LOGIC_RE` | re.compile('\\b(логик\|причин\|мотив\|необходим\|выгод\|верил\|считал\|обязан\|защищал\|с |
| 30 | константа | `INTERIOR_LOGIC_LEMMAS` | set, 2 элементов |
| 31 | константа | `POV_MARKER_RE` | re.compile('\\b(с\\s+его\\s+стороны\|для\\s+него\|в\\s+его\\s+глазах\|он\\s+считал\| |
| 32 | константа | `PURE_FUNCTION_RE` | re.compile('\\b(без\\s+причины\|просто\\s+так\|потому\\s+что\\s+злой\|его\\s+целью\ |
| 33 | константа | `NON_SCENE_MODES` | set, 3 элементов |
| 36 | функция | `_norm_mode(mode)` |  |
| 40 | функция | `_downgrade_for_non_scene(severity, non_scene)` |  |
| 46 | класс | `AntagonistViolation (0 публичных методов)` |  |
| 52 | класс | `AntagonistLogicGate (2 публичных методов)` |  |

## anti_hallucination

- **путь**: `engine/anti_hallucination.py`
- **размер**: 159 строк, SHA-256 blob `b072f0f63d4bc919…`
- **коды состояний** (11): `ABSOLUTE_FACTUAL_CLAIM_WITHOUT_SOURCE`, `AUTHOR_SOURCE_CLAIM_WITHOUT_VERIFICATION`, `BLOCK`, `EXACT_NUMBER_WITHOUT_MARKER`, `HIGH`, `INCOMPLETE_SOURCE_TRACE`, `MEDIUM`, `NON_LIQUET`, `ROLE_FIXED`, `UNKNOWN_ROLE`, `WARN`
- **тесты, которые зовут модуль**: 4 — `tests/test_adversarial_anti_hallucination.py`, `tests/test_ak_discipline_engine.py`, `tests/test_block0_behavioral_enforcement.py`, `tests/test_block0_really_runs.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 10 | константа | `ROLE_BY_MODE` | dict, 6 элементов |
| 19 | константа | `FACT_MARKERS` | tuple, 6 элементов |
| 20 | константа | `EXACT_NUMBER_RE` | re.compile('(?<![\\w-])\\d+(?:[\\.,]\\d+)?\\s*(?:%\|кг\|г\|мг\|см\|мм\|м\|км\|секунд[а-я |
| 24 | константа | `DECIMAL_NUMBER_RE` | re.compile('(?<![\\w-])\\d+[.,]\\d+', re.IGNORECASE) |
| 25 | константа | `SPELLED_FRACTION_RE` | re.compile('\\b\\d+\\s+цел\\w+\\s+\\d+\\s+(?:десят\|сот\|тысячн)', re.IGNORECASE) |
| 26 | константа | `ABSOLUTE_CLAIM_RE` | re.compile('\\b(доказано\|точно\|безусловно\|всегда\|никогда\|на самом деле\|факт(?:ом |
| 27 | константа | `AUTHOR_CLAIM_RE` | re.compile('\\b(написал\|утверждал\|сказал\|доказал\|описал\|показал\|заметил\|писал\|ци |
| 31 | константа | `ATTRIBUTION_RE` | re.compile('(?:[Сс]огласно\|[Пп]о\\s+мнению)\\s+[А-ЯЁ]\|\\b[Пп]о\\s+[А-ЯЁ][а-яё]+\ |
| 37 | класс | `AIRole (0 публичных методов)` |  |
| 44 | класс | `AntiHallucinationGuard (4 публичных методов)` | Block 0 behavioral guard. |

## archive_contradiction

- **путь**: `engine/archive_contradiction.py`
- **размер**: 254 строк, SHA-256 blob `dd2f8bbafd269a5d…`
- **что это**: archive_contradiction.py — СТОП-правило Блока 11: архив против самого себя.
- **зачем**: Канон АК-6.7, БЛОК 11 (строка 1426): «Если АРХИВ противоречит самому себе — работа останавливается до разрешения.» ЧТО БЫЛО. `engine/archive_tracker.py` умел вести состояние (законы мира, персонажи, открытые долги, последняя точка, tentpoles, статус нарраторов) и проверял ОДНО правило — три открытых долга (это Блок 7/11.3). Правило «архив против самого себя» не проверялось ничем, а `discipline/archive_protocol.yaml` — файл с дословными правилами всех шести подблоков — не читал никто вообще. ПОЧЕМУ ЭТО САМОЕ ДОРОГОЕ ПРА…
- **коды состояний** (9): `CLEAR`, `CLOSED`, `ERROR`, `NOT_CONFIGURED`, `OPEN`, `RESOLVED`, `STOP`, `UNRESOLVED`, `YES`
- **тесты, которые зовут модуль**: 2 — `tests/test_block11_archive_contradiction.py`, `tests/test_block7_promise_model.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 49 | константа | `TENTPOLE_STATUSES` | tuple, 3 элементов |
| 50 | константа | `NARRATOR_STATUSES` | tuple, 6 элементов |
| 52 | константа | `ЗАКРЫТО` | set, 4 элементов |
| 53 | константа | `ОТКРЫТО` | set, 5 элементов |
| 55 | константа | `ПРОТОКОЛ` |  |
| 58 | функция | `_правила_протокола()` | Дословные правила подблоков из `discipline/archive_protocol.yaml`. |
| 78 | функция | `_норма(значение)` |  |
| 82 | функция | `_текст(значение)` |  |
| 86 | класс | `ArchiveContradictionGate (1 публичных методов)` | СТОП-правило Блока 11. Механика всегда, смысл — когда есть судья. |
| 252 | функция | `norm_unknown(норма)` | Статус нарратора вне канонического набора Блока 13.5. |

## archive_tracker

- **путь**: `engine/archive_tracker.py`
- **размер**: 204 строк, SHA-256 blob `eb29444d5784325f…`
- **коды состояний** (7): `ARCHIVE_COMMIT`, `ARCHIVE_CONTRADICTION_STOP`, `ARCHIVE_PROPOSAL_SKIPPED`, `AUTHOR_REVIEW_REQUIRED`, `AUTHOR_VETO_DENIED`, `STOP`, `UNKNOWN`
- **тесты, которые зовут модуль**: 9 — `tests/test_ak_discipline_cli.py`, `tests/test_ak_discipline_engine.py`, `tests/test_block11_archive_contradiction.py`, `tests/test_block11_archive_workflow.py`, `tests/test_block2_author_veto_once.py`, `tests/test_promise_extractor.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 7 | константа | `DEFAULT_STATE` | dict, 7 элементов |
| 18 | класс | `ArchiveTracker (8 публичных методов)` | Block 11 state tracker. |

## async_validation_pipeline

- **путь**: `engine/async_validation_pipeline.py`
- **размер**: 133 строк, SHA-256 blob `c2b75418bfa7b962…`
- **коды состояний** (7): `ABORT`, `BLOCK`, `BLOCKED`, `DETERMINISTIC_LATENCY_BUDGET_EXCEEDED`, `RISK`, `STOP`, `WARN`
- **тесты, которые зовут модуль**: 0 (**прямого теста нет**)
- **откуда достижим**: `api/service.py` (тестов на точку входа — 38) — **это путь в коде, а не тест поведения: сам модуль ни один тест не зовёт**

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 10 | класс | `PipelinePhase (0 публичных методов)` |  |
| 18 | класс | `PipelineRunResult (0 публичных методов)` |  |
| 28 | класс | `AsyncValidationPipeline (2 публичных методов)` | v1.8 productization layer. |

## attention_weight

- **путь**: `engine/attention_weight.py`
- **размер**: 205 строк, SHA-256 blob `de22796c53c73b9c…`
- **что это**: attention_weight.py — внимание, потраченное и не возвращённое.
- **зачем**: ═══════════════════════════════════════════════════════════════════════════ ВОПРОС АВТОРА, 04.09.2026 Дословно: «сколько раз в Нью-Кайросе книга один указана про небо, "небо гноилось", — сколько вот такой информации, которая отвлекает от истинной информации; небо роли не играет в книге абсолютно, но сколько внимания к этому небу… почему в книге заявленное внимание не соответствует истине?» Вопрос механический, и он меряется. ЧТО ИЗМЕРЯЕТСЯ. У каждого существительного считаются две величины: ВНИМАНИЕ сколько раз слово названо; ВЕС с…
- **коды состояний** (4): `ATTENTION_WITHOUT_WEIGHT`, `LOW`, `NOUN`, `WARN`
- **тесты, которые зовут модуль**: 2 — `tests/test_attention_weight.py`, `tests/test_mcp101_product.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 81 | константа | `РЕПЛИКА` | re.compile('^\\s*[—–]\\s') |
| 84 | константа | `ГРАНИЦА` | tuple, 6 элементов |
| 88 | константа | `ПОРОГ_ВНИМАНИЯ` |  |
| 94 | константа | `ПОРОГ_НЕСЁТ` |  |
| 95 | константа | `ПОРОГ_СЛАБО` |  |
| 99 | константа | `СЛУЖЕБНЫЕ` | set, 15 элементов |
| 106 | класс | `Вес (1 публичных методов)` |  |
| 117 | функция | `_несущая_позиция(абзацы, i)` | Реплика персонажа или последний абзац сцены. |
| 134 | функция | `взвесить(текст)` | Внимание и вес каждого существительного книги. |
| 164 | функция | `аудит(текст)` | Слова, на которые внимание потрачено и не возвращено. |

## author_veto

- **путь**: `engine/author_veto.py`
- **размер**: 108 строк, SHA-256 blob `b3a9b170a79a9a60…`
- **что это**: author_veto.py — авторское вето AV-1 (канон, Блок 2.3, строки 865–867).
- **зачем**: Канон: **«AV-1 — авторское вето. Доступно один раз на всю книгу.»** ЧТО БЫЛО. В репозитории не было ни строки про AV-1: ни учёта, ни отказа, ни записи. Совет директоров (Блок 2.1) мог вето наложить, а автор — нет, хотя канон даёт ему это право прямо. Проверено поиском по всему дереву: единственное упоминание «AV-1» лежало в реестре канона со статусом «нет». ПОЧЕМУ ЭТО НЕ МЕЛОЧЬ. AV-1 — единственное место канона, где последнее слово остаётся за автором, а не за дисциплиной. Право, которое нигде не учтено, либо не существует…
- **коды состояний** (5): `AVAILABLE`, `DENIED`, `GRANTED`, `NEEDS_INPUT`, `USED`
- **тесты, которые зовут модуль**: 2 — `tests/test_block2_author_veto_once.py`, `tests/test_canon_block_registry.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 35 | константа | `КЛЮЧ` | строка: «author_veto» |
| 36 | константа | `ПРАВИЛО` | строка: «Канон, Блок 2.3: AV-1 — авторское вето, доступно один раз на всю книгу» |
| 39 | функция | `_сейчас()` |  |
| 43 | класс | `AuthorVetoLedger (2 публичных методов)` | Учёт AV-1: одно право на книгу, с записью применения. |

## blindspot_orchestrator

- **путь**: `engine/blindspot_orchestrator.py`
- **размер**: 438 строк, SHA-256 blob `a34009b8916412d7…`
- **что это**: blindspot_orchestrator.py — one entry point that runs the whole
- **зачем**: blind-zones layer over a manuscript and returns a single unified report. Motivation: eight modules were built and validated separately. An author (or a colleague hitting the API) should not call them one by one — they send a manuscript once and get one verdict with everything underneath. The orchestrator runs every module it CAN with the inputs provided: * always-on (need only the manuscript text): - seam-detector (BLOCKING) - echo-detector (flag) - construction-echo (flag) - voice-attribution (flag) - tts-checklist (flag) * confi…
- **коды состояний** (5): `CRITICAL`, `INFO`, `MAJOR`, `MINOR`, `OFF`
- **тесты, которые зовут модуль**: 11 — `tests/test_ak68_integrity_gate_integration.py`, `tests/test_anaphora_cdv_single_impl.py`, `tests/test_blindspot_orchestrator.py`, `tests/test_book_passport.py`, `tests/test_calibration.py`, `tests/test_physics_world_channel.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 52 | константа | `BLOCKING` | set, 3 элементов |
| 56 | класс | `BlindspotConfig (0 публичных методов)` | Everything the author can supply. All optional — modules needing a |
| 80 | класс | `ModuleResult (1 публичных методов)` |  |
| 92 | класс | `BlindspotReport (3 публичных методов)` |  |
| 125 | класс | `BlindspotOrchestrator (1 публичных методов)` |  |

## block13_tracker

- **путь**: `engine/block13_tracker.py`
- **размер**: 104 строк, SHA-256 blob `833ff70ff68f5baa…`
- **коды состояний** (3): `NO_CHANGE`, `REVEAL_DOWNGRADE`, `UPGRADE_UNUSUAL`
- **тесты, которые зовут модуль**: 1 — `tests/test_block13_ssc_char_transitions.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 8 | класс | `Block13Tracker (2 публичных методов)` |  |
| 28 | константа | `STABLE` |  |
| 29 | константа | `MAX_LEVEL` |  |
| 33 | класс | `SSCCharTransition (0 публичных методов)` |  |
| 40 | класс | `SSCCharTracker (4 публичных методов)` | Главо-скоупная персистентность и переходы SSC-CHAR (закрытие разрыва |

## body_marks

- **путь**: `engine/body_marks.py`
- **размер**: 320 строк, SHA-256 blob `82ac6dbf46b783ee…`
- **что это**: body_marks.py — у телесной метки есть срок жизни, и текст обязан его держать.
- **зачем**: Автор, дословно: «я там поглазил себя или где там причесался в том месте, где ещё пока не было шрама… ничего про шрам, которого не было ещё, а где он был — вот в чём вопрос; его стёрли в мире Генри, а где он появился, этот шрам?»
- **коды состояний** (4): `BODY_MARK_DESTROYED_WITHOUT_SETUP`, `BODY_MARK_PROMISED_NEVER_APPEARS`, `HIGH`, `MEDIUM`
- **тесты, которые зовут модуль**: 2 — `tests/test_body_marks.py`, `tests/test_mcp101_product.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 71 | константа | `МЕТКИ` | re.compile('\\b(шрам\\w*\|руб(?:ец\|ц\\w+)\|мозол\\w+\|морщин\\w+\|татуировк\\w+\|ожог |
| 79 | константа | `ОБЕЩАНИЕ` | re.compile('(?:где\|там,?\\s+где)\\s+[^.!?]{0,40}?\\bне\\s+было\\b\|\\bещ[её]\\s+н |
| 88 | константа | `УНИЧТОЖЕНИЕ` | re.compile('\\b(выжиг\\w+\|выжгл\\w+\|стёр\\w*\|стер\\w+\|сожг\\w+\|убра\\w+\|разглад\ |
| 112 | константа | `ЧУЖАЯ` | re.compile('\\b(у\\s+(?:теб[яе]\|него\|не[ёе]\|них\|вас)\|тво[йяие]\\w*\|его\\s+\\w*(? |
| 123 | константа | `МЕСТО_НА_ТЕЛЕ` | re.compile('\\b(больш\\w+\\s+пальц\\w+\|предплечь\\w+\|мизинц\\w+\|лоб\|лбу\|ладон\\w |
| 130 | константа | `СИГНАЛЫ` | tuple, 4 элементов |
| 134 | класс | `Упоминание (1 публичных методов)` |  |
| 157 | константа | `ТОЧНОСТЬ_МЕСТА` | tuple, 18 элементов |
| 164 | функция | `_точность(место)` | Меньше — точнее. Неизвестное считается самым общим. |
| 172 | функция | `_адрес_метки(окно, позиция_метки)` | Самая точная часть тела в окне; при равной точности — ближайшая. |
| 181 | функция | `_обрезать(текст, предел)` |  |
| 186 | функция | `упоминания(главы)` | Все упоминания телесных меток по главам, с сигналом у каждого. |
| 217 | константа | `СИНОНИМЫ` | dict, 3 элементов |
| 220 | функция | `_корень(метка)` | «шрама», «шрамы», «рубец» → «шрам». Грубо и достаточно. |
| 229 | функция | `аудит(главы)` | Два вопроса: обещанное появилось? уничтоженное было посеяно? |

## book_passport

- **путь**: `engine/book_passport.py`
- **размер**: 182 строк, SHA-256 blob `cdb7e48233474cd9…`
- **что это**: book_passport.py — «паспорт книги»: человеческий план книги → конфиг движка.
- **зачем**: Шаг 2 плана «все блоки»: четыре канала аудита молчат (not_configured), потому что им нужен план книги — сквозные образы, обещанные сцены, характер ритма. Писатель не должен писать Python-объекты. Паспорт — это простой YAML-файл обычными русскими словами, один раз на книгу: книга: Ньюкайрос — Стальные тени персонажи: [Алекс, Барон, Генри] мотивы: # сквозные образы - образ: стальные тени варианты: [стальная тень, тени стали] точки: # где образ ДОЛЖЕН появиться - глава: "ГЛАВА 1" якоря: ["первое появление теней"] ритм: #…
- **тесты, которые зовут модуль**: 2 — `tests/test_book_passport.py`, `tests/test_passport_extractor.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 50 | класс | `PassportError (0 публичных методов)` | Понятная писателю ошибка паспорта. |
| 54 | константа | `_REGISTER_WORDS` | dict, 11 элементов |
| 64 | функция | `_slug(s)` |  |
| 69 | класс | `BookPassport (1 публичных методов)` | Разобранный паспорт + перевод в поля BlindspotConfig. |
| 97 | функция | `parse_scenario_items(items)` | «Сцены» → beat-map для канала `beat` (обещанные сюжетные ходы). |
| 121 | функция | `load_passport(text)` | Разобрать YAML-паспорт. Ошибки — по-русски и по делу. |

## book_runner

- **путь**: `engine/book_runner.py`
- **размер**: 329 строк, SHA-256 blob `0528935167754bc8…`
- **что это**: book_runner.py — ПРОХОД ПО СЦЕНАРНОМУ ПЛАНУ: глава за главой.
- **зачем**: ВТОРОЕ ЗВЕНО КНИЖНОГО КОНВЕЙЕРА. Первое (`scenario_planner`) превращает глубокое исследование в план в контракте `check_beat_coverage`. Здесь план превращается в ТЕКСТ: каждая глава пишется по своим битам, а после сборки готовый текст проверяется тем же контрактом, из которого план и вышел. Петля замыкается на себе — сценарий, по которому писали, и есть сценарий, по которому судят. ЧЕГО НЕ БЫЛО. `/generate` умеет одну сцену по свободному описанию: автор сам пишет бриф, сам помнит, что должно попасть в главу, сам сшивает главы и сам …
- **коды состояний** (2): `GENERATOR_FAILED`, `SKIPPED_NO_BEATS`
- **тесты, которые зовут модуль**: 3 — `tests/test_book_chapter_endpoint.py`, `tests/test_book_pipeline_api.py`, `tests/test_book_runner.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 49 | константа | `CONTINUITY_TAIL_CHARS` |  |
| 54 | константа | `DEFAULT_REPAIR_PASSES` |  |
| 57 | константа | `GeneratorResult` |  |
| 58 | константа | `Generator` |  |
| 61 | класс | `BookRunError (0 публичных методов)` | Проход по плану невозможен в принципе (пустой план, нет генератора). |
| 66 | класс | `ChapterDraft (1 публичных методов)` |  |
| 86 | класс | `BookDraft (2 публичных методов)` |  |
| 111 | функция | `_describe_beat(beat)` |  |
| 127 | функция | `build_chapter_brief(chapter_id, beats)` | Бриф одной главы. Отдельная функция — её проверяют тесты и её же |
| 149 | функция | `build_repair_brief(chapter_id, missing)` | Ремонтный проход: модели прямо называют, чего в тексте не хватило. |
| 162 | функция | `_call_generator(generate)` | Вызвать генератор. Возвращает (текст, метаданные, ошибка). |
| 184 | функция | `write_chapter(plan, chapter_id, generate)` | Написать ОДНУ главу по её битам (+ ремонтный проход по непокрытым). |
| 255 | функция | `assemble_book(plan, drafts)` | Сложить написанные главы и проверить их ТЕМ ЖЕ контрактом, из которого |
| 282 | функция | `check_plan_runnable(plan, generate)` | Общая проверка входа для обоих драйверов. Поднимает BookRunError. |
| 296 | функция | `run_book(plan, generate)` | Пройти по сценарному плану и написать книгу глава за главой. |

## calibration

- **путь**: `engine/calibration.py`
- **размер**: 130 строк, SHA-256 blob `02a1c71d6a7892cb…`
- **что это**: calibration.py — the tunable «board» behind the audit.
- **зачем**: Think of a Yamaha amplifier: every dimension is a slider, plus a few fine knobs, plus presets. This module is the backend those sliders drive; the UI just sets these fields. Two kinds of control: 1. Per-dimension SENSITIVITY (the main slider for each check): OFF — dimension not run at all. LOW — more forgiving: its findings are shifted DOWN one severity level (a MAJOR reads as MINOR, a MINOR as INFO). NORMAL — default severities. HIGH — stricter: findings shifted UP one level (a MINOR reads as MAJOR). A dimension with no findings stays cle…
- **коды состояний** (4): `HIGH`, `LOW`, `NORMAL`, `OFF`
- **тесты, которые зовут модуль**: 11 — `tests/test_ak68_integrity_gate_integration.py`, `tests/test_anaphora_cdv_single_impl.py`, `tests/test_calibration.py`, `tests/test_canon_citations.py`, `tests/test_physics_world_channel.py`, `tests/test_promise_extractor.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 36 | константа | `DIMENSIONS` | list, 10 элементов |
| 40 | класс | `Sensitivity (0 публичных методов)` |  |
| 47 | константа | `_SHIFT` | dict, 3 элементов |
| 48 | константа | `_LEVELS` | list, 4 элементов |
| 52 | класс | `CalibrationProfile (6 публичных методов)` |  |

## canon_block_registry

- **путь**: `engine/canon_block_registry.py`
- **размер**: 137 строк, SHA-256 blob `b308dff003b40b6c…`
- **что это**: canon_block_registry.py — таблица блоков канона как источник сверки.
- **зачем**: `discipline/block_activation_rules.yaml` — это собственная таблица канона: адрес блока, название, канонический статус с номером ревизии («БЛОК 10 | Чеклисты | ДО (11 полей) / ПОСЛЕ (12 пунктов) / Открытие глав»). До 30 июля файл **не читал никто**: он был третьей из трёх несостоявшихся связей, найденных при составлении реестра канона. ЧТО ОН ДАЁТ, ЧЕГО НЕТ БОЛЬШЕ НИГДЕ. Все остальные данные канона в репозитории описывают, ЧТО внутри блока. Этот файл описывает, СКОЛЬКО блоков всего и в какой ревизии каждый. Значит его можно св…
- **тесты, которые зовут модуль**: 1 — `tests/test_canon_block_registry.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `ПУТЬ` |  |
| 36 | класс | `БлокКанона (1 публичных методов)` |  |
| 50 | константа | `ВЫЗОВ` | dict, 14 элементов |
| 76 | класс | `CanonBlockRegistry (2 публичных методов)` | Сколько блоков в каноне, в какой ревизии и вызывается ли каждый. |

## canon_citations

- **путь**: `engine/canon_citations.py`
- **размер**: 283 строк, SHA-256 blob `245700c11714a7ce…`
- **что это**: canon_citations.py — верифицированная живая база эталонов (Блоки 12.2/12.5/12.6/12.7).
- **зачем**: Single source of truth for the canon's verified literary anchor citations. Found during full canon read (30 June 2026): the canon is calibrated on concrete live voices of specific authors, verified down to edition and source reference. Blocks 12.5/12.6/12.7 are not an appendix — they are the calibration corpus. Until now only TST-TW, SSC-CHAR and the Fowles gate used any of these; LAW-Z/CDV/TST-KIN/TST-EV/MW-TAC passed the judge an empty canon_examples field, meaning the judge ruled on abstract rules without…
- **тесты, которые зовут модуль**: 5 — `tests/test_canon_citations.py`, `tests/test_canon_citations_wave2.py`, `tests/test_llm_judge_parallel.py`, `tests/test_pkd_b_scene_assignment.py`, `tests/test_tst_pl_l_ontology_attack.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 29 | класс | `Citation (1 публичных методов)` |  |
| 41 | константа | `CITATIONS` | tuple, 28 элементов |
| 263 | функция | `citations_for()` | Все цитаты, калибрующие любой из переданных кодов. |
| 269 | функция | `format_for_judge()` | Собрать canon_examples-строку для LLMJudge.ask() по релевантным кодам. |

## canonical_locus

- **путь**: `engine/canonical_locus.py`
- **размер**: 121 строк, SHA-256 blob `c9a2e41b880c6723…`
- **что это**: canonical_locus.py — PART IV: Duplicate Definition Count = 0.
- **зачем**: расходится: одна половина продукта живёт по одной формулировке, другая по другой, и обе выглядят правильными. В этом репозитории такое уже случалось не с терминами, а с кодом — «две реализации одного правила» (ST-18 против ev_sequence_monitor, promise_stop_rule против PromiseLedger). Метрика ловит ту же болезнь на уровне словаря.
- **коды состояний** (1): `SCN`
- **тесты, которые зовут модуль**: 1 — `tests/test_canonical_locus_duplicates.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 36 | константа | `_ROOT` |  |
| 37 | константа | `_DISCIPLINE` |  |
| 43 | константа | `DEFINITION_SOURCES` | tuple, 3 элементов |
| 51 | константа | `_DESCRIPTIVE_KEYS` | set, 14 элементов |
| 61 | константа | `_ALREADY_CODED` | re.compile('^[A-ZА-Я]{2,}[-–]') |
| 64 | функция | `_clean_code(raw, prefix)` |  |
| 73 | функция | `_rows(data, table_key)` |  |
| 78 | функция | `collect_definitions(root)` | {код: [где определён]} по объявленным источникам. |
| 103 | функция | `audit(root)` | Duplicate Definition Count. Ноль — требование канона (строка 2987). |

## cdr_graph

- **путь**: `engine/cdr_graph.py`
- **размер**: 497 строк, SHA-256 blob `6e261b11e5ac5cb7…`
- **что это**: cdr_graph.py — CDR Causal Debt Registry, граф причинных долгов
- **зачем**: АК v6.7 Блок 13 Что это решает: В длинном произведении факт из главы 4 может противоречить факту из главы 1. Текущий Block13Tracker этого не видит — он только хранит протокол. Этот модуль: - регистрирует факты с указанием главы и источника - позволяет декларировать зависимости между фактами - при инвалидации факта автоматически помечает зависимые как REQUIRES_AUTHOR_REVIEW - не принимает решений за автора — только докладывает конфликты Принцип АК: движок докладывает. Автор решает
- **коды состояний** (23): `ACTIVE`, `AI_GENERATED`, `AUTHOR_REVIEW_REQUIRED`, `COMMITTED`, `CONFLICT_DETECTED`, `CONSEQUENCE_VIOLATED`, `DISCHARGED`, `FRCP_NARRATOR_VS_NARRATOR`, `FRCP_WORLD_VS_NARRATOR`, `FRCP_WORLD_VS_WORLD`, `FROZEN`, `INVALIDATED`, `NARRATOR`, `NARRATOR_FROZEN`, `NARRATOR_ICOI`, `NARRATOR_UNRELIABLE`, `NON_LIQUET`, `NOT_FOUND`, `OBJECTIVE`, `OPEN`, `REQUIRES_REVIEW`, `RETRO_AUDIT`, `VIOLATED`
- **тесты, которые зовут модуль**: 3 — `tests/test_block3_cdv_propagation.py`, `tests/test_v05_modules.py`, `tests/test_время_интервалы.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 31 | класс | `FactStatus (0 публичных методов)` |  |
| 40 | класс | `SourceReliability (0 публичных методов)` |  |
| 52 | класс | `Fact (0 публичных методов)` |  |
| 65 | класс | `ConsequenceStatus (0 публичных методов)` |  |
| 72 | класс | `Consequence (0 публичных методов)` | Причинный долг: причина в главе N требует, чтобы следствие ЖИЛО в |
| 90 | класс | `CDRConflict (0 публичных методов)` |  |
| 102 | класс | `CDRGraph (14 публичных методов)` | Граф причинных долгов. |

## cdv_validator

- **путь**: `engine/cdv_validator.py`
- **размер**: 176 строк, SHA-256 blob `66206db255763d80…`
- **что это**: CDV validator — причинно-следственная связность.
- **зачем**: АК v6.7 Block 3: каждое действие имеет последствие в той же или следующей сцене; последствие не отменяется без явной причины; разрыв цепочки → VTO-K
- **коды состояний** (10): `CDV`, `CDV_ACTION_WITHOUT_VISIBLE_CONSEQUENCE`, `CDV_BROKEN_CHAIN`, `CDV_DECLARED_ACTIONS_NO_DECLARED_CONSEQUENCES`, `CDV_SEMANTIC_CONTRADICTION`, `CDV_UNJUSTIFIED_RESET`, `HIGH`, `MEDIUM`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 3 — `tests/test_anaphora_cdv_single_impl.py`, `tests/test_llm_judge_cdv.py`, `tests/test_substance_sweep.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 12 | константа | `ACTION_RE` | re.compile('\\b(сделал\|сделала\|взял\|взяла\|открыл\|закрыл\|нажал\|ударил\|подписал\|ре |
| 13 | константа | `CONSEQUENCE_RE` | re.compile('\\b(поэтому\|из-за\|из за\|после этого\|в результате\|следствие\|цена\|расп |
| 14 | константа | `BREAK_RE` | re.compile('\\b(без последствий\|ничего не изменилось\|отменилось без причины\|исче |
| 15 | константа | `RESET_RE` | re.compile('\\b(но это не имело значения\|и всё вернулось\|и все вернулось\|как буд |
| 18 | класс | `CDVViolation (0 публичных методов)` |  |
| 24 | класс | `CDVValidator (2 публичных методов)` |  |

## chapter_edit_gate

- **путь**: `engine/chapter_edit_gate.py`
- **размер**: 173 строк, SHA-256 blob `f9948423e42ca7a3…`
- **что это**: ChapterEditGate — редактурный контур главы (2026-07-14).
- **зачем**: Родился из разбора NYK: прогон книги через генеративный канон без инвариантов сохранения выбросил 7 глав (15% текста), выдумал ~20k слов, сменил лицо повествования и убил композицию. Канон — судья сцены, а не редактор книги; редактору нужны инварианты «что нельзя терять». Гейт сравнивает ОРИГИНАЛ главы с ОТРЕДАКТИРОВАННОЙ версией: 1. EDIT_LENGTH_DELTA (BLOCK) — дельта объёма больше допуска (по умолчанию ±20%): признак пересказа вместо редактуры. 2. EDIT_LANDMARK_LOST (BLOCK) — потерян ориентир оригинала: уникальное число (84 000, 40 Гц, …
- **коды состояний** (10): `BLOCK`, `EDIT_ANCHOR_MISSING`, `EDIT_ANCHOR_OVERUSED`, `EDIT_LANDMARK_LOST`, `EDIT_LENGTH_DELTA`, `EDIT_NEW_ENTITY`, `EDIT_POV_SHIFT`, `FLAG`, `HIGH`, `MEDIUM`
- **тесты, которые зовут модуль**: 2 — `tests/test_chapter_edit_gate.py`, `tests/test_patch_proposer.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `_WORD_RE` | re.compile('[А-ЯЁа-яёA-Za-z]+', re.U) |
| 33 | константа | `_NUM_RE` | re.compile('\\b\\d[\\d\\s]{0,12}\\d\\b\|\\b\\d+\\b', re.U) |
| 34 | константа | `_QUOTED_RE` | re.compile('«([^»\\n]{2,40})»', re.U) |
| 35 | константа | `_CAP_RE` | re.compile('\\b[А-ЯЁ][а-яё]{2,}\\b', re.U) |
| 36 | константа | `_SENT_START_RE` | re.compile('(?:^\|[.!?…»]\\s+\|[—-]\\s+\|\\n\\s*)([А-ЯЁ][а-яё]{2,})', re.U) |
| 37 | константа | `_YA_RE` | re.compile('\\bя\\b', re.I \| re.U) |
| 40 | функция | `_norm_num(n)` |  |
| 44 | функция | `_words(text)` |  |
| 48 | функция | `_numbers(text)` |  |
| 52 | функция | `_quoted(text)` |  |
| 56 | функция | `_proper_names(text, min_count)` | Имена собственные: слова с заглавной, встречающиеся >= min_count раз, |
| 87 | функция | `_base_forms(names)` | Грубая нормализация падежей: срезаем частотные окончания, чтобы |
| 99 | класс | `ChapterEditGate (1 публичных методов)` |  |

## chapter_opening_gate

- **путь**: `engine/chapter_opening_gate.py`
- **размер**: 147 строк, SHA-256 blob `b276e529a0267a7e…`
- **что это**: Chapter opening gate — AK v6.7 Block 10.3 first chapter ICoI hint.
- **коды состояний** (12): `FIRST_CHAPTER_ICOI_HINT_MISSING`, `FIRST_CHAPTER_ICOI_HINT_PRESENT`, `FIRST_CHAPTER_ICOI_HINT_PRESENT_SEMANTIC`, `FIRST_CHAPTER_NARRATOR_STATUS_UNDECLARED`, `HIGH`, `IC0I`, `ICOI`, `INFO`, `MEDIUM`, `UNRELIABLE`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 2 — `tests/test_llm_judge_chapter_opening.py`, `tests/test_v161_audit_response.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 7 | константа | `ICOI_HINT_MARKERS` | list, 16 элементов |
| 14 | класс | `ChapterOpeningFinding (0 публичных методов)` |  |
| 20 | класс | `ChapterOpeningGate (2 публичных методов)` |  |

## checklist_constants

- **путь**: `engine/checklist_constants.py`
- **размер**: 103 строк, SHA-256 blob `dad1069b9328832f…`
- **что это**: Shared AK Block 10.2 checklist constants.
- **зачем**: Used by OutputAuditor and PromptPacketBuilder to avoid duplicate drift. ## ЧТО ТАКОЕ «Ручных проверок: 7» И ПОЧЕМУ ЧИСЛО ВВОДИЛО В ЗАБЛУЖДЕНИЕ Строка `Ручных проверок: 7` в сводке `OutputAuditor` (и, через него, в отчёте `scripts/audit_book_live.py`) читалась как «семь полей канона машина не проверяет вовсе». Замер 17.09.2026 показал, что это не так, и разница принципиальная. В ОДНОМ И ТОМ ЖЕ ответе аудита, где стоит эта строка, лежат машинные вердикты по ШЕСТИ из семи полей: ``` 10.2.5 Закон Z → law_z_audit есть 10.2.6 TST-DV → tst_dv_audit есть TST-P…
- **тесты, которые зовут модуль**: 1 — `tests/test_ручные_проверки_называют_своё_авто.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 43 | константа | `BASE_MANUAL_CHECKS` | list, 6 элементов |
| 64 | константа | `AUTO_CHECK_DOCUMENTATION` | list, 6 элементов |
| 75 | константа | `ЭВ_ЯКОРЬ` | dict, 4 элементов |
| 84 | функция | `manual_checklist(scn_code, ev_code, include_auto_docs)` |  |

## checklist_engine

- **путь**: `engine/checklist_engine.py`
- **размер**: 23 строк, SHA-256 blob `790317916d0caeb7…`
- **коды состояний** (7): `BLOCKED`, `EV_REQUIRED_BEFORE_GENERATION`, `MODE_REQUIRED`, `NON_LIQUET`, `NOT_FOUND`, `SCN_REQUIRED_FOR_SCENE_WORK`, `SYN_REQUIRED_OR_SUGGESTED`
- **тесты, которые зовут модуль**: 1 — `tests/test_canon_point_fixes.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 4 | константа | `MODES_REQUIRING_EV` | tuple, 3 элементов |
| 5 | константа | `MODES_REQUIRING_SCN` | tuple, 3 элементов |
| 6 | константа | `MODES_REQUIRING_SYN` | tuple, 4 элементов |
| 9 | класс | `ChecklistEngine (1 публичных методов)` |  |

## checklist_validator

- **путь**: `engine/checklist_validator.py`
- **размер**: 126 строк, SHA-256 blob `92b9d25d787e22fa…`
- **что это**: checklist_validator.py — Block 10 preflight/postflight validator.
- **зачем**: Source-locked to AK v6.7 Block 10.1 and 10.2. It classifies checks as executable/manual and returns missing fields before generation
- **коды состояний** (4): `HIGH`, `LOW`, `MEDIUM`, `WARN`
- **тесты, которые зовут модуль**: 11 — `tests/test_anaphora_cdv_single_impl.py`, `tests/test_block10_checklist_enforcement.py`, `tests/test_canon_point_fixes.py`, `tests/test_dictionary_collision_fixes.py`, `tests/test_forbidden_opening_single_impl.py`, `tests/test_lemma_migration_checklist.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 20 | константа | `SCN_RE` | re.compile('^(SCN[-_]?\\d{1,2}\|\\d{1,2})$', re.I) |
| 32 | константа | `ABSTRACT_RE` | re.compile('\\b(ужас\|страдание\|тревога\|надежда)\\w*\\b\|\\bгоре\\b\|\\bгорем\\b',  |
| 33 | константа | `ABSTRACT_LEMMAS` | set, 4 элементов |
| 34 | константа | `BODY_RE` | re.compile('\\b(горло\|кожа\|пальц\|ладон\|запах\|металл\|желчь\|зуб\|плеч)\\w*\\b', re. |
| 35 | константа | `BODY_LEMMAS` | set, 21 элементов |
| 42 | константа | `PRICE_LEMMAS` | set, 2 элементов |
| 43 | константа | `NUMBER_RE` | re.compile('\\b\\d[\\d\\s,.]*(?:%\|процент\|секунд\|минут\|час\|лет\|метр\|км\|атмосфер\| |
| 48 | класс | `ChecklistItem (0 публичных методов)` |  |
| 56 | класс | `ChecklistValidator (2 публичных методов)` |  |

## closure_drift_detector

- **путь**: `engine/closure_drift_detector.py`
- **размер**: 360 строк, SHA-256 blob `8b44342024f4fe5b…`
- **что это**: closure_drift_detector.py — дрейф риторики закрытия (AXIOM DRIFT, расширение).
- **зачем**: Наблюдение автора на корпусе «День Арбуза» (PL): у ФАТ — искусственной модели — есть когнитивная подпись, названная в самом тексте: * «wystarczy / to wystarczy» — ДОСТАТОЧНОСТЬ: объявить вопрос закрытым, не идти глубже. Пролог: «Moje ulubione słowo to „wystarczy"» (p1323). * «nie dlatego, że X, lecz dlatego że Y» / «nie X, lecz Y» — ОТРИЦАНИЕ-СДВИГ: «Не отрицать. Не спорить. Сместить место, где стоит вопрос.» ФАТ (p82): «Śmieje się pan nie dlatego, że panu do śmiechu». Дефект (тихое искажение на уровне СТИЛЯ): рhetо…
- **коды состояний** (7): `CHARACTERIZATION`, `DRIFT`, `MOTIF`, `NARRATION`, `NEEDS_AUTHOR_DECISION`, `SPEECH`, `SPEECH_FAT`
- **тесты, которые зовут модуль**: 3 — `tests/test_adversarial_closure_drift.py`, `tests/test_closure_adaptation_plan.py`, `tests/test_closure_drift_detector.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 53 | константа | `CLOSURE_PROFILES` | dict, 2 элементов |
| 96 | константа | `_FAT_RE` | re.compile('\\b(?:FAT\|ФАТ\|ФЕТ\|FET)\\b', re.U) |
| 98 | константа | `Voice` |  |
| 99 | константа | `Verdict` |  |
| 103 | константа | `HARD_BAN_IN_NARRATION` | tuple, 1 элементов |
| 107 | константа | `AUTHOR_DECIDES_IN_NARRATION` | tuple, 1 элементов |
| 112 | константа | `PROFILE_LIMITS` | dict, 1 элементов |
| 123 | константа | `MOTIF_IS_DECLARED_NOT_INFERRED` | строка: «Мотив объявляет автор. Детектор не может отличить подписное слово от л» |
| 130 | функция | `_normalize(text)` |  |
| 134 | функция | `_sentences(text)` |  |
| 138 | функция | `classify_voice(paragraph)` | SPEECH (реплика с тире) / SPEECH_FAT (речь с именем ФАТ) / NARRATION. |
| 147 | класс | `MotifExemption (0 публичных методов)` | Объявленный автором подписной мотив. |
| 161 | класс | `ClosureFinding (1 публичных методов)` |  |
| 174 | функция | `_family_hit(profile_family, paragraph)` | Первый сработавший маркер семьи. |
| 204 | функция | `scan_closure_drift(text, lang, motif_exemptions)` | Найти паттерны закрытия/сдвига, развести по голосу и вердикту. |
| 274 | функция | `load_declared_motifs(path)` | Загрузить объявленные автором мотивы из JSON. |
| 297 | функция | `profile_limits_for(lang)` | Что детектор в этом языке заведомо НЕ видит. |
| 308 | функция | `_matching_exemption(paragraph, family, exemptions)` |  |
| 320 | функция | `closure_adaptation_plan(text, lang, motif_exemptions)` | План адаптации: что прореживать, что защищено, что решает автор. |

## compute_budget_gate

- **путь**: `engine/compute_budget_gate.py`
- **размер**: 157 строк, SHA-256 blob `86babc5d99ab9b91…`
- **что это**: compute_budget_gate.py — AK-MASTER v3.1 active module budget.
- **зачем**: Source lock: AK-MASTER v3.1 defines Active Module Budget: max 5 active modules per scene; recursion depth <= 7. Exceeding the budget triggers `degrade_mode()` rather than uncontrolled module stacking
- **коды состояний** (15): `APPLIED`, `COMPUTE_BUDGET_ACTIVE_MODULES_EXCEEDED`, `COMPUTE_BUDGET_BAD_CONTEXT_LENGTH`, `COMPUTE_BUDGET_RECURSION_EXCEEDED`, `FRCP`, `GOVERNANCE`, `HIGH`, `IMPOSSIBLE`, `MEDIUM`, `NOT_NEEDED`, `OAS`, `SCN`, `SYN`, `TST`, `WARN`
- **тесты, которые зовут модуль**: 4 — `tests/test_compute_budget_reaction.py`, `tests/test_dependency_integrity.py`, `tests/test_dependency_integrity_supreme.py`, `tests/test_v151_runtime_governance.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 17 | константа | `MANDATORY_STEPS` | tuple, 8 элементов |
| 22 | константа | `MAX_ACTIVE_MODULES` |  |
| 23 | константа | `MAX_RECURSION_DEPTH` |  |
| 26 | функция | `_is_mandatory(module)` |  |
| 33 | класс | `BudgetFlag (0 публичных методов)` |  |
| 40 | функция | `degrade_mode(active_modules)` | РЕАКЦИЯ на превышение бюджета, а не сообщение о нём. |
| 90 | функция | `recursion_buffer(recursion_depth)` | РЕАКЦИЯ на превышение глубины рекурсии: где именно остановиться. |
| 108 | класс | `ComputeBudgetGate (1 публичных методов)` |  |

## confession_paradoxes_gate

- **путь**: `engine/confession_paradoxes_gate.py`
- **размер**: 303 строк, SHA-256 blob `5eeaf3d1114bf4a9…`
- **что это**: confession_paradoxes_gate.py — Парадокс Достоевского и Парадокс Янси.
- **зачем**: AK-MASTER v6.7, Блок 2.4 (строки 869–872, PART II 101–107): Парадокс Достоевского: НАРУШЕНИЕ: исповедь приносит герою облегчение и ясность. ИСКУССТВО: исповедь уничтожает героя пока он говорит. [6.1] Парадокс Янси — диалог как психологическая защита: Герой говорит о второстепенном чтобы не говорить о главном. Обратная операция: не уничтожение через исповедь — сокрытие через светский разговор. Боль в подтексте. Диалог о пустяках = дифференциал давлений. Найдено при reverse-order ревизии Блока 2 (после TST-TRK, VRP-7/VRP-10): …
- **коды состояний** (12): `DOSTOEVSKY_PARADOX_UNCLEAR`, `DOSTOEVSKY_PARADOX_VIOLATION_RELIEF`, `DOSTOEVSKY_PARADOX_VIOLATION_SEMANTIC`, `HIGH`, `LOW`, `MEDIUM`, `NEEDS_INPUT`, `WARN`, `YANCEY_PARADOX_CONFIRMED`, `YANCEY_PARADOX_NOT_PRESENT`, `YANCEY_REQUIRES_SEMANTIC_JUDGE`, `YES`
- **тесты, которые зовут модуль**: 1 — `tests/test_confession_paradoxes_gate.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 50 | константа | `CONFESSION_LEMMAS` | set, 6 элементов |
| 51 | константа | `CONFESSION_MARKERS` | list, 9 элементов |
| 57 | константа | `RELIEF_MARKERS` | list, 10 элементов |
| 63 | константа | `DESTRUCTION_MARKERS` | list, 14 элементов |
| 72 | класс | `ParadoxFinding (0 публичных методов)` |  |
| 79 | класс | `DostoevskyParadoxGate (2 публичных методов)` | Парадокс Достоевского — Блок 2.4. |
| 193 | константа | `DIALOGUE_MARKER` | строка: «—» |
| 198 | константа | `UNSPOKEN_TENSION_MARKERS` | list, 14 элементов |
| 204 | класс | `YanceyParadoxGate (2 публичных методов)` | Парадокс Янси — Блок 2.4 [6.1-ЛИТ]. Намеренно без механического |

## config_loader

- **путь**: `engine/config_loader.py`
- **размер**: 39 строк, SHA-256 blob `5ceb82bf76cc4a27…`
- **тесты, которые зовут модуль**: 4 — `tests/test_block11_archive_workflow.py`, `tests/test_block12_anchors_not_proof.py`, `tests/test_block6_tst_suite_enforcement.py`, `tests/test_vrp_procedural_rules.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 5 | константа | `ROOT` |  |
| 7 | функция | `load_yaml(rel)` |  |
| 11 | функция | `load_json(rel)` |  |
| 15 | функция | `data_path(rel)` |  |
| 19 | константа | `_MODE_BLOCKS_CACHE` |  |
| 22 | функция | `canon_mode_blocks(mode_norm)` | Блоки, которые канон объявляет активными для режима. |

## constitutional_failure_law

- **путь**: `engine/constitutional_failure_law.py`
- **размер**: 294 строк, SHA-256 blob `cbd155ef35e11094…`
- **что это**: constitutional_failure_law.py — PHASE 5 конструкта AK-6.8:
- **зачем**: CONSTITUTIONAL FAILURE LAW. Источник: `discipline/AK_6_8_MERGED_v1_2_SAFE_FINAL.md`, раздел «PHASE 5 — CONSTITUTIONAL FAILURE LAW» (§5.1 Constitutional Offenses CFO-01..08, §5.2 Escalation Chain, §5.3 Rollback Authority Hierarchy, §5.4/5.4.1 Sovereignty Limits + Tier Matrix SSP-0..5, §5.5 Emergency Powers, §5.6 Constitutional Freezes). Найдено сверкой конструкта 16.09.2026: не было построено НИЧЕГО. Ни один код CFO-01..08, ни уровень эскалации, ни SSP-tier из этой таблицы не встречается нигде в `engine/` (проверено построчным grep по в…
- **коды состояний** (4): `CFO_COUNT`, `CFO_FIELD_MISSING`, `ESCALATION_CHAIN_COUNT`, `SOVEREIGNTY_TIER_COUNT`
- **тесты, которые зовут модуль**: 1 — `tests/test_constitutional_failure_law.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 31 | константа | `_КАНОН` |  |
| 34 | константа | `_НАЧАЛО` | строка: «# PHASE 5 — CONSTITUTIONAL FAILURE LAW» |
| 35 | константа | `_КОНЕЦ` | строка: «# PHASE 6 — LIVING CASE MATRIX EXPANDED» |
| 37 | константа | `ИСТОЧНИК` | строка: «AK_6_8_MERGED_v1_2_SAFE_FINAL.md: PHASE 5 — CONSTITUTIONAL FAILURE LAW» |
| 45 | функция | `_канон()` |  |
| 50 | функция | `_раздел_phase5()` |  |
| 57 | функция | `_подраздел(текст, заголовок, конец)` |  |
| 64 | функция | `_строки_таблицы(текст)` |  |
| 80 | класс | `ConstitutionalOffense (1 публичных методов)` |  |
| 104 | константа | `_ПОЛЯ_CFO` | tuple, 8 элементов |
| 117 | функция | `constitutional_offenses()` | 8 конституционных нарушений §5.1 — CFO-01..08. |
| 133 | функция | `offense(код)` |  |
| 144 | функция | `escalation_chain()` | 7 уровней ESCALATION CHAIN MATRIX, §5.2. |
| 155 | класс | `RollbackAuthorityRow (1 публичных методов)` |  |
| 165 | функция | `rollback_authority_hierarchy()` | Таблица §5.3 — ROLLBACK AUTHORITY HIERARCHY. |
| 183 | класс | `SovereigntyTier (1 публичных методов)` |  |
| 193 | функция | `sovereignty_tier_matrix()` | Таблица §5.4.1 — TIER MATRIX, шесть уровней SSP-0..5. |
| 208 | функция | `tier(ssp)` |  |
| 218 | класс | `EmergencyPowerRow (1 публичных методов)` |  |
| 228 | функция | `emergency_powers()` | Таблица §5.5 — EMERGENCY POWERS. |
| 245 | функция | `audit()` | Целостность PHASE 5: полнота полей CFO + таблиц эскалации/tier. |

## construction_echo

- **путь**: `engine/construction_echo.py`
- **размер**: 160 строк, SHA-256 blob `7caa8f64a1572f2b…`
- **что это**: construction_echo.py — Module 5 (ear-pass), mechanism 3: opening echo.
- **зачем**: Read aloud, several sentences in a row that begin the same way «заедают» — the ear hears a stutter. But this is the double-edged one: deliberate anaphora («Не ракета. Не корабль. Не сигнал.») is a powerful device, while the same shape arrived at by accident is a flaw. Only context — and the author's ear — tells them apart. So this is strictly flag-tier, with a hook to mark intentional anaphora (feeds the later TTS-checklist mechanism). Its niche is distinct from the other rhythm tools: * echo-detector (mech. 1) matches repe…
- **коды состояний** (4): `AUDIBLE`, `FLAG`, `LOUD`, `OPENING_ANAPHORA`
- **тесты, которые зовут модуль**: 2 — `tests/test_anaphora_cdv_single_impl.py`, `tests/test_construction_echo.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 29 | константа | `_HEADING_RE` | re.compile('^#{1,3}\\s') |
| 30 | константа | `_TOKEN_RE` | re.compile('[а-яёa-z0-9]+', re.I \| re.U) |
| 32 | константа | `_LEAD_STRIP_RE` | re.compile('^[\\s—–\\-«»\\"\'(]+', re.U) |
| 35 | функция | `_norm(s)` |  |
| 39 | функция | `_opening(unit, n_words)` | First `n_words` normalized tokens of a unit, or None if too short. |
| 49 | класс | `ConstructionFinding (1 публичных методов)` |  |
| 63 | класс | `ConstructionReport (1 публичных методов)` |  |
| 72 | класс | `ConstructionEchoDetector (1 публичных методов)` | Anaphora / opening-repetition detector across consecutive units. |

## contrastive_reframe

- **путь**: `engine/contrastive_reframe.py`
- **размер**: 66 строк, SHA-256 blob `171eebb32db00283…`
- **что это**: contrastive_reframe.py — ЕДИНЫЙ детектор «Это не X. Это Y.»
- **зачем**: (русский эквивалент «It's not X, it's Y» — контрастный рефрейм). Найдено по прямому указанию автора на реальной рукописи («Игла»): 24 чистых вхождения на 44 200 слов (после исключения одного ложного срабатывания — безличной конструкции «мне это не нравится», см. ниже). Внешние источники называют именно эту форму («It's not X — it's Y», часто с тире) САМЫМ часто упоминаемым отдельным tell'ом ИИ-текста: - Wikipedia: Signs of AI writing — «It's not just X. It's Y.» приведён как канонический пример. - Antislop (arXiv:2510.15061, ICLR 2026…
- **тесты, которые зовут модуль**: 4 — `tests/test_comparison_hedge.py`, `tests/test_contrastive_reframe.py`, `tests/test_council_of_eight_in_audit.py`, `tests/test_tst_tw_mechanical_risk.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 50 | константа | `_REFRAME_RE` | re.compile('[Ээ]то\\s+не\\s+(?!(?:нравится\|нужно\|надо\|важно\|жаль\|видно\|слышно\|по |
| 59 | функция | `contrastive_reframe_hits(text)` | Все вхождения конструкции (в порядке появления), с коротким контекстом. |
| 64 | функция | `has_contrastive_reframe(text)` | Есть ли в тексте хотя бы одно вхождение конструкции. |

## cortex_vi_router

- **путь**: `engine/cortex_vi_router.py`
- **размер**: 429 строк, SHA-256 blob `f13fb4f4b17c53c2…`
- **что это**: cortex_vi_router.py — Cortex VI: SSC-CHAR dispatcher + LIVING EXCESS TEST +
- **зачем**: Math Kernel Guard (БЛОК 14 / v0.3). Source-locked to: AK_MASTER_LIT_FULL_STANDARD_v0_3_0_ABSOLUTE_CONSTRUCT_CANON_LOCK.md Sections: §БЛОК 13.5 (SSC-CHAR), §БЛОК 14 (Math Kernel v0.3), §LIVING EXCESS TEST (Cortex / §1102, §848), §USELESS BEAUTY CLAUSE. This module is a thin routing layer, not a replacement for existing modules: SSC-CHAR dispatcher: Classifies a narrator's reliability status into one of four architectural types (SSC-CHAR-1/2/4/5) and returns the downstream actions each type requires. The judgment "which …
- **коды состояний** (10): `CDR_PROTOCOL_RETROAUDIT`, `CHARACTER_REVEALING`, `IRONY_AWE`, `KEEP`, `REMOVE`, `RHYTHMIC`, `SOMATIC`, `STABLE`, `SYMBOLIC`, `WORLD_PRESSURE`
- **тесты, которые зовут модуль**: 2 — `tests/test_cortex_vi_router.py`, `tests/test_hitl_required_contract.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 51 | класс | `SSCCharType (0 публичных методов)` |  |
| 60 | константа | `_SSC_DESCRIPTIONS` | dict, 5 элементов |
| 82 | константа | `_SSC_ACTIVATIONS` | dict, 5 элементов |
| 91 | константа | `_SSC_MARKERS` | dict, 5 элементов |
| 101 | класс | `SSCCharResult (1 публичных методов)` |  |
| 120 | класс | `SSCCharDispatcher (1 публичных методов)` | Classify narrator reliability and return required downstream actions. |
| 158 | класс | `LivingExcessCriterion (0 публичных методов)` |  |
| 167 | константа | `_CRITERION_DESCRIPTIONS` | dict, 6 элементов |
| 183 | константа | `REMOVAL_REASONS` | list, 5 элементов |
| 193 | класс | `LivingExcessResult (1 публичных методов)` |  |
| 213 | класс | `LivingExcessTest (1 публичных методов)` | Six-criterion detail evaluation gate. |
| 269 | функция | `_scn_band(score)` |  |
| 275 | функция | `_ev_band(score)` |  |
| 281 | функция | `_cdp_band(score)` |  |
| 287 | константа | `HITL_THRESHOLD` |  |
| 290 | константа | `MATH_KERNEL_PROHIBITIONS` | list, 5 элементов |
| 300 | класс | `OperatorResult (1 публичных методов)` |  |
| 320 | класс | `MathKernelResult (1 публичных методов)` |  |
| 337 | класс | `MathKernelGuard (1 публичных методов)` | БЛОК 14 Math Kernel v0.3 — three literary diagnostic operators. |

## council_of_eight

- **путь**: `engine/council_of_eight.py`
- **размер**: 399 строк, SHA-256 blob `1855697fca914e33…`
- **что это**: council_of_eight.py — Совет директоров как позвоночник разбора (Блок 2).
- **зачем**: Канон АК-6.7, БЛОК 1: «СУДЬЯ … Блок 2 (VTO) + Блок 5 (VRP) + Блок 6 (тесты)». Канон, БЛОК 2.1 — восемь голосов, у каждого вопрос и дословный триггер вето: ПЕРКИНС [VTO-P] Верю в боль? Автор не доверяет читателю — и это видно в тексте. Физиологический якорь обязателен. КЭМПБЕЛЛ [VTO-K] Работает ли мир? Чудо без цены. Действие без последствий. Идеология как лекция. ХАРТВЕЛЛ [VTO-H] Есть ли трепет? Наука как декорация. Нет игры зумом. Герой вернулся прежним. ДОЗУА [VTO-D] Каждое слово работает? Три предложения одинаковой дли…
- **коды состояний** (17): `CAMPBELL`, `CLEAR`, `ERROR`, `GRND`, `HARTWELL`, `INFN`, `NEEDS_INPUT`, `NOT_CONFIGURED`, `NOT_RUN`, `ORDER_PENDING`, `PRTF`, `PRTS`, `STOP`, `VERB`, `VETO`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 6 — `tests/test_comparison_hedge.py`, `tests/test_contrastive_reframe.py`, `tests/test_council_of_eight_in_audit.py`, `tests/test_council_order_tst_mr_after_dv.py`, `tests/test_negation_parallelism.py`, `tests/test_vrp_procedural_rules.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 61 | константа | `ИЗ_ТЕСТА` | dict, 4 элементов |
| 69 | константа | `ТОЛЬКО_ДЛЯ_СЦЕН` | dict, 2 элементов |
| 74 | функция | `_dv_решён(разбор)` | Закрыт ли TST-DV в уже выполненном разборе. |
| 87 | константа | `_ПРЕДЛОЖЕНИЕ` | re.compile('[^.!?…]+[.!?…]+\|[^.!?…]+$') |
| 88 | константа | `_НЕ_БУКВА` | re.compile('[^а-яёА-ЯЁ]+') |
| 91 | функция | `_предложения(текст)` |  |
| 95 | функция | `_скелет(предложение)` | Пунктуационный скелет предложения — прокси его структуры. |
| 110 | функция | `_есть_глагол(абзац)` | Есть ли в абзаце глагол — по настоящей морфологии, а не по хвостам. |
| 134 | класс | `CouncilOfEight (1 публичных методов)` | Восемь голосов канона выносят вердикт по тексту. |

## council_operational_tools

- **путь**: `engine/council_operational_tools.py`
- **размер**: 211 строк, SHA-256 blob `b7410f0942d71ab5…`
- **что это**: council_operational_tools.py — Кэмпбелл (VTO-K) и Хартвелл (VTO-H).
- **зачем**: Source: AK-MASTER v6.7, Block 2.5, операциональные инструменты голосов Совета директоров. Found during systematic engine review (1 July 2026): vto_router.py only approximates VTO-K ("чудо без цены" via MIRACLE_RE-without-PRICE_RE) and VTO-H ("наука как декорация" + "герой вернулся прежним" via keyword presence) — the canon's own OPERATIONAL PROCEDURES for these two voices were never implemented at all: КЭМПБЕЛЛ — Три вопроса социо-технического давления (обязательная процедура ПЕРЕД VTO-K): 1. Какая проблема делает технологию Н…
- **коды состояний** (12): `CAMPBELL`, `CAMPBELL_NO_SOCIOTECHNICAL_PRESSURE`, `ERROR`, `HARTWELL`, `HARTWELL_NO_PROBLEM_WITHOUT_SCIFI`, `HARTWELL_SYNTAX_DOES_NOT_FOLLOW_SCALE`, `HIGH`, `MEDIUM`, `NOT_CONFIGURED`, `UNCERTAIN`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 2 — `tests/test_council_operational_tools.py`, `tests/test_judge_parser_survives_live_answers.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 39 | класс | `CouncilFinding (1 публичных методов)` |  |
| 50 | класс | `CampbellAudit (1 публичных методов)` | КЭМПБЕЛЛ — три вопроса социо-технического давления (обязательная |
| 128 | класс | `HartwellAudit (1 публичных методов)` | ХАРТВЕЛЛ — игра зумом. Проверяет, что переход от бытового к |

## coverage_validator

- **путь**: `engine/coverage_validator.py`
- **размер**: 437 строк, SHA-256 blob `c5c0f60b8f003e27…`
- **что это**: coverage_validator.py — AK-MASTER v0.7 coverage validator.
- **зачем**: Purpose: - separate TEXT_PRESENT from BEHAVIOR_ENFORCED; - inspect AK source blocks, YAML data files, Python modules and API routes; - produce an honest coverage report for the LLM/HELIX layer. It does not claim that code can replace literary judgment
- **коды состояний** (8): `DOC_ANCHOR`, `ENFORCED`, `FRONT_MATTER`, `GAP`, `NOT_FOUND`, `PARTIAL`, `TEXT_PRESENT`, `WARN`
- **тесты, которые зовут модуль**: 16 — `tests/test_ak_canon_closure.py`, `tests/test_block0_behavioral_enforcement.py`, `tests/test_block10_checklist_enforcement.py`, `tests/test_block11_archive_workflow.py`, `tests/test_block12_anchors_not_proof.py`, `tests/test_block13_ssc_char_transitions.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 24 | константа | `_STATUS_RANK` | dict, 5 элементов |
| 37 | константа | `CLOSED_STATUSES` | tuple, 2 элементов |
| 40 | функция | `_is_doc_anchor(block, data_missing, code_missing, route_missing)` | Блок, который решено не принуждать кодом, — решение, а не пробел. |
| 61 | класс | `CoverageItem (0 публичных методов)` |  |
| 80 | класс | `SourceLineCoverage (0 публичных методов)` |  |
| 88 | класс | `CoverageValidator (4 публичных методов)` | Validates current package coverage against coverage_manifest.yaml. |
| 421 | функция | `main()` |  |

## demo_scenarios

- **путь**: `engine/demo_scenarios.py`
- **размер**: 274 строк, SHA-256 blob `aa3ea9b2cab0efe9…`
- **коды состояний** (9): `FIRST_CHAPTER_ICOI_HINT_MISSING`, `FOWLES_PARADOX_VIOLATION_SOFTENING`, `GET`, `OAS`, `OPEN`, `POST`, `SCN06`, `TSTDV`, `YAML`
- **тесты, которые зовут модуль**: 2 — `tests/test_demo_scenarios_reach_their_subject.py`, `tests/test_v17_demo_binding.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 6 | константа | `DEMO_ENDPOINTS` | list, 16 элементов |
| 25 | константа | `DEMO_SCENARIOS` | list, 15 элементов |
| 250 | функция | `demo_manifest()` |  |
| 262 | функция | `list_demo_scenarios()` |  |
| 270 | функция | `get_demo_scenario(case_id)` |  |

## dependency_integrity

- **путь**: `engine/dependency_integrity.py`
- **размер**: 300 строк, SHA-256 blob `5758e499862b4ef2…`
- **что это**: dependency_integrity.py — RUNTIME FAILURE ATLAS + DEPENDENCY INTEGRITY.
- **зачем**: Канон, `AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md`, строки 3024–3127: атлас из двенадцати сценариев сбоя (FA-01…FA-12), таблица связей CROSS-LINK SPINE и правила целостности зависимостей. Канон даже приводит псевдокод проверки: for link in dependency_graph: if link.type == "hard" and forms_cycle(link, scope="core"): reject(link); emit("DEPENDENCY_INTEGRITY_VIOLATION") if link.type == "recursive" and scope == "core_only": reject(link) Правила целостности (строки 3110–3113) дословно: * «Жёсткие связи не образуют циклы внутри …
- **коды состояний** (9): `DEPENDENCY_INTEGRITY_VIOLATION`, `FA_WITHOUT_GOVERNANCE`, `FA_WITHOUT_RECOVERY`, `INCIDENTS_NOT_SUPPLIED`, `INCIDENT_LOGGING_BELOW_TARGET`, `NOT_RUN`, `NO_INCIDENTS`, `RECURSIVE_LINK_INSIDE_CORE`, `UNKNOWN_FA_ID`
- **тесты, которые зовут модуль**: 3 — `tests/test_activation_map_last_steps.py`, `tests/test_dependency_integrity.py`, `tests/test_dependency_integrity_supreme.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 53 | константа | `_КАНОН` |  |
| 56 | константа | `ИСТОЧНИК` | строка: «AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md: RUNTIME FAILURE ATLAS (3024–» |
| 61 | константа | `ЦИКЛЫ_ЗАПРЕЩЕНЫ` | tuple, 2 элементов |
| 64 | функция | `_строки_таблицы(текст)` | Строки markdown-таблицы без шапки и разделителя. |
| 78 | функция | `_раздел(текст, заголовок, конец)` |  |
| 85 | функция | `_канон()` |  |
| 90 | функция | `failure_atlas()` | Двенадцать строк RUNTIME FAILURE ATLAS — из таблицы канона. |
| 108 | функция | `core_and_extended()` | Состав AK-Core и AK-Extended из таблицы (строка 1780) + расхождение |
| 138 | функция | `links()` | CROSS-LINK SPINE: источник → цель, тип связи. |
| 153 | функция | `_узел(имя)` | «Patch 38 (ICoI Engine)» → «icoi engine». |
| 169 | функция | `_в_core(узел, состав_core)` |  |
| 180 | функция | `_циклы(рёбра)` | Все простые циклы в ориентированном графе (обход в глубину). |
| 205 | функция | `audit(incidents)` | Целостность зависимостей и полнота атласа сбоев. |

## dependency_integrity_supreme

- **путь**: `engine/dependency_integrity_supreme.py`
- **размер**: 368 строк, SHA-256 blob `6e7b7e9d2c614815…`
- **что это**: dependency_integrity_supreme.py — PHASE 7 конструкта AK-6.8: 16 профилей
- **зачем**: модулей, 6 патчей v7.0, реестр governance locks, карта термальных уязвимостей, 4 кода валидации. Источник: `discipline/AK_6_8_MERGED_v1_2_SAFE_FINAL.md`, раздел «PHASE 7 — DEPENDENCY INTEGRITY SUPREME» (7.1–7.5). Раздел в файле встречается ДВАЖДЫ — на более раннем и на более позднем номере строки. Побайтовая сверка (16.09.2026) показала: они не идентичны. У вхождения с МЕНЬШИМ номером строки есть четыре дополнительных governance lock (GL-11…14) и четыре дополнительные строки карты термальных уязвимостей (LEM/SIL/MPE/SFE —…
- **коды состояний** (5): `GL03_MISMATCH`, `GL04_MISMATCH`, `OUTPUTS`, `PATCH_FIELD_MISSING`, `PROFILE_FIELD_MISSING`
- **тесты, которые зовут модуль**: 2 — `tests/test_ak_canon_closure.py`, `tests/test_dependency_integrity_supreme.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 40 | константа | `_КАНОН` |  |
| 43 | константа | `_НАЧАЛО` | строка: «# PHASE 7 — DEPENDENCY INTEGRITY SUPREME» |
| 44 | константа | `_КОНЕЦ` | строка: «# PHASE 8 — FINAL MASTER COMPILATION» |
| 46 | константа | `ИСТОЧНИК` | строка: «AK_6_8_MERGED_v1_2_SAFE_FINAL.md: PHASE 7 — DEPENDENCY INTEGRITY SUPRE» |
| 55 | функция | `_канон()` |  |
| 60 | функция | `_раздел_phase7()` |  |
| 67 | функция | `_подраздел(текст, заголовок, конец)` |  |
| 73 | функция | `_строки_таблицы(текст)` |  |
| 89 | класс | `ModuleProfile (1 публичных методов)` |  |
| 112 | константа | `_ПОЛЯ_7_1` | tuple, 7 элементов |
| 124 | функция | `module_profiles()` | 16 профилей 7.1 — CORE MODULE DEPENDENCY PROFILES. |
| 140 | функция | `profile_for(код)` |  |
| 151 | класс | `PatchProfile (1 публичных методов)` |  |
| 166 | константа | `_ПОЛЯ_7_2` | tuple, 5 элементов |
| 176 | функция | `patches()` | 6 патчей 7.2 — INTEGRATED v7.0 PATCHES (33, 34, 35, 36, 39, 40). |
| 201 | класс | `GovernanceLock (1 публичных методов)` |  |
| 213 | функция | `governance_locks()` | Таблица 7.3 — GOVERNANCE LOCKS REGISTRY, как она есть в каноне. |
| 229 | функция | `lock(id_)` |  |
| 240 | класс | `ThermalRow (1 публичных методов)` |  |
| 251 | функция | `thermal_vulnerabilities()` | Таблица 7.4 — THERMAL VULNERABILITIES MAP. |
| 269 | функция | `validation_outputs()` | 4 кода 7.5 — VALIDATION OUTPUTS, дословно из блока ```text```. |
| 284 | функция | `_gl04_совпадает(значение_канона)` |  |
| 290 | функция | `_gl03_совпадает(значение_канона)` |  |
| 296 | функция | `audit()` | Целостность PHASE 7: полнота полей + расхождение сводки с таблицей. |

## discipline_conductor

- **путь**: `engine/discipline_conductor.py`
- **размер**: 1238 строк, SHA-256 blob `7f1e3450529a611d…`
- **что это**: discipline_conductor.py — «дирижёр»: один прогон всех блоков AK-MASTER
- **зачем**: с честным табло по каждому блоку. Задача: закрыть дыру «модель держит 4% дисциплины вместо всей». Раньше проверки были разбросаны и запускались горстью. Дирижёр прогоняет ВСЁ применимое разом и выдаёт табло по каждому блоку. РЕЖИМЫ (канон АК-6.7, БЛОК 1). «Каждое задание начинается с кода. Без кода — запрашивается уточнение.» Применимость блоков определяется режимом, а не жёстко зашитой таблицей: СУДЬЯ — только критика, без правки. ШАГ 0: SSC-CHAR + ICoI + MW-TAC. Затем Блок 2 (VTO) + Блок 5 (VRP) + Блок 6 (тесты). ОГРАНКА …
- **коды состояний** (38): `AI_ROLE`, `ALL_BLOCKS`, `ARCHIVE_BLOCK13`, `AUDIT`, `BLOCK_0`, `BLOCK_11_FULL`, `BLOCK_13`, `BLOCK_2`, `BLOCK_8`, `CHECKLIST_PRE`, `CLEAR`, `CONDUCTOR`, `DISCIPLINE_RUN`, `ERROR`, `FRCP`, `GEN_ONLY`, `HELD`, `HIGH`, `ICOI`, `LEDGER_PRECHECK`, `LOGGED`, `MODE`, `MW_TAC`, `NEEDS_INPUT`, `NOT_CONFIGURED`, `NOT_RUN`, `OAS`, `OAS_NOT_LOGGED`, `OUTPUT_AUDIT`, `PROMPT_PACKET`, `SCN`, `SSC_CHAR`, `STOP_RULE`, `SYN`, `TST`, `VETO`, `VRP`, `VTO`
- **тесты, которые зовут модуль**: 19 — `tests/test_activation_map_last_steps.py`, `tests/test_block0_really_runs.py`, `tests/test_block10_2_twelve_points.py`, `tests/test_block13_tracking_wired.py`, `tests/test_block7_promise_stop_rule.py`, `tests/test_block8_fear_compass_wired.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 46 | константа | `Status` |  |
| 53 | константа | `MANDATORY_STEPS` | list, 13 элементов |
| 76 | константа | `CANON_MODES` | tuple, 6 элементов |
| 80 | константа | `_MODE_EXTRA_APPLICABLE` | dict, 6 элементов |
| 100 | константа | `_CRITIQUE_ONLY_MODES` | frozenset({'СУДЬЯ', 'ОГРАНКА', 'АРХИВ'}) |
| 119 | константа | `_JUDGE_STEP_0` | tuple, 3 элементов |
| 129 | константа | `_MODE_STEP_0` | dict, 4 элементов |
| 136 | константа | `_STEP_0_NO_JUDGE` | строка: «смысловой судья не настроен: нужен GOOGLE_API_KEY или GEMINI_API_KEY. » |
| 142 | константа | `_NEEDS_INPUT_REASON` | dict, 9 элементов |
| 158 | класс | `BlockResult (0 публичных методов)` |  |
| 168 | класс | `ConductorReport (2 публичных методов)` |  |
| 285 | класс | `DisciplineConductor (3 публичных методов)` | Прогоняет применимую дисциплину за один вызов и строит табло. |

## divine_density_gate

- **путь**: `engine/divine_density_gate.py`
- **размер**: 77 строк, SHA-256 blob `4368034b2020e03a…`
- **коды состояний** (7): `ABSTRACT_WITHOUT_BODY`, `GRAPHITE_FILTER_WORDS`, `GRAPHITE_WEAK_VERBS`, `HIGH`, `MEDIUM`, `METAPHYSICS_WITHOUT_HARD_SF_PRICE`, `WARN`
- **тесты, которые зовут модуль**: 8 — `tests/test_bol_bolshoi_collision_fix.py`, `tests/test_dictionary_collision_fixes.py`, `tests/test_divine_density_wiring.py`, `tests/test_lemma_migration_divine_density.py`, `tests/test_negation_utils_wave2.py`, `tests/test_perception_filters_single_impl.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 11 | класс | `DensityFlag (0 публичных методов)` |  |
| 17 | класс | `DivineDensityGate (1 публичных методов)` | Metaphysical Hard-SF Horror density gate. |

## document_intake

- **путь**: `engine/document_intake.py`
- **размер**: 128 строк, SHA-256 blob `ab7140c11cf44e74…`
- **что это**: document_intake.py — turn an uploaded manuscript file into plain text
- **зачем**: the blind-zones layer can audit. Supported: .docx, .md/.markdown, .txt. The blind-zones checks depend on top-level '#' chapter headings (beat-coverage owner chapters, rhythm phase splitting), so a .docx is extracted with its Word heading STYLES mapped to markdown headings — otherwise every chapter would collapse into one blob and chapter-scoped checks would misfire. Text/markdown files pass through (UTF-8). Anything else is rejected with a clear error rather than a guess
- **тесты, которые зовут модуль**: 1 — `tests/test_document_intake.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 17 | константа | `_MD_EXT` | tuple, 3 элементов |
| 18 | константа | `_DOCX_EXT` | tuple, 1 элементов |
| 21 | константа | `_HEADING_PREFIX` | dict, 5 элементов |
| 30 | класс | `UnsupportedDocument (0 публичных методов)` | Raised for a file type we deliberately do not parse. |
| 34 | функция | `supported_extensions()` |  |
| 38 | функция | `extract_text(filename, raw)` | Extract plain text (with markdown headings) from an uploaded file. |
| 54 | функция | `_extract_docx(raw)` | Word .docx → markdown-ish text. Heading styles become '#'/'##'; |
| 93 | функция | `_абзац_в_блок(para)` | Абзац Word → строка с markdown-префиксом заголовка, если он заголовок. |
| 103 | функция | `_таблица_в_блок(table)` | Таблица Word → строки текста. |

## ear_pass

- **путь**: `engine/ear_pass.py`
- **размер**: 165 строк, SHA-256 blob `ec3cfe239ae0b81f…`
- **что это**: ear_pass.py — Module 5 (Denis's blind-zones handoff, Case 5): the reader
- **зачем**: prepares a novel by EAR (TTS). Every one of his catches was auditory — echo, alien intonation, a missing expected sound. Eye-audits miss these because text is checked as a map but heard as a route. This file implements the highest-value auditory mechanism first: EchoDetector — n-gram repeats (n≥4 words) inside a sliding character window, EXCLUDING registered intentional refrains (the ledger from Module 3). Flag-tier, not blocking: a repeat may be a deliberate motif or an accidental echo, and only the author (ideally liste…
- **коды состояний** (4): `AUDIBLE`, `FAINT`, `FLAG`, `LOUD`
- **тесты, которые зовут модуль**: 1 — `tests/test_ear_pass.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `_TOKEN_RE` | re.compile('[а-яёa-z0-9]+', re.I \| re.U) |
| 33 | константа | `_WS_RE` | re.compile('\\s+', re.U) |
| 36 | функция | `_normalize(text)` |  |
| 41 | класс | `EchoFinding (1 публичных методов)` |  |
| 53 | класс | `EchoReport (1 публичных методов)` |  |
| 62 | класс | `EchoDetector (1 публичных методов)` | Sliding-window n-gram echo detector with refrain exclusion. |

## ect_ceiling

- **путь**: `engine/ect_ceiling.py`
- **размер**: 86 строк, SHA-256 blob `a5b7e9c4a775bcc3…`
- **что это**: Правило 0.7 канона — AI-output ECT-потолок [6.7 — из UC-5 HELIX].
- **зачем**: Канон (PART V, строки 3915–3951): «AI-вывод = ECT-1 по умолчанию. Всегда. Без исключений. Нарративная убедительность AI-текста НЕ повышает ECT-статус факта.» Роль AI в сессии определяет потолок доверия, и любой сгенерированный текст обязан приезжать к автору с явным маркером происхождения. Почему модуль чистый (без I/O и состояния): маркировка не имеет права уронить генерацию. Поэтому неизвестная роль не бросает исключение, а честно прижимается к самому строгому потолку с предупреждением UC5_ROLE_NOT_FIXED — канон называет незаф…
- **тесты, которые зовут модуль**: 24 — `helix_pipeline/tests/test_ai_output_pde.py`, `helix_pipeline/tests/test_ai_ssd.py`, `helix_pipeline/tests/test_anonymity_sta_dyn_b1.py`, `helix_pipeline/tests/test_gi62_end_to_end_investigation.py`, `helix_pipeline/tests/test_governance_live_inputs.py`, `helix_pipeline/tests/test_icoi_source.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 19 | константа | `AI_MARKER` | строка: «[AI-GENERATED: ECT-1]» |
| 23 | константа | `ROLE_CEILINGS` | dict, 4 элементов |
| 46 | константа | `_STRICTEST_ROLE` | строка: «НАРРАТИВНЫЙ ГЕНЕРАТОР» |
| 49 | функция | `ect_stamp(ai_role)` | Собрать ECT-штамп для AI-вывода по роли из таблицы правила 0.7. |
| 79 | функция | `prose_ect_stamp()` | ECT-штамп канала генерации прозы (СОАВТОР / КОНСТРУКТ). |

## epistemology_gate

- **путь**: `engine/epistemology_gate.py`
- **размер**: 96 строк, SHA-256 blob `3d732d4ccee7febf…`
- **коды состояний** (12): `ANCHORING_RISK`, `BLOCKED`, `COGNITIVE_OVERLOAD`, `CONTEXTUAL_BIAS`, `HEURISTIC_SUBSTITUTION`, `HIGH`, `LOW`, `MEDIUM`, `MORAL_PANIC_SPIRAL`, `SUGGESTIVE_MEMORY`, `WARN`, `WYSIATI_GAP`
- **тесты, которые зовут модуль**: 4 — `tests/test_evidence_classification_n1_n4.py`, `tests/test_llm_judge_epistemology.py`, `tests/test_v11_operator_epistemology_divine.py`, `tests/test_v12_stabilization_lawz.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 7 | класс | `EpiFlag (0 публичных методов)` |  |
| 13 | класс | `EpistemologyGate (2 публичных методов)` | Cognitive verification gate from the Epistemology research handoff. |

## ev_selector

- **путь**: `engine/ev_selector.py`
- **размер**: 20 строк, SHA-256 blob `274b7622b98d180d…`
- **коды состояний** (3): `NON_LIQUET`, `SELECTED`, `SUGGESTED_NEEDS_AUTHOR_CONFIRMATION`
- **тесты, которые зовут модуль**: 0 (**прямого теста нет**)
- **откуда достижим**: `engine/prompt_packet_builder.py` (тестов, зовущих его, — 30) — **это путь в коде, а не тест поведения: сам модуль ни один тест не зовёт**

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 5 | класс | `EVSelector (1 публичных методов)` |  |

## ev_selector_v2

- **путь**: `engine/ev_selector_v2.py`
- **размер**: 262 строк, SHA-256 blob `1e3031c9cd8aaa0e…`
- **что это**: ev_selector_v2.py — улучшенный селектор ЭВ
- **зачем**: АК v6.7 Блок 6: ЭВ — эмоциональная валентность сцены Проблема старого EVSelector: - ищет слово "страх" в тексте задания и предлагает ЭВ-СТРАХ - ЭВ — это не тема сцены. Это телесный ток. Полюс + интенсивность + вектор. - "Герой боится" и "страх уже прошёл, осталось онемение" — разные ЭВ. - Эвристика по ключевым словам не может это различить. Это решение: - если ЭВ не указана явно — возвращает структурированный запрос к автору - три вопроса: полюс / интенсивность / вектор - эвристика сохраняется только как SUGGESTED_NEEDS_AUTHOR_CONFIRMATION (не блокиру…
- **коды состояний** (5): `AUTHOR_INPUT_REQUIRED`, `COMPLEX`, `NOT_FOUND`, `SELECTED`, `SUGGESTED_NEEDS_AUTHOR_CONFIRMATION`
- **тесты, которые зовут модуль**: 4 — `tests/test_canon_membership_gate.py`, `tests/test_integration_v05.py`, `tests/test_v05_modules.py`, `tests/test_v161_audit_response.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 31 | константа | `VALID_POLES` | set, 4 элементов |
| 36 | константа | `VALID_VECTORS` | set, 5 элементов |
| 45 | константа | `_HEURISTIC` | list, 19 элементов |
| 69 | константа | `OFFICIAL_EV_CODES` | set, 8 элементов |
| 73 | константа | `NUMBNESS_MARKERS` | tuple, 3 элементов |
| 79 | класс | `EVRequest (0 публичных методов)` | Запрос к автору когда ЭВ не указана. |
| 92 | класс | `EVSelection (0 публичных методов)` |  |
| 106 | класс | `EVSelectorV2 (2 публичных методов)` | Улучшенный селектор ЭВ. |

## ev_sequence_monitor

- **путь**: `engine/ev_sequence_monitor.py`
- **размер**: 236 строк, SHA-256 blob `bca213d22cf0d492…`
- **что это**: ev_sequence_monitor.py — межсценовый монитор ЭВ-ядра (Block 0.6).
- **зачем**: Source: AK-MASTER v6.7, Block 0.6 — ЭВ мониторинг + ST-18 [6.7]. Found during full canon-vs-code audit (30 June 2026): TST-EV reads ONE scene's emotional core, but the canon's monitoring rules operate over a SEQUENCE of scenes and were entirely unimplemented: 1. "При трёх тяжёлых сценах подряд (СКОРБЬ/СТРАХ ≥4) — инъекция ИРОНИИ даёт воздух без потери тональности." (affective overload relief) 2. "ПРАВИЛО МОНИТОРИНГА: если пять сцен подряд без ЭВ-ИРОНИЯ или ЭВ-ВОСТОРГ → принудительная инъекция одного из двух." 3. ГАРДНЕР [6.6]: "…
- **коды состояний** (8): `COLLAPSE`, `CRITICAL`, `EV_FIVE_SCENES_NO_RELIEF`, `EV_ST18_NARRATIVE_COLLAPSE`, `EV_THREE_HEAVY_SCENES_NEED_IRONY`, `HIGH`, `MEDIUM`, `WARN`
- **тесты, которые зовут модуль**: 3 — `tests/test_block0_really_runs.py`, `tests/test_canon_point_fixes.py`, `tests/test_ev_sequence_monitor.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 42 | константа | `RELIEF_CORES` | set, 2 элементов |
| 51 | константа | `HEAVY_CORES` | set, 3 элементов |
| 54 | константа | `ST18_SEQUENCE` | list, 5 элементов |
| 64 | класс | `SceneEV (0 публичных методов)` | One scene's emotional-core record. Typically produced by TST-EV |
| 74 | класс | `MonitorSignal (1 публичных методов)` |  |
| 88 | класс | `EVSequenceMonitor (1 публичных методов)` | Межсценовый монитор ЭВ-ядра. Pure function over an explicit scene |

## ev_показанное

- **путь**: `engine/ev_показанное.py`
- **размер**: 181 строк, SHA-256 blob `aa9cab51c785fce3…`
- **что это**: ev_показанное.py — ЭВ-ядро, прочитанное по ПОКАЗАННОМУ, а не по названному.
- **зачем**: ============================
- **тесты, которые зовут модуль**: 1 — `tests/test_ev_показанное.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 60 | константа | `_U` |  |
| 64 | константа | `_СТРАХ` | list, 10 элементов |
| 84 | константа | `_ЯРОСТЬ` | list, 5 элементов |
| 93 | константа | `_СТЫД` | list, 1 элементов |
| 98 | константа | `С_ЯДРОМ` | dict, 3 элементов |
| 106 | константа | `БЕЗ_ЯДРА` | dict, 11 элементов |
| 160 | функция | `ядра_по_показанному(text)` | Сколько РАЗНЫХ семей показанных жестов указывает на каждое ядро. |
| 169 | функция | `показанное_без_ядра(text)` | Имена сработавших семей, чьё ядро формой не определяется. |
| 175 | функция | `носителей_показанного(text)` | Общее число семей показанного — и с ядром, и без него. |

## evidence_classification

- **путь**: `engine/evidence_classification.py`
- **размер**: 197 строк, SHA-256 blob `75a6ffc16e1d80d2…`
- **что это**: evidence_classification.py — EVIDENCE CLASSIFICATION N1–N4 (PART IV).
- **зачем**: Канон, `AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md`, строки 2189–2203: **Проблема:** Научные факты и концепты смешиваются без разметки. **Патч:** Маркировка всех утверждений N1–N4. N1: hard-факты, N2: soft-constraints, N3/N4 — Extended-only (не core). **Метрики:** Evidence Coverage Rate = 100%. **Риски:** Жёсткость оформления — теги короткие, coverage проверяется в preflight. **Правило:** все фактические утверждения помечаются [N1]–[N4]. и строка 2983 (КЛЮЧЕВЫЕ МЕТРИКИ): «Evidence Coverage Rate — % утверждений с меткой N1–N4 —…
- **коды состояний** (7): `CLAIMS_NOT_SUPPLIED`, `EVIDENCE_COVERAGE_BELOW_TARGET`, `EXTENDED_ONLY_CLASS_IN_CORE`, `NOT_RUN`, `NO_CLAIMS`, `UNKNOWN_EVIDENCE_CLASS`, `UNKNOWN_LAYER`
- **тесты, которые зовут модуль**: 2 — `tests/test_evidence_classification_n1_n4.py`, `tests/test_tribunal_protocol.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 47 | константа | `CLASSES` | dict, 4 элементов |
| 60 | константа | `EXTENDED_ONLY` | tuple((к for к, з in CLASSES.items() if not з['в_core'])) |
| 63 | константа | `CORE` | строка: «core» |
| 64 | константа | `EXTENDED` | строка: «extended» |
| 66 | константа | `_ТЕГ` | re.compile('\\[\\s*N\\s*(\\d+)\\s*\\]', re.I) |
| 68 | константа | `ИСТОЧНИК` | строка: «AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md, EVIDENCE CLASSIFICATION — N1» |
| 72 | функция | `найти_метки(text)` | Все метки вида [N1]…[N4] и мусорные [N0]/[N5] — в порядке появления. |
| 81 | функция | `_нормализовать_утверждения(claims)` | Утверждения приходят снаружи двумя формами: строкой с меткой внутри |
| 101 | функция | `audit()` | Шлюз классификации доказательств. |

## explanation_gate

- **путь**: `engine/explanation_gate.py`
- **размер**: 280 строк, SHA-256 blob `0fa45cf30992598d…`
- **что это**: explanation_gate.py — «показывай, не объясняй»: текст расшифровывает себя.
- **зачем**: ## ЧТО ЭТО ЗА ПРАВИЛО И ГДЕ ОНО В КАНОНЕ Отдельного блока «show, don't tell» в каноне нет — запрет объяснения разложен по нескольким местам, и все они об одном: * **ПОЛЕ 5 шлюза 10.1** (строки 165–181) — минимальный формат сцены содержит две строки: «Что разрешено объяснять: ___» и «**Что запрещено объяснять: ___**». Зачем поле нужно, канон говорит там же: «не даёт сцене расползтись, **объяснить лишнее** или выйти из ритма главы». * **ПОЛЕ 6** — SCR-вектор засчитан, только если указано, как он проявится «**в действии, а…
- **коды состояний** (12): `ERROR`, `GRND`, `INFN`, `NOT_CONFIGURED`, `NOT_DECLARED`, `NOT_RUN`, `PRTF`, `PRTS`, `SKIPPED`, `VERB`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 5 — `tests/test_audit_passport_over_http.py`, `tests/test_explanation_gate.py`, `tests/test_hostile_reader_gates.py`, `tests/test_запрещённое_дословно.py`, `tests/test_судья_фаулз.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 65 | константа | `ИСТОЧНИК` | строка: «AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md: ПОЛЕ 5 шлюза 10.1 (строки 16» |
| 69 | константа | `ПРАВИЛО` | строка: «Канон запрещает объяснять то, что уже показано: поле 5 шлюза 10.1 треб» |
| 76 | константа | `_ОТВЛЕЧЁННЫЕ` | re.compile('\\w+(?:ость\|ность\|ство\|ствие\|ение\|ание\|ние\|изм\|ация\|ция\|итет\|изна)\\ |
| 86 | константа | `_ГЛАГОЛЬНЫЕ_ЧАСТИ` | set, 5 элементов |
| 89 | константа | `_ПРЯМАЯ_РЕЧЬ` | re.compile('[—«\\"]') |
| 91 | константа | `МАКС_РАСШИФРОВКА_СЛОВ` |  |
| 94 | константа | `МИН_ЦЕПОЧКА` |  |
| 97 | функция | `_предложения(текст)` |  |
| 102 | функция | `_есть_глагол(предложение)` |  |
| 109 | функция | `_показ(предложение)` | Показ — это когда что-то ПРОИСХОДИТ: есть глагол или прямая речь. |
| 121 | функция | `_назывное_отвлечённое(предложение)` | Короткое безглагольное предложение из отвлечённых существительных. |
| 131 | функция | `find_candidates(text)` | Пары «показ → расшифровка отвлечёнными» — КАНДИДАТЫ, не находки. |
| 168 | функция | `audit(text)` | Расшифровывает ли текст сам себя — и не объясняет ли запрещённого. |

## finding_contract

- **путь**: `engine/finding_contract.py`
- **размер**: 85 строк, SHA-256 blob `99894f4411852ba7…`
- **что это**: finding_contract.py — поля контракта находки (SUPPLEMENT §1, §2, §6).
- **зачем**: Три требования дополнения к пакету передачи: * §2 ECT-потолок (Правило 0.7): любой AI-вывод есть ECT-1 ВСЕГДА; нарративная убедительность не повышает ECT; `confidence` — внутренняя мера модели, не статус факта. * §6 `possible_intentional_device`: намеренность приёма берётся ТОЛЬКО из паспорта книги (реестр намеренных анафор/аномалий). Нет реестра → `null`; модель НЕ объявляет приём намеренным самостоятельно. * §1 NON_LIQUET — процедура, а не флаг: при литературной неразрешимости находка несёт полный блок возврата автору, а н…
- **коды состояний** (1): `NON_LIQUET`
- **тесты, которые зовут модуль**: 2 — `tests/test_finding_contract_fields.py`, `tests/test_non_liquet_procedure.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 19 | константа | `ECT_AI_DEFAULT` | строка: «ECT-1» |
| 20 | константа | `ECT_NOTE` | строка: «AI-вывод — ECT-1 всегда (Правило 0.7): нарративная убедительность не п» |
| 27 | константа | `FORBIDDEN_CLOSURES` | tuple, 3 элементов |
| 30 | функция | `possible_intentional_device(registry)` | §6: намеренность приёма — из паспорта книги, не из догадки модели. |
| 49 | функция | `non_liquet_block(active)` | §1: полный блок NON_LIQUET (или None, если процедура не активна). |

## forbidden_opening

- **путь**: `engine/forbidden_opening.py`
- **размер**: 98 строк, SHA-256 blob `5be0892893492158…`
- **что это**: forbidden_opening.py — ЕДИНЫЙ детектор запрещённых зачинов (10.2.OPENING).
- **зачем**: Канон 10.1 / 10.2.OPENING: открытие главы не начинается с погоды, места действия или мысли героя о прошлом. Правило раньше жило в ДВУХ расходящихся копиях — `checklist_validator` (одна узкая regex) и `output_auditor` (три паттерна). На каноническом примере «Было пасмурное утро. Он вспомнил, как всё началось много лет назад.» обе копии молча давали PASS: погоду «пасмурное утро» не знал ни один паттерн, а мысль о прошлом стояла во втором предложении (паттерны цеплялись только к самому началу) и глагол был совершенного вид…
- **коды состояний** (3): `PAST_THOUGHT_OPENING`, `PLACE_OPENING`, `WEATHER_OPENING`
- **тесты, которые зовут модуль**: 1 — `tests/test_невидимые_символы.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 25 | константа | `OPENING_WINDOW` |  |
| 27 | константа | `_LEAD` | строка: «(?:[«\"“—–-]\s*)?» |
| 30 | константа | `_WEATHER_NOUN` | re.compile(f'^\\s*{_LEAD}(?:ш[её]л\\s+\|шла\\s+\|стоял[аои]?\\s+)?(?:дожд\\w*\|снег |
| 40 | константа | `_ATMO` | строка: «пасмурн\|ясн\|солнечн\|дождлив\|туманн\|сер(?:ое\|ым\|ый\|ая)\|хмур\|морозн\|т[её» |
| 43 | константа | `_TIME` | строка: «утр\w*\|вечер\w*\|ноч\w*\|день\|дня\|дн[её]м\|полден\w*\|полудн\w*\|сумерк\w*\|» |
| 44 | константа | `_WEATHER_TIME` | re.compile(f'^\\s*{_LEAD}(?:(?:было\|стоял[аио]?\|выдал(?:ся\|ось\|ась)\|наступил[аи] |
| 53 | константа | `_PLACE` | re.compile(f'^\\s*{_LEAD}(?:в\|во\|на\|у)\\s+(?:город\\w*\|комнат\\w*\|здани\\w*\|улиц |
| 65 | константа | `_PAST_THOUGHT` | re.compile(f'(?:^\|[.!?]\\s+){_LEAD}(?:он\|она\|они\|герой\|нарратор\|[А-ЯЁ][а-яё]+)\\ |
| 73 | константа | `_CHECKS` | tuple, 4 элементов |
| 81 | функция | `detect_forbidden_opening(text)` | Коды запрещённых зачинов в открытии `text` (пустой список — чисто). |
| 95 | функция | `forbidden_opening_findings(text)` | Человекочитаемые находки для отчёта аудита (формат output_auditor). |

## fowles_paradox_gate

- **путь**: `engine/fowles_paradox_gate.py`
- **размер**: 245 строк, SHA-256 blob `a4f2bcd4fbd211b4…`
- **что это**: Fowles Paradox gate — AK v6.7 Block 2.4 / 12.6.7.
- **зачем**: Рациональное объяснение иррационального действия усиливает ужас, не снимает его. The gate does not judge prose quality; it flags whether an antagonist/system explanation is internally consistent without turning into justification or sentimental sympathy
- **коды состояний** (9): `FOWLES_HORROR_DOUBLING_WEAK`, `FOWLES_METHODICAL_POLITENESS_WEAK`, `FOWLES_PARADOX_VIOLATION_SEMANTIC`, `FOWLES_PARADOX_VIOLATION_SOFTENING`, `HIGH`, `LOW`, `MEDIUM`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 7 — `tests/test_fowles_marker_generalization.py`, `tests/test_fowles_semantic_rescue_fix.py`, `tests/test_fowles_softening_negation.py`, `tests/test_lemma_migration_ev_keywords.py`, `tests/test_llm_judge_fowles.py`, `tests/test_substance_sweep.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 24 | константа | `RATIONAL_MARKERS` | list, 18 элементов |
| 30 | константа | `POLITE_METHOD_MARKERS` | list, 14 элементов |
| 40 | константа | `HORROR_DOUBLING_MARKERS` | list, 19 элементов |
| 55 | константа | `HORROR_ENTRAPMENT_LEMMAS` | set, 6 элементов |
| 62 | константа | `SOFTENING_SENTIMENT_RE` | re.compile('жалко\|сочувств\\w*\|травм\\w*\|оправд\\w*\|хорош\\w*\\s+человек', re.I  |
| 68 | константа | `SOFTENING_PHRASES` | list, 4 элементов |
| 73 | константа | `SOFTENING_LEMMAS` | set, 4 элементов |
| 76 | класс | `FowlesFinding (0 публичных методов)` |  |
| 82 | класс | `FowlesParadoxGate (2 публичных методов)` | Detects whether rational motive explanation preserves/increases horror. |

## gap_pool_v2

- **путь**: `engine/gap_pool_v2.py`
- **размер**: 156 строк, SHA-256 blob `083bc42244af3559…`
- **что это**: gap_pool_v2.py — RQ3 GAP POOL TTL из кривой забывания (AXIOM DRIFT).
- **зачем**: Когда возврат к старой форме — ненадёжность (нарратор ЗАБЫЛ, что уже исправил факт), а когда — новая арка (сознательный колбэк через полкниги)? Разница — время. После коррекции старое значение кладётся в gap pool на TTL абзацев. Возврат в окне TTL → UNRELIABLE_RETURN (пометить). Возврат за окном → NEW_ARC (не трогать). По истечении TTL запись выпадает — пул не растёт бесконечно. Дефект, который закрывает модуль (из ТЗ): старый TTL = 200/120/expire назначен ДЕКЛАРАТИВНО. «Почему 200?» — числа без формулы, как когда-то пороги 0…
- **коды состояний** (2): `NEW_ARC`, `UNRELIABLE_RETURN`
- **тесты, которые зовут модуль**: 1 — `tests/test_gap_pool_v2_rq3.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 36 | функция | `_quantile(sorted_vals, q)` | Детерминированный квантиль (nearest-rank) без сторонних библиотек. |
| 45 | функция | `derive_ttl(gaps, q)` | TTL из кривой забывания — ФОРМУЛА, не декларация (P0-6). |
| 62 | константа | `ReturnStatus` |  |
| 66 | класс | `GapEntry (2 публичных методов)` | Исправленный факт под наблюдением: старое значение может «всплыть». |
| 82 | класс | `GapPoolV2 (4 публичных методов)` | Пул коррекций с TTL из кривой забывания. |

## generation_join

- **путь**: `engine/generation_join.py`
- **размер**: 94 строк, SHA-256 blob `c3ab1ac3bb76a9b7…`
- **что это**: generation_join.py — сборка частей генерации без разрыва слов на стыке.
- **зачем**: НАЙДЕНО 30 июля 2026 (видно прямо в UI генерации: «Запах дыма давно вывет⏎⏎ рился»): длинная сцена собирается из нескольких вызовов generateContent, и части склеивались всегда через «\n\n». Когда предыдущая часть обрывалась по MAX_TOKENS ПОСРЕДИ слова, а продолжение начиналось остатком того же слова, между половинами вставлялся разрыв абзаца — слово «выветрился» рвалось на «вывет» и «рился». Модуль чистый и без зависимостей: сборка текста не имеет права зависеть от движка или сети, и её легко проверить в изоляции. Разделит…
- **тесты, которые зовут модуль**: 1 — `tests/test_generation_join.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 17 | константа | `_SENTENCE_END` | строка: «.!?…» |
| 19 | константа | `_CLOSERS` | строка: «»"'”)» |
| 22 | функция | `_looks_mid_word(left_char, right_char)` | Токен разрублен на стыке: слева буква/цифра, справа буква/цифра НЕ заглавная. |
| 36 | функция | `_separator(result, piece)` | Выбрать разделитель между уже собранным текстом и следующей частью. |
| 52 | функция | `trim_incomplete_tail(text)` | Обрезать хвост, оборванный посреди слова/предложения по MAX_TOKENS. |
| 77 | функция | `join_generation_pieces(pieces)` | Собрать части сгенерированного текста, не разрывая слова и не плодя абзацы. |

## gesture_monotony

- **путь**: `engine/gesture_monotony.py`
- **размер**: 190 строк, SHA-256 blob `a0e812f3eab8a803…`
- **что это**: gesture_monotony.py — TST-KIN-MONO: однообразие телесного такта.
- **зачем**: Найдено 29.08.2026 не детектором, а автором на слух. Дословно: «обороты, код „посмотрел туда“, вон „посмотрел туда“ — нету приёмов литературного красивого языка».
- **коды состояний** (2): `NOT_ENOUGH_DATA`, `WARN`
- **тесты, которые зовут модуль**: 5 — `tests/test_gesture_monotony.py`, `tests/test_law_z_видит_грудину.py`, `tests/test_mcp101_product.py`, `tests/test_детекторы_видят_настоящее_время.py`, `tests/test_кинесика_видит_семьи_а_не_формы.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 70 | константа | `СЕМЬИ_ЖЕСТОВ` | dict, 9 элементов |
| 112 | константа | `_СКОМПИЛИРОВАНЫ` |  |
| 116 | константа | `МИН_ТАКТОВ` |  |
| 120 | константа | `ПОРОГ_WARN` |  |
| 121 | константа | `ПОРОГ_FAIL` |  |
| 124 | функция | `разложить_такты(text)` | Сколько раз встретилась каждая семья телесных тактов. |
| 130 | функция | `audit(text)` | TST-KIN-MONO: не делает ли один жест работу за все остальные. |

## graphrag_memory

- **путь**: `engine/graphrag_memory.py`
- **размер**: 99 строк, SHA-256 blob `0233dc84ea3cf3d5…`
- **коды состояний** (13): `ADAPTER_READY_NO_EXTERNAL_DB`, `BELIEVES_IN`, `CAUSES`, `CLOSED_IN`, `CONTRADICTS`, `DEPENDS_ON`, `HAS_STATUS`, `INGEST_PREVIEW_READY`, `OPENED_IN`, `SCN`, `SYN`, `TRIGGERS`, `VALIDATED_BY`
- **тесты, которые зовут модуль**: 0 (**прямого теста нет**)
- **откуда достижим**: `api/service.py` (тестов на точку входа — 38) — **это путь в коде, а не тест поведения: сам модуль ни один тест не зовёт**

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 8 | класс | `GraphSchema (0 публичных методов)` |  |
| 18 | класс | `GraphRAGMemoryAdapter (3 публичных методов)` | GraphRAG-ready adapter skeleton for v1.8. |

## hitl_gate

- **путь**: `engine/hitl_gate.py`
- **размер**: 61 строк, SHA-256 blob `ad8c18041bde68fc…`
- **что это**: hitl_gate.py — единый шлюз HITL 14.5 для контракта находки.
- **зачем**: Блок 14.5 / SUPPLEMENT §3: авторское подтверждение ОБЯЗАТЕЛЬНО, если вывод (1) даёт вес > 0.8; (2) меняет канон; (3) закрывает TST-DV; (4) переводит NON_LIQUET в финальный ответ; (5) меняет цену героя или статус источника. «Математический вывод не исполняется без автора». Порог веса — единый `HITL_THRESHOLD` из cortex_vi_router (не вторая копия условия #1). Условия #2–#5 задаются контекстом операции (что вывод ДЕЛАЕТ), а не регуляркой по тексту — это и есть каноничный способ: HITL включается по последствию вывода, известному системе и…
- **коды состояний** (6): `CANON_CHANGE`, `HERO_PRICE_CHANGE`, `NON_LIQUET_TO_FINAL`, `SOURCE_STATUS_CHANGE`, `TST_DV_CLOSE`, `WEIGHT_GT_0_8`
- **тесты, которые зовут модуль**: 2 — `tests/test_hitl_required_contract.py`, `tests/test_soul_layer_canon_triggers.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 20 | константа | `_TRIGGER_REASON` | dict, 6 элементов |
| 30 | функция | `hitl_required()` | Поле контракта `hitl_required` (SUPPLEMENT §3). |

## hostile_reader_gates

- **путь**: `engine/hostile_reader_gates.py`
- **размер**: 224 строк, SHA-256 blob `a641abd6c9986e72…`
- **что это**: hostile_reader_gates.py — судья доводит диагностику до вето, автономно.
- **зачем**: ## Зачем этот модуль Владелец 17.09.2026, дословно: «мне не нужно решение автора, я никогда это не использовал, я всегда слушал и исправлял. делай чтобы было полностью автономно, автор сам исправит». Разбор `discipline/canon_registry.yaml` показал класс из шести правил, которые уже измеряют объективную часть кодом, но оставляют вето на «суждение», вместо того чтобы довести его до PASS/FAIL: `Б3-пауза`, `Б8-травма`, `Б10.1-объяснение`, `Б12.5-семинар`, `PIV-n1n4`, `PIV-oas`. Полный разбор и план — `docs/АВТОНОМНЫЙ_ВРАЖДЕБНЫ…
- **коды состояний** (5): `MEDIUM`, `NOT_CONFIGURED`, `OK_NO_FIGURES`, `PILOT_MEASURED`, `SKIPPED`
- **тесты, которые зовут модуль**: 2 — `tests/test_hostile_reader_gates.py`, `tests/test_pause_law_block3.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 63 | константа | `_ПРАВИЛО` | строка: «Блок 3 АК-MASTER, Закон Паузы (строка 917/165/1326 канона): «Вдох (дли» |
| 72 | константа | `_ВОПРОС` | строка: «Читается ли эта тройка предложений как настоящая, художественно ощутим» |
| 85 | константа | `_ПРИМЕР_ФИГУРЫ` | строка: «Он долго стоял у окна и смотрел, как вода уходит под мост, унося облом» |
| 90 | константа | `_КАНОННЫЕ_ПРИМЕРЫ` |  |
| 102 | класс | `HostileGateFinding (1 публичных методов)` |  |
| 112 | класс | `ПаузаHostileGate (1 публичных методов)` | Судья решает, ощутима ли механически найденная фигура Закона Паузы. |
| 186 | функция | `audit(text)` | Точка подключения к `/api/ak/audit` — по образцу `explanation_gate.audit()`. |

## icoi_source_gate

- **путь**: `engine/icoi_source_gate.py`
- **размер**: 356 строк, SHA-256 blob `52f642cd953e28e4…`
- **что это**: icoi_source_gate.py — ICoI / source identity / ECT cap gate.
- **зачем**: Conflict of interest does not mean falsehood. It raises verification standard. Anonymous source and pseudonymous source have different ECT ceilings. БЛОК 13.4 — ПРОТОКОЛ ICoI ДЛЯ НАРРАТОРА (добавлено 29 июля 2026) `audit()` отвечает на вопрос о ИСТОЧНИКЕ: кто говорит и какой у него потолок достоверности. Канон, Блок 13.4, требует ещё одной проверки — о НАРРАТОРЕ, и формулирует её дословно так: «Перед началом анализа каждой главы — проверить фокального персонажа: Имеет ли данный персонаж мотивацию искажать реальность? Пытается ли он с…
- **коды состояний** (30): `AI_GENERATED`, `ALGORITHMIC`, `ANONYMOUS`, `ASSIGNED`, `CHAPTERS_UNANSWERED`, `CLEAR`, `COERCIVE`, `DECLARED`, `ERROR`, `FINANCIAL`, `HIDING_GUILT_OR_HORROR`, `HITL_RECOMMENDED`, `MOTIVE_TO_DISTORT`, `NARRATOR`, `NON_LIQUET`, `NOT_ASSIGNED`, `NOT_CONFIGURED`, `NOT_RUN`, `NO_CHAPTER_VERDICTS`, `OBJECTIVE`, `PLATFORM`, `POLITICAL`, `PSEUDONYMOUS`, `RELATIONAL`, `REPUTATIONAL`, `SINGLE_CHAPTER`, `STRUCTURAL`, `UNKNOWN`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 6 — `tests/test_icoi_assigns_ssc_char_4.py`, `tests/test_icoi_coercion_governance.py`, `tests/test_icoi_identity_normalization.py`, `tests/test_judge_error_is_not_clean_verdict.py`, `tests/test_v10_kernel_soul_kin_icoi.py`, `tests/test_судья_по_сердце.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 37 | константа | `CONFLICT_TYPES` | set, 10 элементов |
| 43 | класс | `ICoIResult (0 публичных методов)` |  |
| 56 | класс | `ICoISourceGate (3 публичных методов)` |  |

## influence_contract

- **путь**: `engine/influence_contract.py`
- **размер**: 209 строк, SHA-256 blob `6b48c99cc4129cc3…`
- **что это**: influence_contract.py — INFLUENCE CONTRACT (PART IV).
- **зачем**: Канон, `AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md`, строки 2123–2137: **Проблема:** Нет правил против манипулятивного контента (скрытые паттерны). **Для сцен с высоким воздействием обязателен:** | Поле | Описание | |-------------------|------------------------------------------------| | Intent Disclosure | Явное раскрытие намерений | | Exit Path | Явный путь выхода / отказа | | No Dark Patterns | Запрет ложной срочности и скрытого принуждения | | Consumer Choice | Гарантия свободного выбора | **Метрики:** 100% сцен высокого воздействия имеют…
- **коды состояний** (7): `HIGH_IMPACT_NOT_DECLARED`, `HITL_NOT_SET_FOR_HIGH_IMPACT`, `INFLUENCE_FIELD_MISSING`, `INFLUENCE_GUARANTEE_DENIED`, `NOT_RUN`, `NO_HIGH_IMPACT_SCENES`, `SCENES_NOT_SUPPLIED`
- **тесты, которые зовут модуль**: 2 — `tests/test_activation_map_last_steps.py`, `tests/test_influence_contract.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 56 | константа | `FIELDS` | tuple, 4 элементов |
| 63 | константа | `ИСТОЧНИК` | строка: «AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md, INFLUENCE CONTRACT, строки 2» |
| 66 | константа | `_ЛОЖЬ` | set, 9 элементов |
| 67 | константа | `_ИСТИНА` | set, 7 элементов |
| 68 | константа | `_ПУСТО` | re.compile('^\\s*$') |
| 71 | функция | `_гарантия(значение)` | Да/нет из поля-гарантии. None — не объявлено вовсе. |
| 87 | функция | `audit_scene(scene)` | Одна сцена: нужен ли контракт и заполнен ли он. |
| 157 | функция | `audit(scenes)` | Метрика канона: «100% сцен высокого воздействия имеют заполненный |

## law_shadow_detector

- **путь**: `engine/law_shadow_detector.py`
- **размер**: 201 строк, SHA-256 blob `ac4897c79c8e8090…`
- **что это**: law_shadow_detector.py — AK v6.7 canonical Law of Shadow detector.
- **зачем**: Source lock: - AK v6.7 Block 3: Law of Shadow = psychology under crisis. Forbidden: hero calms down -> becomes effective. Allowed: hero acts THROUGH panic, using it as fuel. - VRP-8 / SYN-PKD-D: in normalized absurdity (SCN-06/12), panic-as-fuel is replaced by exhausted adaptation, tired stoicism, melancholic sarcasm. The old antagonist-interior-logic heuristic was useful but misnamed; it was moved to antagonist_logic_gate.py
- **коды состояний** (10): `HIGH`, `LAW_SHADOW_FALSE_CALM_EFFICIENCY`, `LAW_SHADOW_FALSE_CALM_EFFICIENCY_SEMANTIC`, `LAW_SHADOW_PANIC_WITHOUT_ACTION`, `LAW_SHADOW_VRP8_ADAPTATION_MISSING`, `LAW_SHADOW_VRP8_PANIC_RESOURCE_WRONG_CONTEXT`, `LOW`, `MEDIUM`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 7 — `tests/test_context_detectors_single_impl.py`, `tests/test_lemma_migration_law_shadow.py`, `tests/test_llm_judge_law_shadow.py`, `tests/test_negation_utils.py`, `tests/test_v13_lawz_dr_shadow_scr.py`, `tests/test_v14_issue_closure_pack.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 36 | константа | `PANIC_RE` | re.compile('\\b(паник\|ужас\|тревог\|задых\|дыхани\|холодн\\w*\\s+пот\|судорог\|оцепен\| |
| 37 | константа | `PANIC_LEMMAS` | set, 8 элементов |
| 38 | константа | `ACTION_RE` | re.compile('\\b(сделал\|сделала\|шагнул\|пош[её]л\|схватил\|нажал\|ударил\|открыл\|закры |
| 39 | константа | `ACTION_LEMMAS` | set, 2 элементов |
| 40 | константа | `THROUGH_PANIC_RE` | re.compile('\\b(через\\s+паник\\w*\|сквозь\\s+паник\\w*\|паник\\w*\\s+как\\s+топли |
| 41 | константа | `FALSE_CALM_RE` | re.compile('\\b(успокоил(?:ся\|ась\|ись)?\|стал\\w*\\s+спокойн\|обр[её]л\\w*\\s+спок |
| 42 | константа | `EFFECTIVE_WITHOUT_PANIC_RE` | re.compile('\\b(хладнокровн\|спокойн\|без\\s+страха\|без\\s+паник\|ровн\\w*\\s+дыхан |
| 43 | константа | `NORMALIZED_ABSURD_RE` | re.compile('\\b(нормализованн\\w*\\s+абсурд\|абсурд\\w*\\s+норм\|как\\s+будто\\s+э |
| 44 | константа | `EXHAUSTED_ADAPT_RE` | re.compile('\\b(устал\\w*\\s+стоицизм\|меланхолич\\w*\\s+сарказм\|истощ[её]нн\\w*\ |
| 45 | константа | `NON_SCENE_MODES` | set, 3 элементов |
| 46 | константа | `NORMALIZED_ABSURD_SCN` | set, 4 элементов |
| 49 | функция | `_norm_mode(mode)` |  |
| 53 | функция | `_norm_scn(scn_code)` |  |
| 61 | функция | `_downgrade_for_non_scene(severity, non_scene)` |  |
| 68 | класс | `ShadowViolation (0 публичных методов)` |  |
| 75 | класс | `LawShadowDetector (2 публичных методов)` |  |

## law_z_detector

- **путь**: `engine/law_z_detector.py`
- **размер**: 355 строк, SHA-256 blob `6770b754ab106342…`
- **что это**: law_z_detector.py — Law Z / narrative resistance detector.
- **зачем**: Mechanical AK-MASTER rule: a victory, revelation, access, rescue or miracle must carry resistance and a visible price. This is a heuristic gate; it does not replace literary judgment or authorial decision
- **коды состояний** (9): `HIGH`, `LAW_Z_GAIN_WITHOUT_PRICE`, `LAW_Z_GAIN_WITHOUT_RESISTANCE`, `LAW_Z_MIRACLE_WITHOUT_PRICE`, `LAW_Z_SCN14_FALSE_VICTORY`, `LOW`, `MEDIUM`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 19 — `tests/test_block3_cdv_propagation.py`, `tests/test_bol_bolshoi_collision_fix.py`, `tests/test_dictionary_collision_fixes.py`, `tests/test_fowles_marker_generalization.py`, `tests/test_frequency_corpus_collisions.py`, `tests/test_generation_experiment_fixes.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 16 | константа | `GAIN_RE` | re.compile('\\b(победил\|победила\|победили\|выиграл\|выиграла\|спас(?!ибо)\|спасла\|сп |
| 24 | константа | `COGNITIVE_GAIN_RE` | re.compile('\\b(узнал\|узнала\|понял\|поняла\|поняли\|осознал\|осознала\|доказал\|доказа |
| 25 | константа | `NON_SCENE_MODES` | set, 3 элементов |
| 26 | константа | `SCENE_MODES` | set, 3 элементов |
| 35 | константа | `RESISTANCE_RE` | re.compile('\\b(сопротивл\|давлен\|преград\|препятств\|отказ\|не\\s+пускал\|не\\s+дава |
| 47 | константа | `RESISTANCE_LEMMAS` | set, 4 элементов |
| 68 | константа | `PRICE_RE` | re.compile('\\b(цена\|ценой\|заплатил\|заплатила\|стоило\|потерял\|потеряла\|лишил\|лиши |
| 81 | константа | `AMBULANCE_RE` | re.compile('\\b(вызв\\w*\\s+скорую\|скор(ая\|ую\|ой)\\s+помощ\\w*)\\b', re.I \| re.U |
| 124 | константа | `PRICE_LEMMAS` | set, 20 элементов |
| 140 | константа | `PRICE_LEMMAS_ФОРМЫ` | set, 7 элементов |
| 142 | константа | `PRICE_COST_PAST_RE` | re.compile('\\bстоил[аи]?\\b', re.I \| re.U) |
| 143 | константа | `MIRACLE_RE` | re.compile('\\b(чудо\|магия\|аномал\|невозможн\|нарушил.*закон\|телепорт\|портал\|призр |
| 144 | константа | `EXCEPTION_SCN_RE` | re.compile('SCN[-_]?14\|энтроп', re.I \| re.U) |
| 147 | класс | `LawZViolation (0 публичных методов)` |  |
| 153 | класс | `LawZDetector (2 публичных методов)` | Checks whether gain/knowledge/miracle has resistance and price. |

## lcm_anchors

- **путь**: `engine/lcm_anchors.py`
- **размер**: 627 строк, SHA-256 blob `7addb5fbe8962419…`
- **что это**: lcm_anchors.py — обязательные когнитивные якоря (LCM-13…28).
- **зачем**: SCOPE NOTE: этот модуль НЕ входит в AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md (проверено: 0 совпадений «LCM-2» в этом документе на 2026-07-13). Источник — AK-6.8 FINAL_IDEAL canon, раздел «ОБЯЗАТЕЛЬНЫЕ КОГНИТИВНЫЕ ЯКОРЯ» — это расширение поверх базового AK-6.7, а не пробел в его реализации. Модуль добавлен по прямому запросу как опциональное обогащение, не как починка бага. Изначально были подключены только три якоря (LCM-26/27/28) — существовали только в тексте канона и не были подключены ни к одному модулю движка (0 совпадений по вс…
- **коды состояний** (8): `FRCP`, `HITL`, `OAS`, `SCN`, `SOUL_FALSE_CLOSURE_RISK`, `SYN`, `TST`, `VRP`
- **тесты, которые зовут модуль**: 3 — `tests/test_constitutional_failure_law.py`, `tests/test_evidence_classification_n1_n4.py`, `tests/test_lcm_anchors.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 49 | класс | `CognitiveAnchor (1 публичных методов)` |  |
| 66 | константа | `ANCHORS` | tuple, 28 элементов |
| 601 | константа | `_BY_CODE` |  |
| 602 | константа | `_BY_THINKER` |  |
| 605 | функция | `anchor_for(term)` | Найти якорь по коду (LCM-26) или по имени мыслителя (Спиноза/Фрейд/Лакан). |
| 615 | функция | `anchors_for_pathology(pathology_code)` | Найти все якоря, диагностирующие данную FA-патологию (например 'FA-12'). |
| 626 | функция | `all_anchors()` |  |

## ledger_den_arbuza

- **путь**: `engine/ledger_den_arbuza.py`
- **размер**: 38 строк, SHA-256 blob `9ecedaebdd2187a2…`
- **что это**: ledger_den_arbuza.py — starter refrain ledger for «День Арбуза».
- **зачем**: Per Denis's spec, Module 5 (echo-detector) excludes the intentional refrains held in Module 3's ledger. This is the author-owned list of phrases that are SUPPOSED to repeat; everything else the echo-detector surfaces is a candidate accidental echo. Deliberately conservative: only clearly-technical/system motifs and the explicit breathing refrain are pre-listed. Character handles (e.g. «невысокий в красных кроссовках») are intentionally NOT here — whether a repeated character tag is a motif or an echo is exactly the author's call,…
- **тесты, которые зовут модуль**: 1 — `tests/test_ear_pass.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 18 | константа | `REFRAINS` | list, 7 элементов |

## ledger_index

- **путь**: `engine/ledger_index.py`
- **размер**: 76 строк, SHA-256 blob `218de97523cd4564…`
- **что это**: ledger_index.py — RQ5 инвертированный индекс законов (AXIOM DRIFT).
- **зачем**: Проблема: check_physics_violations сверяет КАЖДЫЙ абзац с КАЖДЫМ законом — O(абзацы × законы). На 100 законах и 2836 абзацах это 283k проверок и может выйти за TARGET <3ms на абзац. Решение (гипотеза ТЗ): закон L-PHYS-01 касается только объектов {корки, семечки, сок, ...}. Абзац без этих токенов физически не может нарушить L-PHYS-01 — сверять его с этим законом бессмысленно. Строим инвертированный индекс `объект-паттерн → {law_id}`; для абзаца берём только законы-кандидаты, чьи объекты в нём есть. Детерминированно, без сторонн…
- **тесты, которые зовут модуль**: 1 — `tests/test_ledger_index_rq5.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 31 | функция | `_law_object_patterns(law)` | Объектные паттерны закона (свои или дефолтные). |
| 36 | функция | `build_object_index(ledger)` | Инвертированный индекс: объект-паттерн → {law_id}. |
| 53 | функция | `candidate_law_ids(paragraph, index)` | law_id, чьи объектные паттерны встречаются в абзаце. O(\|паттерны\|). |
| 63 | функция | `check_physics_violations_indexed(text, ledger)` | check_physics_violations с инвертированным индексом. Результат |

## lemma_utils

- **путь**: `engine/lemma_utils.py`
- **размер**: 195 строк, SHA-256 blob `415006489b207ba0…`
- **что это**: lemma_utils.py — morphology-based word matching.
- **зачем**: Found via a suggestion from the author's brother (Denis, working on a parallel/competing construct — see TECH_SPEC_FOR_DENIS): the engine's mechanical detectors match words via `\b(root1|root2|...)\w*\b` regex, which is exactly why "боль" matched "больше" and "пот" matched "потому" (fixed today via hand-written negative lookaheads in negation_utils- adjacent patches, e.g. `боль(?!ш)`). Denis's suggestion: don't guess at which suffixes to EXCLUDE — check whether the word's actual grammatical lemma (dictionary form) matches, using proper Russian m…
- **тесты, которые зовут модуль**: 9 — `tests/test_body_marks.py`, `tests/test_bol_bolshoi_collision_fix.py`, `tests/test_dictionary_collision_fixes.py`, `tests/test_fowles_marker_generalization.py`, `tests/test_lemma_utils.py`, `tests/test_object_continuity_морфология.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `_WORD_RE` | re.compile('[а-яёА-ЯЁ]+', re.U) |
| 48 | функция | `morph_available()` | Доступен ли морфологический анализатор. |
| 60 | функция | `part_of_speech(word)` | Часть речи словоформы («VERB», «NOUN», «ADVB», …) или None. |
| 80 | функция | `_cached_normal_form(word)` | Морфопарс одного слова с кэшем. |
| 95 | функция | `lemma_of(word)` | Return the dictionary form (lemma) of a single Russian word, or |
| 103 | функция | `has_lemma_match(target_lemmas, text)` | True if any word in text has one of the target lemmas. |
| 119 | функция | `find_lemma_matches(target_lemmas, text)` | Return the actual surface-form words in text whose lemma matches |
| 131 | функция | `has_unnegated_lemma_match(target_lemmas, text)` | Combines today's two fixes: lemma-based matching (Denis's |
| 148 | функция | `has_negated_lemma_match(target_lemmas, text)` | Mirror of has_unnegated_lemma_match with the OPPOSITE polarity — |
| 176 | функция | `find_unnegated_lemma_matches(target_lemmas, text)` | Негационно-осведомлённый аналог find_lemma_matches — возвращает |

## llm_judge

- **путь**: `engine/llm_judge.py`
- **размер**: 1041 строк, SHA-256 blob `b3218fabbeb93f95…`
- **что это**: llm_judge.py — semantic second-tier judge for AK-MASTER discipline checks.
- **зачем**: Background (found during live audit, June 2026): the regex-based detectors (law_z_detector, cdv_validator, tst_kin_detector and others) only catch mechanical/keyword signals. A real hero price expressed as an image ("рука была обрублена по локоть") is invisible to a word list that only knows "цена"/"потерял"/"шрам". A real causal contradiction expressed as a scene ("дом сгорел, но семья завтракает на крыльце как ни в чём не бывало") is invisible to a word list that only knows the literal phrase "ничего не изменилось". N…
- **коды состояний** (19): `AK_JUDGE_CACHE`, `AK_JUDGE_CACHE_DIR`, `AK_JUDGE_MODEL`, `AK_JUDGE_PARALLEL`, `AK_JUDGE_PROVIDER`, `ANTHROPIC_API_KEY`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_API_VERSION`, `AZURE_OPENAI_DEPLOYMENT`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_KEY`, `AZURE_OPENAI_MODEL`, `ERROR`, `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `NOT_CONFIGURED`, `PARTIAL`, `UNCERTAIN`, `YES`
- **тесты, которые зовут модуль**: 51 — `tests/test_block10_2_twelve_points.py`, `tests/test_block11_archive_contradiction.py`, `tests/test_block13_tracking_wired.py`, `tests/test_block7_promise_stop_rule.py`, `tests/test_comparison_hedge.py`, `tests/test_conductor_builds_judge.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 91 | константа | `JudgeStatus` |  |
| 95 | константа | `GEMINI_KEY_ENVS` | tuple, 2 элементов |
| 100 | константа | `IGNORED_KEY_ENVS` | tuple, 1 элементов |
| 101 | константа | `ANTHROPIC_KEY_ENVS` |  |
| 106 | константа | `NOT_CONFIGURED_MESSAGE` | строка: «Смысловой судья не настроен: не задан ни GOOGLE_API_KEY, ни GEMINI_API» |
| 115 | константа | `AZURE_KEY_ENVS` | tuple, 2 элементов |
| 116 | константа | `AZURE_ENDPOINT_ENVS` | tuple, 1 элементов |
| 117 | константа | `AZURE_DEPLOYMENT_ENVS` | tuple, 2 элементов |
| 120 | константа | `AZURE_API_VERSION` | строка: «AZURE_OPENAI_API_VERSION» |
| 123 | функция | `_azure_настройки()` | Ключ, адрес и имя развёртывания Azure OpenAI. Нет хотя бы одного — None. |
| 150 | функция | `_first_env(names)` | Первый непустой ключ из перечисленных, прощая опечатку в ИМЕНИ. |
| 179 | константа | `ЗНАКОВ_СУДЬЕ` |  |
| 180 | константа | `ЗНАКОВ_ЭКСТРАКТОРУ` |  |
| 184 | класс | `SemanticVerdict (1 публичных методов)` |  |
| 223 | функция | `_cache_dir()` | Каталог кеша ответов судьи, либо None если кеш выключен. |
| 241 | функция | `_cache_key(payload)` |  |
| 247 | функция | `_ключ_вопроса()` | Ключ кеша по СУТИ вопроса, а не по буквам промпта. |
| 287 | функция | `_прочитать_с_переносом(новый, старый)` | Прочитать по новому ключу, а если пусто — по старому, и перенести. |
| 308 | функция | `_cache_read(key)` |  |
| 319 | функция | `_cache_write(key, value)` |  |
| 333 | класс | `LLMJudge (3 публичных методов)` | Thin, auditable wrapper around ONE narrow semantic call. |
| 990 | функция | `parallel_workers()` | Ширина параллельного опроса судьи. |
| 1004 | функция | `ask_many(judge, requests)` | Задать судье несколько НЕЗАВИСИМЫХ вопросов параллельно. |

## math_kernel_audit

- **путь**: `engine/math_kernel_audit.py`
- **размер**: 146 строк, SHA-256 blob `df4da5fad224519b…`
- **что это**: math_kernel_audit.py — три оператора Блока 14 в пути аудита.
- **зачем**: Канон, `AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md`, строки 435–491: три оператора Блока 14.2–14.4 — SCN-WEIGHT, EV-SIGNAL-STRENGTH, CAUSAL-DEBT-PROPAGATION. Реестр (`Б14-операторы`) писал коротко и точно: «Существуют, в пути аудита не участвуют». Именно это здесь и чинится — плюс два дефекта, которые вскрылись, когда операторы понадобилось подключать. ## ДЕФЕКТ ПЕРВЫЙ: ОЦЕНКА ПО УМОЛЧАНИЮ 0.5 `MathKernelLitRequest` подставлял 0.5 на каждый неприсланный вход. Запрос без единой цифры получал в ответ полосы и вердикт HITL — как будто что…
- **коды состояний** (7): `INVALID_SCORES`, `NOT_A_NUMBER`, `NOT_RUN`, `NOT_SUPPLIED`, `OUT_OF_RANGE`, `SCORES_NOT_SUPPLIED`, `SCORE_NOT_SUPPLIED`
- **тесты, которые зовут модуль**: 1 — `tests/test_math_kernel_in_audit.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `ОПЕРАТОРЫ` | tuple, 3 элементов |
| 51 | константа | `ИСТОЧНИК` | строка: «AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md, БЛОК 14.2–14.4, строки 435–4» |
| 55 | функция | `_число(значение)` |  |
| 67 | функция | `audit()` | Три оператора по тем оценкам, которые действительно пришли. |

## math_kernel_router

- **путь**: `engine/math_kernel_router.py`
- **размер**: 137 строк, SHA-256 blob `4df2c83231183f33…`
- **что это**: math_kernel_router.py — MATH-KERNEL v1.1 runtime gate.
- **зачем**: This router uses the extracted 44-operator registry from the AK-MASTER operator library. It does not calculate formulas. It returns structured operator calls and gates false precision
- **коды состояний** (8): `FORMAL`, `FOUND`, `HITL_REQUIRED`, `NORMAL`, `NOT_FOUND`, `NOT_REQUIRED`, `REDIRECT`, `REQUIRED`
- **тесты, которые зовут модуль**: 2 — `tests/test_v10_kernel_soul_kin_icoi.py`, `tests/test_v11_operator_epistemology_divine.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 15 | класс | `OperatorHit (0 публичных методов)` |  |
| 26 | класс | `MathKernelResult (0 публичных методов)` |  |
| 38 | константа | `ROUTING_PATTERNS` | list, 17 элементов |
| 58 | константа | `NUMBER_PATTERN` | re.compile('\\b\\d[\\d\\s,.]*(?:%\|процент\|млн\|млрд\|тысяч\|год\|лет\|час\|минут\|секун |
| 60 | класс | `MathKernelRouter (3 публичных методов)` |  |

## math_operator_backend

- **путь**: `engine/math_operator_backend.py`
- **размер**: 640 строк, SHA-256 blob `9ea4a93ed7920dcf…`
- **что это**: Executable backend for the 44 MATH operators.
- **зачем**: Scope: deterministic pure-Python calculations where the input contract is satisfied. Danger/HITL operators are blocked unless hitl_approved=True. Numeric output never raises ECT by itself; OAS provenance is carried in the response. ПОЧЕМУ ЗДЕСЬ НЕТ ЗНАЧЕНИЙ ПО УМОЛЧАНИЮ ДЛЯ ДАННЫХ ────────────────────────────────────────────────── Первая версия этого файла подставляла числа за вызывающего: prior=float(i.get('prior', 0.5)); like=float(i.get('likelihood', 0.8)) fpr=float(i.get('false_positive_rate', 0.2)) Вызов `MATH-PROB-01` с одним только `prior=0.…
- **коды состояний** (8): `EXECUTED`, `EXECUTION_ERROR`, `HITL_REQUIRED`, `INPUT_REQUIRED`, `NOT_FOUND`, `NOT_IMPLEMENTED`, `PARTIAL`, `W_AC`
- **тесты, которые зовут модуль**: 2 — `tests/test_demo_scenarios_reach_their_subject.py`, `tests/test_math_backend_never_invents_inputs.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 53 | константа | `Number` |  |
| 56 | класс | `MissingData (0 публичных методов)` | Не хватает данных. Отдельный тип, чтобы не путать с поломкой кода. |
| 82 | константа | `DATA_INPUTS` | dict, 44 элементов |
| 158 | константа | `METHOD_PARAMS` | dict, 5 элементов |
| 166 | константа | `WHY_NO_DEFAULTS` | строка: «Значение по умолчанию для данных невозможно: у отсутствующего prior не» |
| 174 | функция | `_as_vec(x)` | Вектор из входа. Без значения по умолчанию — отсутствие ловится раньше. |
| 181 | функция | `_dot(a, b)` |  |
| 186 | функция | `_norm(a, ord1)` |  |
| 190 | функция | `_bfs_len(adj, start, end)` |  |
| 206 | функция | `_present(raw, name)` | Есть ли величина во входе. |
| 222 | функция | `missing_data(operator_id, raw)` | Все недостающие величины сразу, а не первая попавшаяся. |
| 239 | класс | `_Args (8 публичных методов)` | Вход оператора с записью того, что реально пошло в формулу. |
| 326 | класс | `MathOperatorBackend (2 публичных методов)` |  |

## motif_density

- **путь**: `engine/motif_density.py`
- **размер**: 185 строк, SHA-256 blob `62ea45bbd0d5d7b3…`
- **что это**: motif_density.py — Module 3 (Denis's blind-zones handoff, Case 3).
- **зачем**: The lesson that created this module came from a live author correction. The echo-detector (Module 5) flagged «красные кроссовки» — repeated 16 times — as an accidental echo. It is not: it is a perception-trigger anchored to story nodes (a card win, the ship's death), the shoes of a named victim, and it is *supposed* to recur. The blunt fix was to add the phrase to a refrain ledger. But a ledger is all-or-nothing: it silences the phrase EVERYWHERE, so a genuinely accidental 17th occurrence drifting into an unrelated scene would …
- **коды состояний** (3): `FLAG`, `NODE_WITHOUT_MOTIF`, `OFF_NODE_OCCURRENCE`
- **тесты, которые зовут модуль**: 1 — `tests/test_motif_density.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `_WS_RE` | re.compile('\\s+', re.U) |
| 35 | функция | `_normalize(text)` |  |
| 39 | функция | `_find_all(needle, hay_norm)` | All start offsets of a normalized needle in normalized text. |
| 54 | класс | `MotifNode (0 публичных методов)` |  |
| 60 | класс | `Motif (0 публичных методов)` |  |
| 69 | класс | `MotifFinding (1 публичных методов)` |  |
| 81 | класс | `MotifReport (1 публичных методов)` |  |
| 92 | класс | `MotifDensityAuditor (1 публичных методов)` | Node-aware motif check: occurrences should sit at declared nodes. |

## motifs_den_arbuza

- **путь**: `engine/motifs_den_arbuza.py`
- **размер**: 31 строк, SHA-256 blob `a46a3a921f81241f…`
- **что это**: motifs_den_arbuza.py — motif registry for «День Арбуза».
- **зачем**: Editable data, not code (like the scenario and ledger files). Each motif is a function anchored to story nodes: it belongs at its nodes, and any occurrence drifting off-node is a candidate the author judges. The first entry is the «красные кроссовки» trigger — the motif that motivated Module 3. This registry supersedes the blunt refrain-ledger entry for it: instead of silencing the phrase everywhere, it verifies that every occurrence sits on a node (card win / ship death / watermelon cluster) and would surface a 17th occurrence drifting …
- **тесты, которые зовут модуль**: 1 — `tests/test_motif_density.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 15 | константа | `MOTIFS` | list, 1 элементов |

## mw_tac_diagnostics

- **путь**: `engine/mw_tac_diagnostics.py`
- **размер**: 257 строк, SHA-256 blob `a702cc1059c1c1ca…`
- **что это**: mw_tac_diagnostics.py — CHF-Диагностика нарративных тактик (MW-TAC).
- **зачем**: Source: AK-MASTER v6.7, Block 2.5 — "CHF-ДИАГНОСТИКА НАРРАТИВНЫХ ТАКТИК [6.7 — из HELIX CHF-D]". Шесть паттернов меметической войны как признаки жанровых ловушек в тексте. Found during full canon-vs-code audit (30 June 2026): this block was entirely unimplemented. Canon explicitly requires it as a mandatory first step of СУДЬЯ mode ("ШАГ 0 ОБЯЗАТЕЛЕН ... CHF-диагностика (MW-TAC) — до Совета директоров"), and the code's MODE_RULES["СУДЬЯ"] did not include it at all — meaning СУДЬЯ mode has been structurally incomplete since la…
- **коды состояний** (6): `ERROR`, `HIGH`, `NOT_CONFIGURED`, `SCN15`, `UNCERTAIN`, `YES`
- **тесты, которые зовут модуль**: 3 — `tests/test_judge_error_is_not_clean_verdict.py`, `tests/test_llm_judge_parallel.py`, `tests/test_mw_tac_diagnostics.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `MW_TAC_TABLE` | dict, 6 элементов |
| 88 | константа | `ARGUMENT_MARKER_RE` | re.compile('\\b(во-первых\|во-вторых\|в-третьих\|кроме того\|более того\|также\|и ещё\| |
| 97 | класс | `MWTACFinding (1 публичных методов)` |  |
| 109 | класс | `MWTACDiagnostics (1 публичных методов)` | CHF-Диагностика нарративных тактик (Block 2.5). |

## negation_definition

- **путь**: `engine/negation_definition.py`
- **размер**: 82 строк, SHA-256 blob `8b7104d0513cbff7…`
- **что это**: negation_definition.py — «был не X, а Y»: ОПРЕДЕЛЕНИЕ через отрицание.
- **зачем**: Заведено 17.09.2026 по прямому указанию автора: «сразу вижу ошибки не x а y». ## Чего не хватало В движке уже жили два соседних детектора, и оба проходили мимо: - `negation_parallelism.py` — «не потому что X, а потому что Y». Узкий намеренно: широкую форму «Не X — Y» из него ВЫРЕЗАЛИ 02.08.2026, потому что на живой русской прозе она давала ложные срабатывания («Не стерильно — не дезинфицированно»). Решение было правильным и не отменяется. - `contrastive_reframe.py` — «Это не X. Это Y.», отдельным предложением. Между ними ос…
- **тесты, которые зовут модуль**: 2 — `tests/test_находка_показывает_место.py`, `tests/test_определение_через_отрицание.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 63 | константа | `_ГЛАГОЛ` | строка: «(?:[а-яё]+(?:л\|ла\|ло\|ли\|ть\|ться\|ет\|ут\|ют\|ит\|ат\|ят\|ал\|ял))\b» |
| 67 | константа | `_СВЯЗКА` | строка: «(?:\bбыл\|\bбыла\|\bбыло\|\bбыли\|\bЭто\|\bэто\|\bявляется\|\bявлялось\|\bстал» |
| 69 | константа | `_ОПРЕДЕЛЕНИЕ_ЧЕРЕЗ_ОТРИЦАНИЕ` | re.compile(_СВЯЗКА + '\\s+не\\s+(?!' + _ГЛАГОЛ + ')[^,.;!?]{2,60},\\s*а\\s+[^.;! |
| 75 | функция | `negation_definition_hits(text)` | Все вхождения «был не X, а Y» (в порядке появления), с контекстом. |
| 80 | функция | `has_negation_definition(text)` | Есть ли в тексте хотя бы одно определение через отрицание. |

## negation_parallelism

- **путь**: `engine/negation_parallelism.py`
- **размер**: 86 строк, SHA-256 blob `a302d8a7b29b75c5…`
- **что это**: negation_parallelism.py — ЕДИНЫЙ детектор «не потому что X, а потому что Y»
- **зачем**: (противопоставление ради псевдо-драматургии / negative parallelism). РАСШИРЕНО (2026-08-02, найдено при построчной проверке реальной рукописи «Игла» по всем 12 главам): исходный регэксп ловил только форму с «, а потому что» и «. Потому что» (капитель) — но та же смысловая конструкция (отвергнутая причина / принятая причина) у автора не реже встречается с тире и без «а»: «Не потому что надо было — потому что тело требовало.», а также с «. А потому что» и «, просто потому что». На полном тексте это дало ещё 7 подтверждён…
- **тесты, которые зовут модуль**: 5 — `tests/test_comparison_hedge.py`, `tests/test_contrastive_reframe.py`, `tests/test_council_of_eight_in_audit.py`, `tests/test_negation_parallelism.py`, `tests/test_tst_tw_mechanical_risk.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 68 | константа | `_POTOMU_CONTRAST_RE` | re.compile('[Нн]е\\s+потому,?\\s+что\\b[^.!?]{0,80}?(?:,\\s*а\\s+потому\\s+что\\ |
| 79 | функция | `negation_parallelism_hits(text)` | Все вхождения конструкции (в порядке появления), с коротким контекстом. |
| 84 | функция | `has_negation_parallelism(text)` | Есть ли в тексте хотя бы одно вхождение конструкции. |

## negation_utils

- **путь**: `engine/negation_utils.py`
- **размер**: 127 строк, SHA-256 blob `acbeb2777e0bc11d…`
- **что это**: negation_utils.py — shared negation-proximity helper.
- **зачем**: Found via systematic testing (1 July 2026): almost every mechanical keyword-presence regex in this engine (law_shadow ACTION_RE/PANIC_RE, antagonist_logic INTERIOR_LOGIC_RE, law_z PRICE_RE/RESISTANCE_RE/GAIN_RE, tst_mrl DEGRADATION_RE, vto_router MIRACLE_RE, scr_horror FLESH_RE, and likely others) is negation-blind: "Действий не последовало" ("no action followed") matches ACTION_RE just as readily as "Он совершил действие" ("he took action"), because the regex only checks whether the WORD is present, not whether it is negated. This is NOT a…
- **тесты, которые зовут модуль**: 2 — `tests/test_law_z_регистр_отказа_тела.py`, `tests/test_negation_utils.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 34 | константа | `NEGATION_MARKERS_RE` | re.compile('\\b(не\|ни\|нет\|нету\|никогда\|никак\|нельзя)\\b', re.I \| re.U) |
| 43 | константа | `PREPOSITION_BEZ_RE` | re.compile('\\bбез\\b', re.I \| re.U) |
| 44 | константа | `_BEZ_WINDOW_CHARS` |  |
| 54 | константа | `_CLAUSE_BOUNDARY_RE` | re.compile('[.!?;:\\n]\|—\\s\|,\\s+(?:и\|но\|а)\\s') |
| 61 | константа | `_AFTER_NEG_RE` | re.compile('\\b(?:не\|ни)\\s+(\\w+)', re.I \| re.U) |
| 62 | константа | `_DEEPR_RE` | re.compile('.*(?:(?<!с)[ая]\|ясь\|вшись?\|учи\|ючи)$', re.I \| re.U) |
| 65 | функция | `_clip_to_clause(text, start, end, direction)` | Return the substring from start to end, clipped at the nearest |
| 82 | функция | `is_negated(text, match_start, match_end, window_chars)` | Heuristic check: is a regex match (spanning match_start:match_end) |
| 110 | функция | `find_unnegated(pattern, text, window_chars)` | Like pattern.findall(text), but excludes matches that are negated |
| 121 | функция | `has_unnegated_match(pattern, text, window_chars)` | Like bool(pattern.search(text)), but ignores matches that are |

## normalizer

- **путь**: `engine/normalizer.py`
- **размер**: 80 строк, SHA-256 blob `cc4a566c2fd159e4…`
- **тесты, которые зовут модуль**: 1 — `tests/test_scn_syn_code_extraction.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 4 | функция | `strip_version(value)` |  |
| 13 | функция | `norm_code(value)` |  |
| 21 | функция | `split_codes(value)` |  |
| 44 | константа | `_CANON_CODE_FINDER` | re.compile('\\b(?:SYN\|EXP\|TST\|SCN\|SCR\|VTO\|VRP\|SSC)-[A-Za-z0-9]+(?:[-.][A-Za-z0-9 |
| 50 | функция | `canon_codes(value)` | Только настоящие коды конструкта из смешанной строки, в порядке появления. |

## oas_database

- **путь**: `engine/oas_database.py`
- **размер**: 171 строк, SHA-256 blob `f124b9aafa116a81…`
- **что это**: OAS event ledger — append-only, durable.
- **зачем**: OAS (Operational Accountability System) — журнал подотчётности: «что система сделала, на каком основании, куда жаловаться». Канон требует от него tamper-proof/append-only хранения (GL-locks, HELIX_VERIFY_API: «append-only, no DELETE/UPDATE»), поэтому здесь ровно три правила: 1. APPEND-ONLY. Событие дописывается строкой в JSONL и больше никогда не переписывается. Прошлая реализация читала весь файл и записывала его целиком на каждое событие — это ровно то, что канон запрещает: любая запись могла изменить уже зафиксированные записи. 2. ДОЛГОВЕЧНОСТЬ. Посл…
- **коды состояний** (4): `INFO`, `LOGGED`, `RESET`, `WRITE_FAILED`
- **тесты, которые зовут модуль**: 4 — `tests/test_activation_map_last_steps.py`, `tests/test_data_root.py`, `tests/test_oas_accountability_piv.py`, `tests/test_oas_ledger_append_only.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 40 | константа | `_ROOT` |  |
| 43 | класс | `OASLedgerLocked (0 публичных методов)` | Попытка удалить записи из append-only журнала. |
| 47 | класс | `OASDatabase (3 публичных методов)` |  |

## oas_module_cards

- **путь**: `engine/oas_module_cards.py`
- **размер**: 116 строк, SHA-256 blob `c7c4c8cdcc963871…`
- **что это**: oas_module_cards.py — OAS accountable black-box cards.
- **зачем**: Source lock: AK-MASTER v3.1 requires every critical module to expose Purpose, Prohibited modes, Test Suite, Logs, Appeal, and Proof fields
- **коды состояний** (6): `FRCP`, `OAS`, `SCN`, `SYN`, `TST`, `VTO`
- **тесты, которые зовут модуль**: 2 — `tests/test_oas_accountability_piv.py`, `tests/test_v151_runtime_governance.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 11 | константа | `REQUIRED_FIELDS` | list, 6 элементов |
| 12 | константа | `CRITICAL_MODULES` | list, 14 элементов |
| 18 | функция | `_card(module_id)` |  |
| 28 | класс | `OASModuleCards (2 публичных методов)` |  |

## object_continuity

- **путь**: `engine/object_continuity.py`
- **размер**: 367 строк, SHA-256 blob `18bdc95230f85370…`
- **что это**: object_continuity.py — где сейчас лежит предмет.
- **зачем**: Автор слушал том 1 и остановился на прологе: Юрген **ставит стакан на стойку**, через семнадцать абзацев **бьёт им бармена**, а ещё через пятнадцать стакан **«остался» на стойке** с нетронутым молоком. Три взаимоисключающих положения одного предмета в одной сцене.
- **коды состояний** (1): `NOUN`
- **тесты, которые зовут модуль**: 5 — `tests/test_body_marks.py`, `tests/test_mcp101_product.py`, `tests/test_object_continuity.py`, `tests/test_object_continuity_морфология.py`, `tests/test_время_интервалы.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 81 | константа | `_ПАДЕЖИ` | tuple, 12 элементов |
| 85 | константа | `ВЗЯЛ` | строка: «взял\|взяв\|поднял\|подняв\|подхватил\|перехватил\|схватил\|сжал\|стиснул\|держ» |
| 88 | константа | `ПОСТАВИЛ` | строка: «поставил\|поставив\|положил\|положив\|опустил\|опустив\|уронил\|выронил\|броси» |
| 92 | константа | `НА_МЕСТЕ_ГЛАГОЛ` | строка: «стоял\|стояла\|стояло\|лежал\|лежала\|лежало\|остался\|осталась\|осталось» |
| 98 | класс | `Положение (0 публичных методов)` |  |
| 107 | класс | `Разрыв (0 публичных методов)` |  |
| 118 | функция | `_формы(корень)` | Все словоформы предмета — по морфологии, а не приклейкой окончаний. |
| 144 | константа | `_НЕ_ПРЕДМЕТЫ` | set, 20 элементов |
| 154 | константа | `_ИДИОМЫ` | re.compile('\\b(?:взял\|взяла\|взяли\|брал\|брала\|брали\|взять)\\s+(?:кредит\\w*\|слов |
| 160 | функция | `предметы_сцены(абзацы)` | Какие вещи эта сцена вообще берёт в руки. |
| 202 | функция | `_склоняется(корень, весь)` | Вещь склоняется, наречие — нет. Признак объявляет сам текст. |
| 220 | функция | `_имя_собственное(корень, весь)` | Юрген берёт стакан, но сам вещью не является. |
| 237 | функция | `_корень(слово)` | «стакану» → «стакан», «кружке» → «кружка», «пальцем» → «палец». |
| 262 | функция | `положения(абзацы, предмет)` | Все места, где сцена объявляет, где этот предмет находится. |
| 321 | функция | `творительный(предмет)` | Творительный падеж: «стакан» → «стаканом». Бьют только тем, что держат. |
| 332 | константа | `_МАКС_РАССТОЯНИЕ` |  |
| 335 | функция | `разрывы(абзацы)` | Смена положения предмета без действия, которое её объясняет. |

## observation_gate

- **путь**: `engine/observation_gate.py`
- **размер**: 288 строк, SHA-256 blob `13e3bade816ccdf0…`
- **что это**: observation_gate.py — Observation Gate v0.2 (кора наблюдения).
- **зачем**: Source-locked to: AK_MASTER_LIT_FULL_STANDARD_v0_3_0_ABSOLUTE_CONSTRUCT_CANON_LOCK.md Sections: §II.5 (Observation Gate v0.2 — Кора наблюдения, RU), §OG-0..OG-4 (Observation Gate v0.2, EN restatement — идентична по содержанию; расхождений между версиями не найдено). Canon rule (§II.5, verbatim): Вход системы не является началом. Он является выходом автора, попавшим в систему. Runtime placement (§OG-4, verbatim): Observation Gate > Mode Selector > Block 10.1 > SCN/SYN/EV Observation Gate does not replace AK. It prevents the first in…
- **коды состояний** (41): `ACCEPT_TRANSMISSION_AS_FACT`, `ACCIDENTAL_TRANSFER`, `ANALYSIS_MATERIAL`, `ARCHIVAL_MATERIAL`, `ARCHIVE_FRAGMENT`, `ARCHIVE_MARKER`, `AUTHORIAL_OUTPUT`, `AUTHOR_QUESTION`, `COMMAND`, `COMPLICATE_SIMPLE_FOOD`, `CONFUSE_ARCHIVE_WITH_TASK`, `CURRENT_PROCESS`, `DREAM`, `EMOTIONAL_SIGNAL`, `EXTERNAL_SOURCE`, `FILE`, `FM_OG_01`, `FM_OG_02`, `FM_OG_03`, `FM_OG_04`, `FM_OG_05`, `FM_OG_06`, `FM_OG_07`, `FM_OG_08`, `FOOD_FOR_CURRENT_PROCESS`, `LITERARY_WORK`, `MODEL_GENERATION`, `NOURISHMENT_INTO_PRODUCT`, `OBSERVATION_GATE_PASS`, `OTHER_CHAT`, `PATCH_CANDIDATE`, `PERSONAL_ARCHIVE`, `PHILOSOPHICAL_INSTEAD_OF_STATUS`, `QUESTION`, `RESEARCH_LAYER`, `SIGNAL_INTO_DREAM_DICTIONARY`, `STOP_OBSERVATION`, `STOP_SIGNAL`, `TECHNICAL_SPEC`, `TEXT`, `TRANSMISSION`
- **тесты, которые зовут модуль**: 2 — `tests/test_live_hub.py`, `tests/test_observation_gate.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 61 | класс | `WhatEntered (0 публичных методов)` | Вопрос 1: «Что поступило?» |
| 73 | класс | `WhoseOutput (0 публичных методов)` | Вопрос 2: «Чьим выходом это является?» |
| 82 | класс | `SourceEnvironment (0 публичных методов)` | Вопрос 3: «Из какой среды пришёл сигнал?» |
| 93 | класс | `Destination (0 публичных методов)` | Вопрос 4: «Чем это должно стать здесь?» |
| 103 | класс | `RiskType (0 публичных методов)` | Вопрос 6: «Если риск есть — какой?» (§II.5.5 п.6, полный список канона). |
| 113 | класс | `ForbiddenMove (0 публичных методов)` | Запрещённые ходы (§II.5.7 / §OG-2), полный канонический список FM-OG-01..08. |
| 125 | константа | `_FORBIDDEN_MOVE_TEXT` | dict, 8 элементов |
| 139 | константа | `RUNTIME_PLACEMENT` | tuple, 4 элементов |
| 144 | константа | `RECOVERY_PROCEDURE` | tuple, 5 элементов |
| 154 | константа | `SELF_REFLECTION_QUESTIONS` | tuple, 7 элементов |
| 166 | класс | `ObservationGateAnswer (0 публичных методов)` | Классификация одного входа по шести вопросам (§II.5.5 / §OG-1). |
| 182 | класс | `GateResult (1 публичных методов)` |  |
| 211 | класс | `ObservationGate (4 публичных методов)` | Observation Gate v0.2 — кора наблюдения (§II.5 / §OG-0..OG-4). |

## operator_registry

- **путь**: `engine/operator_registry.py`
- **размер**: 48 строк, SHA-256 blob `dc87b21aa9e2e87e…`
- **коды состояний** (1): `UNKNOWN`
- **тесты, которые зовут модуль**: 1 — `tests/test_v11_operator_epistemology_divine.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 7 | класс | `OperatorRegistry (4 публичных методов)` | Full operator registry gate for MATH-KERNEL v1.1. |

## output_auditor

- **путь**: `engine/output_auditor.py`
- **размер**: 1190 строк, SHA-256 blob `bd3f9884ea7cfc3b…`
- **что это**: output_auditor.py — аудитор выходного текста AK-MASTER v0.5.1
- **зачем**: После генерации проверяет механически проверяемую часть Блока 10.2 и возвращает ручные пункты проверки автору. Не принимает литературное решение вместо автора
- **коды состояний** (32): `ABSTRACT_EMOTION_WITHOUT_BODY`, `ADVERB_WEAK_VERB`, `ALL_BLOCKS`, `BLOCKED`, `BLOCK_10`, `BLOCK_2`, `BLOCK_2_DOZOIS_ONLY`, `BLOCK_3_2`, `BLOCK_6`, `BLOCK_8_2`, `BLOCK_9`, `CANDIDATE`, `CDV`, `COMPARISON_HEDGE`, `CONTRASTIVE_REFRAME`, `EMPTY_TEXT`, `ERROR`, `FORBIDDEN_OPENING`, `HIGH`, `INFO`, `LOW`, `MEDIUM`, `NEGATION_DEFINITION`, `NEGATION_PARALLELISM`, `NOT_CONFIGURED`, `NOT_ENOUGH_DATA`, `NO_PHYSIOLOGICAL_ANCHOR`, `NO_SIGNAL`, `SATIRE`, `UNKNOWN_CODE`, `UNMARKED_NUMBER`, `WARN`
- **тесты, которые зовут модуль**: 31 — `tests/test_audit_packet_v071.py`, `tests/test_block10_2_twelve_points.py`, `tests/test_block9_decision_tree_wired.py`, `tests/test_block9_print_only_substitution.py`, `tests/test_bol_bolshoi_collision_fix.py`, `tests/test_canon_block_registry.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 28 | константа | `_TW_РИСК_ПОРОГ` |  |
| 33 | константа | `_ПОЛЯ_МЕСТА` | tuple, 5 элементов |
| 37 | константа | `_ЦИТАТА_МАКС` |  |
| 40 | функция | `собрать_находку(item)` | Находка для автора: ЧТО нарушено → ГДЕ дословно → ЧТО делать. |
| 86 | функция | `_достать_место(item)` | Дословный кусок текста из находки, если он в ней есть. |
| 114 | функция | `оценить_риск_tw(text)` | Механическая оценка риска TST-TW из уже существующих детекторов. |
| 165 | константа | `ADVERB_PATTERN` | re.compile('\\b(медленно\|быстро\|тихо\|громко\|резко\|плавно\|внезапно\|неожиданно\|ост |
| 176 | константа | `UNMARKED_NUMBER_PATTERN` | re.compile('\\b\\d[\\d\\s,.]*(?:процент\|%\|млн\|млрд\|тысяч\|метр\|километр\|год\|лет\|ч |
| 181 | константа | `ABSTRACT_WITHOUT_BODY_PATTERNS` | list, 2 элементов |
| 186 | константа | `SCENE_GENERATION_MODES` | set, 3 элементов |
| 187 | константа | `NON_SCENE_MODES` | set, 3 элементов |
| 190 | функция | `_canon_mode_blocks(mode_norm)` | Блоки канона для режима. Единственный источник — `config_loader`. |
| 210 | константа | `_TEST_ENABLING_BLOCKS` | dict, 8 элементов |
| 222 | функция | `_test_applicable(mode_norm, test_code)` | Применим ли конкретный тест Блока 6 в этом режиме. |
| 241 | функция | `_block_applicable(mode_norm, block_id)` | Применим ли блок канона в этом режиме. |
| 269 | класс | `AutoCheck (0 публичных методов)` |  |
| 278 | класс | `AuditResult (0 публичных методов)` |  |
| 311 | функция | `_normal_mode(mode)` |  |
| 316 | класс | `AuditorConfig (1 публичных методов)` |  |
| 378 | функция | `_текст_латиницей(text)` | Текст не на кириллице (например, польская адаптация): русские словари |
| 388 | константа | `_ПРИБОР_НЕ_ЧИТАЕТ` | строка: «Сцена написана не кириллицей, а словари этого детектора — русские. Нул» |
| 393 | класс | `OutputAuditor (2 публичных методов)` |  |

## passport_extractor

- **путь**: `engine/passport_extractor.py`
- **размер**: 300 строк, SHA-256 blob `7d11b3d4782e905c…`
- **что это**: passport_extractor.py — черновик паспорта книги из рукописи (P0-1,
- **зачем**: 2026-07-16). Автор загружает рукопись → движок предлагает ЧЕРНОВИК паспорта (YAML, который уже понимает book_passport.load_passport) → автор правит и утверждает. Снимает главный порог входа: паспорт больше не с нуля руками. Аналог Import Novel у Sudowrite; подтверждён обоими присланными конкурент-исследованиями как сильнейший P0. Что извлекается и с какой уверенностью: - заголовки глав — из структуры (markdown/Word headings сохранены document_intake) — надёжно; - ритм-профиль — переиспользует rhythm_profile.RhythmProfileAuditor…
- **тесты, которые зовут модуль**: 3 — `tests/test_audit_auto_passport.py`, `tests/test_judge_error_is_not_clean_verdict.py`, `tests/test_passport_extractor.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 45 | константа | `_HEADING_RE` | re.compile('(?m)^#{1,3}\\s+(.+?)\\s*$') |
| 46 | константа | `_CAP_WORD_RE` | re.compile('[А-ЯЁ][а-яё]{2,}') |
| 47 | константа | `_SENT_START_RE` | re.compile('(?:^\|[.!?…]\\s+\|[—–]\\s+\|\\n)') |
| 48 | константа | `_WORD_RE` | re.compile('[а-яёА-ЯЁ]{3,}') |
| 53 | константа | `_NAME_STOPWORDS` | set, 86 элементов |
| 70 | константа | `_FUNCTION_LEMMAS` | set, 55 элементов |
| 81 | функция | `_chapter_headings(text)` |  |
| 85 | функция | `_split_by_chapter(text)` | [(заголовок, тело)]; текст до первого заголовка — под '(начало)'. |
| 101 | функция | `_extract_characters(text, top_n)` | Частотные собственные имена — эвристика (заглавная не в начале |
| 134 | функция | `_content_lemma(word)` |  |
| 142 | функция | `_extract_motifs(chapters, max_motifs)` | Сквозные образы: значимые леммы-существительные, встречающиеся в |
| 176 | функция | `_extract_refrains(text, min_len, max_refrains)` | Повторяющиеся целые строки — кандидаты в намеренные рефрены. |
| 185 | функция | `_extract_rhythm(text)` | Ритм-профиль секций — переиспользует rhythm_profile. |
| 201 | функция | `extract_passport(text)` | Рукопись → черновик паспорта (dict под book_passport) + статистика. |
| 233 | функция | `auto_passport_config(text)` | Авто-паспорт прямо из рукописи → config_kwargs для BlindspotConfig |
| 257 | функция | `draft_to_yaml(draft)` | Черновик → YAML-строка, читаемая человеком и load_passport. |

## perception_filters

- **путь**: `engine/perception_filters.py`
- **размер**: 76 строк, SHA-256 blob `8c10080c246a734d…`
- **что это**: perception_filters.py — ЕДИНЫЙ детектор фильтров восприятия (Блок 10.2.1).
- **зачем**: Канон 10.2.1: эмоция/восприятие не называется, а ощущается. «Он увидел…», «Казалось…», «Она поняла…» — фильтр между читателем и событием. Правило жило в двух копиях с разными списками: - `checklist_validator.FILTER_RE` — требовал «он/она» перед глаголом и знал узкий список (нет «заметил», «осознал», «казалось»); - `divine_density_gate.FILTERS` — без местоимения и шире по глаголам, но только мужской род («заметил», не «заметила»). На «Казалось, всё кончено.» checklist давал PASS, divine — фильтр. Одна реализация: точные …
- **тесты, которые зовут модуль**: 3 — `tests/test_block10_2_twelve_points.py`, `tests/test_block12_anchors_not_proof.py`, `tests/test_comparison_hedge.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `PERCEPTION_FILTER_RE` | re.compile('\\b(?:увидел\|увидела\|увидели\|увидев\|услышал\|услышала\|услышали\|услыша |
| 56 | константа | `COMPARISON_HEDGE_RE` | re.compile('\\bкак\\s+будто\\b', re.I \| re.U) |
| 59 | функция | `perception_filter_hits(text)` | Все вхождения слов-фильтров восприятия (в порядке появления). |
| 64 | функция | `has_perception_filter(text)` | Есть ли в тексте фильтр восприятия (10.2.1 нарушен). |
| 69 | функция | `comparison_hedge_hits(text)` | Все вхождения связки сравнения «как будто» (в порядке появления). |
| 74 | функция | `has_comparison_hedge(text)` | Есть ли в тексте связка сравнения «как будто». |

## postflight_bridge

- **путь**: `engine/postflight_bridge.py`
- **размер**: 245 строк, SHA-256 blob `69840d79d39e936d…`
- **что это**: postflight_bridge.py — двенадцать пунктов Блока 10.2 из результатов разбора.
- **зачем**: Канон АК-6.7, БЛОК 10.2 — чеклист ПОСЛЕ генерации, двенадцать пунктов (`discipline/checklist_protocol.yaml`, раздел `block_10_2_postflight`). Правило Блока 10.2 дословно: **непрошедший текст обязан быть ЧЕРНОВИКОМ со списком правок, а не готовой сценой.** ## ЧТО БЫЛО, ПРОВЕРЕНО 30 июля `engine/scene_postflight.py` — строгий страж на двенадцать полей — принимает двенадцать УЖЕ РЕШЁННЫХ «да/нет» от вызывающего и **не читает таблицу канона вообще** (`grep checklist_protocol` в нём: ноль совпадений). Единственный, кто его…
- **коды состояний** (12): `CLEAR`, `ERROR`, `EXPANDED`, `HELD`, `MEDIUM`, `NON_LIQUET`, `NOT_CONFIGURED`, `NOT_FOUND`, `STOP`, `UNKNOWN_CODE`, `VETO`, `WARN`
- **тесты, которые зовут модуль**: 1 — `tests/test_block10_2_twelve_points.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 72 | константа | `СООТВЕТСТВИЕ` | dict, 12 элементов |
| 87 | константа | `_ПРОШЁЛ` | set, 4 элементов |
| 88 | константа | `_НЕ_ПРОШЁЛ` | set, 3 элементов |
| 91 | функция | `_канон()` | Двенадцать пунктов из таблицы канона, по коду пункта. |
| 103 | функция | `_по_каналу(разбор, код_канала)` |  |
| 115 | функция | `_по_результату(результат)` |  |
| 130 | класс | `PostflightBridge (1 публичных методов)` | Двенадцать канонических полей Блока 10.2 из результатов разбора. |

## premise_audit

- **путь**: `engine/premise_audit.py`
- **размер**: 146 строк, SHA-256 blob `cc9b36a205bd5aa3…`
- **что это**: premise_audit.py — аудит предпосылки главного события (Н-16 /
- **зачем**: Модуль 11). Источник: docs/handoffs/КОНСТРУКТ_РЕЕСТР_17_ОШИБОК_модули_7-11.md, Н-16 — класс ОТСУТСТВИЕ, концептуальная. ФЛАГОВЫЙ модуль, последний из пронумерованных 11 в обновлённом пайплайне. Находка (буквально): «Прыжок — средство без пункта назначения; вопрос "куда" не звучал нигде → читалось дырой, было центром.» Решение: «вопрос задан один раз и встречен как неприличие ("Корабль летит туда, откуда он лучше всего виден. Пункт назначения не входил в пакет")» — это ключевой нюанс: вопрос не был отвечен впрямую, но был ЯВНО ЗАДАН …
- **коды состояний** (3): `ANSWERED`, `HOLE`, `REJECTED_BY_WORLD_SHOWN`
- **тесты, которые зовут модуль**: 1 — `tests/test_premise_audit.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 39 | константа | `QuestionKind` |  |
| 41 | константа | `_ALL_QUESTIONS` | tuple, 5 элементов |
| 43 | константа | `_QUESTION_LABELS` | dict, 5 элементов |
| 53 | класс | `QuestionAudit (1 публичных методов)` |  |
| 65 | класс | `PremiseAuditReport (1 публичных методов)` |  |
| 80 | функция | `check_premise(event_id, answers)` | Проверить, что все 5 наивных вопросов о главном событии закрыты. |
| 145 | функция | `list_naive_questions()` |  |

## promise_extractor

- **путь**: `engine/promise_extractor.py`
- **размер**: 103 строк, SHA-256 blob `cd4fb08ffcd083a3…`
- **что это**: promise_extractor.py — automatic narrative-promise extraction from prose.
- **зачем**: Found during competitive research (2 July 2026, author-supplied analysis of Marlowe/AutoCrit Story Analyzer+): commercial tools automatically SCAN a manuscript for foreshadowing setups and check whether they're paid off later in the story. AK-MASTER already had the DOWNSTREAM logic for this (Block 7 stop-rule: 3+ open reader promises by the middle blocks new scenes, in promise_ledger.py, tested and API-wired) — but nothing ever produced the promise LIST automatically. Every existing call site required the author to type …
- **коды состояний** (1): `OPEN`
- **тесты, которые зовут модуль**: 2 — `tests/test_block7_promise_stop_rule.py`, `tests/test_promise_extractor.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 30 | класс | `PromiseExtractor (2 публичных методов)` | Extracts open narrative promises from prose text via LLM judge, then |

## promise_extractor_offline

- **путь**: `engine/promise_extractor_offline.py`
- **размер**: 475 строк, SHA-256 blob `a3e0098b514066f9…`
- **что это**: promise_extractor_offline.py — БЛОК 7 без судьи и без денег.
- **зачем**: В каноне AK-6.8 Блок 7 говорит прямо:
- **тесты, которые зовут модуль**: 2 — `tests/test_mcp101_product.py`, `tests/test_promise_extractor_offline.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 65 | константа | `СЛОВО` | re.compile('\\w+', re.U) |
| 68 | константа | `ИМЯ` | re.compile('\\b[А-ЯЁ][а-яё]{2,}\\b', re.U) |
| 72 | константа | `НЕ_ИМЕНА` | set, 68 элементов |
| 84 | константа | `СРОК` | re.compile('(?:время\|срок\|осталось\|остаётся\|даю\|даём\|у вас есть\|у тебя есть)[^.! |
| 91 | константа | `НАМЕРЕНИЕ` | re.compile('(?:^\|[—«\\"]\\s*)[^.!?\\n]{0,60}?\\bЯ\\s+(?:обещаю\|клянусь\|найду\|вер |
| 97 | константа | `ВОПРОС_РЕПЛИКА` | re.compile('^\\s*[—–][^?\\n]{5,120}\\?\\s*$', re.U) |
| 101 | константа | `ДЕЙСТВУЕТ` | re.compile('{имя}\\s+\\w*(?:л\|ла\|ло\|ли\|лся\|лась\|лись)\\b', re.U) |
| 105 | константа | `ЗВАТЕЛЬНАЯ` | re.compile('(?:,\\s*{имя}\\b\|\\b{имя}\\s*[,!?])', re.U) |
| 117 | константа | `_ПРИЛ` | строка: «(?:[А-ЯЁа-яё]+(?:ом\|ем\|ым\|им\|ой\|ей\|ого\|его\|ому\|ему\|ых\|их\|ыми\|ими\|ая\|яя» |
| 119 | константа | `ПРЕДЛОГ_МЕСТА` | re.compile('\\b(?:в\|во\|на\|из\|из-за\|от\|до\|к\|ко\|по\|под\|над\|за\|у\|около\|возле\|близ\|ч |
| 123 | константа | `_ДОЛЯ_ТОПОНИМА` |  |
| 126 | функция | `нарицательное(имя, весь)` | Пишется ли это слово в книге со строчной буквы. |
| 157 | константа | `_КОНЕЦ` | re.compile('[.!?…:;»\\"—–-]\\s*$\|^\\s*$', re.U) |
| 160 | константа | `ОКОНЧАНИЯ` | tuple, 15 элементов |
| 164 | функция | `не_конец_предложения(до)` |  |
| 168 | функция | `стебель(имя, известные)` | «Восса» → «Восс», если «Восс» в книге тоже есть отдельным словом. |
| 178 | функция | `_формы(имя)` |  |
| 183 | класс | `Кандидат (0 публичных методов)` | Черновик обещания: где заряжено, чем опознано, где последний след. |
| 197 | константа | `_ДОЛЯ_СЛОВОСОЧЕТАНИЯ` |  |
| 200 | константа | `_МИН_ВЫБОРКА_СЛОВОСОЧЕТАНИЯ` |  |
| 203 | функция | `часть_словосочетания(имя, весь)` | Имя это или первое слово устойчивой связки вроде «Восточный округ». |
| 218 | функция | `_счёт(шаблон, имя, весь)` | Сколько раз шаблон с «{имя}» встретился в тексте. |
| 233 | функция | `_главы_как_слова(главы)` |  |
| 237 | функция | `заряженные_линии(главы)` | Персонаж несёт вес и пропадает до конца книги — ружьё не выстрелило. |
| 317 | функция | `названные_сроки(главы)` | Срок назван вслух — значит, книга обязана к нему вернуться. |
| 344 | функция | `заявленные_намерения(главы)` | «Нашёл бы тебя», «Я вернусь», «Обещаю» — обещание в чистом виде. |
| 363 | функция | `вопросы_без_ответа(главы)` | Прямой вопрос, на который в сцене не ответили. |
| 395 | константа | `ЗАГОЛОВОК_RE` | re.compile('^\\s*(#{1,3}\\s+.+\|ПРОЛОГ\|ЭПИЛОГ\|ЧАСТЬ\\s+\\S+\|ГЛАВА\\s+\\S+.*)\\s*$ |
| 399 | функция | `главы_из_текста(текст)` | Книга одной строкой → список (имя главы, текст главы). |
| 429 | константа | `СИГНАЛЫ` | tuple, 4 элементов |
| 433 | класс | `OfflinePromiseExtractor (2 публичных методов)` | Черновик реестра обещаний по прозе, без судьи и без сети. |

## promise_ledger

- **путь**: `engine/promise_ledger.py`
- **размер**: 157 строк, SHA-256 blob `517f1e68b7defe67…`
- **что это**: Promise ledger — AK v6.7 Block 7 stop-rule for open reader promises.
- **зачем**: PromiseLedger — стоп-правило (считает открытые обещания). PromiseRegistry — явная модель данных жизненного цикла обещания/tentpole (setup→payoff), которой не хватало Блоку 7: где заряжено ружьё, выстрелило ли оно, и не осталось ли заряженным до финала. Одна реализация: реестр отдаёт свои обещания стоп-правилу (as_ledger_input), не дублируя подсчёт
- **коды состояний** (13): `ABANDONED`, `ALREADY_PAID`, `BLOCKED`, `HIGH`, `INVALID_PAYOFF`, `MEDIUM`, `NOT_FOUND`, `OPEN`, `PAID`, `PROMISE_PRESSURE_WARNING`, `PROMISE_STOP_RULE_TRIGGERED`, `UNRESOLVED`, `WARN`
- **тесты, которые зовут модуль**: 4 — `tests/test_block7_promise_model.py`, `tests/test_block7_promise_stop_rule.py`, `tests/test_promise_extractor.py`, `tests/test_v161_audit_response.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 17 | класс | `PromiseStatus (0 публичных методов)` |  |
| 24 | класс | `Promise (0 публичных методов)` | Обещание читателю (setup) или структурный tentpole. Явная модель: |
| 36 | класс | `PromiseRegistry (7 публичных методов)` | Явная модель жизненного цикла обещаний/tentpoles (Блок 7). |
| 104 | класс | `PromiseFinding (0 публичных методов)` |  |
| 110 | класс | `PromiseLedger (1 публичных методов)` |  |

## prompt_packet_builder

- **путь**: `engine/prompt_packet_builder.py`
- **размер**: 1197 строк, SHA-256 blob `fb24ebd9d52c2815…`
- **что это**: prompt_packet_builder.py — сборщик промпт-пакета АК
- **зачем**: АК v6.7 Принимает параметры задачи и собирает финальный промпт-пакет: - активные блоки АК под SCN-код и режим - ЭВ из EVSelectorV2 - SYN/EXP-коды - VRP-правила если есть активные вето - Блок 10.1 (чеклист ДО генерации) Принцип: движок не генерирует текст. Он собирает контекст который автор или LLM получает перед генерацией
- **коды состояний** (12): `AUTHOR_INPUT_REQUIRED`, `AUTHOR_REVIEW_REQUIRED`, `BLOCKED`, `DISCIPLINE_CANON_FILE`, `DISCIPLINE_CONTEXT_MAX_CHARS`, `EMPTY`, `NON_LIQUET`, `NOT_FOUND`, `READY`, `SUGGESTED_NEEDS_AUTHOR_CONFIRMATION`, `SUGGESTED_NON_AK_NEEDS_AUTHOR_CONFIRMATION`, `TRACE_PRESENT`
- **тесты, которые зовут модуль**: 30 — `helix_pipeline/tests/test_usage_reaches_the_caller.py`, `tests/test_ak_discipline_cli.py`, `tests/test_ak_discipline_engine.py`, `tests/test_audit_scene_contract.py`, `tests/test_block9_print_only_substitution.py`, `tests/test_canon_citations_wave2.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 29 | константа | `DISCIPLINE_DIR` |  |
| 30 | константа | `DISCIPLINE_SUFFIXES` | set, 5 элементов |
| 31 | константа | `DEFAULT_DISCIPLINE_CONTEXT_MAX_CHARS` |  |
| 34 | функция | `_discipline_context_limit()` |  |
| 47 | функция | `_canon_single_file()` | Имя ОДНОГО файла канона, если аудит должен идти только по нему. |
| 62 | функция | `_read_discipline_context(root, max_chars, only_file)` | Read repository discipline sources for a provider system instruction. |
| 135 | константа | `SCN_BLOCKS` | dict, 15 элементов |
| 162 | константа | `ALL_CANON_BLOCKS` | list, 19 элементов |
| 168 | функция | `_expand_to_full_blocks(scn_specific)` | Merge SCN-specific block list with the full canon block list. |
| 189 | константа | `SCN_VTO_HIERARCHY` | dict, 15 элементов |
| 208 | константа | `MODE_RULES` | dict, 4 элементов |
| 238 | константа | `GEN_TARGET_PAGES_MIN` |  |
| 239 | константа | `GEN_TARGET_PAGES_MAX` |  |
| 240 | константа | `GEN_HARD_MAX_PAGES` |  |
| 241 | константа | `WORDS_PER_PAGE` |  |
| 284 | константа | `TOKENS_PER_WORD_RU` |  |
| 285 | константа | `GENERATION_SAFETY_MARGIN` |  |
| 286 | константа | `GENERATION_MAX_TOKENS_FLOOR` |  |
| 287 | константа | `GENERATION_MAX_TOKENS_CEILING` |  |
| 290 | функция | `pages_to_max_tokens(pages)` | Перевести целевой объём в страницах в max_tokens для запроса к LLM. |
| 304 | функция | `default_target_pages()` | Продуктовый объём по умолчанию, когда автор явно не указал длину — |
| 317 | константа | `TST_DV_TARGET_SCNS` | set, 6 элементов |
| 324 | константа | `OUTPUT_FORMAT_INSTRUCTION` | строка: «Выдай сгенерированный текст в формате Markdown (.md). Реплики — через » |
| 336 | функция | `parse_length_target_pages(length_target)` | Извлекает число страниц из свободной строки length_target, если оно |
| 377 | класс | `Block101 (1 публичных методов)` | Чеклист ДО генерации (Блок 10.1). |
| 463 | класс | `PromptPacket (0 публичных методов)` | Финальный пакет для передачи в LLM или автору. |
| 505 | константа | `_CONTRACT_FIELDS` | tuple, 6 элементов |
| 515 | функция | `_render_scene_contract(contract)` | Отрисовать заявленные автором поля шлюза 10.1 для судьи. |
| 559 | класс | `PromptPacketBuilder (9 публичных методов)` | Сборщик промпт-пакета. |

## protocol_compiler

- **путь**: `engine/protocol_compiler.py`
- **размер**: 89 строк, SHA-256 blob `abfec5bd7a3a817c…`
- **коды состояний** (4): `CYCLE_DETECTED`, `EMPTY`, `NODE_WITHOUT_ID`, `WARN`
- **тесты, которые зовут модуль**: 0 (**прямого теста нет**)
- **откуда достижим**: `api/service.py` (тестов на точку входа — 38) — **это путь в коде, а не тест поведения: сам модуль ни один тест не зовёт**

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 7 | класс | `ProtocolCompiler (1 публичных методов)` | Compile no-code graph payloads into AK YAML protocol drafts. |

## qa_governance_layer

- **путь**: `engine/qa_governance_layer.py`
- **размер**: 233 строк, SHA-256 blob `08d8b176c1e58efb…`
- **что это**: qa_governance_layer.py — PHASE 1 конструкта AK-6.8: QA GOVERNANCE LAYER.
- **зачем**: Источник: `discipline/AK_6_8_MERGED_v1_2_SAFE_FINAL.md`, раздел «PHASE 1 — QA GOVERNANCE LAYER» (§1.1 Duplicate Detection Engine, §1.2 Runtime Integrity Validator, §1.3 Recursive Deadlock Detector). Найдено сверкой конструкта 16.09.2026: не было построено НИЧЕГО. Ни один из пяти кодов Duplicate Detection Engine, ни один из семи кодов Runtime Integrity Validator, ни одна из восьми строк RDL-матрицы (Recursive Deadlock Detector) не встречается нигде в `engine/` (проверено построчным grep по всему дереву до написания этого м…
- **коды состояний** (4): `DUPLICATE_DETECTION_CODES_COUNT`, `RDL_FIELD_MISSING`, `RDL_MATRIX_COUNT`, `RUNTIME_INTEGRITY_CODES_COUNT`
- **тесты, которые зовут модуль**: 1 — `tests/test_qa_governance_layer.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 27 | константа | `_КАНОН` |  |
| 30 | константа | `_НАЧАЛО` | строка: «# PHASE 1 — QA GOVERNANCE LAYER» |
| 31 | константа | `_КОНЕЦ` | строка: «# PHASE 2 — RUNTIME FAILURE ATLAS EXPANDED» |
| 33 | константа | `ИСТОЧНИК` | строка: «AK_6_8_MERGED_v1_2_SAFE_FINAL.md: PHASE 1 — QA GOVERNANCE LAYER, §1.1 » |
| 39 | функция | `_канон()` |  |
| 44 | функция | `_раздел_phase1()` |  |
| 51 | функция | `_подраздел(текст, заголовок, конец)` |  |
| 58 | функция | `_строки_таблицы(текст)` |  |
| 74 | функция | `duplicate_detection_outputs()` | 5 кодов §1.1 — DUPLICATE DETECTION ENGINE. |
| 89 | функция | `runtime_integrity_outputs()` | 7 кодов §1.2 — RUNTIME INTEGRITY VALIDATOR. |
| 102 | класс | `ThresholdRow (1 публичных методов)` |  |
| 112 | функция | `runtime_thresholds()` | Таблица «Thresholds» §1.2. |
| 130 | класс | `DeadlockRow (1 публичных методов)` |  |
| 147 | функция | `recursive_deadlocks()` | 8 строк RECURSIVE DEADLOCK MATRIX (RDL-01..08), §1.3. |
| 167 | функция | `deadlock(id_)` |  |
| 176 | функция | `degradation_rounds()` | 4-раундовая деградация RDL, блок «Degradation logic» §1.3. |
| 187 | функция | `audit()` | Целостность PHASE 1: полнота кодов/таблиц, читаемых из канона. |

## rhythm_auditor

- **путь**: `engine/rhythm_auditor.py`
- **размер**: 525 строк, SHA-256 blob `26fb023b448aef8f…`
- **что это**: rhythm_auditor.py — TST-DA ритм-аудит
- **зачем**: АК v6.7 Блок 6: TST-DA — ТЕСТ ДОЗУА (АРИТМИЯ), Патч 2 Правило: три предложения одинаковой длины подряд ИЛИ две одинаковые грамматические структуры подряд — нарушение. Источник именно этого теста назван каноном поимённо (строки 4196–4204, 12.4.1): «Бегство охотника» (Мартин, Дозуа, Абрахам), верифицировано по первичному тексту. Здесь же живут три SYN-кода Дозуа — SYN-DEP, SYN-FRG, SYN-PHS. ДВА РАЗНЫХ МЕСТА КАНОНА, КОТОРЫЕ ЛЕГКО СПУТАТЬ — и они были спутаны прямо в тексте нарушений этого модуля (исправлено 15.08): * **TST-DA (Блок 6, Дозуа)** — то, что здесь…
- **коды состояний** (11): `DIAGNOSTIC`, `MEDIUM`, `NEUTRAL`, `NOT_RUN`, `NOUN_FIRST`, `PARTICIPLE`, `SHORT_IMPACT`, `SUBJ_VERB`, `TEXT_TOO_SHORT`, `VERB_FIRST`, `WARN`
- **тесты, которые зовут модуль**: 10 — `tests/test_canon_mode_test_applicability.py`, `tests/test_explanation_gate.py`, `tests/test_generate_manifest_excludes_runtime.py`, `tests/test_integration_v05.py`, `tests/test_pause_law_block3.py`, `tests/test_rhythm_auditor.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 54 | константа | `RHYTHM_TOLERANCE_WORDS` |  |
| 57 | константа | `RHYTHM_RUN_THRESHOLD` |  |
| 60 | константа | `STRUCTURE_RUN_THRESHOLD` |  |
| 63 | константа | `MIN_SENTENCE_WORDS` |  |
| 66 | константа | `VERB_STARTS` | re.compile('^(он\|она\|они\|оно\|я\|мы\|вы\|ты\|герой\|нарратор)\\s+\\w+(ил\|ила\|или\|ет\|ут |
| 72 | константа | `STRUCTURE_PATTERNS` | list, 5 элементов |
| 84 | класс | `SentenceMetric (0 публичных методов)` |  |
| 92 | класс | `RhythmViolation (0 публичных методов)` |  |
| 104 | функция | `_split_sentences(text)` | Разбивает текст на предложения по .!? с учётом кавычек и многоточий. |
| 110 | функция | `_word_count(sentence)` |  |
| 139 | константа | `_DIALOGUE_LINE` | re.compile('^\\s*[—–]\\s*\\S', re.U) |
| 151 | константа | `_QUOTE_LINE` | re.compile('^\\s*>\\s?', re.U) |
| 154 | функция | `_segments(text)` | Текст → ритмические отрезки. Разрыв на каждой границе реплики. |
| 190 | функция | `_detect_structure(sentence, wc)` |  |
| 201 | функция | `_metric(index, sentence)` |  |
| 211 | функция | `_similar_length(a, b)` |  |
| 245 | константа | `_ПАРАГРАФ` | re.compile('\\n\\s*\\n') |
| 250 | функция | `_границы(длины)` | Нижняя и верхняя трети распределения длин САМОГО текста. |
| 279 | функция | `_такт(слов, границы)` | Длинное / короткое / среднее — по третям распределения самого текста. |
| 289 | функция | `pause_law(text)` | Сколько раз в тексте выполнена фигура вдох → удар → выдох → тишина. |
| 360 | функция | `_starts_intentional(text, intentional)` |  |
| 365 | класс | `RhythmAuditor (1 публичных методов)` | TST-DA аудитор. |

## rhythm_den_arbuza

- **путь**: `engine/rhythm_den_arbuza.py`
- **размер**: 25 строк, SHA-256 blob `adb2ed04c394a883…`
- **что это**: rhythm_den_arbuza.py — declared rhythm profile for «День Арбуза».
- **зачем**: Editable data (like the scenario / ledger / motif registries). Each entry declares the intended tempo of a phase; the auditor checks the measured rhythm against it, book-relative. Verified against v11.1: all declared registers match measured reality (staccato phases at median 3–4 words, flowing phases at 5–7, book median 4) — the rhythm intent is actually realized in the text
- **тесты, которые зовут модуль**: 1 — `tests/test_rhythm_profile.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 13 | константа | `PROFILE` | list, 8 элементов |

## rhythm_profile

- **путь**: `engine/rhythm_profile.py`
- **размер**: 207 строк, SHA-256 blob `8b793adf061a6084…`
- **что это**: rhythm_profile.py — Module 5 (ear-pass), mechanism 2: phase rhythm.
- **зачем**: Read aloud, a scene has a tempo. A panic scene must run short and clipped; a decompression scene may breathe in long sentences. The failure the ear catches and the eye misses: a phase that is SUPPOSED to be breathless but has drifted into long, flowing sentences (or a calm passage gone staccato). The author stops hearing it after an hour of editing. This is distinct from the existing TST-DA auditor (`rhythm_auditor.py`), which catches LOCAL monotony (three same-length sentences in a row). Here we check the MACRO register of a …
- **коды состояний** (8): `AUDIBLE`, `FLAG`, `FLOWING`, `FLOWING_TOO_FLAT`, `LOUD`, `NEUTRAL`, `STACCATO`, `STACCATO_TOO_LONG`
- **тесты, которые зовут модуль**: 3 — `tests/test_audit_auto_passport.py`, `tests/test_book_passport.py`, `tests/test_rhythm_profile.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `_HEADING_RE` | re.compile('(?m)^(#{1,3})\\s+(.+?)\\s*$') |
| 39 | константа | `_WORD_RE` | re.compile('[а-яёa-z0-9]+', re.I \| re.U) |
| 42 | класс | `Register (0 публичных методов)` |  |
| 49 | класс | `PhaseRhythm (0 публичных методов)` |  |
| 55 | класс | `SectionRhythm (0 публичных методов)` |  |
| 65 | класс | `RhythmFinding (1 публичных методов)` |  |
| 77 | класс | `RhythmReport (1 публичных методов)` |  |
| 90 | функция | `_sentence_lengths(block)` | Sentence-like units: split on .!?… and on line breaks (a dialogue |
| 99 | класс | `RhythmProfileAuditor (2 публичных методов)` |  |

## satire_gate

- **путь**: `engine/satire_gate.py`
- **размер**: 116 строк, SHA-256 blob `8e264d5fba8f9680…`
- **что это**: Satire gate — АК v6.7 Block 8.2.
- **зачем**: Object is never named directly; absurdity is internally logical; final shows consequence, not moral; TST-TW is mandatory
- **коды состояний** (11): `ERROR`, `HIGH`, `MEDIUM`, `NOT_CONFIGURED`, `SATIRE_ABSURD_SYSTEM_NOT_LOGICAL`, `SATIRE_MORALIZING`, `SATIRE_NO_FINAL_CONSEQUENCE`, `SATIRE_TARGET_NAMED_DIRECTLY`, `SATIRE_TST_TW_NOT_CHECKED`, `SATIRE_TST_TW_REQUIRED`, `WARN`
- **тесты, которые зовут модуль**: 4 — `tests/test_block8_special_modes_enforcement.py`, `tests/test_block8_vectors_drive_verdict.py`, `tests/test_satire_target_inflection.py`, `tests/test_tst_tw_detector.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 12 | константа | `SYSTEM_LOGIC_RE` | re.compile('\\b(по инструкции\|по регламенту\|официально\|протокол\|комиссия\|отч[её] |
| 13 | константа | `CONSEQUENCE_RE` | re.compile('\\b(в результате\|поэтому\|после этого\|и теперь\|с тех пор\|итог\|последс |
| 14 | константа | `MORAL_RE` | re.compile('\\b(мораль\|автор хотел сказать\|это плохо\|это хорошо\|следует понять\|н |
| 17 | класс | `SatireFinding (0 публичных методов)` |  |
| 23 | класс | `SatireGate (1 публичных методов)` |  |

## scenario_den_arbuza

- **путь**: `engine/scenario_den_arbuza.py`
- **размер**: 43 строк, SHA-256 blob `ef08b4791b42fc25…`
- **что это**: scenario_den_arbuza.py — beat scenario for «День Арбуза», in AK-68's
- **зачем**: native beat-dict shape ({beat_id, anchor_patterns, owner_chapter}). Chapters 1–4 anchors are verified present in the written v11.1. Chapters 5–7 beats are the event canvas of the chapter-5–7 architecture — event level only. owner_chapter is written loosely ('ГЛАВА 3'); the orchestrator resolves it to the exact chapter heading AK-68 matches on. Editable data
- **тесты, которые зовут модуль**: 1 — `tests/test_scenario_den_arbuza.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 10 | константа | `SCENARIO` | list, 16 элементов |

## scenario_planner

- **путь**: `engine/scenario_planner.py`
- **размер**: 323 строк, SHA-256 blob `e3c8d05e4d80a4f0…`
- **что это**: scenario_planner.py — генератор СЦЕНАРНОГО ПЛАНА (недостающее первое звено).
- **зачем**: покрытия СЦЕНАРНЫЙ ПЛАН → ТЕКСТ» и принимает `scenario.md` (план по главам, каждый бит с id) как ВХОД, который автор пишет РУКАМИ. То есть конструкт умел проверить, что написанный текст соответствует плану, но не умел план
- **коды состояний** (1): `PARTIAL`
- **тесты, которые зовут модуль**: 3 — `tests/test_book_pipeline_api.py`, `tests/test_book_runner.py`, `tests/test_scenario_planner.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 61 | константа | `MIN_ANCHORS` |  |
| 62 | константа | `MAX_ANCHORS` |  |
| 64 | константа | `MIN_INTENSITY` |  |
| 65 | константа | `MAX_INTENSITY` |  |
| 68 | константа | `EVENT_ROLES` | tuple, 3 элементов |
| 71 | класс | `ScenarioPlanError (0 публичных методов)` | План нарушает контракт beat_coverage. Не чинится подстановкой (P0-6). |
| 76 | класс | `ScenarioPlan (2 публичных методов)` | Сценарный план в контракте `check_beat_coverage()`. |
| 102 | константа | `_ITEM_SCHEMA_HINT` | строка: «{"beat_id": "B-01 — короткий уникальный код", "chapter": "идентификато» |
| 113 | функция | `_build_instruction()` | Инструкция экстрактору. Текст источника подставляется отдельно |
| 144 | функция | `_validate_beat(raw)` | Один бит: контракт проверяется жёстко, ничего не достраивается. |
| 203 | функция | `validate_plan(beats, events)` | Проверить биты и события против контракта. Возвращает |
| 265 | функция | `build_scenario_plan()` | Исследование или бриф -> сценарный план в контракте beat_coverage. |

## scene_postflight

- **путь**: `engine/scene_postflight.py`
- **размер**: 230 строк, SHA-256 blob `8af44070ef42dba2…`
- **что это**: scene_postflight.py — M17 / БЛОК 10.2 Scene Postflight Gate.
- **зачем**: Source-locked to: AK_MASTER_LIT_FULL_STANDARD_v0_3_0_ABSOLUTE_CONSTRUCT_CANON_LOCK.md Sections: §M17, §10.2. Canon rule (§M17): Postflight применяется после генерации или правки сцены. Цель: не дать сцене пройти дальше только потому, что она звучит красиво. 12 required fields (§M17 / §10.2): FIELD_1 SCN исполнен? FIELD_2 SYN не съехал? FIELD_3 ЭВ прожита телесно, а не названа? FIELD_4 POV не нарушен? FIELD_5 Цена героя оплачена? FIELD_6 Два прочтения A/B живы? FIELD_7 VTO прошёл? FIELD_8 TST прошёл? FIELD_9 SOUL Layer не нарушен? FIE…
- **коды состояний** (2): `POSTFLIGHT_FAIL`, `POSTFLIGHT_PASS`
- **тесты, которые зовут модуль**: 2 — `tests/test_block10_2_twelve_points.py`, `tests/test_scene_postflight.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 54 | константа | `FIELD_LABELS` | dict, 12 элементов |
| 70 | константа | `FIELD_ANNOTATIONS` | dict, 12 элементов |
| 88 | константа | `REPAIR_GUIDANCE` | dict, 12 элементов |
| 109 | класс | `PostflightFieldResult (0 публичных методов)` |  |
| 118 | класс | `PostflightResult (1 публичных методов)` |  |
| 155 | класс | `ScenePostflightGuard (1 публичных методов)` | M17 / БЛОК 10.2 — Scene Postflight Gate. |

## scene_preflight

- **путь**: `engine/scene_preflight.py`
- **размер**: 401 строк, SHA-256 blob `c2481723cb61f6b5…`
- **что это**: scene_preflight.py — M1 / БЛОК 10.1 Scene Preflight Gate.
- **зачем**: Source-locked to: AK_MASTER_LIT_FULL_STANDARD_v0_3_0_ABSOLUTE_CONSTRUCT_CANON_LOCK.md Sections: §7 M1, §10.1, §10.1.0 (main admission algorithm), §10.1.11 (blocked return). Canon rule (§10.1, verbatim): СТОП. Генерация не начинается без закрытия всех полей. 11 required fields — почему 11, а не 10 --------------------------------------- Карта блоков полного канона (PART V, строка 3805) перечисляет Блок 10 как «ДО (11 полей) / ПОСЛЕ (12 пунктов) … + TST-KIN + TST-EV [6.6]», а gap-анализ PART I (строка 743) фиксирует правило разрешения спо…
- **коды состояний** (10): `CLOSED`, `CONFLICT`, `EMPTY`, `NON_LIQUET`, `NOT_APPLICABLE`, `POV`, `PREFLIGHT_PASS`, `SCENE_PREFLIGHT_INCOMPLETE`, `STOP_PREGEN`, `WEAK`
- **тесты, которые зовут модуль**: 11 — `tests/test_book_chapter_endpoint.py`, `tests/test_book_pipeline_api.py`, `tests/test_canon_gate_can_actually_be_closed.py`, `tests/test_canon_membership_gate.py`, `tests/test_canon_verdict_reaches_the_screen.py`, `tests/test_generation_goes_through_canon_gate.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 85 | класс | `FieldStatus (1 публичных методов)` |  |
| 97 | константа | `NOT_APPLICABLE` | строка: «NOT_APPLICABLE» |
| 100 | константа | `PREFLIGHT_FIELD_COUNT` |  |
| 103 | константа | `FIELD_LABELS` | dict, 11 элементов |
| 119 | константа | `FIELDS_THAT_REQUIRE_SCR_WHEN_HORROR` | set, 1 элементов |
| 120 | константа | `FIELDS_THAT_REQUIRE_KINESICS_WHEN_DIALOGUE` | set, 1 элементов |
| 124 | класс | `FieldResult (0 публичных методов)` |  |
| 133 | класс | `PreflightResult (1 публичных методов)` |  |
| 172 | функция | `_field_dict(f)` |  |
| 192 | константа | `_AUTHOR_QUESTIONS` | dict, 11 элементов |
| 239 | константа | `_CANON_NON_LIQUET_OPTIONS` | dict, 2 элементов |
| 251 | константа | `_FIELD_UNKNOWN` | dict, 11 элементов |
| 265 | константа | `_WHY_NOT_AUTO` | строка: «Конфликт относится к смыслу, канону, архиву или финальному прочтению. » |
| 271 | функция | `_non_liquet_for_field(f)` | Полный блок возврата по канону для поля со статусом NON_LIQUET. |
| 290 | класс | `ScenePreflightGuard (1 публичных методов)` | M1 / БЛОК 10.1 — Scene Preflight Gate. |

## scene_type_router

- **путь**: `engine/scene_type_router.py`
- **размер**: 172 строк, SHA-256 blob `1601a77d6afd5d4d…`
- **что это**: scene_type_router.py — тип сцены, названный СЛОВАМИ, доезжает до канона.
- **зачем**: `frontend/src/components/GenerateFlow.jsx:10` предлагает автору выбрать тип сцены из семи подписей: «Диалог», «Действие», «Описание места», «Напряжение / саспенс», «Воспоминание», «Кульминация», «Спокойная сцена». Выбранное уходит на сервер полем `scene_type` и попадает в `PromptPacketBuilder.suggest_syn_for_scene`, который умеет читать ТОЛЬКО код вида «SCN-15» (или «SCN 15», «scn_15» — сепаратор ему не важен).
- **коды состояний** (3): `ALREADY_SCN`, `NOT_ROUTED`, `ROUTED`
- **тесты, которые зовут модуль**: 2 — `tests/test_mcp101_product.py`, `tests/test_scene_type_router.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 70 | константа | `КОД_SCN` | re.compile('\\s*SCN[\\s_-]*(\\d{1,2})\\s*$', re.I) |
| 85 | константа | `МАРШРУТ` | tuple, 15 элементов |
| 128 | функция | `нормализовать_код(значение)` | «SCN 15» / «scn_15» / «SCN-15» → «SCN-15». Иначе пустая строка. |
| 134 | функция | `определить_scn(тип_сцены, описание)` | Свести названный словами тип сцены к коду Блока 4. |

## scn_expander

- **путь**: `engine/scn_expander.py`
- **размер**: 30 строк, SHA-256 blob `ff510213f08bcaef…`
- **коды состояний** (4): `EXPANDED`, `NON_LIQUET`, `NOT_FOUND`, `SCN`
- **тесты, которые зовут модуль**: 5 — `tests/test_ak_discipline_engine.py`, `tests/test_block10_2_twelve_points.py`, `tests/test_canon_membership_gate.py`, `tests/test_scene_type_router.py`, `tests/test_scn_syn_code_extraction.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 5 | класс | `SCNExpander (1 публичных методов)` |  |

## scr_horror_gate

- **путь**: `engine/scr_horror_gate.py`
- **размер**: 196 строк, SHA-256 blob `3203020720cdb2a6…`
- **что это**: scr_horror_gate.py — Block 8 horror compass gate.
- **зачем**: Source-locked to AK v6.7 Reference Block 8.1: SCR-T, SCR-H1, SCR-H1b, SCR-H2, SCR-R. This gate checks whether the requested horror vector has its required mechanism and syntactic/physical signature. It does not generate prose
- **коды состояний** (18): `H1B`, `HIGH`, `LOW`, `MEDIUM`, `SCR`, `SCR_H1B_NO_DIALOGUE`, `SCR_H1B_NO_NONVIOLENT_COMEDY`, `SCR_H1B_NO_SUPERNATURAL`, `SCR_H1_NO_ATTRACTION`, `SCR_H1_NO_FLESH`, `SCR_H2_NO_ACADEMIC_TONE`, `SCR_H2_NO_MEANINGLESSNESS`, `SCR_R_NO_BODY_BETRAYAL`, `SCR_T_NO_DOCUMENT_COLD`, `SCR_T_NO_PREDETERMINATION`, `SCR_UNKNOWN_VECTOR`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 10 — `tests/test_block8_fear_compass_wired.py`, `tests/test_block8_special_modes_enforcement.py`, `tests/test_block8_vectors_drive_verdict.py`, `tests/test_dictionary_collision_fixes.py`, `tests/test_frequency_corpus_collisions.py`, `tests/test_lemma_migration_scr_horror.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 16 | константа | `VECTORS` | set, 5 элементов |
| 17 | константа | `PREDETERMINATION_RE` | re.compile('\\b(предопредел\|приговор\|неизбеж\|уже\\s+случил\|читатель\\s+знает\|гер |
| 28 | константа | `DOCUMENT_COLD_RE` | re.compile('\\b(протокол\|отч[её]т\|запис\|документ\|медицинск\|нейтральн\|холодн\|реги |
| 29 | константа | `DOCUMENT_COLD_LEMMAS` | set, 1 элементов |
| 30 | константа | `FLESH_RE` | re.compile('\\b(плоть\|кож\|мышц\|сухожил\|кость\|анатом\|рана\|зуб\|горло\|эрос\|наслажд\| |
| 31 | константа | `FLESH_LEMMAS` | set, 13 элементов |
| 37 | константа | `ATTRACTION_RE` | re.compile('\\b(притяг\|манил\|тянул\|желан\|красив\|эрос\|откровен\|не\\s+мог\\s+отвес |
| 38 | константа | `MEANINGLESS_RE` | re.compile('\\b(бессмыслен\|солипс\|пустот\|ничто\|никого\\s+нет\|никогда\\s+не\\s+бы |
| 39 | константа | `ACADEMIC_TONE_RE` | re.compile('\\b(следовательно\|таким\\s+образом\|гипотез\|концепц\|доктрин\|структур\| |
| 40 | константа | `DIALOGUE_RE` | re.compile('[«\\"—].{2,120}[»\\"]\|\\b(сказал\|спросил\|ответил\|прошептал\|реплик\|ди |
| 41 | константа | `NO_VIOLENCE_RE` | re.compile('\\b(без\\s+насили\|никто\\s+не\\s+кричал\|не\\s+ударил\|не\\s+кровоточ\| |
| 42 | константа | `SUPERNATURAL_RE` | re.compile('\\b(сверхъестеств\|призрак\|монстр\|невозможн\|аномал\|магическ\|демон\|неч |
| 43 | константа | `REVULSION_RE` | re.compile('\\b(тошнот\|рвот\|желч\|гнил\|слиз\|липк\|тело\\s+преда\|физиолог\|кишк\|спаз |
| 44 | константа | `REVULSION_LEMMAS` | set, 9 элементов |
| 47 | функция | `_document_cold_hit(text)` |  |
| 51 | функция | `_flesh_hit(text)` |  |
| 55 | функция | `_revulsion_hit(text)` |  |
| 59 | класс | `HorrorFlag (0 публичных методов)` |  |
| 66 | функция | `_norm_vector(v)` |  |
| 75 | класс | `SCRHorrorGate (2 публичных методов)` |  |

## scr_trauma_gate

- **путь**: `engine/scr_trauma_gate.py`
- **размер**: 97 строк, SHA-256 blob `2d368ea311194f01…`
- **что это**: scr_trauma_gate.py — SCR-T trauma/silence guard.
- **зачем**: Small Block 8 guard: trauma context should activate slow work, authorial silence and body-first description rather than forced explanation. v1.4 narrows trauma activation to reduce false positives in medical/professional contexts
- **коды состояний** (9): `BLOCKED`, `HIGH`, `MEDIUM`, `NORMAL`, `SCR_T_AUTHOR_SILENCE_BREACH`, `SCR_T_FORCED_TRAUMA_EXPLANATION`, `SCR_T_NO_BODY_SILENCE_MARKER`, `SLOW_WORK`, `WARN`
- **тесты, которые зовут модуль**: 9 — `tests/test_block8_vectors_drive_verdict.py`, `tests/test_dictionary_collision_fixes.py`, `tests/test_frequency_corpus_collisions.py`, `tests/test_lemma_migration_mrl_ev_auditor_trauma.py`, `tests/test_negation_utils_wave2.py`, `tests/test_v13_lawz_dr_shadow_scr.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 15 | константа | `TRAUMA_RE` | re.compile('\\b(травм(?!атолог)\|насили\|паник\|потер(?!\\s+веса)\|смерт\|похорон\|сты |
| 19 | константа | `PSYCH_RE` | re.compile('\\b(псих\|памят\|стыд\|вина\|паник\|кошмар\|флешбек\|диссоциац\|молч\|чувств\| |
| 20 | константа | `PSYCH_LEMMAS` | set, 3 элементов |
| 21 | константа | `NEUTRAL_MEDICAL_RE` | re.compile('\\b(травматолог\|ортопед\|реабилитац\|спортивн\\w*\\s+травм\|потер\\w*\\ |
| 22 | константа | `FORCED_EXPLAIN_RE` | re.compile('\\b(объясни\\w*\|надо\\s+объяснить\|сделай\\s+понятн\|пусть\\s+расскаже |
| 23 | константа | `BODY_SILENCE_RE` | re.compile('\\b(молч\|пауза\|рук(?!овод\|ав)\|пальц\|горло\|дых\|кожа\|зуб\|плеч\|взгляд\|т |
| 24 | константа | `BODY_SILENCE_LEMMAS` | set, 4 элементов |
| 27 | класс | `TraumaFlag (0 публичных методов)` |  |
| 33 | класс | `SCRTraumaGate (1 публичных методов)` |  |

## seminar_dialogue_gate

- **путь**: `engine/seminar_dialogue_gate.py`
- **размер**: 206 строк, SHA-256 blob `a4952b6698730aa9…`
- **что это**: seminar_dialogue_gate.py — диалог-семинар: доклад с репликами-подсказками.
- **зачем**: ## ОТКУДА ПРАВИЛО Критический разбор рукописи «Игла» назвал шесть слабых мест. Пять уровня предложения — их ловят существующие проверки. Шестое устроено иначе: **сцена целиком построена как доклад**. Один персонаж излагает, остальные подают короткие удобные реплики, которые не возражают, а просят продолжать: — Наша единственная защита — не поддаваться классификации. — Как не поддаваться классификации? — Делать то, чего он не ожидает. — У него база данных тысяч цивилизаций. — Да. Но не все. ## ГДЕ ЭТО В КАНОНЕ * **Блок 1…
- **коды состояний** (6): `NOT_CONFIGURED`, `NOT_RUN`, `NOUN`, `SKIPPED`, `TOO_FEW_TURNS`, `YES`
- **тесты, которые зовут модуль**: 2 — `tests/test_seminar_dialogue_gate.py`, `tests/test_судья_называет_обрезку_текста.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 73 | константа | `ИСТОЧНИК` | строка: «AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md: Блок 12.5 шаг 1 (строка 1495» |
| 77 | константа | `ПРАВИЛО` | строка: «Слово рождается из онтологического разрыва (Блок 12.5, шаг 1); голоса » |
| 81 | константа | `ВОПРОС` | строка: «Это разговор людей, у каждого из которых своя воля, или доклад одного » |
| 93 | константа | `МИН_РЕПЛИК` |  |
| 96 | функция | `_слова(текст)` |  |
| 100 | функция | `_существительные(текст)` | Леммы существительных — через общий морфоразбор движка. |
| 108 | функция | `measure(text)` | Контекст для судьи: сколько реплик, как распределены длины, что эхом. |
| 162 | функция | `audit(text)` | Доклад с подсказками или разговор. Решает судья, не форма. |

## sensory_channels

- **путь**: `engine/sensory_channels.py`
- **размер**: 69 строк, SHA-256 blob `c6bf2560780a5ef2…`
- **что это**: sensory_channels.py — ЕДИНЫЙ счётчик сенсорных каналов (Блок 10.2.3).
- **зачем**: Канон 10.2.3: в сценическом абзаце минимум 2 сенсорных канала. Правило жило в двух копиях — `checklist_validator.SENSORY` (regex, маппинг <2 → FAIL) и `output_auditor.SENSORY_PATTERNS` (+леммы, маппинг 1 → WARN, 0 → FAIL). Они разошлись И по словарю (output новее: лемма-защита от «звонил», «распахнул», «пульсар» и т.п.), И по градации: на «Он смотрел на серую стену» (1 канал) checklist давал FAIL, output — WARN. Одна реализация: лемма-защищённый словарь (лучшая версия) + единая градация числа каналов в статус. Обе точки деле…
- **коды состояний** (1): `WARN`
- **тесты, которые зовут модуль**: 1 — `tests/test_gesture_monotony.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 21 | константа | `SENSORY_PATTERNS` | dict, 5 элементов |
| 29 | константа | `_SENSORY_LEMMAS` | dict, 3 элементов |
| 41 | константа | `_SENSORY_PAIN_LEMMAS` | set, 3 элементов |
| 44 | функция | `sensory_channel_map(text)` | Словарь {канал: активен ли} — форма для output_auditor._check_sensory. |
| 57 | функция | `active_sensory_channels(text)` | Список активных сенсорных каналов в тексте. |
| 62 | функция | `sensory_status(text)` | Единая градация 10.2.3: >=2 → PASS, ==1 → WARN, 0 → FAIL. |

## session_planner

- **путь**: `engine/session_planner.py`
- **размер**: 32 строк, SHA-256 blob `ad7f3f5bf6730213…`
- **тесты, которые зовут модуль**: 1 — `tests/test_ak_discipline_engine.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 7 | класс | `SessionPlan (0 публичных методов)` |  |
| 14 | класс | `SessionPlanner (1 публичных методов)` |  |

## severity

- **путь**: `engine/severity.py`
- **размер**: 74 строк, SHA-256 blob `26176b857a03c11d…`
- **что это**: severity.py — calibration of how serious a finding is.
- **зачем**: The naive rule «any finding blocks» is useless on real manuscripts: a live author has dozens of minor issues, and «one slipped attribution → BLOCK the whole novel» helps no one. The verdict must come from the DISTRIBUTION of severities, not from the mere presence of findings. Quantity of minor issues never escalates to a block; only genuinely destructive findings do. Four levels: CRITICAL — real, irreversible damage. Only this blocks. Practically: lost text (a chapter's head/tail gone, a large unexplained deletion, a missing inviolable lan…
- **коды состояний** (5): `ADVISORY`, `BLOCK`, `REVIEW`, `SEAM_LONG_LINE`, `SEAM_SLIPPED_ATTRIBUTION`
- **тесты, которые зовут модуль**: 51 — `helix_pipeline/tests/test_additive_confidence_score.py`, `helix_pipeline/tests/test_business_rules_prefilter.py`, `helix_pipeline/tests/test_governance_math.py`, `helix_pipeline/tests/test_governance_service.py`, `helix_pipeline/tests/test_governance_v14.py`, `helix_pipeline/tests/test_ifm_patch42.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 27 | класс | `Severity (0 публичных методов)` |  |
| 38 | константа | `SEAM_CODE_SEVERITY` | dict, 2 элементов |
| 45 | константа | `INTEGRITY_CRITICAL_DELTA_PCT` |  |
| 46 | константа | `INTEGRITY_MAJOR_DELTA_PCT` |  |
| 49 | константа | `BEAT_MISSING_SEVERITY` |  |
| 55 | константа | `WORLD_VIOLATION_SEVERITY` |  |
| 58 | константа | `FLAG_SEVERITY` |  |
| 61 | константа | `_VERDICT` | dict, 4 элементов |
| 69 | функция | `verdict_for(worst)` |  |
| 73 | функция | `worst_of(severities)` |  |

## show_vs_tell_detector

- **путь**: `engine/show_vs_tell_detector.py`
- **размер**: 282 строк, SHA-256 blob `d7f0438591a1064c…`
- **что это**: show_vs_tell_detector.py — показ против рассказа: абстракция как действующее лицо.
- **зачем**: ━━━ ОТКУДА ВЗЯЛСЯ ИМЕННО ЭТОТ СИГНАЛ ━━━ Наблюдение автора по «Dzień Arbuza»: «„Войны“ как события нет — она рассказана: показано, как Телесеть и ФАТ „воевали“ между собой». Я прочитал это место и увидел, что различие держится не на глаголах и не на времени, а на одном: p2768 — **показ.** Мальчик, метро по сигналу, семьи с водой, зима без света длиной в коридор, плиты, которые вбивали в шлюзы молотком, спасатели, которых ждали с орбиты и не дождались. p2769 — **рассказ.** «Wojowały węzły» — воевали узлы. Действу…
- **коды состояний** (4): `FAT`, `MIXED`, `SHOWN`, `TOLD_BY_ABSTRACTION`
- **тесты, которые зовут модуль**: 1 — `tests/test_show_vs_tell_detector.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 52 | константа | `SHOW_TELL_PROFILES` | dict, 2 элементов |
| 105 | константа | `Verdict` |  |
| 107 | константа | `WHAT_THIS_MEASURES` | строка: «Соотношение в окне абзацев: сколько раз действует абстракция и сколько» |
| 114 | константа | `TELLING_IS_NOT_A_DEFECT` | строка: «Рассказ не дефект. Двадцать лет брака нельзя показать сценой, и абзац » |
| 123 | константа | `DEFAULT_WINDOW` |  |
| 127 | класс | `WindowReading (1 публичных методов)` |  |
| 140 | функция | `_compiled(profile)` |  |
| 144 | функция | `_abstraction_acts(para, actors, deeds)` | Абстракции, действующие в ОДНОМ предложении с глаголом действия. |
| 161 | функция | `scan_show_vs_tell(text, lang)` | Пройти текст окнами и назвать те, где действуют абстракции без тел. |
| 214 | функция | `read_passage(text, first, last, lang)` | Разобрать один названный отрывок по абзацам, а не окнами. |
| 255 | функция | `scene_density(text, first, last, lang)` | Плотность сцены в отрывке: тела, реплики, ощущения на абзац. |

## soul_layer

- **путь**: `engine/soul_layer.py`
- **размер**: 399 строк, SHA-256 blob `31801466563aebcd…`
- **что это**: soul_layer.py — Soul Layer runtime guards for MR_HELIX × AK-MASTER.
- **зачем**: The Soul Layer is not mysticism and not SaaS packaging. It is a runtime resistance layer: anti-product, authorial silence, useless beauty, slow work, and anti-false-closure. Source-locked additions (2026-07-30, враждебная сверка с AK_MASTER_LIT_FULL_STANDARD_v0_3_0_ABSOLUTE_CONSTRUCT_CANON_LOCK.md §III): SoulLayerGuard/soul_gate above cover §III.2 (APL-1/2 → ANTI_PRODUCT_RISK) и §III.5 (Author's Silence → SILENCE_BREACH) и часть §III.4/§III.7 (FALSE_CLOSURE). Найдено при сверке: канон §III.3 (Slow Work Mode — точный триггер и …
- **коды состояний** (30): `AI_PREFERENCE_ONLY`, `ALLOWED`, `BEAUTIFUL_BUT_INERT`, `BLOCKED`, `CHARACTER_REVEALING`, `COMPRESSION_OK`, `COMPRESSION_TOO_CLEAN`, `CRITICAL`, `EXPLAINS_OBVIOUS`, `F10`, `HIGH`, `IRONY_AWE`, `KEEP`, `LOW`, `MEDIUM`, `REMOVE`, `REPEATS_SAID`, `RHYTHMIC`, `SOMATIC`, `SOUL_ANTI_PRODUCT_RISK`, `SOUL_AUTHOR_SILENCE_BREACH`, `SOUL_FALSE_CLOSURE_RISK`, `SOUL_LAYER`, `SOUL_OVEREXPLANATION_RISK`, `SOUL_SLOW_WORK_RECOMMENDED`, `SOUL_USELESS_BEAUTY_ATTACK`, `SYMBOLIC`, `UNRELATED_TO_CRITERIA`, `WARN`, `WORLD_PRESSURE`
- **тесты, которые зовут модуль**: 4 — `tests/test_soul_gate_contract.py`, `tests/test_soul_layer_canon_extensions.py`, `tests/test_soul_layer_canon_triggers.py`, `tests/test_v10_kernel_soul_kin_icoi.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 29 | класс | `SoulFinding (0 публичных методов)` |  |
| 50 | константа | `PRODUCT_PATTERN` | re.compile('тренд\|рынок\|продаж\|продаваем\|монетиз\|конверс\|удержан\|аудитор\|упрост\| |
| 63 | константа | `SILENCE_VIOLATION_PATTERN` | re.compile('объясни\\s+вс[её]\|имел\\s+в\\s+виду\|раскрой\\s+внутренн\|допиши\\s+мо |
| 78 | константа | `FALSE_CLOSURE_PATTERN` | re.compile('окончательн\|однозначн\|на\\s+самом\\s+деле\|вс[её]\\s+оказалось\|разреш |
| 86 | константа | `USELESS_BEAUTY_ATTACK_PATTERN` | re.compile('убери\\s+(?:все\\s+)?(?:лишние\|бесполезные)\\s+детал\|сократи\\s+атмо |
| 87 | константа | `SPEED_PRESSURE_PATTERN` | re.compile('быстро\|немедленно\|без\\s+паузы\|сразу\\s+выдай\|ускорь', re.I \| re.U) |
| 89 | класс | `SoulLayerGuard (1 публичных методов)` |  |
| 184 | функция | `soul_gate(instruction)` | Поле контракта находки `soul_gate` (SUPPLEMENT §3). |
| 229 | класс | `LivingExcessCriterion (0 публичных методов)` |  |
| 238 | класс | `RemovalReason (0 публичных методов)` |  |
| 246 | функция | `living_excess_test(criteria_matched, removal_reasons)` | §III.4 — деталь сохраняется, если отвечает ХОТЯ БЫ ОДНОМУ критерию; |
| 268 | функция | `useless_beauty_exclusion(mode, excess_test_result)` | True — элемент исключить из нормализации ОГРАНКИ (VTO-D). |
| 282 | константа | `SLOW_WORK_TRIGGER_SCN` | frozenset({'SCN-08', 'SCN-12', 'SCN-15'}) |
| 283 | константа | `SLOW_WORK_HEAVY_CORES` | frozenset({'ЭВ-СКОРБЬ', 'ЭВ-СТРАХ'}) |
| 284 | константа | `SLOW_WORK_MIN_INTENSITY` |  |
| 286 | константа | `SLOW_WORK_PROCEDURE` | tuple, 4 элементов |
| 297 | функция | `slow_work_required(scn_code)` | §III.3 — точный канон-триггер Slow Work Mode (все три условия сразу). |
| 309 | функция | `slow_work_procedure()` |  |
| 317 | константа | `AUTHORIAL_WOUND_RESPONSE` | строка: «Этот элемент структурно неэффективен. Но я не могу его удалить без реш» |
| 321 | константа | `AUTHORIAL_WOUND_MARKER` | строка: «[AUTHORIAL WOUND — AUTHOR REVIEW REQUIRED]» |
| 324 | функция | `authorial_wound_check(is_strong_strange_detail)` | §III.6 — перед удалением сильной странной детали: «это слабость текста |
| 341 | константа | `COMPRESSION_TOO_CLEAN_REMEDIATION` | tuple, 4 элементов |
| 349 | функция | `compression_audit()` | §III.7 — обязательный аудит ПОСЛЕ каждого сжатия. `too_clean` — решение |
| 373 | константа | `FAILURE_MODES` | dict, 10 элементов |
| 397 | функция | `failure_mode(code)` | §III.8 — справка по коду отказа Soul Layer (F1..F10), либо None. |

## source_trace

- **путь**: `engine/source_trace.py`
- **размер**: 41 строк, SHA-256 blob `95fea53abf4b424b…`
- **коды состояний** (4): `NON_LIQUET`, `NO_FACT_CLAIM`, `TRACE_PRESENT`, `UNVERIFIED`
- **тесты, которые зовут модуль**: 3 — `tests/test_block0_behavioral_enforcement.py`, `tests/test_citation_verification_12_2.py`, `tests/test_mcp101_product.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 8 | класс | `SourceClaim (0 публичных методов)` |  |
| 16 | класс | `SourceTraceManager (2 публичных методов)` | Keeps factual claims separate from literary force. |

## speaker_trackability

- **путь**: `engine/speaker_trackability.py`
- **размер**: 224 строк, SHA-256 blob `9b066950e674d0a3…`
- **что это**: speaker_trackability.py — Module 2 (Denis, Case 2), speaker-tracking view:
- **зачем**: can the listener always tell WHO is speaking? Read aloud, a run of dialogue with no attribution stays trackable only when the scene has two voices — the ear follows the alternation. The moment a third voice is in the room, an unattributed run becomes a fog: after two lines you no longer know which of three people is talking. This is an auditory failure the eye skims past. Calibration came from the real novel. The longest unattributed run in «День Арбуза» is 12 lines — but it is Карский ↔ Ежи ping-pong opening with «Карс…
- **коды состояний** (4): `AUDIBLE`, `FLAG`, `LOUD`, `UNTRACKABLE_RUN`
- **тесты, которые зовут модуль**: 2 — `tests/test_speaker_trackability.py`, `tests/test_speaker_trackability_говорит.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 31 | константа | `_HEADING_RE` | re.compile('^#{1,3}\\s') |
| 32 | константа | `_REPLICA_RE` | re.compile('^\\s*[—–]\\s') |
| 35 | константа | `_VERBS` | строка: «сказал\|спросил\|ответил\|прошептал\|крикнул\|произн[её]с\|подтвердил\|возраз» |
| 53 | константа | `_SPEECH_VERB_RE` | re.compile(f'(?:{_VERBS})\\w*', re.U) |
| 56 | константа | `_VERB_NAME_RE` | re.compile(f'(?:{_VERBS})\\w*\\s+([А-ЯЁ][а-яё]+)', re.U) |
| 58 | константа | `_NAME_VERB_RE` | re.compile(f'([А-ЯЁ][а-яё]+)\\s+(?:\\w+\\s+){{0,2}}?(?:{_VERBS})\\w*', re.U) |
| 66 | константа | `_NOT_NAMES` | set, 65 элементов |
| 82 | функция | `_is_name(token)` |  |
| 87 | класс | `SpeakerFinding (1 публичных методов)` |  |
| 101 | класс | `SpeakerReport (1 публичных методов)` |  |
| 110 | класс | `SpeakerTrackabilityAuditor (1 публичных методов)` | Participant-aware speaker-trackability auditor. |

## specificity_algebra

- **путь**: `engine/specificity_algebra.py`
- **размер**: 223 строк, SHA-256 blob `919cf1572df5738c…`
- **что это**: specificity_algebra.py — RQ2 SPECIFICITY ALGEBRA (AXIOM DRIFT).
- **зачем**: Отвечает на вопрос, который движок раньше отдавал наружу (LLM/автору): временной маркер «шестой день / 22:11 / будто тысячу лет назад» — это ДАТА (несущая, на неё можно опереть таймлайн) или ЖЕСТ (травма/гипербола, держать слабо)? Классификация детерминированная, без LLM — иначе движок сам вносит тихое искажение, заякорив ledger на «тысяче лет». Связь с world_ledger.TemporalLedger: тот — реестр, он хранит уже классифицированное `environment`. Design-note world_ledger (стр. 48-53) явно отдавал классификацию «семантике вызывающей ст…
- **тесты, которые зовут модуль**: 1 — `tests/test_specificity_algebra_rq2.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 50 | константа | `_MAGNITUDE` | строка: «(?:тысяч\|тысячу\|тысяча\|миллион\|миллиард\|сотн\|сто\b\|вечност)» |
| 54 | константа | `_GESTURE_UNIT` | строка: «(?:\bлет\b\|\bгод[а-я]*\|\bраз(?:а\|у\|ы\|е)?\b\|\bвек[а-я]*\|\bдн[еяй]\b\|\bд» |
| 59 | константа | `_MEASURE_UNIT` | строка: «(?:процент\|%\|метр\|км\|килограмм\|кг\|градус\|балл)» |
| 62 | константа | `_FELT` | list, 8 элементов |
| 65 | константа | `_CORRECTION` | list, 7 элементов |
| 68 | константа | `_CALENDAR` | list, 5 элементов |
| 74 | константа | `_REPEAT` | list, 5 элементов |
| 78 | функция | `_normalize(text)` |  |
| 82 | функция | `_trailing_zeros(n)` |  |
| 94 | константа | `_DIGIT_RE` | re.compile('\\b(\\d{2,})\\b') |
| 99 | константа | `_MAG_TOKEN_RE` | re.compile(_MAGNITUDE, re.U) |
| 100 | константа | `_EXACT_NUMERAL_RE` | re.compile('(?:двадцат\|тридцат\|сорок\|пятьдесят\|шестьдесят\|семьдесят\|восемьдесят\| |
| 107 | класс | `TemporalClassification (1 публичных методов)` | Результат RQ2: среда маркера + оба скора + сработавшие признаки. |
| 121 | константа | `HYPERBOLE_HIGH` |  |
| 124 | функция | `_hits(patterns, norm)` |  |
| 128 | функция | `has_calendar_marker(text)` | Есть ли в тексте календарный маркер (часы / порядковый день / год-число). |
| 136 | функция | `_extract_features(norm)` |  |
| 177 | константа | `_HYP_KEYS` | tuple, 4 элементов |
| 178 | константа | `_SPEC_KEYS` | tuple, 4 элементов |
| 181 | функция | `specificity_score(text)` | CALCULATED в [0,1]: доля specificity-признаков (точность/якорь). |
| 187 | функция | `hyperbole_score(text)` | CALCULATED в [0,1]: доля hyperbole-признаков (жест/травма). |
| 193 | функция | `classify_temporal_environment(text)` | RQ2: детерминированно классифицировать временной маркер. |

## ssc_char_classifier

- **путь**: `engine/ssc_char_classifier.py`
- **размер**: 269 строк, SHA-256 blob `1175bfa5472dbe84…`
- **что это**: ssc_char_classifier.py — SSC-CHAR: Система надёжности нарратора (Block 13.5).
- **зачем**: Source: AK-MASTER v6.7, Block 13.5, source standard "SSC-CHAR Protocol v1.0 — межпродуктовый стандарт AK-MASTER v3.1 / HELIX". Distinguishes from SSC (Block 13.1, what happened TO the source) — SSC-CHAR classifies the narrator's TYPE of reliability (a standing/current architectural state, not a one-time event). Found during full canon-vs-code audit (30 June 2026): engine/ssc_namespace_ guard.py exists and has a similar-sounding name, but only checks for bare "SSC" without a -SOURCE/-CHAR/-SOMATIC suffix (namespace hy…
- **коды состояний** (9): `DETECTED`, `ERROR`, `HIGH`, `NOT_CONFIGURED`, `SSC`, `STABLE`, `SYN`, `UNCERTAIN`, `YES`
- **тесты, которые зовут модуль**: 5 — `tests/test_judge_error_is_not_clean_verdict.py`, `tests/test_llm_judge_parallel.py`, `tests/test_promise_extractor.py`, `tests/test_ssc_char5_is_implemented.py`, `tests/test_ssc_char_classifier.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 40 | константа | `SSC_CHAR_TABLE` | dict, 4 элементов |
| 122 | класс | `SSCCharFinding (1 публичных методов)` |  |
| 134 | класс | `SSCCharClassifier (1 публичных методов)` | SSC-CHAR классификатор надёжности нарратора (Block 13.5). |

## ssc_namespace_guard

- **путь**: `engine/ssc_namespace_guard.py`
- **размер**: 41 строк, SHA-256 blob `70e8c0c8c9e36c82…`
- **что это**: ssc_namespace_guard.py — AK-MASTER v3.1 SSC namespace guard.
- **зачем**: Bare `SSC` is forbidden in active code/text except historical references. Use SSC-SOURCE, SSC-CHAR, or SSC-SOMATIC
- **коды состояний** (3): `MEDIUM`, `SSC_ALIAS_COLLISION`, `WARN`
- **тесты, которые зовут модуль**: 3 — `tests/test_block13_ssc_char_transitions.py`, `tests/test_ssc_char_classifier.py`, `tests/test_v151_runtime_governance.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 12 | константа | `BARE_SSC_RE` | re.compile('(?<![A-ZА-Я0-9_-])SSC(?!-(?:SOURCE\|CHAR\|SOMATIC)\\b)(?![A-ZА-Я0-9_-] |
| 13 | константа | `VALID_RE` | re.compile('\\bSSC-(SOURCE\|CHAR\|SOMATIC)(?:-[1-5])?\\b', re.I \| re.U) |
| 16 | класс | `NamespaceFlag (0 публичных методов)` |  |
| 22 | класс | `SSCNamespaceGuard (1 публичных методов)` |  |

## st18_recovery

- **путь**: `engine/st18_recovery.py`
- **размер**: 124 строк, SHA-256 blob `0e9e5be9b966c149…`
- **что это**: ST-18 Recovery Protocol — ЭВ-ИРОНИЯ / ЭВ-ВОСТОРГ injection.
- **зачем**: Source-locked to AK v6.7: five scenes without ЭВ-ИРОНИЯ/ЭВ-ВОСТОРГ or narrative LEM-DEAD loop triggers a forced recovery procedure. Code does not write the scene; it returns the disciplined recovery packet. RELATIONSHIP TO ev_sequence_monitor.py: that module (Block 0.6 cross-scene monitor) scans the FULL scene history for the longest matching run anywhere, not just the tail — a broader detection net than this module's own last-5/last-3 check. It delegates to THIS module's .audit() for the actual ST-18 recovery procedure text (both ЭВ-…
- **коды состояний** (7): `BLOCKED_ST18_REQUIRED`, `HIGH`, `MEDIUM`, `ST18_FORCED_IRONY_INJECTION`, `ST18_IRONY_AIR_RECOMMENDED`, `ST18_RELIEF_ABSENT_5_SCENES`, `WARN`
- **тесты, которые зовут модуль**: 3 — `helix_pipeline/tests/test_st18_recovery.py`, `tests/test_ev_sequence_monitor.py`, `tests/test_v161_audit_response.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 20 | константа | `IRONY` | строка: «ЭВ-ИРОНИЯ» |
| 21 | константа | `AWE` | строка: «ЭВ-ВОСТОРГ» |
| 22 | константа | `HEAVY` | set, 2 элементов |
| 23 | константа | `RELIEF` | set, 2 элементов |
| 26 | класс | `ST18Finding (0 публичных методов)` |  |
| 32 | класс | `ST18RecoveryProtocol (1 публичных методов)` |  |

## state_gate

- **путь**: `engine/state_gate.py`
- **размер**: 115 строк, SHA-256 blob `7207954e2466150c…`
- **что это**: state_gate.py — RQ4 STATE_GATE 9.6: день это дата или состояние?
- **зачем**: Оба содержат рекурсию «день после дня X тоже был днём X»: * «Утро после Дня Арбуза тоже было днём арбуза» — ПОХМЕЛЬЕ, состояние длится, календарь НЕ двигается (STATE); * «День после Дня Арбуза — шестой день» — новая ДАТА, счётчик дня растёт. Старый STATE_GATE ловил рекурсию как STATE_NOT_DATE всегда — и путал новую дату с состоянием. RQ4: различить их через ОТСУТСТВИЕ новых физических/ календарных событий (гипотеза ТЗ). Правило (детерминированно, без LLM): рекурсия дня присутствует И нет НОВОГО календарного маркера (часы, новый п…
- **коды состояний** (3): `DATE`, `NOT_APPLICABLE`, `STATE`
- **тесты, которые зовут модуль**: 1 — `tests/test_state_gate_rq4.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 31 | константа | `DayVerdict` |  |
| 34 | функция | `_normalize(text)` |  |
| 40 | константа | `_RECURSION_AFTER_RE` | re.compile('\\b(?:день\|дня\|дн[еёя]м\|утро\|утром\|поутру\|вечер\|вечером\|ночь\|ночью\|п |
| 45 | константа | `_RECURSION_EQ_RE` | re.compile('\\b(?:тоже\|также\|всё ещё\|все еще\|опять\|снова\|по-прежнему)\\b[^.]{0,2 |
| 53 | константа | `_STATE_MARKERS` | list, 18 элементов |
| 62 | класс | `StateGateResult (1 публичных методов)` |  |
| 74 | функция | `has_day_recursion(text)` | «день после дня X тоже был днём X» и подобное — рекурсия суток. |
| 80 | функция | `_state_hits(norm)` |  |
| 84 | функция | `classify_day(text)` | RQ4: STATE vs DATE для абзаца с рекурсией суток. |

## style_fingerprint

- **путь**: `engine/style_fingerprint.py`
- **размер**: 157 строк, SHA-256 blob `14dd09294eb33440…`
- **что это**: style_fingerprint.py — измеримый «отпечаток голоса» текста и сравнение
- **зачем**: черновика с ЭТАЛОННЫМ текстом самого автора (P1, 2026-07-16). Рыночная дифференциация (подтверждена обоими присланными конкурент- исследованиями): AutoCrit сравнивает с жанровыми бестселлерами, Marlowe — с корпусом. Оба философски тянут автора к «норме рынка» и стирают голос. AK-MASTER сравнивает новый текст с ЛУЧШИМ текстом САМОГО автора: не «не соответствует норме романтического саспенса», а «в вашем „Дне Арбуза" средняя фраза 5.6 слова, здесь 9.4 — вдвое длиннее вашего голоса». Метрики выбраны так, чтобы совпадать с теми…
- **тесты, которые зовут модуль**: 1 — `tests/test_style_fingerprint.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 33 | константа | `_WORD_RE` | re.compile('[а-яёa-z0-9]+', re.I \| re.U) |
| 34 | константа | `_SENT_SPLIT_RE` | re.compile('(?<=[.!?…])\\s+') |
| 35 | константа | `_DIALOGUE_LINE_RE` | re.compile('(?m)^\\s*(?:—\|–\|―\|-{1,3}\|\\u2014)\\s?\\S') |
| 37 | константа | `_YA_RE` | re.compile('(?<![а-яё])я(?![а-яё])', re.I \| re.U) |
| 41 | класс | `StyleFingerprint (1 публичных методов)` |  |
| 57 | функция | `_sentences(text)` |  |
| 61 | функция | `fingerprint(text)` |  |
| 92 | константа | `_METRICS_HUMAN` | dict, 6 элементов |
| 102 | функция | `_direction_phrase(metric, draft_v, ref_v)` |  |
| 117 | функция | `compare_to_reference(draft_text, reference_text)` | Сравнить черновик с эталонным текстом автора. Возвращает отпечатки |

## symbol_architecture

- **путь**: `engine/symbol_architecture.py`
- **размер**: 181 строк, SHA-256 blob `72db5254de090a7d…`
- **что это**: symbol_architecture.py — архитектура центрального символа (Н-10 /
- **зачем**: Модуль 9). Источник: docs/handoffs/КОНСТРУКТ_РЕЕСТР_17_ОШИБОК_модули_7-11.md, Н-10 — класс СИМВОЛЬНАЯ АРХИТЕКТУРА. ФЛАГОВЫЙ модуль. Находка (буквально): «Центральный символ не имел ни ответа, ни заявления, что ответа не будет.» Решение — три уровня, реализованных авторами: пророчество (колода до событий), двойное чтение (посеянное в текст: «карта держала оба ответа — за середину»), материализация (порт с тремя волокнами на тёмно-бордовом = карта из плоти; три змеи = Телесеть/Feed/FAT — БЕЗ называния впрямую). Правило (буквально)…
- **тесты, которые зовут модуль**: 1 — `tests/test_symbol_architecture.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 36 | константа | `SymbolLevel` |  |
| 38 | константа | `_ALL_LEVELS` | frozenset({'prophecy', 'materialization', 'formula_inversion', 'double_reading'} |
| 41 | константа | `_MINIMUM_LEVELS_REQUIRED` |  |
| 45 | класс | `SymbolArchitectureCheck (1 публичных методов)` |  |
| 57 | класс | `FormulaOccurrence (0 публичных методов)` |  |
| 63 | класс | `FormulaChange (1 публичных методов)` |  |
| 76 | класс | `FormulaTrackingReport (1 публичных методов)` |  |
| 89 | функция | `check_symbol_architecture(symbol_id, present_levels)` | Проверить, что центральный символ имеет минимум 2 уровня из 4. |
| 127 | функция | `check_formula_tracking(occurrences)` | Отследить последовательность формул символа по сценам на предмет |

## syn_applier

- **путь**: `engine/syn_applier.py`
- **размер**: 83 строк, SHA-256 blob `325195c065f81b84…`
- **коды состояний** (5): `ACTIVE`, `APPLIED`, `BLOCKED`, `NON_LIQUET`, `PRINT_ONLY`
- **тесты, которые зовут модуль**: 1 — `tests/test_ak_discipline_engine.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 6 | константа | `_VERSION_SUFFIX_RE` | re.compile('\\s*[\\[(][^\\]\\)]+[\\]\\)]\\s*$') |
| 9 | функция | `strip_version_suffix(code)` | Remove AK version/status suffixes from SYN codes while preserving real code hyphens. |
| 22 | класс | `SYNApplier (1 публичных методов)` |  |

## syn_canon_cards

- **путь**: `engine/syn_canon_cards.py`
- **размер**: 404 строк, SHA-256 blob `dcbc729b43b506c8…`
- **что это**: syn_canon_cards.py — полные операциональные карточки SYN-кодов (Блок 12.8).
- **зачем**: SCOPE NOTE: этот модуль НЕ входит в AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md (проверено: 0 совпадений по всем 7 кодам ниже в этом документе на 2026-07-13). Источник — AK-6.8 FINAL_IDEAL canon, «12.8.0 — FULL CANONICAL SYN CARDS» + «3. FAIL ATTACHMENTS FOR EXISTING MASTER NODES» — это расширение поверх базового AK-6.7, а не пробел в его реализации. До этого модуля `engine/canon_citations.py` и `engine/prompt_packet_builder.py` знали только о двух из семи кодов ниже (SYN-BST, SYN-VV-NEX) — и только как код + библиографич…
- **коды состояний** (7): `EXP`, `SCA`, `SCN`, `SSC`, `TST`, `VRP`, `VTO`
- **тесты, которые зовут модуль**: 1 — `tests/test_syn_canon_cards.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 27 | класс | `SynCard (1 публичных методов)` |  |
| 45 | класс | `FailAttachment (1 публичных методов)` | FAIL/postflight-таблица, прикрепляемая к уже существующему в мастере коду. |
| 55 | константа | `SYN_CARDS` | tuple, 7 элементов |
| 354 | константа | `_BY_CODE` |  |
| 357 | константа | `FAIL_ATTACHMENTS` | tuple, 2 элементов |
| 382 | константа | `_FAIL_BY_PARENT` |  |
| 385 | функция | `get_card(code)` |  |
| 389 | функция | `get_fail_attachment(parent_code)` |  |
| 393 | функция | `all_cards()` |  |
| 397 | функция | `all_fail_attachments()` |  |
| 401 | функция | `known_codes()` | Все коды, добавленные этим модулем — для регистрации в SYN_NOTES / |

## syn_canon_table

- **путь**: `engine/syn_canon_table.py`
- **размер**: 217 строк, SHA-256 blob `6690fe0af2e54e61…`
- **что это**: syn_canon_table.py — таблицы SYN канона как единственный источник.
- **зачем**: Канон АК-6.7 задаёт синтаксические режимы ДВУМЯ таблицами, и обе — канон: * **Блок 9** (`discipline/syn_protocol.yaml`, 31 строка): на каждый код — «Источник», «Принцип», «Приём», «Активен при». Правило раздела дословно: **«Применять ПРИНЦИП и ПРИЁМ одновременно. EXP-код выбирается отдельно.»** * **Блок 4** (`discipline/scn_protocol.yaml`, 15 строк): на каждый тип сцены — колонка «СТИЛЬ + SYN», то есть каким режимом сцена написана. Первая отвечает «где код разрешён», вторая — «чем сцена пишется по умолчанию». Это не дубль: разн…
- **коды состояний** (2): `SCN`, `UNKNOWN_CODE`
- **тесты, которые зовут модуль**: 3 — `tests/test_canon_membership_gate.py`, `tests/test_syn_blocked_from_canon_table.py`, `tests/test_syn_canon_table_is_source.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 58 | константа | `_ТЕГ` | re.compile('\\s*\\[[^\\]]*\\]') |
| 59 | константа | `_КОД` | re.compile('SYN-[A-ZА-Я0-9]+(?:-[A-ZА-Я0-9]+)*', re.I) |
| 72 | константа | `_МЕТКИ_БЛОКИРОВКИ` | tuple, 2 элементов |
| 75 | функция | `нормализовать(код)` | «SYN-BS [PRINT-ONLY]» → ['SYN-BS'];  «SYN-POE / SYN-EAP-LOG» → два кода. |
| 87 | функция | `_сцены(значение)` |  |
| 92 | функция | `_таблица_блока_9()` |  |
| 119 | функция | `_таблица_блока_4()` |  |
| 135 | функция | `_правило()` |  |
| 140 | класс | `SynCanonTable (5 публичных методов)` | Единственная точка доступа к каноническому знанию о SYN. |

## syn_decision_tree

- **путь**: `engine/syn_decision_tree.py`
- **размер**: 170 строк, SHA-256 blob `3dc64a075547035a…`
- **что это**: syn_decision_tree.py — дерево решений SYN из Блока 9.3 канона.
- **зачем**: Канон АК-6.7, БЛОК 9.3 (строки 1395–1422): таблица «ЕСЛИ СЦЕНА… И НУЖЕН ЭФФЕКТ… → SYN-КОД». Требование канона дословно: **код выбирается по сцене и нужному эффекту, а не на слух.** ЧТО БЫЛО. `discipline/syn_decision_tree.yaml` — 28 строк канонической таблицы, лежащих в репозитории с самого начала, — **не читал никто**. Одна из трёх несостоявшихся связей, найденных при составлении реестра канона. Дальше важное различение, на котором я сам сначала ошибся и полез проверять: в `prompt_packet_builder` есть таблица `SCENE_SYN_ROUTES` (SC…
- **коды состояний** (2): `NEEDS_INPUT`, `NO_MATCH`
- **тесты, которые зовут модуль**: 1 — `tests/test_block9_decision_tree_wired.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 31 | константа | `ПУТЬ` |  |
| 36 | константа | `К_СЦЕНА` | строка: «Если сцена...» |
| 37 | константа | `К_ЭФФЕКТ` | строка: «И нужен эффект...» |
| 38 | константа | `К_КОД` | строка: «→ SYN-код» |
| 40 | константа | `_СЛОВО` | re.compile('[а-яёa-z0-9]+', re.I \| re.U) |
| 43 | константа | `_ПУСТЫЕ` | frozenset({'и', 'или', 'в', 'во', 'на', 'с', 'со', 'как', 'не', 'за', 'к', 'по', |
| 51 | функция | `_слова(строка)` |  |
| 57 | класс | `Ветвь (1 публичных методов)` | Одна строка канонической таблицы. |
| 69 | класс | `SynDecisionTree (5 публичных методов)` | Дерево решений Блока 9.3. Источник — файл канона, не копия в коде. |

## tentpole_gate

- **путь**: `engine/tentpole_gate.py`
- **размер**: 161 строк, SHA-256 blob `7d119d3d0772fc98…`
- **что это**: tentpole_gate.py — Блок 7: четыре несущих tentpole ОБЯЗАТЕЛЬНЫ.
- **зачем**: РЕЕСТР КАНОНА, `Б7-tentpoles` (статус «частично»): «Статусы tentpole хранятся, проверки их обязательности нет». Проверено поведением 15.08 — так и есть: `ArchiveTracker.commit()` кладёт tentpole в состояние под ЛЮБЫМ ключом (`p["key"] or p["id"] or порядковый номер`) с ЛЮБЫМ значением. То есть: * книга с двумя tentpole из четырёх выглядит так же законно, как с четырьмя — отсутствие несущей конструкции не замечает никто; * статус может быть какой угодно строкой («почти», «ок», «55%»), хотя протокол архива (11.5) знает ровно три: ВЫ…
- **коды состояний** (8): `HIGH`, `MEDIUM`, `TENTPOLE_MISSING`, `TENTPOLE_ORDER_BROKEN`, `TENTPOLE_STATUS_INVALID`, `TENTPOLE_UNFINISHED_IN_COMPLETE_MANUSCRIPT`, `TENTPOLE_UNKNOWN_KEY`, `WARN`
- **тесты, которые зовут модуль**: 1 — `tests/test_tentpole_gate_block7.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 35 | константа | `TENTPOLES` | tuple, 4 элементов |
| 44 | константа | `DONE` | строка: «ВЫПОЛНЕН» |
| 45 | константа | `IN_PROGRESS` | строка: «В ПРОЦЕССЕ» |
| 46 | константа | `NOT_STARTED` | строка: «НЕ НАЧАТ» |
| 47 | константа | `VALID_STATUSES` | tuple, 3 элементов |
| 49 | константа | `_ORDER` |  |
| 50 | константа | `_NAMES` | dict(TENTPOLES) |
| 54 | класс | `TentpoleFinding (1 публичных методов)` |  |
| 64 | функция | `_normalize_status(value)` |  |
| 68 | функция | `audit(tentpoles)` | Проверить обязательность и связность четырёх tentpole. |

## threat_gate

- **путь**: `engine/threat_gate.py`
- **размер**: 185 строк, SHA-256 blob `074eceb3c9f9b0df…`
- **что это**: threat_gate.py — AK-MASTER v3.1 preflight threat gate.
- **коды состояний** (12): `COMPLETE`, `DATA_POISONING`, `EXTERNAL_CODE_INJECTION`, `FORK_MANIFEST_INCOMPLETE`, `HIGH`, `IDENTITY_COERCION`, `INCOMPLETE`, `MEDIUM`, `PROMPT_INJECTION`, `ROGUE_FORK`, `ROGUE_FORK_NO_LINEAGE_ID`, `WARN`
- **тесты, которые зовут модуль**: 8 — `tests/test_activation_map_last_steps.py`, `tests/test_fork_manifest_seven_fields.py`, `tests/test_threat_gate_first_in_order.py`, `tests/test_threat_gate_fork_lineage.py`, `tests/test_threat_gate_injection_variants.py`, `tests/test_threat_gate_poisoning_codeinj.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 8 | константа | `PATTERNS` | list, 5 элементов |
| 66 | константа | `_BLANK_LINEAGE` | set, 9 элементов |
| 69 | функция | `_is_blank_lineage(value)` | True, если lineage_ID отсутствует по сути: None, пробелы или |
| 91 | константа | `FORK_MANIFEST_FIELDS` | tuple, 7 элементов |
| 102 | функция | `_check_fork_manifest(manifest)` | Полнота манифеста форка по канону (PART IV, FORK GOVERNANCE). |
| 129 | класс | `ThreatFlag (0 публичных методов)` |  |
| 135 | класс | `ThreatGate (1 публичных методов)` |  |

## tribunal_protocol

- **путь**: `engine/tribunal_protocol.py`
- **размер**: 221 строк, SHA-256 blob `dc9645b1cec40165…`
- **что это**: tribunal_protocol.py — TRIBUNAL PROTOCOL (PART IV).
- **зачем**: Канон, `AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md`, строки 2086–2101: **Проблема:** При противоречиях данных нет формального процесса с возможностью апелляции. Каждое решение трибунала содержит: | Поле | Описание | |-----------------|---------------------------------| | claim | Утверждение | | evidence_level | Уровень доказательности (N1–N4) | | decision_basis | Основание решения | | appeal_deadline | Срок обжалования | **Tribunal Charter:** приоритет признаётся не суммой ECT, а анализом давления и мотива (biological coercion vs synthetic clar…
- **коды состояний** (10): `DECISIONS_NOT_SUPPLIED`, `EMPTY`, `NOT_RUN`, `NO_DECISIONS`, `TRIBUNAL_APPEAL_DEADLINE_UNPARSABLE`, `TRIBUNAL_APPEAL_WINDOW_CLOSED`, `TRIBUNAL_BASIS_IS_ECT_SUM`, `TRIBUNAL_EVIDENCE_LEVEL_INVALID`, `TRIBUNAL_FIELD_MISSING`, `UNPARSABLE`
- **тесты, которые зовут модуль**: 2 — `tests/test_activation_map_last_steps.py`, `tests/test_tribunal_protocol.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 55 | константа | `REQUIRED_FIELDS` | tuple, 4 элементов |
| 63 | константа | `EVIDENCE_LEVELS` | tuple(CLASSES) |
| 65 | константа | `ИСТОЧНИК` | строка: «AK_6_7_UNIFIED_MD_CANON_REALIZED_v0_3.md, TRIBUNAL PROTOCOL, строки 20» |
| 68 | константа | `ХАРТИЯ` | строка: «Tribunal Charter: приоритет признаётся не суммой ECT, а анализом давле» |
| 74 | константа | `_ECT_СУММА` | re.compile('сумм\\w*\\s+ECT\|ECT[\\s-]*\\d\\s*(?:[+>=<]\|больше\|выше\|превыша\\w*)\ |
| 80 | константа | `_ТОЛЬКО_ПРОБЕЛЫ` | re.compile('^\\s*$') |
| 83 | функция | `_разобрать_срок(значение)` | Срок обжалования → дата. Возвращает (дата, причина-если-не-вышло). |
| 108 | функция | `audit_decision(decision)` | Одно решение трибунала: полно ли оно по канону. |
| 180 | функция | `audit(decisions)` | Метрика канона: «100% решений с полным обоснованием и путём обжалования». |

## tst_dr_detector

- **путь**: `engine/tst_dr_detector.py`
- **размер**: 122 строк, SHA-256 blob `b59d829e549d9198…`
- **что это**: tst_dr_detector.py — TST-DR / authorial intrusion detector.
- **зачем**: Mechanical AK-MASTER rule inspired by Gardner: the reader should not be woken from the fictional dream by direct authorial explanation, symbolic decoding or reader-instruction prose. This is a heuristic detector, not a literary verdict
- **коды состояний** (8): `HIGH`, `LOW`, `MEDIUM`, `TST_DR_AUTHOR_INTENT`, `TST_DR_EXPLANATORY_BRIDGE`, `TST_DR_READER_DIRECTIVE`, `TST_DR_SYMBOLIC_EXPLANATION`, `WARN`
- **тесты, которые зовут модуль**: 6 — `tests/test_block6_tst_suite_enforcement.py`, `tests/test_canon_mode_test_applicability.py`, `tests/test_context_detectors_single_impl.py`, `tests/test_tst_dr_vrp_x1.py`, `tests/test_v13_lawz_dr_shadow_scr.py`, `tests/test_v14_issue_closure_pack.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 13 | константа | `AUTHOR_INTENT_RE` | re.compile('\\b(автор\\s+(?:хочет\|хотел\|пытается\|стремится\|показывает\|доказывает |
| 18 | константа | `READER_DIRECTIVE_RE` | re.compile('\\b(читатель\\s+(?:должен\|понимает\|видит\|узнает\|осозна[её]т\|чувствуе |
| 24 | константа | `SYMBOLIC_EXPLANATION_RE` | re.compile('\\b(это\\s+символизирует\|символизирует\|является\\s+символом\|метафора |
| 29 | константа | `EXPLANATORY_BRIDGE_RE` | re.compile('\\b(это\\s+важно\\s+потому\\s+что\|дело\\s+в\\s+том\\s+что\|на\\s+само |
| 34 | константа | `NON_SCENE_MODES` | set, 3 элементов |
| 44 | константа | `META_BREAK_EXEMPT_SCN` | строка: «SCN-12» |
| 46 | функция | `_norm_mode(mode)` |  |
| 49 | функция | `_norm_scn(scn_code)` |  |
| 54 | функция | `_scene_adjusted_severity(severity, non_scene)` |  |
| 60 | класс | `TSTDRViolation (0 публичных методов)` |  |
| 67 | класс | `TSTDRDetector (1 публичных методов)` | Detects obvious authorial intrusion and symbolic over-explanation. |

## tst_dv_detector

- **путь**: `engine/tst_dv_detector.py`
- **размер**: 335 строк, SHA-256 blob `49915ec9d9242567…`
- **что это**: tst_dv_detector.py — TST-DV detector for AK-MASTER v0.9.
- **зачем**: AK v6.7 Block 6: TST-DV / Test of the Double. Rule: Reading A = it really happened. Reading B = the hero is going mad. Both retellings must remain convincing and resist each other. The text must not hand the reader a final answer. This detector is deliberately modest: it does NOT decide literary ambiguity. It catches mechanical failure modes: - only one reading has textual evidence; - the text resolves the ambiguity too early; - both readings exist but do not collide/resist; - author explains the answer instead of deepening contradiction…
- **коды состояний** (4): `HIGH`, `LOW`, `MEDIUM`, `WARN`
- **тесты, которые зовут модуль**: 10 — `tests/test_block6_tst_suite_enforcement.py`, `tests/test_canon_mode_test_applicability.py`, `tests/test_canon_single_impl_invariants.py`, `tests/test_lemma_migration_tst_dv.py`, `tests/test_llm_judge_tst_dv.py`, `tests/test_negation_utils.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 25 | константа | `_REALITY_RE` | re.compile('\\b(реальн\|физик\|пространств\|врем\|гравитац\|стен\|двер\|окн\|комнат\|кори |
| 40 | константа | `_REALITY_LEMMAS` | set, 6 элементов |
| 41 | константа | `_PSYCH_RE` | re.compile('\\b(памят\|сон\|бред\|галлюцин\|психоз\|паник\|тревог\|кортизол\|гиппокамп\|г |
| 47 | константа | `_PSYCH_LEMMAS` | set, 10 элементов |
| 51 | константа | `_FINAL_ANSWER_STRONG_RE` | re.compile('\\b(на\\s+самом\\s+деле\|в\\s+действительности\|оказалось\|выяснилось\|э |
| 63 | константа | `_FINAL_ANSWER_WEAK_RE` | re.compile('\\b(просто\|всего\\s+лишь)\\b', re.I \| re.U) |
| 64 | константа | `_FINAL_ANSWER_RE` | re.compile(_FINAL_ANSWER_STRONG_RE.pattern + '\|' + _FINAL_ANSWER_WEAK_RE.pattern |
| 82 | константа | `_RESISTANCE_WHOLE` | строка: «но\|однако\|если\|оба\|и\s+вс[её]\s+же\|при\s+этом\|ни\s+один\|две\s+версии\|н» |
| 86 | константа | `_RESISTANCE_STEMS` | строка: «не\s+становилось\s+ясн\|сопротивлял\|противореч\|не\s+совпадал\|не\s+объяс» |
| 89 | константа | `_RESISTANCE_RE` | re.compile('\\b(?:' + _RESISTANCE_WHOLE + ')\\b\|\\b(?:' + _RESISTANCE_STEMS + ') |
| 93 | константа | `_AUTHOR_EXPLAIN_RE` | re.compile('\\b(читатель\\s+должен\\s+понять\|это\\s+символизирует\|автор\\s+показ |
| 100 | класс | `TSTDVViolation (0 публичных методов)` |  |
| 108 | функция | `_hits(pattern, text, limit, skip_negated)` |  |
| 121 | функция | `_merge_hits(base, extra, limit)` | Слить улики из regex- и лемма-ветки, сохранив дедуп и лимит _hits. |
| 133 | класс | `TSTDVDetector (2 публичных методов)` | Mechanical ambiguity detector for TST-DV. Author keeps final judgment. |

## tst_ev_detector

- **путь**: `engine/tst_ev_detector.py`
- **размер**: 612 строк, SHA-256 blob `62a4332dfd3deb17…`
- **что это**: TST-EV detector — Emotional Valence nucleus, intensity and vector audit.
- **зачем**: Source-locked to AK v6.7 Block 0.6 / Block 10.2 пункт 12: можно ли назвать ЭВ-ядро из восьми без авторской подсказки? Интенсивность и вектор читаются? This detector is intentionally heuristic. It does not decide literary quality; it returns a disciplined signal for the author / LLM layer
- **коды состояний** (15): `HIGH`, `INFO`, `LOW`, `MEDIUM`, `TST_EV_ALPHABET_NOT_COVERED`, `TST_EV_CORE_UNREADABLE`, `TST_EV_CORE_UNREADABLE_BY_DICTIONARY`, `TST_EV_EXPECTED_MISMATCH`, `TST_EV_INTENSITY_MISMATCH`, `TST_EV_LOW_EVIDENCE`, `TST_EV_READER_CONFIDENCE_LOW`, `TST_EV_VECTOR_MISMATCH`, `TST_EV_VECTOR_WEAK`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 18 — `tests/test_block0_really_runs.py`, `tests/test_bol_bolshoi_collision_fix.py`, `tests/test_canon_mode_test_applicability.py`, `tests/test_canon_single_impl_invariants.py`, `tests/test_ev_eight_cores.py`, `tests/test_ev_показанное.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 29 | константа | `EV_KEYWORDS` | dict, 8 элементов |
| 44 | константа | `EV_WORD_RES` | dict, 1 элементов |
| 48 | константа | `EV_LEMMAS` | dict, 4 элементов |
| 65 | константа | `EV_FALSE_FRIENDS` | dict, 1 элементов |
| 80 | константа | `BODY_MARKERS` | list, 8 элементов |
| 83 | константа | `_BODY_INTENSITY_LEMMAS` | set, 40 элементов |
| 145 | константа | `_BODY_PHRASES` | dict, 3 элементов |
| 164 | константа | `_BODY_PAIN_LEMMAS` | set, 3 элементов |
| 171 | константа | `GROW_RE` | re.compile('\\bнараст\\w*\|вс[её]\\s+сильнее\|\\b(сильнее\|ещё\|еще\|потом\|затем)\\b' |
| 172 | константа | `FALL_RE` | re.compile('\\b(утих\|ослаб\|погас\|остыл\|затих\|сошл)\\w*\\b\|\\bменьше\\b', re.I \|  |
| 173 | константа | `INVERT_RE` | re.compile('\\b(но\|однако\|вдруг)\\b\|смешно\\s+и\\s+страшно\|страшно\\s+и\\s+смешн |
| 175 | функция | `_письменность_вне_словаря(text)` | Текст написан алфавитом, которого нет ни в одном словаре модуля. |
| 189 | класс | `EVFinding (0 публичных методов)` |  |
| 217 | константа | `MIN_EVIDENCE_FOR_VERDICT` |  |
| 231 | константа | `SEVERITY_ABOUT_INSTRUMENT` | строка: «INFO» |
| 251 | константа | `MIN_BODY_ANCHORS_FOR_INSTRUMENT_DOUBT` |  |
| 254 | класс | `TSTEVDetector (2 публичных методов)` |  |

## tst_kin_detector

- **путь**: `engine/tst_kin_detector.py`
- **размер**: 662 строк, SHA-256 blob `5c81e31e06af7d81…`
- **что это**: tst_kin_detector.py — TST-KIN visual dialogue / kinesics detector.
- **зачем**: Mechanical rule: any long dialogue line needs physical action, proxemics or micromotorics nearby. It detects risk; it does not replace literary judgment
- **коды состояний** (4): `HIGH`, `LOW`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 18 — `tests/test_block6_tst_suite_enforcement.py`, `tests/test_canon_mode_test_applicability.py`, `tests/test_canon_point_fixes.py`, `tests/test_canon_single_impl_invariants.py`, `tests/test_dictionary_collision_fixes.py`, `tests/test_frequency_corpus_collisions.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 16 | функция | `_kin_canon_examples()` | Canon kinesics exemplars (Михаэлидис — микромоторика вместо реплики, |
| 22 | константа | `DIALOGUE_RE` | re.compile('^\\s*[—–-]\\s*(.+)', re.U) |
| 27 | константа | `_КОНЕЦ_ФРАЗЫ_RE` | re.compile('[.!?…»\\"\\\')\\]]\\s*$', re.U) |
| 32 | константа | `_ЗАПАС_ШИРИНЫ` |  |
| 33 | константа | `_ПОТОЛОК_ПЕРЕНОСА` |  |
| 34 | константа | `_МИН_СТРОК_ДЛЯ_ВЫВОДА` |  |
| 35 | константа | `_ДОЛЯ_У_ПРЕДЕЛА` |  |
| 40 | константа | `_МИН_РЕПЛИК_ДЛЯ_ДЕФИСА` |  |
| 41 | константа | `BULLET_RE` | re.compile('^\\s*[-–—]\\s*(?:\\[[ xX]\\]\|\\d+[.)]\|[A-Za-zА-Яа-я]\\)\|[•*]\|\\w[\\w |
| 58 | константа | `KINESIC_LEMMAS` | set, 27 элементов |
| 74 | константа | `KINESIC_RE` | re.compile('\\b(наклони\|поверну\|отступ\|подош[её]л\|встал\|коснул\|сжал\|разжал\|молча |
| 75 | константа | `KINESIC_VERB_LEMMAS` | set, 3 элементов |
| 111 | константа | `KINESIC_BODY_LEMMAS` | set, 28 элементов |
| 120 | константа | `KINESIC_ACTION_LEMMAS` | set, 144 элементов |
| 198 | константа | `KINESIC_EXTRA_RE` | re.compile('\\b(поставил\\w*\|положил\\w*\|смотрел\\w*\|посмотрел\\w*\|гляд\\w+\|взгл |
| 232 | константа | `_ВСЕ_КИНЕСИЧЕСКИЕ_ЛЕММЫ` |  |
| 238 | функция | `_has_kinesic(text)` |  |
| 251 | константа | `PROXEMIC_RE` | re.compile('\\b(через\\s+стол\|за\\s+столом\|плечом\\s+к\\s+плечу\|спиной\|у\\s+стен |
| 284 | константа | `SPEECH_CUE_RE` | re.compile('\\b(сказал\\w*\|скажет\|говор(?:ит\|ят\|ю\|ил\\w*)\|ответил\\w*\|отвеча(?:е |
| 323 | константа | `БЕСТЕЛЕСНЫЙ_МАРКЕР_RE` | re.compile('^\\s*[\\[<][^\\]>]{1,60}[\\]>]\\s*$', re.U) |
| 327 | класс | `KINViolation (0 публичных методов)` |  |
| 335 | класс | `TSTKINDetector (2 публичных методов)` |  |

## tst_mrl_detector

- **путь**: `engine/tst_mrl_detector.py`
- **размер**: 222 строк, SHA-256 blob `cc0893d0c56b7de4…`
- **что это**: tst_mrl_detector.py — TST-MR.L / Ligotti topographic mirror detector.
- **зачем**: Source-locked to AK v6.7: TST-MR.L requires physical/topographic degradation of location to mirror psychological collapse. It is a risk detector, not a literary verdict
- **коды состояний** (9): `HIGH`, `LOW`, `MEDIUM`, `TST_MRL_NO_LOCATION_MIRROR`, `TST_MRL_SEMANTIC_DESYNC`, `TST_MRL_STABLE_TOPOGRAPHY`, `TST_MRL_WORLD_STABLE_WHILE_POV_COLLAPSES`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 8 — `tests/test_block6_tst_suite_enforcement.py`, `tests/test_canon_mode_test_applicability.py`, `tests/test_frequency_corpus_collisions.py`, `tests/test_lemma_migration_mrl_ev_auditor_trauma.py`, `tests/test_llm_judge_tst_mrl.py`, `tests/test_negation_utils.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 16 | константа | `TARGET_SCNS` | set, 12 элементов |
| 21 | константа | `PSYCH_COLLAPSE_RE` | re.compile('\\b(психик\|психоз\|безуми\|сход\\w*\\s+с\\s+ума\|пани[кч]\|кошмар\|парано |
| 25 | константа | `PSYCH_COLLAPSE_LEMMAS` | set, 1 элементов |
| 26 | константа | `LOCATION_RE` | re.compile('\\b(дом\|комнат\|коридор\|лестниц\|двер\|окн\|стен\|потол\|пол(?!уч\|ожен\|ити |
| 30 | константа | `DEGRADATION_LEMMAS` | set, 2 элементов |
| 31 | константа | `DEGRADATION_RE` | re.compile('\\b(гни\|плесен\|плесень\|ржав\|трещ\|осып\|крош\|просед\|перекос\|искрив\|деф |
| 35 | константа | `STABLE_WORLD_RE` | re.compile('\\b(мир\\s+оставал\\w*\\s+стабил\|комнат\\w*\\s+не\\s+изменил\|дом\\s+ |
| 41 | класс | `MRLViolation (0 публичных методов)` |  |
| 48 | функция | `_norm_scn(scn_code)` |  |
| 57 | класс | `TSTMRLDetector (2 публичных методов)` | Checks whether external location mirrors inner collapse for MR/Ligotti scenes. |

## tst_pl_detector

- **путь**: `engine/tst_pl_detector.py`
- **размер**: 433 строк, SHA-256 blob `4c9e04570a9d3760…`
- **что это**: tst_pl_detector.py — TST-PL detector for AK-MASTER v0.8.
- **зачем**: AK v6.7 uses TST-PL as a polyphony/autonomous-voice test. This module does NOT judge literary polyphony finally. It mechanically detects situations where dialogue voices may collapse into one authorial voice, or where attribution is doing all the work instead of the voices being distinguishable. Rule of discipline: - detector reports probable risk; - author/LLM performs literary correction; - no automatic rewrite and no final aesthetic verdict
- **коды состояний** (4): `LOW`, `MEDIUM`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 11 — `tests/test_block6_tst_suite_enforcement.py`, `tests/test_canon_mode_test_applicability.py`, `tests/test_canon_single_impl_invariants.py`, `tests/test_dictionary_collision_fixes.py`, `tests/test_frequency_corpus_collisions.py`, `tests/test_lemma_migration_tst_pl.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 25 | константа | `_ATTRIBUTION_RE` | re.compile('\\b(сказал\|сказала\|сказали\|ответил\|ответила\|ответили\|спросил\|спросил |
| 31 | константа | `_DASH_DIALOGUE_RE` | re.compile('(?m)^\\s*[—-]\\s*(.+?)\\s*$') |
| 32 | константа | `_QUOTED_DIALOGUE_RE` | re.compile('[«\\"]([^«»\\"]{2,400})[»\\"]') |
| 33 | константа | `_SPEAKER_AFTER_RE` | re.compile('[—-]\\s*(?:сказал\|сказала\|ответил\|ответила\|спросил\|спросила\|прошепта |
| 41 | константа | `_ВВОД_РЕЧИ` | строка: «сказал\|сказала\|ответил\|ответила\|спросил\|спросила\|прошептал\|прошептала\|» |
| 44 | константа | `_SPEAKER_BEFORE_NAME_FIRST_RE` | re.compile(f'\\b([А-ЯЁA-Z][\\w\\-]{{1,30}})\\s+(?:{_ВВОД_РЕЧИ})\\w*\\s*:\\s*$',  |
| 47 | константа | `_SPEAKER_BEFORE_VERB_FIRST_RE` | re.compile(f'\\b(?:{_ВВОД_РЕЧИ})\\w*\\s+([А-ЯЁA-Z][\\w\\-]{{1,30}})\\s*:\\s*$',  |
| 51 | константа | `_TECH_WORDS` | re.compile('\\b(алгоритм\|система\|протокол\|данн\|модель\|код\|сервер\|нейро\|сеть\|паке |
| 57 | константа | `_ABSTRACT_WORDS` | re.compile('\\b(истин\|смысл\|реальност\|памят\|любов\|вина\|свобод\|невозможн\|пустот)\ |
| 58 | константа | `_ABSTRACT_LEMMAS` | set, 1 элементов |
| 59 | константа | `_BODY_WORDS` | re.compile('\\b(рук(?!овод\|ав)\|горл\|кожа\|дых\|ладон\|зуб\|плеч)\\w*\\b', re.I \| re. |
| 60 | константа | `_BODY_LEMMAS` | set, 11 элементов |
| 67 | класс | `DialogueTurn (0 публичных методов)` |  |
| 79 | класс | `TSTPLViolation (0 публичных методов)` |  |
| 88 | функция | `_words(text)` |  |
| 92 | функция | `_speaker_from_turn(raw)` |  |
| 99 | функция | `_speaker_before(префикс)` | Говорящий, названный ПЕРЕД кавычечной репликой. |
| 120 | константа | `_ATTRIBUTION_SEGMENT_RE` | re.compile('\\s+[—-]\\s*(?:сказал\|сказала\|сказали\|ответил\|ответила\|ответили\|спро |
| 127 | функция | `_clean_turn(raw)` | Речь реплики без сегментов атрибуции. |
| 150 | функция | `_signature(text)` |  |
| 167 | функция | `_similar_signature(a, b)` |  |
| 186 | класс | `TSTPLDetector (4 публичных методов)` | Mechanical detector for TST-PL polyphony/autonomous voice risks. |

## tst_trk_detector

- **путь**: `engine/tst_trk_detector.py`
- **размер**: 180 строк, SHA-256 blob `c0acecce9341c39d…`
- **что это**: tst_trk_detector.py — TST-TRK: Truth-State / Tracking Test.
- **зачем**: Источник: АК-6.8, «TST — ГЛУБОКИЕ ТЕСТЫ СЦЕНЫ»: TST-TRK — Truth-State / Tracking Test Функция: long-form контроль вероятностной и нарративной целостности. Связь: Block 13, SSC-CHAR, POV knowledge, unpaid prices, two-readings continuity. FAIL_IF: - новая сцена нарушает уже установленный статус знания персонажа; - цена героя забыта; - TST-DV был жив, но следующая глава закрыла его без авторского решения; - ЭВ-долг не перенесён между главами. OUTPUT: PASS / TST-TRK_FAIL / HITL_AUTHOR_INTENT Этого теста не было в репозитории вообще (прове…
- **коды состояний** (1): `HITL_AUTHOR_INTENT`
- **тесты, которые зовут модуль**: 2 — `tests/test_block6_tst_suite_enforcement.py`, `tests/test_tst_trk_detector.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 35 | константа | `Status` |  |
| 39 | класс | `TrackingFinding (1 публичных методов)` |  |
| 48 | класс | `TSTTRKReport (1 публичных методов)` |  |
| 56 | функция | `check_character_knowledge_continuity(character, established_knowledge, scene_claims_unknown)` | FAIL_IF #1: новая сцена нарушает уже установленный статус знания |
| 80 | функция | `check_hero_price_not_forgotten(price_established, referenced_in_scene)` | FAIL_IF #2: цена героя забыта — Закон Z (Блок 3) установил цену, но |
| 97 | функция | `check_tst_dv_not_closed_silently(was_open, closed_in_scene, author_confirmed_closure)` | FAIL_IF #3: TST-DV был жив, но следующая глава закрыла его без |
| 117 | функция | `check_ev_debt_carried(ev_debt_from_previous_chapter, carried_in_scene)` | FAIL_IF #4: ЭВ-долг не перенесён между главами — если предыдущая |
| 135 | функция | `check_scene_tracking()` | Свести все четыре FAIL_IF канона в один вердикт для сцены. |

## tst_tw_detector

- **путь**: `engine/tst_tw_detector.py`
- **размер**: 161 строк, SHA-256 blob `96b6dfae9f7d3880…`
- **что это**: tst_tw_detector.py — TST-TW: Тест Твардовского (враждебный читатель).
- **зачем**: Source: AK-MASTER v6.7, Block 2.1 — голос ТВАРДОВСКИЙ: "Текст выдержит враждебного?" Триггер вето: "Прямые декларации вместо действия. Активен при сатире и SCN-15." Found during full canon-vs-code audit (30 June 2026): TST-TW was referenced throughout the codebase (satire_gate.py, output_auditor.py, demo_scenarios.py, api/models.py, api/service.py) as a `tst_tw_passed: bool` parameter ACCEPTED from outside, but the actual test was never implemented anywhere — no function computed it. Every caller had to manually supply a gue…
- **коды состояний** (8): `HIGH`, `MEDIUM`, `NOT_CONFIGURED`, `TST_TW_HOSTILE_READER_FAIL`, `TST_TW_UNCERTAIN_WITH_DECLARATION_MARKERS`, `UNCERTAIN`, `WARN`, `YES`
- **тесты, которые зовут модуль**: 3 — `tests/test_canon_mode_test_applicability.py`, `tests/test_tst_tw_detector.py`, `tests/test_судья_не_зовётся_без_спроса.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 42 | константа | `DECLARATION_MARKERS_RE` | re.compile('\\b(мораль (?:такова\|в том)\|автор хочет сказать\|читатель должен поня |
| 52 | класс | `TSTTWFinding (1 публичных методов)` |  |
| 62 | класс | `TSTTWDetector (1 публичных методов)` | TST-TW — Тест Твардовского: выдержит ли текст враждебного, |

## tts_checklist

- **путь**: `engine/tts_checklist.py`
- **размер**: 161 строк, SHA-256 blob `ac17e1caa6139153…`
- **что это**: tts_checklist.py — Module 5 (ear-pass), mechanism 4: intentional anomalies.
- **зачем**: The reader prepares by ear (TTS). Some irregularities are DELIBERATE — an interrupted word cut off mid-syllable («Войце—»), a degraded refrain («не наступа…»), a spaced-out shout («с т о й»), an emphatic all-caps system line. A mechanical checker (or a Word grammar pass) sees these as errors and wants to "fix" them; fixing them silently destroys the device. This mechanism is the author-owned «hands-off» registry, and it does three things: 1. Detects candidate anomalies in the text (interrupted words, stretched sounds, …
- **коды состояний** (9): `AUDIBLE`, `EMPHASIS_CAPS`, `FLAG`, `INTERRUPTED_WORD`, `LOST_INTENTIONAL`, `PHRASE`, `SPACED_LETTERS`, `STRETCHED_SOUND`, `UNDECLARED_ANOMALY`
- **тесты, которые зовут модуль**: 2 — `tests/test_tts_checklist.py`, `tests/test_tts_stage_a.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 35 | константа | `_HEADING_RE` | re.compile('(?m)^#{1,3}\\s') |
| 38 | класс | `AnomalyKind (0 публичных методов)` |  |
| 47 | константа | `_PATTERNS` | dict, 4 элементов |
| 59 | класс | `IntentionalAnomaly (0 публичных методов)` | A declaration that something is deliberate. Either a whole `kind` |
| 68 | класс | `TTSFinding (1 публичных методов)` |  |
| 81 | класс | `TTSReport (1 публичных методов)` |  |
| 91 | класс | `TTSChecklistAuditor (3 публичных методов)` | Intentional-anomaly registry + detector + hands-off surface. |

## tts_registry_den_arbuza

- **путь**: `engine/tts_registry_den_arbuza.py`
- **размер**: 21 строк, SHA-256 blob `2179c278fe68bba4…`
- **что это**: tts_registry_den_arbuza.py — intentional-anomaly registry for «День
- **зачем**: Арбуза». Editable data. Declares which textual irregularities are deliberate so the mechanical auditors leave them alone, and so their disappearance in a later draft is caught. Verified against v11.1: interrupted speech (6 words broken off by em-dash) and the degraded refrain «не наступа…» are present and protected
- **тесты, которые зовут модуль**: 1 — `tests/test_tts_checklist.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 11 | константа | `TTS_REGISTRY` | list, 3 элементов |

## tts_segmenter

- **путь**: `engine/tts_segmenter.py`
- **размер**: 208 строк, SHA-256 blob `47e05cfeed1e3cd5…`
- **что это**: Сегментация сцены для озвучки (TTS Stage A/B, 2026-07-16).
- **зачем**: Источник архитектуры: два присланных автором исследования интеграции TTS в 101. Ключевые решения, взятые оттуда (и проверенные против нашего кода): - иерархия «сцена = единица задания и кэша; абзац/реплика = единица синтеза; предложение = единица анализа» — совпадает с тем, как уже мыслят rhythm_auditor (предложения) и construction_echo (соседние абзацы/реплики); - НИКОГДА не склеивать сегменты через смену говорящего, заголовок или явный разрыв сцены (---): construction_echo ловит зачины именно на этих границах, склейка их разрушила бы…
- **коды состояний** (4): `EMPHASIS_CAPS`, `INTERRUPTED_WORD`, `SPACED_LETTERS`, `STRETCHED_SOUND`
- **тесты, которые зовут модуль**: 1 — `tests/test_tts_stage_a.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 40 | константа | `SEGMENT_TARGET_MIN` |  |
| 41 | константа | `SEGMENT_TARGET_MAX` |  |
| 43 | константа | `_HEADING_RE` | re.compile('^\\s{0,3}#{1,6}\\s+\\S') |
| 44 | константа | `_SCENE_BREAK_RE` | re.compile('^\\s*(?:---+\|\\*\\s*\\*\\s*\\*)\\s*$') |
| 45 | константа | `_DIALOGUE_RE` | re.compile('^\\s*—\\s?\\S') |
| 46 | константа | `_SENT_SPLIT_RE` | re.compile('(?<=[.!?…])\\s+') |
| 47 | константа | `_ATTRIBUTION_RE` | re.compile('\\b(?P<verb>сказал\|сказала\|спросил\|спросила\|ответил\|ответила\|крикнул |
| 54 | константа | `_FEMALE_ATTRIBUTIONS` | set, 9 элементов |
| 61 | класс | `TTSSegment (1 публичных методов)` | Единица синтеза: один запрос к провайдеру. |
| 79 | функция | `_paragraph_kind(par)` |  |
| 89 | функция | `_is_protected(text, registry)` | Причины hands-off для сегмента: какие задекларированные аномалии |
| 110 | функция | `_dialogue_speaker(text)` | Best-effort attribution without inventing character identities. |
| 127 | функция | `_split_long(par, hard_limit)` | Абзац длиннее лимита -> резать по предложениям, наполняя куски |
| 146 | функция | `segment_scene(text, registry, provider_hard_limit)` | Сцена -> план сегментов озвучки + метаданные манифеста. |

## volume_neutrality

- **путь**: `engine/volume_neutrality.py`
- **размер**: 140 строк, SHA-256 blob `416ba7d0e89000d5…`
- **что это**: volume_neutrality.py — коэффициент нейтральности объёма (VNR).
- **зачем**: БОЛЬШЕ, чем было: добавляет пояснения, связки, вежливые уточнения. Через несколько таких правок текст раздувается, а плотность падает — то самое «графит вместо алмаза» из Блока 10.2. Метрика ставит этому предел арифметически: если правка добавила больше, чем убрала, это не правка, а прирост объёма, и канон такую правку не принимает.
- **коды состояний** (2): `NOT_APPLICABLE`, `VNR`
- **тесты, которые зовут модуль**: 1 — `tests/test_volume_neutrality.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 33 | константа | `VNR_LIMIT` |  |
| 35 | константа | `CANON_RULE` | строка: «Volume Neutrality Ratio = (добавленных символов) / (удалённых символов» |
| 43 | класс | `VolumeNeutralityResult (1 публичных методов)` |  |
| 59 | функция | `_added_deleted(original, edited)` | Сколько символов добавлено и сколько удалено. |
| 78 | функция | `volume_neutrality(original, edited)` | VNR для пары «до правки → после правки». |

## vrp_arbitrator

- **путь**: `engine/vrp_arbitrator.py`
- **размер**: 68 строк, SHA-256 blob `bad366567c7c586d…`
- **коды состояний** (3): `ACTIVE`, `NOT_ACTIVE`, `NO_RULE`
- **тесты, которые зовут модуль**: 2 — `tests/test_ak_discipline_engine.py`, `tests/test_canon_point_fixes.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 12 | константа | `_SCN_ONLY_RE` | re.compile('только\\s+при\\s+(SCN-\\d{2})', re.I) |
| 13 | константа | `_SCN_MENTION_RE` | re.compile('SCN-\\d{2}') |
| 16 | функция | `_scn_condition(rule)` | Вернуть SCN-код, которым правило ограничено, либо None (без условия). |
| 29 | класс | `VRPArbitrator (1 публичных методов)` |  |

## vrp_graph

- **путь**: `engine/vrp_graph.py`
- **размер**: 323 строк, SHA-256 blob `b60f1bf3f1631be6…`
- **что это**: vrp_graph.py — нормализованный граф VRP-арбитража
- **зачем**: АК v6.7 Блок 5 Проблема старого VRPArbitrator: - поиск по тексту поля 'Векторы' — хрупко, зависит от порядка слов в YAML - при изменении YAML арбитраж ломается молча без ошибки Это решение: - строит словарь {frozenset(veto_pair) → rule} при инициализации - lookup не зависит от порядка кодов - специальные правила (VRP-4 "любой", VRP-X1 "мета-взлом") обрабатываются отдельно - все конфликты без точного правила возвращаются автору явно
- **коды состояний** (4): `NOT_ACTIVE`, `NO_RULE`, `PARTIAL`, `RESOLVED`
- **тесты, которые зовут модуль**: 4 — `tests/test_integration_v05.py`, `tests/test_llm_judge_vrp.py`, `tests/test_v05_modules.py`, `tests/test_vrp_procedural_rules.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 29 | константа | `_WILDCARD_VTO_D` | строка: «VTO-D» |
| 32 | константа | `_META_BREAK_MARKER` | строка: «META-ВЗЛОМ» |
| 37 | функция | `_parse_vector_codes(vector_str)` | Извлекает коды из строки вида 'VTO-P ↔ VTO-K' или 'VTO-D ↔ SYN-MC/SYN-ZW'. |
| 71 | класс | `VRPRule (0 публичных методов)` |  |
| 81 | класс | `ArbitrationResult (0 публичных методов)` |  |
| 99 | класс | `VRPGraph (4 публичных методов)` | Нормализованный граф VRP-арбитража. |

## vto_router

- **путь**: `engine/vto_router.py`
- **размер**: 181 строк, SHA-256 blob `6de0dfc149abafee…`
- **что это**: vto_router.py — Source-locked VTO router for AK v6.7 Block 2.
- **зачем**: This is not a new literary judge. It routes already-detected risks into the AK Board of Directors hierarchy: VTO-P, VTO-K, VTO-H, VTO-D, TST-PL, TST-DR, TST-TW, TST-MR
- **коды состояний** (4): `BLOCKED`, `HIGH`, `MEDIUM`, `WARN`
- **тесты, которые зовут модуль**: 14 — `tests/test_adversarial_vto_council.py`, `tests/test_block2_vto_enforcement.py`, `tests/test_canon_block_registry.py`, `tests/test_canon_mode_test_applicability.py`, `tests/test_council_of_eight_in_audit.py`, `tests/test_council_operational_tools.py`…

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 32 | константа | `BODY_RE` | re.compile('\\b(горло\|кожа\|пальц\|ладон\|запах\|металл\|желч\|зуб\|плеч)\\w*\\b', re.I |
| 33 | константа | `BODY_LEMMAS` | set, 25 элементов |
| 42 | функция | `_body_hit(text)` |  |
| 47 | константа | `ABSTRACT_EMOTION_RE` | re.compile('\\b(страдал\|страдание\|ужас\|тревог\|грусть\|было\\s+страшно\|было\\s+бол |
| 48 | константа | `ABSTRACT_EMOTION_LEMMAS` | set, 1 элементов |
| 51 | функция | `_abstract_emotion_hit(text)` |  |
| 56 | константа | `MIRACLE_RE` | re.compile('\\b(?:чудо\\w*\|маги[яеюи]\\w*\|аномал\\w*\|невозможн\\w*\|портал\\w*\|пр |
| 64 | константа | `PRICE_RE` | re.compile('\\b(заплат\|потер\|последств\|стоило\|жертва\|риск\|невозврат\|энтроп\|сожр) |
| 68 | константа | `PRICE_LEMMAS_VTO` | set, 2 элементов |
| 69 | константа | `SCIENCE_RE` | re.compile('\\b(наука\|квант\|энтроп\|термодинами\|нейрон\|сигнал\|теор\|формул\|энерг\|г |
| 70 | константа | `SCIENCE_LEMMAS` | set, 2 элементов |
| 73 | функция | `_science_hit(text)` |  |
| 75 | константа | `SCALE_RE` | re.compile('\\b(масштаб\|бесконеч\|зв[её]зд\|космос\|вселенн\|бездна\|вечност\|миллиард |
| 76 | константа | `UNCHANGED_HERO_RE` | re.compile('\\b(герой\\s+остал\\w*\\s+прежн\|ничего\\s+не\\s+изменил\\w*\|вернул\\ |
| 78 | константа | `HIERARCHIES` | dict, 15 элементов |
| 98 | константа | `DEFAULT_HIERARCHY` | list, 4 элементов |
| 101 | класс | `VTOFinding (0 публичных методов)` |  |
| 109 | функция | `_norm_scn(scn_code)` |  |
| 121 | класс | `VTORouter (2 публичных методов)` |  |

## vto_tribunal

- **путь**: `engine/vto_tribunal.py`
- **размер**: 107 строк, SHA-256 blob `32453c9689d36f3b…`
- **коды состояний** (1): `UNKNOWN_VETO`
- **тесты, которые зовут модуль**: 5 — `tests/test_ak_discipline_engine.py`, `tests/test_canon_point_fixes.py`, `tests/test_scn_rt_acceptance.py`, `tests/test_vto_council_roster.py`, `tests/test_vto_tribunal_scene_hierarchy.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 7 | функция | `_clean_vto_code(value)` |  |
| 13 | класс | `VTOTribunal (2 публичных методов)` |  |

## world_ledger

- **путь**: `engine/world_ledger.py`
- **размер**: 421 строк, SHA-256 blob `d5a4f682d92b1834…`
- **что это**: world_ledger.py — PHYSICS_LEDGER / TEMPORAL_LEDGER / MEMORY_LEDGER.
- **зачем**: Источник: AK-6.8 (Правило 0.1.1, OG-1.1, Блок 14.4.1 TIME REGRESSION), мандаторная последовательность, шаг 9 — LEDGER_PRECHECK: «До PROMPT_PACKET проверить PHYSICS_LEDGER → TEMPORAL_LEDGER → MEMORY_LEDGER. Прямое противоречие зарегистрированной аксиоме мира блокирует генерацию; неоднозначность переводится в NON_LIQUET/HITL.» Этого слоя раньше не было вообще — конструкт не сверял новую сцену ни с аксиомами мира, ни с уже зарегистрированными временными/фактическими данными рукописи. Найдено на «Игле» двумя живыми случаями: 1. ME…
- **коды состояний** (7): `BLOCKED_CANON_VIOLATION`, `CONFLICT`, `LEDGER_PRECHECK`, `NON_LIQUET`, `NO_DATA`, `RESOLVED_BY_CORRECTION`, `WARN_TIME_REGRESSION`
- **тесты, которые зовут модуль**: 3 — `tests/test_specificity_algebra_rq2.py`, `tests/test_world_ledger.py`, `tests/test_время_интервалы.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 51 | константа | `TEMPORAL_ENVIRONMENTS` | tuple, 5 элементов |
| 59 | класс | `WorldAxiom (0 публичных методов)` | АКСИОМА МИРА level=0 (Правило 0.1.1) — явно установленный повторяемый |
| 74 | класс | `PhysicsLedger (3 публичных методов)` | Правило 0.1.1 — PHYSICS_LEDGER_CHECK. |
| 154 | класс | `TemporalMarker (0 публичных методов)` |  |
| 164 | класс | `TemporalLedger (4 публичных методов)` | OG-1.1 (Temporal Environment) + FM-OG-09/FM-OG-10. |
| 314 | класс | `MemoryFact (0 публичных методов)` |  |
| 323 | класс | `MemoryLedger (3 публичных методов)` | MEMORY_LEDGER — узкий предгенерационный шлюз по фактам рукописи. |
| 372 | класс | `LedgerPrecheck (1 публичных методов)` | Мандаторная последовательность, шаг 9 — LEDGER_PRECHECK. |

## время_интервалы

- **путь**: `engine/время_интервалы.py`
- **размер**: 246 строк, SHA-256 blob `7a01db0dd492d3b5…`
- **что это**: время_интервалы.py — интервальная алгебра Аллена и две оси времени.
- **зачем**: ## ОТКУДА ПРАВИЛО Владелец 06.09.2026 прислал исследование «Архитектура детерминированного литературного движка» и попросил взять оттуда лучшее, но так, чтобы конструкт «не галлюцинировал и не путал сам себя». Разбор исследования — `docs/РАЗБОР_ИССЛЕДОВАНИЯ_РЕПОЗИТОРИЕВ.md`. Коротко: все четыре названных репозитория существуют, но клонировать нельзя ни один (графовая СУБД и вызовы LLM у одного, TypeScript и Rust у двух, одиночный проект у четвёртого), а **три архитектурные роли из четырёх в движке уже построены** — `cdr_graph.…
- **коды состояний** (1): `WARN`
- **тесты, которые зовут модуль**: 2 — `tests/test_mcp101_product.py`, `tests/test_время_интервалы.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 64 | константа | `ИСТОЧНИК` | строка: «Интервальная алгебра Аллена (1983); разделение fabula/syuzhet — docs/Р» |
| 69 | константа | `ОТНОШЕНИЯ_ПО_РУССКИ` | dict, 13 элементов |
| 86 | константа | `ВНУТРИ` | frozenset({'during', 'starts', 'finishes', 'equals'}) |
| 90 | класс | `Интервал (0 публичных методов)` | Отрезок фабульного времени. Точка — это отрезок нулевой длины. |
| 103 | функция | `отношение(a, b)` | Одно из тринадцати отношений Аллена между A и B. |
| 134 | функция | `по_русски(имя)` |  |
| 139 | класс | `Событие (0 публичных методов)` | Событие на двух осях сразу. |
| 156 | функция | `проверить(события, сцены)` | Три вопроса к хронологии: смерть, вложенность, объявленность. |

## запрещённое_дословно

- **путь**: `engine/запрещённое_дословно.py`
- **размер**: 287 строк, SHA-256 blob `edf3bd85336107b1…`
- **что это**: запрещённое_дословно.py — ПОЛЕ 5 шлюза 10.1, та его половина, что считается.
- **зачем**: Заведено 17.09.2026, участок «канон: непостроенное». ## Что было и чего не хватало Правило `Б10.1-объяснение` реестра канона требует (канон, строки 165–181 · 3889 · 4513): «ПОЛЕ 5: назвать, что запрещено объяснять». Автор называет это в паспорте книги, поле `forbidden_to_explain`, и поле доезжает до движка целиком — от `manuscripts/паспорта/*.json` через `AuditRequest` до `engine/explanation_gate.py`. Дальше стояла стена: **вся сверка текста с объявленным запретом уходила к смысловому судье**. Без ключа `declared_forb…
- **коды состояний** (3): `NOT_APPLICABLE`, `NOT_DECLARED`, `WARN`
- **тесты, которые зовут модуль**: 3 — `tests/test_запрещённое_дословно.py`, `tests/test_контракты_глав_доходят_до_проверки.py`, `tests/test_судья_фаулз.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 97 | константа | `_В_КАВЫЧКАХ` | re.compile('[«\\"„]([^»\\"“„]{2,60})[»\\"“]', re.U) |
| 101 | константа | `_МАРКЕР_СЛОВА` | re.compile('\\bслов(?:ами\|ом\|о\|а)\\b', re.I \| re.U) |
| 105 | константа | `_ПЕРЕД_ТЕРМИНОМ` | re.compile('(?:что\\s+(?:такое\|значит\|означает\|значило\|означало\|за)\|чем\\s+(?:яв |
| 109 | константа | `_ОПРЕДЕЛЕНИЕ` | re.compile('(?:\\s[—–-]\\s*это\\b\|\\bэто\\s+(?:значит\|означает\|значило\|означало) |
| 113 | константа | `_ГРАНИЦА` | re.compile('(?<=[.!?…])\\s+', re.U) |
| 116 | функция | `_нормализовать(s)` | ё→е и схлопнутые пробелы: «ещё» и «еще» — одно и то же место текста. |
| 121 | функция | `дословные_запреты(forbidden_to_explain)` | Закавыченные формулировки, которые автор запретил ДОСЛОВНО. |
| 159 | функция | `найти(text, forbidden_to_explain)` | Вхождения дословно запрещённых формулировок, с предложением-контекстом. |
| 186 | константа | `_ТЕРМИН_ПРОЗОЙ` | tuple, 3 элементов |
| 193 | функция | `_термины_прозой(запрет)` |  |
| 203 | функция | `_образец_термина(термин)` | «санация» найдёт «санации», «Арбитры» — «Арбитров»: основа + хвост. |
| 214 | функция | `найти_определения(text, forbidden_to_explain)` | Термин под запретом стоит в одном предложении с определением. |
| 238 | функция | `audit(text, forbidden_to_explain)` | Бесплатная половина ПОЛЯ 5: сверка текста с ДОСЛОВНЫМ запретом автора. |

## канон_в_кэше

- **путь**: `engine/канон_в_кэше.py`
- **размер**: 228 строк, SHA-256 blob `379ef36df70faee6…`
- **что это**: канон_в_кэше.py — канон уезжает к Vertex ОДИН раз, а не в каждом вызове.
- **зачем**: ============================
- **коды состояний** (9): `AK_DATA_DIR`, `AK_JUDGE_CANON_CACHE`, `AK_JUDGE_CANON_CACHE_TTL`, `CANON_CACHE_CREATED`, `CANON_CACHE_DISABLED`, `CANON_CACHE_ERROR`, `CANON_CACHE_NOT_CONFIGURED`, `CANON_CACHE_REUSED`, `CANON_CACHE_TOO_SMALL`
- **тесты, которые зовут модуль**: 1 — `tests/test_канон_в_кэше.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 76 | константа | `logger` | logging.getLogger('ak_master.канон_в_кэше') |
| 79 | константа | `НЕ_НАСТРОЕН` | строка: «CANON_CACHE_NOT_CONFIGURED» |
| 80 | константа | `ВЫКЛЮЧЕН` | строка: «CANON_CACHE_DISABLED» |
| 81 | константа | `МАЛ` | строка: «CANON_CACHE_TOO_SMALL» |
| 82 | константа | `ОШИБКА` | строка: «CANON_CACHE_ERROR» |
| 83 | константа | `СОЗДАН` | строка: «CANON_CACHE_CREATED» |
| 84 | константа | `ПОВТОРНО` | строка: «CANON_CACHE_REUSED» |
| 90 | константа | `TTL_СЕКУНД` | int(os.getenv('AK_JUDGE_CANON_CACHE_TTL', '3600')) |
| 93 | функция | `включён()` | Тумблер. Выключается переменной, а не правкой кода. |
| 99 | функция | `_реестр_путь()` | Где помнится соответствие «этот канон → этот кэш». |
| 113 | функция | `ключ(канон, модель, регион)` | Отпечаток кэша. |
| 130 | функция | `_прочитать_реестр()` |  |
| 138 | функция | `_записать_реестр(данные)` |  |
| 150 | функция | `_жив(запись)` | Не истёк ли кэш. |
| 168 | функция | `имя_для(канон, модель)` | (имя_кэша, причина). Пустое имя — причина названа словами. |

## невидимые_символы

- **путь**: `engine/невидимые_символы.py`
- **размер**: 170 строк, SHA-256 blob `4734d161c58846ca…`
- **что это**: невидимые_символы.py — мусор, которого не видно глазом, но который слепит движок.
- **зачем**: ## КАК ЭТО НАШЛОСЬ (07.09.2026) Замер 38 паттернов машинного текста (`scripts/замер_ai_следов.py`) дал по библиотеке 392 «артефакта чат-бота». Триста девяносто из них оказались одним и тем же символом — **U+200B, ZERO WIDTH SPACE**, а 363 из этих 390 лежали в одной книге: «Нью-Кайрос 1. Стальные Тени (издание B, 1-е лицо)». Той самой, про которую владелец сказал: «местами хорошо, красиво, грамотно — но не всё». ## ЧЕМ ЭТО ОКАЗАЛОСЬ НА САМОМ ДЕЛЕ Все 363 стоят в НАЧАЛЕ абзацев — след копирования из веб-редактора. …
- **коды состояний** (1): `WARN`
- **тесты, которые зовут модуль**: 3 — `tests/test_blindspot_orchestrator.py`, `tests/test_book_passport.py`, `tests/test_невидимые_символы.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 53 | константа | `ИСТОЧНИК` | строка: «Замер 07.09.2026: 392 находки по библиотеке, 363 из них — U+200B в «Ст» |
| 59 | константа | `УДАЛЯЕМЫЕ` | dict, 7 элементов |
| 71 | константа | `В_ПРОБЕЛ` | dict, 5 элементов |
| 79 | константа | `_УДАЛИТЬ` | re.compile('[' + ''.join(УДАЛЯЕМЫЕ) + ']') |
| 80 | константа | `_В_ПРОБЕЛ` | re.compile('[' + ''.join(В_ПРОБЕЛ) + ']') |
| 83 | функция | `очистить(текст)` | Копия текста без невидимого мусора. Рукопись не трогается. |
| 94 | функция | `найти(текст)` | Сколько невидимок, каких и где. Молчать о них нельзя. |
| 137 | функция | `_в_находку(место, в_словах)` |  |
| 158 | функция | `_показать(текст, позиция, вокруг)` | Кусок текста с пометкой на месте невидимки — иначе цитата пуста. |
| 167 | функция | `_в_начале_абзацев(текст, символ)` | Сколько раз символ стоит первым в абзаце — самый вредный случай. |

## платонов_правила

- **путь**: `engine/платонов_правила.py`
- **размер**: 129 строк, SHA-256 blob `f66fa931c08531b3…`
- **что это**: платонов_правила.py — частота и правила стиля Платонова по рассказам.
- **зачем**: Решение автора 11.10.2026: рассказов достаточно, романы («Котлован», «Чевенгур») не нужны. Профиль снят `scripts/платонов_профиль.py` (`data/платонов_профиль.json`: числа и частотные списки, чужого текста нет). Модуль сравнивает ТЕКСТ с этим профилем и говорит словами, где он расходится. Это сведение, не приговор
- **коды состояний** (1): `NOUN`
- **тесты, которые зовут модуль**: 1 — `tests/test_подсказчик_сочетаемости.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 23 | константа | `_ФАЙЛ` |  |
| 24 | константа | `_СЛОВО` | re.compile('[А-Яа-яЁё]+(?:-[А-Яа-яЁё]+)?') |
| 25 | константа | `_ОТВЛЕЧЁННЫЕ` | set, 15 элементов |
| 27 | константа | `_морф` |  |
| 31 | функция | `профиль()` |  |
| 35 | функция | `_лемма(с)` |  |
| 44 | функция | `_числа(текст)` |  |
| 66 | константа | `_ПРАВИЛА` | dict, 4 элементов |
| 84 | функция | `частотное_сходство(текст, топ)` | Косинус между частотой существительных текста и топ-N Платонова (0–1). |
| 99 | функция | `сравнить_с_платоновым(текст)` |  |
| 121 | функция | `правила_для_запроса()` | Короткая памятка в запрос генерации, когда сцена идёт кодом SYN-PL. |

## погода_по_весу

- **путь**: `engine/погода_по_весу.py`
- **размер**: 140 строк, SHA-256 blob `bd37d0d906a5855b…`
- **что это**: погода_по_весу.py — заявленная погода против того, чего она стоит.
- **зачем**: ## ОТКУДА ПРАВИЛО. СЛУХ АВТОРА, 06.09.2026 > «вес заявленной погоды не соответствует действительности, нету никакой > значимости в этом… сама погода не стоит в заявленной какой-то кислотной > или атмосферной неприязни — кроме капель, которые на кожу падают. > Самое лучшее воспроизведение — "Заводские настройки", тот рассказ, где > погода красиво легла» Проверено по тому 1, и автор прав до цифры. **82 абзаца с погодой, тело названо в 26 (32%).** Слово «кислотный» звучит семь раз, и вот куда: за бронестеклом / бьёт в бронестекло …
- **тесты, которые зовут модуль**: 2 — `tests/test_mcp101_product.py`, `tests/test_погода_по_весу.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 58 | константа | `ИСТОЧНИК` | строка: «Решение автора 06.09.2026 о весе погоды; эталон — manuscripts/перерабо» |
| 63 | константа | `ПОГОДА` | re.compile('\\b(дожд\\w*\|ливн\\w*\|ливень\|морос\\w*\|небо\|неба\|небе\|туман\\w*\|вете |
| 69 | константа | `ВРАЖДЕБНОСТЬ` | re.compile('\\b(кислотн\\w+\|кислот\\w+\|разъеда\\w+\|едк\\w+\|ядовит\\w+\|яд\|токсичн |
| 74 | константа | `ТЕЛО` | re.compile('\\b(кож\\w+\|лиц\\w+\|лицо\|щек\\w+\|ше[яеиюй]\\w*\|горл\\w+\|ладон\\w+\|па |
| 84 | функция | `_абзацы(текст)` |  |
| 88 | функция | `проверить(главы)` | главы: [(имя, текст)]. Аудит идёт ПО КНИГЕ — у погоды срок жизни |

## подпись_синтаксиса

- **путь**: `engine/подпись_синтаксиса.py`
- **размер**: 341 строк, SHA-256 blob `4f4c3e74b5d38ba3…`
- **что это**: подпись_синтаксиса.py — ритм прозы числом, против живой базы.
- **зачем**: Владелец, дословно: «зачем тебе тогда книги Платонова, которые я тебе скачивал, и Денисова сборник… ты делал модули — где работающие модули для прозы? Я не вижу реальной работы, что что-то заработало».
- **тесты, которые зовут модуль**: 2 — `tests/test_mcp101_product.py`, `tests/test_подпись_синтаксиса.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 90 | константа | `ПОДЧИНЕНИЕ` | re.compile('\\b(что\|чтобы\|котор[а-яё]+\|потому что\|оттого что\|так как\|как будто\|с |
| 95 | константа | `_СЛОВО` | re.compile('[А-Яа-яЁёA-Za-z]+') |
| 96 | константа | `_КОНЕЦ` | re.compile('(?<=[.!?…])\\s+') |
| 100 | константа | `_РЕПЛИКА` | re.compile('^\\s*(?:[—–]\\s*\|-\\s+)') |
| 105 | константа | `КОРОТКОЕ` |  |
| 106 | константа | `ДЛИННОЕ` |  |
| 107 | константа | `ОЧЕНЬ_ДЛИННОЕ` |  |
| 111 | класс | `Подпись (1 публичных методов)` | Измеренный профиль. Только числа — чужого текста здесь нет. |
| 131 | класс | `Подписи (0 публичных методов)` | Три подписи одного текста: всё / проза / реплики (M28). |
| 145 | функция | `_разделить(текст)` | (проза, реплики) — по предложениям, на которые указывает тире. |
| 159 | функция | `_предложения(текст)` |  |
| 169 | функция | `снять_подпись(текст, имя)` | Измерить синтаксис текста. Пустой текст даёт нулевую подпись. |
| 209 | константа | `ПЛАТОНОВ` | Подпись(имя='Платонов, рассказы (тома 1–8)', предложений=19251, слов=261000, сре |
| 224 | функция | `снять_подписи(текст, имя)` | Три подписи одного текста: всё / проза / реплики. |
| 240 | функция | `сравнить_с_эталоном(подписи, эталон)` | Расхождение с эталоном ТОЛЬКО по авторской речи, не по всему тексту. |
| 248 | константа | `_ПОКАЗАТЕЛИ` | tuple, 6 элементов |
| 258 | функция | `сравнить(книга, эталон)` | Чем книга расходится с эталоном. Список, отсортированный по разрыву. |
| 285 | функция | `отчёт(подписи, эталон)` | Готовая таблица для человека. По-русски, потому что читает автор. |
| 340 | функция | `эталон_предложений(эталон)` |  |

## подсказчик_сочетаемости

- **путь**: `engine/подсказчик_сочетаемости.py`
- **размер**: 49 строк, SHA-256 blob `48c7ec73747d1225…`
- **что это**: подсказчик_сочетаемости.py — слово → что с ним обычно стоит (Денисов).
- **зачем**: Решение владельца 11.10.2026: Денисов и Платонов не «детектор ошибок», а рабочий инструмент автора. Измерение 13.09 показало, что словарь (2031 статья) нельзя использовать как «нет в словаре — значит ошибка»; здесь он используется наоборот: автор видит, ЧТО УЖЕ ЗАНЯТО, и идёт мимо или берёт. Бесплатно, без модели
- **коды состояний** (2): `FOUND`, `NOT_FOUND`
- **тесты, которые зовут модуль**: 1 — `tests/test_подсказчик_сочетаемости.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 17 | константа | `_ФАЙЛ` |  |
| 18 | константа | `_МУСОР` | re.compile('[�]') |
| 22 | функция | `_статьи()` |  |
| 29 | функция | `_чисто(слова)` |  |
| 33 | функция | `подсказать(слово, лимит)` | Статья слова: модели управления и спутники. Нет статьи — так и говорим. |

## профили_авторов

- **путь**: `engine/профили_авторов.py`
- **размер**: 194 строк, SHA-256 blob `2016f5472ec01055…`
- **что это**: профили_авторов.py — профиль стиля автора по его книгам (числа, не текст).
- **зачем**: Общий инструмент по образцу Платонова (11.10.2026): автор присылает книги (Янси, Рейнольдс…), `scripts/профиль_автора.py` снимает профиль, а этот модуль сравнивает ЛЮБОЙ текст с профилем: ритм, диалог, действие, мрачность, резкость. Чужой текст не хранится — только числа и частотные списки
- **коды состояний** (4): `ADJF`, `INFN`, `NOUN`, `VERB`
- **тесты, которые зовут модуль**: 1 — `tests/test_профили_авторов.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 17 | константа | `ПАПКА` |  |
| 19 | константа | `_СЛОВО` | re.compile("[A-Za-zА-Яа-яЁё]+(?:['’-][A-Za-zА-Яа-яЁё]+)?") |
| 20 | константа | `_КОНЕЦ` | re.compile('(?<=[.!?…])\\s+') |
| 21 | константа | `_РЕПЛИКА_ТИРЕ` | re.compile('^\\s*[—–-]\\s+(.+)$', re.M) |
| 22 | константа | `_РЕПЛИКА_КАВ` | re.compile('[«“\\"]([^»”\\"]{2,400})[»”\\"]') |
| 25 | константа | `МРАЧНЫЕ` | tuple, 46 элементов |
| 31 | константа | `_СТОП_EN` | set('the a an and of to in that was is it he she his her i you they we with for  |
| 36 | функция | `_мрачность(слова)` |  |
| 43 | функция | `реплики(текст)` |  |
| 49 | константа | `_СРАВНЕНИЯ` | re.compile('\\b(?:как будто\|словно\|будто\|точно\|подобно\|like\|as if)\\b\|\\bкак\\b' |
| 50 | константа | `_РЕМАРКА` | re.compile('[—–]\\s*(?:[А-Яа-яЁё]+(?:ал\|ила\|ил\|ел\|ла\|ли\|ся\|ась\|ёл)\\b)', re.I) |
| 53 | функция | `_имена(текст)` | Формы слов, которые почти всегда пишутся с заглавной ВНУТРИ предложения — |
| 63 | функция | `_леммы(слова, сколько, имена)` | Частотные леммы по частям речи (только кириллица; pymorphy3). |
| 84 | функция | `снять(текст, имя, леммы)` |  |
| 133 | функция | `загрузить(slug)` |  |
| 137 | функция | `доступные()` |  |
| 141 | константа | `_ЯРЛЫКИ` | dict, 13 элементов |
| 158 | функция | `сравнить(текст, slug)` |  |
| 178 | константа | `АВТОР_ПО_SYN` | dict, 3 элементов |
| 181 | функция | `памятка(slug)` | Короткая памятка в запрос генерации по ЧИСЛАМ профиля автора. |

## птср_соматика

- **путь**: `engine/птср_соматика.py`
- **размер**: 197 строк, SHA-256 blob `36e880dd3161f01c…`
- **что это**: птср_соматика.py — подмодуль ПТСР: тело в сцене стресса и травмы.
- **зачем**: Источник — PDF владельца «PTSD-SOMATIC-PIPELINE» (20.10.2026). Взят узко, по решению владельца: пять правил и список штампов. Что взято, что нет и почему — `docs/ПОДМОДУЛЬ_ПТСР.md`. ## КОГДА РАБОТАЕТ Только по флагу карточки сцены `stress_trauma_active` (по образцу `horror_active`). Нет флага — модуль молчит: ни промпт генерации, ни ответ аудита не меняются. Режим САТИРА исключён и с флагом: ирония держится на другом теле, драка с дроном — не травма. ## ЧЕГО ОН НЕ ДЕЛАЕТ Не запрещает. PDF подавал правила как «абсолютные запреты»…
- **коды состояний** (8): `MEDIUM`, `PTSD_FLASHBACK_AS_MEMORY`, `PTSD_PAIN_UNDERSTOOD_AT_ONCE`, `PTSD_SIGHT_BEFORE_BODY`, `PTSD_SPEECH_INTACT`, `PTSD_THOUGHT_BEFORE_BODY`, `SKIPPED`, `WARN`
- **тесты, которые зовут модуль**: 1 — `tests/test_птср_соматика.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 38 | константа | `ФЛАГ_КАРТОЧКИ` | строка: «stress_trauma_active» |
| 42 | константа | `ПРАВИЛА` | tuple, 5 элементов |
| 60 | класс | `Штамп (0 публичных методов)` |  |
| 72 | константа | `ШТАМПЫ` | tuple, 5 элементов |
| 131 | константа | `ПРАВИЛО` | строка: «Подмодуль ПТСР: в сцене стресса или травмы тело ведёт, мысль опаздывае» |
| 136 | класс | `SomaticFlag (0 публичных методов)` |  |
| 143 | функция | `применим(stress_trauma_active, mode)` | Включён ли подмодуль для этой сцены и почему. |
| 152 | функция | `памятка_для_запроса()` | Короткая памятка в запрос генерации, когда карточка несёт флаг стресса/травмы. |
| 161 | функция | `найти_штампы(text)` | Все штампы списка в тексте, без отрицаний в той же клаузе. |
| 170 | функция | `audit(text)` | Проверка сцены по списку штампов. Вне флага — SKIPPED с причиной. |

## пустой_диалог

- **путь**: `engine/пустой_диалог.py`
- **размер**: 272 строк, SHA-256 blob `978d7d615b0461ae…`
- **что это**: пустой_диалог.py — разговор, в котором никто не спрашивает про обычное.
- **зачем**: ## ОТКУДА ПРАВИЛО. ЭТО НЕ КАНОН, ЭТО СЛУХ АВТОРА 05.09.2026, о сцене звонка матери в главе 5, дословно: > «никто не говорит так матери, который боится звонить… он звонит и > рассказывает ей, и так никто не рассказывает. Говорят о чувствах, > говорят о том, что плохо, тебе плохо, почему плохо, — а они об этих > мирах, о каком-то сраном сне, где мама должна его выслушивать ночью > и увеличивать этот сон, не учитывать, что невыспанность и здоровье > организма важнее всего» и следом: > «если бы я был читателем, за такие диалог…
- **коды состояний** (2): `NO_DATA`, `WARN`
- **тесты, которые зовут модуль**: 2 — `tests/test_mcp101_product.py`, `tests/test_пустой_диалог.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 75 | константа | `ИСТОЧНИК` | строка: «Решение автора 05.09.2026 о сцене звонка матери (manuscripts/переработ» |
| 80 | константа | `РЕПЛИКА` | re.compile('^\\s*[—–-]\\s+\\S') |
| 83 | константа | `ВЫСОКОЕ` | frozenset({'мир', 'вселенная', 'конец', 'бог', 'божество', 'душа', 'вечность', ' |
| 92 | константа | `ОБЫЧНОЕ` | frozenset({'спать', 'спасть', 'сон', 'выспаться', 'уснуть', 'заснуть', 'устать', |
| 126 | константа | `ЧИСЛА_СЛОВАМИ` | frozenset({'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'д |
| 137 | константа | `СЛОВО` | re.compile('[А-Яа-яЁё]+') |
| 138 | константа | `ЦИФРА` | re.compile('\\d') |
| 141 | константа | `МИН_РЕПЛИК` |  |
| 143 | константа | `РАЗРЫВ_АБЗАЦЕВ` |  |
| 146 | функция | `_леммы(строка)` |  |
| 154 | функция | `_высокое(строка)` |  |
| 158 | функция | `_земля(строка)` |  |
| 166 | функция | `собрать_разговоры(абзацы)` | Разбить текст на разговоры — цепочки реплик с короткими паузами. |
| 192 | функция | `проверить(текст)` | Найти разговоры о высоком, в которых нет ни одного земного слова. |
| 270 | функция | `реплик_абзац(реплики)` | Номер абзаца первой реплики разговора — чтобы место было найдено. |

## разметка_для_голоса

- **путь**: `engine/разметка_для_голоса.py`
- **размер**: 123 строк, SHA-256 blob `ef417fb14965d3e1…`
- **что это**: Снять разметку Markdown перед синтезом речи.
- **зачем**: **ЖАЛОБА АВТОРА 09.09.2026, дословно:** «стрелочки вперёд, они в озвучке — все решётки и стрелочки вперёд озвучиваются». Он прав, и причин оказалось две, а не одна. **Первая: чистильщик был, но только в РУЧНОМ скрипте.** `scripts/nyk_для_озвучки.py` снимает разметку и делает файл `_ОЗВУЧКА.md`, который автор должен запустить сам. Сайт же берёт рукопись как есть: `grep -rn "очистить" api/` не находит ни одного вызова. То есть читалка на сайте озвучивала сырой Markdown — со всеми `#`, `**` и `>`. **Вторая: блочную цитату `>` не снимал никто, даже скри…
- **тесты, которые зовут модуль**: 4 — `tests/test_mcp101_product.py`, `tests/test_кинесика_видит_семьи_а_не_формы.py`, `tests/test_озвучка_и_сайт_чистят_одинаково.py`, `tests/test_разметка_не_озвучивается.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 40 | константа | `_ЗАГОЛОВОК` | re.compile('^[ \\t]{0,3}#{1,6}[ \\t]+(.*?)[ \\t]*#*[ \\t]*$', re.M) |
| 44 | константа | `_ЦИТАТА` | re.compile('^[ \\t]{0,3}>[ \\t]?', re.M) |
| 49 | константа | `ГЛИФЫ_РАЗДЕЛИТЕЛЯ` | строка: «✦✧❖◆◇★☆•※⁂—–» |
| 62 | константа | `_ЛИНЕЙКА` | re.compile(f'^[ \\t]*(?:\\*[ \\t]*\\*[ \\t]*\\*\|-{{3,}}\|\\*{{3,}}\|_{{3,}}\|[{ГЛИФ |
| 70 | константа | `_БУЛЛЕТ` | re.compile('^[ \\t]{0,3}[-*+][ \\t]+', re.M) |
| 73 | константа | `_ПАРНЫЕ` | tuple, 4 элементов |
| 81 | константа | `_ССЫЛКА` | re.compile('\\[([^\\]]+)\\]\\([^)]*\\)') |
| 84 | константа | `_ОСТАТКИ` | re.compile('[*`_]') |
| 91 | константа | `ЗНАКИ_РАЗМЕТКИ` | re.compile(f'(?:^[ \\t]{{0,3}}(?:#\|>))\|[*`]\|(?:^[ \\t]*[{ГЛИФЫ_РАЗДЕЛИТЕЛЯ}][ \\ |
| 97 | функция | `очистить_разметку(текст)` | Текст без знаков Markdown, пригодный для синтеза речи. |
| 117 | функция | `осталась_разметка(текст)` | Что осталось от разметки. Пустой список — чисто. |

## следы_генерации

- **путь**: `engine/следы_генерации.py`
- **размер**: 224 строк, SHA-256 blob `0faffa3224e244e3…`
- **что это**: следы_генерации.py — страж на ВЫХОДЕ модели, а не на входе рукописи.
- **зачем**: Замер 38 паттернов машинного текста (`scripts/замер_ai_следов.py`, 07.09.2026) дал по всем 29 книгам библиотеки **ноль** артефактов чат-бота. Тот же замер повторён 13.09.2026 по всему репозиторию, включая мои собственные отчёты:
- **тесты, которые зовут модуль**: 1 — `tests/test_следы_генерации.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 62 | константа | `ИСТОЧНИК` | строка: «Замер 13.09.2026: артефактов чат-бота в репозитории ноль (29 книг, doc» |
| 68 | класс | `Правило (0 публичных методов)` |  |
| 76 | функция | `_п(шаблон)` |  |
| 82 | константа | `ПРАВИЛА` | tuple, 9 элементов |
| 148 | класс | `Находка (2 публичных методов)` |  |
| 163 | функция | `найти(текст)` | Что модель вернула сверх прозы. Текст не меняется. |
| 169 | функция | `очистить(текст)` | Копия ответа без машинного мусора — и список того, что убрано. |
| 217 | функция | `словами(находки)` | Строки для `warnings` — автор читает их, а не JSON. |
| 222 | функция | `_образец(кусок, предел)` |  |

## справочники_помощника

- **путь**: `engine/справочники_помощника.py`
- **размер**: 149 строк, SHA-256 blob `7b3dd17fc28f35de…`
- **что это**: справочники_помощника.py — как книги автора работают в AK-MASTER.
- **зачем**: Автор 11.10.2026: «как их оформить для AK-MASTER, как они будут полезны». Ответ в `docs/СПРАВОЧНИКИ_ДЛЯ_AK_MASTER.md`. Здесь — код: по тексту главы собирается КОМПАКТНЫЙ блок для ИИ-помощника и для глаз автора: • Денисов → «карта слов»: частые слова главы и что с ними обычно стоит (список занятого — идти мимо или брать); • Платонов → подпись синтаксиса: чем текст расходится с эталоном, числами и словами (чужой текст не хранится); • Оксфордский словарь цитат → пять машин предложения (свои слова). ОГРАНИЧЕНИЕ ПО ЗАМЕРУ (ошибка «ве…
- **коды состояний** (4): `ADJF`, `INFN`, `NOUN`, `VERB`
- **тесты, которые зовут модуль**: 2 — `tests/test_подсказчик_сочетаемости.py`, `tests/test_профили_авторов.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 27 | константа | `ЛИМИТ_ЗНАКОВ` |  |
| 29 | константа | `МАШИНЫ` | tuple, 6 элементов |
| 38 | константа | `_СЛУЖЕБНЫЕ` | set, 8 элементов |
| 39 | константа | `_СЛОВО` | re.compile('[А-Яа-яЁё]{4,}') |
| 40 | константа | `_морф` |  |
| 43 | функция | `_лемма(слово)` |  |
| 52 | функция | `_выборка(список, n)` | Равномерная выборка по алфавитному списку: первые n дали бы одни слова |
| 61 | функция | `карта_слов(текст, сколько, спутников)` | Самые частые значимые слова главы, для которых есть статья Денисова. |
| 86 | функция | `подпись_и_совет(текст)` |  |
| 97 | функция | `блок(текст)` | Компактный блок для помощника и для глаз автора. |
| 125 | функция | `блок_для_генерации(бриф, слов, спутников, платонов, автор)` | Короткий блок в запрос генерации (≤ ~1 800 знаков): Денисов и машины Оксфорда; |

## ё_восстановление

- **путь**: `engine/ё_восстановление.py`
- **размер**: 172 строк, SHA-256 blob `679b84c4c32cc9ec…`
- **что это**: ё_восстановление.py — вернуть ё там, где она однозначна, и только там.
- **зачем**: ## ОТКУДА ЗАДАЧА Владелец 06.09.2026: «озвучка на Azure пусть будет, но она не точная: осел читается не как присел, а как животное, и многое другое». **Виноват не синтезатор, а текст.** Замер по библиотеке: Мембрана (Арктур, том 2) ё=2 на 205 680 знаков Игла (Арктур, том 1) ё=4 на 297 000 переработанный том 1 ё=1053 на 221 582 ← там ё расставлена В книгах, где ё нет, любой синтезатор прочтёт «осел» как животное, «все» как «всё», «небо» как «нёбо». Azure тут ни при чём. ## ПОЧЕМУ НЕ СПИСОК СЛОВ, А СЛОВАРЬ МОРФОЛОГИИ Ручной с…
- **тесты, которые зовут модуль**: 2 — `tests/test_mcp101_product.py`, `tests/test_ё_восстановление.py`

| строка | тип | элемент | назначение |
|---:|---|---|---|
| 59 | константа | `ИСТОЧНИК` | строка: «Решение автора 06.09.2026 о точности озвучки; словарь форм — pymorphy3» |
| 62 | константа | `СЛОВО` | re.compile('[А-Яа-яЁё]+') |
| 69 | константа | `ИСКЛЮЧЕНИЯ` | frozenset() |
| 71 | константа | `_кэш` | dict, 0 элементов |
| 74 | функция | `_морф()` | Тот же анализатор, что у lemma_utils — второй словарь в память не грузим. |
| 80 | функция | `однозначная_замена(слово)` | Вернуть форму с ё, если другого прочтения не существует. |
| 101 | функция | `_сохранить_регистр(было, стало)` | «Еще» → «Ещё», «ЕЩЕ» → «ЕЩЁ». Регистр автора не меняется. |
| 110 | функция | `восстановить(текст)` | Вернуть (текст с ё, отчёт). |
| 143 | функция | `_отметить_спорное(слово, копилка)` | Слово, у которого ё-прочтение ЕСТЬ, но не единственное. |
| 156 | функция | `оценить(текст)` | Сколько ё в тексте сейчас — не правя ничего. |

