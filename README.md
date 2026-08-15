> # ⚠️ АРХИВ. Код переехал в `101`.
>
> **Живой код HELIX: [`dendenden10231-ai/101`](https://github.com/dendenden10231-ai/101), папка `helix_pipeline/`.**
> Сайт собирается ТОЛЬКО из `101`. Этот репозиторий больше не развивается.
>
> **НЕ ПОДКЛЮЧАТЬ К RAILWAY.** Здесь лежит `Procfile`, поэтому репозиторий
> способен подняться ОТДЕЛЬНЫМ сайтом — это тот самый лишний деплой, который
> автор уже дважды удалял.
>
> **Сверено побайтно 15.08.2026** (`101/docs/REPO_MERGE_AUDIT_2026-08-15.md`):
> 15 файлов совпадают полностью; файлов, которых нет в `101`, — **ноль**.
> Два отличия — осознанные решения, уже принятые в `101`:
> транспорт Anthropic удалён по правилу провайдера («только Google»), а четыре
> полосы `CONFIDENCE_THRESHOLDS` удалены сверкой со спецификацией — их нет
> нигде в `HELIX_GOVERNANCE_v1_3_FINAL.md`, они были выдуманы.
> Возврат любого из них нарушил бы правило продукта.

# HELIX GOVERNANCE — Backend

Детерминированный аудит AI-вывода. Реализация по спецификации `HELIX_GOVERNANCE_v1_3_FINAL.md`
+ ядро `GI_v6_2_COMPLETE.docx`. Продукт 1 из 4 в экосистеме HELIX
(GOVERNANCE / INTELLIGENCE / TRACE / MARKET) — остальные три ещё не реализованы.

## Архитектурный принцип

```
Claude (LLM)  →  возвращает ТОЛЬКО семантические сигналы (JSON)
Python движок →  считает ВСЮ математику детерминированно
```

Классификатор (Claude) никогда не возвращает числа confidence/score/weight —
это жёстко проверяется в `governance_service.parse_classifier_response()`
и будет выброшена ошибка, если LLM попытается посчитать что-то сам.

## Структура

```
docs/specs/                Полные исходные спецификации (12 файлов, см. docs/specs/INDEX.md)
                           3 из них были .docx — сконвертированы в .md для читаемости
                           и грепа прямо в репозитории (таблицы сохранены, форматирование
                           текста могло упроститься при конвертации)

engine/
  governance_math.py      Module 0 — чистая математика (RPL, Confidence,
                           NGI, CIRI, Article 9, Decision). Zero LLM calls.
                           Источник: docs/specs/HELIX_GOVERNANCE_v1_3_FINAL.md, Раздел 14-15
  gi_core.py               Module 1 — ядро GI v6.2: SSC, FRCP, CDR, SAD,
                           NGI-действия, PPS (приоритизация), OAS (журнал аудита)
                           Источник: docs/specs/GI_v6_2_COMPLETE.md, патчи P33/34/35/45/46/55/56
  governance_service.py    Module 2 — связывает классификатор + math + gi_core
  claude_classifier.py     Module 2b — HTTP-клиент к Anthropic API,
                           system prompt дословно из docs/specs/HELIX_GOVERNANCE_v1_3_FINAL.md, РАЗДЕЛ 16

api/
  main.py                  Module 3 — FastAPI: POST /governance/analyze,
                           GET /health, GET /governance/oas/summary

tests/
  test_governance_math.py      36 тестов — вся математика Module 0
  test_gi_core.py               35 тестов — все 7 протоколов Module 1
  test_governance_service.py    21 тест — контракт классификатора + интеграция

requirements.txt / Procfile     готово к Railway deploy
```

## Статус на момент передачи

✅ **Проверено и зелёное: 92/92 теста.**
Прогонялось так: `python3 tests/test_<module>.py` (у каждого файла есть
собственный runner в `if __name__ == "__main__"`, pytest не обязателен,
но `pytest tests/` тоже отработает — тесты обычного pytest-формата).

⚠️ **Не тестировалось (нет сети в песочнице сборки):**
`claude_classifier.py` — реальный вызов `anthropic.messages.create()`.
Код написан по официальному SDK-паттерну, но живого end-to-end прогона
с реальным `ANTHROPIC_API_KEY` не было. Первое что стоит сделать на
Railway — прогнать один реальный запрос через `/governance/analyze`
и свериться, что классификатор действительно возвращает JSON по контракту
РАЗДЕЛ 16 (парсер это провалидирует и кинет `ClassifierResponseError`
с понятным сообщением, если формат поплывёт).

## Известные ограничения (осознанные, не баги)

- **OAS-журнал живёт в памяти процесса** (`_gi_core` — один глобальный
  инстанс в `api/main.py`). Переживёт запросы, но не переживёт рестарт
  и не расшарится между несколькими инстансами при масштабировании.
  Следующий шаг — вынести в PostgreSQL (см. `HELIX_Runtime_Spec_v1_1.docx`
  у автора проекта, если нужен design для этого).
- **Нет аутентификации / rate limiting** — сейчас endpoint открыт всем,
  кто достучится до Railway-URL. Добавить до реального продакшна.
- **Article 9 (EU AI Act) считается, но не вызывается из API** —
  `calculate_article9_score()` есть в Module 0 и покрыт тестами, но
  `governance_service.evaluate()` его пока не запускает (нужны
  `requirements_met` / `evidence_counts`, которые ещё не приходят
  от классификатора — потребует расширения РАЗДЕЛ 16 промпта).

## Запуск локально

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
uvicorn api.main:app --reload --port 8000
```

```bash
curl -X POST http://localhost:8000/governance/analyze \
  -H "Content-Type: application/json" \
  -d '{"ai_output": "Столица Франции — Париж.", "context_type": "internal"}'
```

## Запуск тестов

```bash
cd helix_pipeline
python3 tests/test_governance_math.py
python3 tests/test_gi_core.py
python3 tests/test_governance_service.py
# либо
pytest tests/ -v
```

## Деплой на Railway

1. Залить репозиторий на GitHub
2. В Railway: New Project → Deploy from GitHub repo
3. Variables → добавить `ANTHROPIC_API_KEY`
4. Railway подхватит `Procfile` автоматически

## Что дальше (не входит в этот пакет)

- Module 3+: продукты INTELLIGENCE / TRACE / MARKET — используют тот же
  `gi_core.py` (SSC/FRCP/CDR/SAD уже готовы для этого), но пока не подключены
- PostgreSQL для OAS-журнала (сейчас in-memory)
- Auth-слой перед `/governance/analyze`
- Article 9 полная интеграция в API-путь
