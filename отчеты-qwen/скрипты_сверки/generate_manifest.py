#!/usr/bin/env python3
"""generate_manifest.py — генерирует MANIFEST_SHA256.md по реальному
текущему состоянию каталога.

ПОЧЕМУ ЭТОТ СКРИПТ ПОЯВИЛСЯ (2026-07-15): проверила оба архива (101 и 68)
против их же MANIFEST_SHA256.md — 41/219 и 44/219 записей не совпадали,
4 файла упомянуты в манифесте, но физически отсутствуют. Причина
найдена: ни в scripts/local_ci.sh, ни в .github/workflows/ak-master-ci.yml
нет ШАГА генерации манифеста вообще — он делается вручную, в произвольный
момент, обычно ДО финальной пересборки фронтенда (Vite меняет
content-hash в именах файлов при каждой пересборке — это и объясняет
конкретно frontend/dist/assets/* несовпадения).

ПРАВИЛО ИСПОЛЬЗОВАНИЯ: запускать этот скрипт ПОСЛЕДНИМ шагом перед
упаковкой в zip — после `npm run build`, после всех правок кода, после
`pytest`. Не раньше. Если после генерации манифеста менялся хоть один
файл — манифест снова невалиден, перезапустить.

Использование:
    python3 scripts/generate_manifest.py > MANIFEST_SHA256.md
    python3 scripts/generate_manifest.py --verify   # сверить с существующим
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_NAME = "MANIFEST_SHA256.md"

#: Сколько первых байтов git проверяет на NUL, решая, двоичный файл или текст
#: (`buffer_is_binary`, FIRST_FEW_BYTES в convert.c). Нужно только для файлов,
#: которых ещё нет в индексе: по ним некого спросить, кроме самого правила git.
GIT_BINARY_PROBE = 8000

# Каталоги, которые не имеет смысла хэшировать (генерируются заново при
# каждой сборке/окружении, не часть поставляемого содержимого).
EXCLUDE_DIRS = {
    ".git", "__pycache__", "node_modules", ".venv", "venv",
    ".pytest_cache", ".mypy_cache", ".github",
    # 2026-08-28: КОРЕНЬ ПОВТОРЯЮЩЕЙСЯ ПОЛОМКИ МАНИФЕСТА.
    #
    # `.runtime/` — рантайм-каталог (кэш судьи, временные артефакты
    # прогонов). Он в .gitignore, то есть в коммит НЕ попадает, но
    # генератор его хэшировал. Следствие: манифест, сгенерированный на
    # машине, где хоть раз запускали аудит, содержал сотни записей о
    # файлах, которых на чистом checkout'е не существует — и CI (всегда
    # чистый checkout) честно падал на `--verify`.
    #
    # Замерено в этот день: рабочее дерево 1331 файл против 1212 на
    # чистой копии того же коммита — ровно 119 файлов `.runtime/`.
    # Манифест не чинился с 11.07 именно поэтому: каждая регенерация
    # закрепляла локальный мусор, а не поставляемое содержимое.
    #
    # Правило простое: манифест описывает то, что уезжает в поставку.
    # Игнорируемое гитом в поставку не уезжает.
    ".runtime",
}
# Сам манифест не хэширует сам себя (иначе неразрешимый парадокс
# курицы-и-яйца — значение хэша меняется от факта записи хэша).
# oas_events.jsonl (и legacy oas_events.json) — рантайм-журнал OAS: растёт при
# каждом прогоне тестов (OASDatabase.log_event), в манифесте ему делать нечего;
# файл создаётся кодом автоматически (engine/oas_database.py).
# `build-info.json` пишется плагином vite при КАЖДОЙ сборке и содержит
# `built_at` (метка времени) и `ui_build` (идентификатор сборки). Он по
# построению отличается от прошлого раза.
#
# А в `.github/workflows/ak-master-ci.yml` шаги идут так: `npm run build`,
# и СРАЗУ ПОСЛЕ него `generate_manifest.py --verify`. То есть CI сам
# пересобирал фронт и сам же ловил себя на том, что метка времени
# изменилась. Эта проверка не могла пройти НИКОГДА, независимо от того,
# кто и когда регенерировал манифест.
#
# Проверено 28.08.2026 прогоном в порядке CI на чистой копии: имена
# файлов с content-hash после пересборки совпали до буквы
# (index-Dt-wWOJw.js), разошёлся ровно один файл — этот.
#
# Из манифеста он уходит, из поставки — нет: файл по-прежнему коммитится
# и по-прежнему отдаётся бэкендом в /api/version.
EXCLUDE_FILES = {
    MANIFEST_NAME, "oas_events.json", "oas_events.jsonl", "build-info.json",
    # docs/CI_DIAGNOSTICS.md пишет сам CI шагом `if: failure()` (102-ci.yml):
    # это артефакт раннера, а не поставляемое содержимое. Без исключения
    # следующий прогон падал бы на «есть в каталоге, но не в манифесте» —
    # красный CI воспроизводил бы сам себя бесконечно.
    # ВАЖНО: сверка в iter_files идёт по ИМЕНИ файла (rel.name), как и для
    # остальных записей множества, поэтому здесь имя, а не путь: запись
    # «docs/CI_DIAGNOSTICS.md» не срабатывала, и прогон от 29.10 00:01Z
    # покраснел именно на этом.
    "CI_DIAGNOSTICS.md",
}


def игнорируемое_гитом(root: Path) -> frozenset[str]:
    """Пути, которые гит игнорирует. Спрашиваем гит, а не помним список.

    ## ПОЧЕМУ ПРАВИЛО, А НЕ ПЕРЕЧЕНЬ (07.09.2026)

    28.08 в `EXCLUDE_DIRS` завели `.runtime` и записали над ним правило
    дословно: «манифест описывает то, что уезжает в поставку; игнорируемое
    гитом в поставку не уезжает».

    Правило записали, а применили руками — одной строкой про один каталог.
    07.09 та же поломка нашлась во втором месте: `data/patch_docs/` тоже
    в `.gitignore`, тоже пишется на каждом прогоне (`api/patch_workflow.py`),
    и его 14 файлов честно роняли `--verify` на чистом checkout'е.

    Перечень, который надо помнить, устаревает при первой же новой строке
    в `.gitignore`. Правило — не устаревает. Гит знает ответ точно, и
    спросить его дешевле, чем угадать.

    Пустое множество означает «гита нет» — например, в распакованном zip у
    рецензента. Тогда работают прежние списки: они остаются как запасной
    путь, а не как основной.

    `-z` здесь не для красоты: без него git печатает не-ASCII пути в
    восьмеричных кавычках (`"docs/\320\267\320\260..."`), и сравнение с
    настоящим именем файла не сходится — игнорируемый файл с кириллическим
    именем молча попадал в поставку.
    """
    try:
        готово = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--others", "--ignored",
             "--exclude-standard", "-z"],
            capture_output=True, timeout=60, check=False)
    except (OSError, subprocess.SubprocessError):
        return frozenset()
    if готово.returncode != 0:
        return frozenset()
    return frozenset(п.decode("utf-8", "surrogateescape")
                     for п in готово.stdout.split(b"\0") if п)


def переводы_строк(root: Path) -> dict[str, str]:
    """{posix-путь: 'lf' | 'raw'} — в каком виде файл лежит в индексе git.

    ## ЗАЧЕМ СПРАШИВАТЬ GIT, А НЕ УГАДЫВАТЬ ПО БАЙТАМ (27.10.2026, Windows)

    Манифест описывает поставляемое содержимое, а поставляется то, что лежит
    в git. На машине с `core.autocrlf=true` рабочее дерево держит CRLF, а
    индекс — LF: хэш рабочего дерева не совпадает с записанным у каждого
    текстового файла. Замер на этой машине: README.md — raw не совпадает,
    CRLF→LF совпадает, `git cat-file blob :README.md` совпадает.

    Соблазн «нормализовать всё подряд» ломает поставку: PDF, DOCX, ZIP и TTF
    нормализацию не переживают. Угадать двоичность по байтам тоже не
    получается — `The Oxford Dictionary Of Quotations.pdf` начинается с
    чистого ASCII, NUL в первых килобайтах нет, а git считает его двоичным.

    `git ls-files --eol` уже знает ответ про каждый отслеживаемый файл:
    `i/lf w/crlf` — в индексе LF (нормализовать), `i/-text` — двоичный
    (байт в байт). Замер на этом коммите: 2014 / 28 / 29 / 1.

    Пустой словарь означает «гита нет» — тогда решение принимается по
    правилу самого git для неиндексированных файлов (см. `sha256_of`).
    """
    try:
        готово = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--eol", "-z"],
            capture_output=True, timeout=120, check=False)
    except (OSError, subprocess.SubprocessError):
        return {}
    if готово.returncode != 0:
        return {}
    правила: dict[str, str] = {}
    for запись in готово.stdout.split(b"\0"):
        if not запись:
            continue
        мета, _, путь = запись.partition(b"\t")
        if not путь:
            continue
        поля = мета.split()
        if len(поля) < 2:
            continue
        индекс, дерево = поля[0].decode(), поля[1].decode()
        правила[путь.decode("utf-8", "surrogateescape")] = (
            "lf" if индекс == "i/lf" and дерево in ("w/crlf", "w/mixed")
            else "raw")
    return правила


def вложенные_рабочие_копии(root: Path) -> list[Path]:
    """Каталоги, которые сами являются гит-копией, — не часть этой поставки.

    НАЙДЕНО 18.09.2026: `--verify` показал 1565 «забытых» файлов, и все они
    лежали в `.claude/worktrees/agent-…/` — во второй рабочей копии
    репозитория, которую заводит подагент. Гит про них молчит в обе стороны:
    не отслеживает (чужая копия) и не считает игнорируемыми (граница
    репозитория), поэтому запрос `ls-files --ignored` их не ловит по
    устройству. Манифест описывает то, что уезжает в поставку; чужая
    рабочая копия не уезжает.
    """
    найдено: list[Path] = []
    for метка in root.rglob(".git"):
        каталог = метка.parent
        if каталог == root:
            continue
        if any(ч in EXCLUDE_DIRS for ч in каталог.relative_to(root).parts):
            continue
        найдено.append(каталог)
    return найдено


def iter_files(root: Path):
    игнор = игнорируемое_гитом(root)
    чужие = вложенные_рабочие_копии(root)
    # Сортировка по posix-строке, а не по `Path`: на Windows сравнение путей
    # нечувствительно к регистру (`PureWindowsPath` нормализует регистр),
    # поэтому `sorted(rglob)` давал порядок, отличный от Linux, и
    # регенерация переставляла ~450 строк при неизменных хэшах.
    for path in sorted(root.rglob("*"),
                       key=lambda p: p.relative_to(root).as_posix()):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if any(path.is_relative_to(ч) for ч in чужие):
            continue
        if rel.name in EXCLUDE_FILES:
            continue
        if rel.as_posix() in игнор:
            continue
        yield rel


def sha256_of(path: Path, правило: str | None = None) -> str:
    """SHA-256 поставляемого содержимого — того, что лежит в индексе git.

    `правило=None` означает, что файл не отслеживается и спросить git некого;
    тогда двоичность определяется так же, как её определит `git add` — NUL в
    первых `GIT_BINARY_PROBE` байтах.
    """
    данные = path.read_bytes()
    if правило is None:
        правило = "raw" if b"\0" in данные[:GIT_BINARY_PROBE] else "lf"
    if правило == "lf":
        данные = данные.replace(b"\r\n", b"\n")
    return hashlib.sha256(данные).hexdigest()


def generate(root: Path) -> list[tuple[str, str]]:
    правила = переводы_строк(root)
    return [(rel.as_posix(), sha256_of(root / rel, правила.get(rel.as_posix())))
            for rel in iter_files(root)]


def verify(root: Path) -> int:
    """Возвращает 0, если существующий манифест совпадает с реальным
    состоянием каталога, иначе печатает расхождения и возвращает 1 —
    удобно вызывать этот же скрипт как последнюю проверку в CI, а не
    только для генерации."""
    manifest_path = root / MANIFEST_NAME
    if not manifest_path.exists():
        print(f"ОШИБКА: {MANIFEST_NAME} не найден в {root}", file=sys.stderr)
        return 1

    existing = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        parts = line.split(None, 1)
        if len(parts) == 2 and len(parts[0]) == 64:
            existing[parts[1]] = parts[0]

    actual = dict(generate(root))

    missing_locally = sorted(set(existing) - set(actual))
    extra_untracked = sorted(set(actual) - set(existing))
    mismatched = sorted(p for p in set(existing) & set(actual) if existing[p] != actual[p])

    # ЛИШНИЙ ФАЙЛ — ТОЖЕ РАСХОЖДЕНИЕ (07.09.2026). Здесь стояло
    # `not (missing_locally or mismatched)`: `extra_untracked` печатался,
    # но в вердикт не входил, и манифест мог молча отстать от каталога на
    # десяток файлов, оставаясь «OK».
    #
    # Смысл манифеста — сказать рецензенту, что именно он держит в руках.
    # Файл, которого в манифесте нет, ровно это обещание и ломает: в
    # поставке он есть, а в описи его нет.
    #
    # Ложных срабатываний это не добавляет: рантайм-мусор сюда больше не
    # попадает вовсе — `iter_files` спрашивает гит, что он игнорирует.
    ok = not (missing_locally or mismatched or extra_untracked)
    print(f"записей в манифесте: {len(existing)}")
    print(f"реальных файлов (кроме исключённых): {len(actual)}")
    print(f"упомянуты в манифесте, но отсутствуют: {len(missing_locally)}")
    print(f"хэш не совпадает: {len(mismatched)}")
    print(f"есть в каталоге, но не в манифесте: {len(extra_untracked)}")
    if missing_locally:
        print("\nотсутствуют:", *missing_locally[:20], sep="\n  ")
    if mismatched:
        print("\nне совпадает хэш:", *mismatched[:20], sep="\n  ")
    if extra_untracked:
        print("\nне в манифесте (возможно, забыли добавить):", *extra_untracked[:20], sep="\n  ")

    print("\nOK" if ok else "\nFAIL — манифест не соответствует реальному состоянию каталога")
    return 0 if ok else 1


def main():
    if "--verify" in sys.argv:
        sys.exit(verify(ROOT))
    for rel, digest in generate(ROOT):
        print(f"{digest}  {rel}")


if __name__ == "__main__":
    main()
