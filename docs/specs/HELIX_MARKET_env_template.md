# HELIX MARKET — переменные окружения

Этот файл сделан из `.env.example` и предназначен для сохранения как Markdown-документ.

## Главное правило

1. Скопируй `.env.example` в файл `.env`.
2. Заполни реальные значения вместо `change_me...` и `sk-...`.
3. Файл `.env` **нельзя коммитить в git**.
4. `.env.example` можно хранить в репозитории как безопасный шаблон без настоящих секретов.

## Готовый шаблон `.env.example`

```env
# .env.example
# HELIX MARKET — Environment Variables
# Скопировать в .env и заполнить реальными значениями.
# .env НИКОГДА не коммитить в git.

# ─── OpenAI ───────────────────────────
OPENAI_API_KEY=sk-...

# ─── PostgreSQL ───────────────────────
PG_PASSWORD=change_me_strong_password
POSTGRES_URI=postgresql+asyncpg://helix:change_me_strong_password@postgres:5432/helix_market

# ─── Neo4j ────────────────────────────
NEO4J_PASSWORD=change_me_strong_password
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j

# ─── Redis ────────────────────────────
REDIS_URI=redis://redis:6379

# ─── Auth ─────────────────────────────
JWT_SECRET=change_me_to_random_64_char_string

# ─── CORS ─────────────────────────────
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com

# ─── Logging ──────────────────────────
LOG_LEVEL=INFO

# ─── Rate Limiting ────────────────────
RATE_LIMIT_PER_MINUTE=10
```

## Что нужно заменить перед запуском

| Переменная | Что вставить |
|---|---|
| `OPENAI_API_KEY` | Настоящий API-ключ OpenAI. |
| `PG_PASSWORD` | Сильный пароль PostgreSQL. |
| `POSTGRES_URI` | Строка подключения PostgreSQL с тем же паролем. |
| `NEO4J_PASSWORD` | Сильный пароль Neo4j. |
| `JWT_SECRET` | Случайная секретная строка длиной примерно 64 символа. |
| `ALLOWED_ORIGINS` | Разрешённые адреса фронтенда: локальный и боевой домен. |
| `RATE_LIMIT_PER_MINUTE` | Лимит запросов в минуту. |

## Минимальный рабочий порядок

```bash
cp .env.example .env
nano .env
```

После этого заменить все временные значения на реальные.
