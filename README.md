# HELIX — public dossier and audit record

**A deterministic verification engine for AI-generated output.** The language
model is permitted to read and to name; it is forbidden to compute and to
decide. Every number, threshold, and verdict is produced by deterministic
Python, verified line by line against a written specification.

Built and maintained by one person. This repository is the public window onto
that work: the dossier, the audit record, and a reader's guide to the
specifications. The source code and the specifications themselves remain
private and are available for review on request.

*Русская версия — ниже.*

---

## Start here

| | |
|---|---|
| **[The dossier (English)](dossier/HELIX_DOSSIER_EN.html)** | The main document. Quotes the running system directly — the classifier prompt that forbids the model from returning numbers, the risk formula with its weights, the scientific sources compiled into executable rules, and three documented cases where the audit found a defect inside the system itself. |
| **[Досье (русский)](dossier/HELIX_DOSSIER_RU.html)** | The same document in Russian. |
| **[Reader's guide to the specifications](guide/SPECIFICATION_GUIDE_EN.md)** | The specifications are in Russian. This maps what lives where, names every protocol in English, and explains the vocabulary you need to read them. |
| **[Taking part](PARTNERSHIP_EN.md)** · [(RU)](PARTNERSHIP_RU.md) | How to fund, join, partner, or simply review this — what is open to negotiation, what is not, and what happens to the work if the author stops. |
| **[Letters](letters/LETTERS_EN.md)** · [(RU)](letters/LETTERS_RU.md) | The letters sent to cloud programs, model developers, and grant programs, published as sent. |

**The system is live.** This is a deployed site, not a specification:
[web-production-b540f.up.railway.app](https://web-production-b540f.up.railway.app) —
three products on one engine, live model calls, real grounded investigations.
Sign-in via Google. A guided walkthrough is available on request.

The dossier files are self-contained HTML — download and open in any browser,
no server or build step. They follow your system's light or dark theme.

The letters are open for the same reason everything else here is: the same case
is made to every recipient, in the same words, with the same numbers. If you are
one of those recipients, you can see exactly what was said to the others.

## The audit record

In August 2026 the entire engine was read line by line against the exact text
of its governing specifications. Not against a summary, and not against a prior
comment claiming everything was fine. Fourteen discrepancies were found and
fixed in code the same day, each with tests.

| Report | Covers |
|---|---|
| [`HELIX_AUDIT_COMPLETE_FINAL.md`](audit/HELIX_AUDIT_COMPLETE_FINAL.md) | Summary of all five closed sections, with the consolidated list of all 14 findings |
| [`GOVERNANCE_AUDIT_REPORT_FINAL.md`](audit/GOVERNANCE_AUDIT_REPORT_FINAL.md) | AI-output audit product |
| [`INTELLIGENCE_AUDIT_REPORT_FINAL.md`](audit/INTELLIGENCE_AUDIT_REPORT_FINAL.md) | Investigation product, all 33 protocols |
| [`TRACE_AUDIT_REPORT_FINAL.md`](audit/TRACE_AUDIT_REPORT_FINAL.md) | Adversarial / red-team product |
| [`GI_V62_CORE_STABILIZATION_AUDIT_REPORT_FINAL.md`](audit/GI_V62_CORE_STABILIZATION_AUDIT_REPORT_FINAL.md) | Shared core and hardening layer |
| [`ENGINE_FULL_COVERAGE_REPORT.md`](audit/ENGINE_FULL_COVERAGE_REPORT.md) | File-by-file coverage, all 70 engine files |

These reports are in Russian, as the specifications are. The dossier and the
guide carry their substance in English.

## The numbers

Measured by running against the repository on 19 August 2026 — not recalled,
not carried forward from an older file.

```
Python                 138,225 lines across 692 files
Specifications          82,801 lines
Tests                    3,951 passing, 18 skipped, 0 failing
HELIX engine            19,003 lines across 71 modules
Engine files audited        70 of 70, line by line
Discrepancies fixed         14, each with tests
Executable patches          38 of 38 enforced, 100% behavioural coverage
Math operators              44, governed by 10 absolute laws
```

## What is not here

The source code, the specifications, and the two sibling systems (AK-MASTER, a
literary engine, and MR_HELIX, an autonomous agent) are private. That is a
deliberate choice while this remains one person's unfinished work — not an
attempt to avoid scrutiny.

Full read access, a live walkthrough, or a guided run of the test suite is
available on request to anyone evaluating this for cloud credit, a research
grant, or partnership. Contact details are at the foot of the dossier.

## Contact

Dzianis Vashkevich — dendenden043@gmail.com — Luboń, Poland

---
---

# HELIX — открытое досье и запись аудита

**Детерминированный движок проверки вывода ИИ.** Языковой модели разрешено
читать и называть; ей запрещено считать и решать. Каждое число, порог и
вердикт производит детерминированный Python, сверенный построчно с письменной
спецификацией.

Построено и поддерживается одним человеком. Этот репозиторий — открытое окно в
эту работу: досье, запись аудита и путеводитель по спецификациям для
англоязычного читателя. Сам код и сами спецификации остаются закрытыми и
доступны для изучения по запросу.

## С чего начать

| | |
|---|---|
| **[Досье (русский)](dossier/HELIX_DOSSIER_RU.html)** | Главный документ. Показывает работающую систему напрямую: промпт классификатора, запрещающий модели возвращать числа; формулу риска с весами; научные источники, превращённые в исполняемые правила; три задокументированных случая, когда проверка нашла дефект внутри самой системы. |
| **[The dossier (English)](dossier/HELIX_DOSSIER_EN.html)** | Тот же документ на английском. |
| **[Путеводитель по спецификациям](guide/SPECIFICATION_GUIDE_EN.md)** | На английском — для тех, кто не читает по-русски: что где лежит, все протоколы с английскими названиями, нужный словарь. |
| **[Участие в проекте](PARTNERSHIP_RU.md)** · [(EN)](PARTNERSHIP_EN.md) | Как профинансировать, войти, стать партнёром или просто разобрать технически — что обсуждаемо, что нет, и что происходит с работой, если автор остановится. |
| **[Письма](letters/LETTERS_RU.md)** · [(EN)](letters/LETTERS_EN.md) | Письма в облачные программы, разработчикам моделей и в грантовые программы — опубликованы в том виде, в каком отправлены. |

**Система работает вживую.** Это развёрнутый сайт, а не спецификация:
[web-production-b540f.up.railway.app](https://web-production-b540f.up.railway.app) —
три продукта на одном движке, живые вызовы модели, реальные заземлённые
расследования. Вход через Google. Проведу по системе лично по запросу.

Файлы досье самодостаточны — скачиваются и открываются в любом браузере, без
сервера и без сборки. Тёмная или светлая тема подхватывается от системы.

Письма лежат открыто по той же причине, что и всё остальное здесь: всем
адресатам говорится одно и то же, теми же словами и с теми же цифрами. Если вы
один из адресатов — вы видите ровно то, что сказано остальным.

## Запись аудита

В августе 2026 весь движок был прочитан построчно против точного текста
управляющих спецификаций. Не против пересказа и не против прежнего
комментария, утверждавшего, что всё в порядке. Найдено и починено кодом
четырнадцать расхождений, каждое с тестами. Шесть итоговых отчётов — в
каталоге [`audit/`](audit/).

## Чего здесь нет

Исходный код, спецификации и две смежные системы (AK-MASTER — литературный
движок, MR_HELIX — автономный агент) закрыты. Это осознанный выбор, пока это
неоконченная работа одного человека, а не попытка избежать проверки.

Полный доступ на чтение, живая демонстрация или сопровождаемый прогон тестов —
по запросу любому, кто оценивает это для облачного кредита, гранта или
партнёрства. Контакты — в подвале досье.

## Контакт

Вашкевич Денис Георгиевич — dendenden043@gmail.com — Luboń, Polska
