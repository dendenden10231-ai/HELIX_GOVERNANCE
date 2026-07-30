# Индекс спецификаций

Все документы — оригиналы автора проекта. Три .docx сконвертированы в .md
(конвертация механическая: текст + таблицы; форматирование могло упроститься —
при разночтениях ориентироваться на оригинал .docx у автора).

## Реализовано в этом пакете

| Файл | Статус | Что из него взято |
|---|---|---|
| `HELIX_GOVERNANCE_v1_3_FINAL.md` | ✅ Реализовано | Вся математика (Раздел 14-15), classifier system prompt (Раздел 16) |
| `GI_v6_2_COMPLETE.md` | ✅ Частично реализовано | Протоколы P33 SSC, P34 FRCP, P35 CDR, P45 SAD, P46 NGI, P55 PPS, P56 OAS. Остальные ~45 патчей — не реализованы |

## Не реализовано — справочно для дальнейшей разработки

| Файл | Продукт | Статус |
|---|---|---|
| `HELIX_INTELLIGENCE_v2_1.md` | INTELLIGENCE | Не начато. Может переиспользовать `gi_core.py` (SSC/FRCP/CDR/SAD уже готовы) |
| `HELIX_TRACE_MERGED.md` | TRACE | Не начато |
| `HELIX_MARKET_v1_0.md` | MARKET | Не начато |
| `HELIX_MARKET_env_template.md` | MARKET | `.env` шаблон, когда дойдёт очередь до MARKET |
| `HELIX_VERIFY_API_v1_2.md` | VERIFY API | Не начато — общий API-слой для INTELLIGENCE/VERIFY |
| `HELIX_Runtime_Spec_v1_1.md` | Инфраструктура | Enterprise-архитектура (multi-tenant, PostgreSQL, RAG) — понадобится когда OAS будет выноситься из памяти в БД |
| `HELIX_SOUL_AK_LITERARY_RUNTIME_v1_1_OBSERVATION_GATE.md` | Отдельный литературный runtime | Не относится к GOVERNANCE backend напрямую — мост к другому проекту автора (AK) |
| `HELIX_Final_Stabilization_MERGED.md` | Hardening / stress-тесты | Справочно, для дальнейшего аудита устойчивости |
| `HELIX_Research_Brief_v1_3.md` | Маркетинг/позиционирование | Не техническая спецификация — бриф на рыночное исследование |
| `HELIX_v2_0_1_GI62.md` | Ядро (расширенная версия) | Крупный файл (927 KB) — более ранняя/широкая версия ядра, включает материал уже покрытый GI_v6_2_COMPLETE.md; при расхождениях GI_v6_2_COMPLETE.md новее |

## Не включено в этот пакет

- `AK68_*` — отдельный литературный проект автора (система для написания книг), не относится к HELIX backend
- `TICKET_module1_integrity_gate.md` — тикет для другого репозитория (`101` / AK68 canon runtime), не для этого GOVERNANCE backend
