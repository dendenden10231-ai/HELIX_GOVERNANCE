#!/usr/bin/env python3
"""реестр_продуктов.py — печатает ПОЭЛЕМЕНТНЫЕ реестры кода, а не сводки.

ЗАЧЕМ (27.10.2026). Владелец прислал `HELIX_PASSPORT_26_10_2026_FULL.docx`,
где раздел 7.2 — построчный реестр всех 62 элементов `привязка_чисел.py`.
Перенос в репозиторий дал сводку («8 шагов»), и реестр потерялся: по нему
нельзя ответить на вопрос «что делает вот эта константа на строке 141».
Плюс по Mr. Helix вообще не было отчёта по каждой из 99 капсул.

Отсюда правило этого скрипта: **реестр генерируется, а не пишется руками.**
Рукописный реестр устаревает при первом же PR (номер строки уехал — и запись
в документе стала ложью). Здесь номера строк берутся из AST живого файла,
назначение — из докстринга самого элемента, статус капсулы — из
`capsule_coverage_validator`, который уже считает его по коду и тестам.

Что печатает:
    docs/passports/HELIX_РЕЕСТР_ПО_МОДУЛЯМ.md
        113 модулей `helix_pipeline/engine/`: размер, хэш, назначение,
        каждый элемент верхнего уровня со строкой и докстрингом, коды
        состояний, спека-якорь, тесты, которые модуль зовут.
    docs/passports/MR_HELIX_РЕЕСТР_ПО_КАПСУЛАМ.md
        99 капсул: id, имя, модуль и его размер, каждый символ со строкой,
        статус ENFORCED/PARTIAL/SPEC_ONLY, якорь в спеке PACK_xx, тесты.

Тесты ищутся в ОБОИХ каталогах — `tests/` и `helix_pipeline/tests/`: модуль,
названный только в корневом тесте, иначе выглядел непроверенным. Если модуль
не зовёт ни один тест, печатается «откуда достижим» — `api/service.py`,
`api/router.py` или другой модуль пакета, у которого тесты есть. Это путь
в коде, а не проверка поведения, и в реестре он так и подписан.

Использование:
    PYTHONUTF8=1 python scripts/реестр_продуктов.py
    PYTHONUTF8=1 python scripts/реестр_продуктов.py --stdout   # не писать файлы
"""
from __future__ import annotations

import ast
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_HELIX = ROOT / "docs" / "passports" / "HELIX_РЕЕСТР_ПО_МОДУЛЯМ.md"
OUT_MR = ROOT / "docs" / "passports" / "MR_HELIX_РЕЕСТР_ПО_КАПСУЛАМ.md"
OUT_AK = ROOT / "docs" / "passports" / "AK_MASTER_РЕЕСТР_ПО_МОДУЛЯМ.md"

ENGINE = ROOT / "helix_pipeline" / "engine"
TESTS_HELIX = ROOT / "helix_pipeline" / "tests"
MR_ENGINE = ROOT / "mr_helix" / "engine"
MR_TESTS = ROOT / "mr_helix" / "tests"
MR_MANIFEST = ROOT / "mr_helix" / "docs" / "capsule_manifest.yaml"
MR_SPEC = ROOT / "mr_helix" / "docs" / "spec"

# Спеки HELIX: якорь ищется в тексте модуля, чтобы реестр сам говорил,
# какую спеку модуль реализует (иначе это снова проза на слово).
SPEC_ANCHORS = {
    "GI_v6_2": "GI_v6_2_COMPLETE.md",
    "INTELLIGENCE_v2": "HELIX_INTELLIGENCE_v2_1.md",
    "TRACE_MERGED": "HELIX_TRACE_MERGED.md",
    "GOVERNANCE_v1": "HELIX_GOVERNANCE_v1_4.md",
    "CORE_v2": "HELIX_CORE_v2_5.md",
    "MARKET_v1": "HELIX_MARKET_v1_0.md",
}

ЗАЧЕМ = re.compile(r"ЗАЧЕМ[^\n]*\n(.+?)(?:\n\s*\n|\n[A-ZА-Я]{3,})", re.S)


def sha256_blob(path: Path) -> str:
    """Хэш содержимого в форме git-блоба (LF), а не рабочего дерева.

    На Windows рабочее дерево в CRLF (`core.autocrlf=true`), и хэш «как есть»
    не совпадает ни с манифестом поставки, ни с тем, что видит CI на Linux.
    """
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def строк_в_файле(текст: str) -> int:
    """Число строк как у `wc -l` и у AST, а не как у `str.splitlines()`.

    НАЙДЕНО 27.10.2026 СОБСТВЕННЫМ ПРОВЕРЯЛЬЩИКОМ. Две ловушки в одном месте:

    1. `splitlines()` режет строку ещё и по `\\x0b \\x0c \\x1c \\x1d \\x1e \\x85
       \\u2028 \\u2029`. В `engine/невидимые_символы.py` лежат литеральные
       U+2028 и U+2029 (это детектор невидимых символов, он хранит образцы),
       и `splitlines()` давал 172 строки против 171 у `wc -l` и у `ast` —
       номера строк в реестре уезжали на единицу ровно в этом модуле.
    2. `len(текст.split("\\n"))` даёт на единицу БОЛЬШЕ `wc -l` у каждого файла
       с завершающим переносом (появляется пустой последний элемент). На 113
       модулях это ровно +113 строки: 38 592 вместо 38 479.

    Поэтому: для РАЗМЕРА — `count("\\n")` (совпадает с `wc -l`), для НОМЕРА
    СТРОКИ — индекс в `split("\\n")`, он совпадает с `ast.lineno`.
    """
    return текст.count("\n")


def первая_строка_докстринга(node) -> str:
    doc = (ast.get_docstring(node) or "").strip()
    if not doc:
        return ""
    return doc.split("\n")[0].strip()


def зачем_модуля(tree: ast.Module) -> str:
    """Абзац «ЗАЧЕМ» из докстринга модуля — замысел, а не пересказ кода."""
    doc = ast.get_docstring(tree) or ""
    m = ЗАЧЕМ.search(doc)
    текст = (m.group(1) if m else doc).strip()
    текст = " ".join(текст.split())
    return текст[:600] + ("…" if len(текст) > 600 else "")


def элементы(tree: ast.Module, src_lines: list[str]) -> list[tuple[int, str, str, str]]:
    """(строка, тип, имя, назначение) для каждого элемента верхнего уровня."""
    out = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = [a.arg for a in node.args.args if a.arg not in ("self", "cls")]
            sig = f"{node.name}({', '.join(args)})"
            out.append((node.lineno, "функция", sig, первая_строка_докстринга(node)))
        elif isinstance(node, ast.ClassDef):
            методы = [n.name for n in node.body
                      if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                      and not n.name.startswith("_")]
            out.append((node.lineno, "класс",
                        f"{node.name} ({len(методы)} публичных методов)",
                        первая_строка_докстринга(node)))
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            имена = []
            цели = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in цели:
                if isinstance(t, ast.Name):
                    имена.append(t.id)
            if not имена:
                continue
            значение = node.value
            описание = ""
            if isinstance(значение, (ast.Dict, ast.List, ast.Set, ast.Tuple)):
                описание = f"{type(значение).__name__.lower()}, {len(значение.elts if isinstance(значение, (ast.List, ast.Set, ast.Tuple)) else значение.keys)} элементов"
            elif isinstance(значение, ast.Constant) and isinstance(значение.value, str):
                описание = f"строка: «{значение.value[:70]}»"
            elif isinstance(значение, ast.Call):
                описание = ast.unparse(значение)[:80]
            for имя in имена:
                out.append((node.lineno, "константа", имя, описание))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
    out.sort()
    return out


def коды_состояний(path: Path) -> list[str]:
    """Строковые литералы в ВЕРХНЕМ РЕГИСТРЕ — коды состояний/вердиктов.

    Именно их объявляют спеки и именно их сверяет контрактный аудит, поэтому
    в реестре они нужны списком, а не «примерно такие».
    """
    текст = path.read_text(encoding="utf-8", errors="replace")
    найдено = set(re.findall(r'"([A-Z][A-Z0-9_]{2,})"', текст))
    найдено |= set(re.findall(r"'([A-Z][A-Z0-9_]{2,})'", текст))
    мусор = {"UTF", "SHA", "JSON", "HTTP", "HTTPS", "URL", "API", "CPU", "GPU",
             "TODO", "NOTE", "PASS", "FAIL", "TRUE", "FALSE", "NONE", "AND",
             "NOT", "OR", "SQL", "CSV", "PDF", "DOCX", "MD", "R", "M", "N"}
    return sorted(x for x in найдено if x not in мусор)


def тесты_для(имя: str, каталоги: Path | list[Path]) -> list[str]:
    """Тестовые файлы, которые зовут модуль по имени.

    Каталогов два (`tests/` и `helix_pipeline/tests/`), потому что модуль
    ядра HELIX может быть назван только в корневом тесте: `market_text`
    проверяется `tests/test_helix_market_text.py`, а не своим пакетом.
    Поиск по одному каталогу объявлял такие модули непроверенными.

    Путь печатается от корня репозитория: одинаковые имена файлов в двух
    каталогах иначе слились бы в одну строку.
    """
    if isinstance(каталоги, Path):
        каталоги = [каталоги]
    out: list[str] = []
    for каталог in каталоги:
        try:
            от_корня = каталог.resolve().relative_to(ROOT).as_posix()
        except ValueError:
            от_корня = каталог.name
        for f in sorted(каталог.glob("*.py")):
            текст = f.read_text(encoding="utf-8", errors="replace")
            if re.search(rf"\b{re.escape(имя)}\b", текст):
                out.append(f"{от_корня}/{f.name}")
    return sorted(out)


ТОЧКИ_ВХОДА = (ROOT / "api" / "service.py", ROOT / "api" / "router.py")


def _импортирует(tree: ast.AST, модуль: str) -> bool:
    """Файл импортирует модуль или что-то из него — по AST, не по подстроке."""
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module == модуль or node.module.startswith(модуль + "."):
                return True
            пакет, _, имя = модуль.rpartition(".")
            if node.module == пакет and any(a.name == имя for a in node.names):
                return True
        elif isinstance(node, ast.Import):
            if any(a.name == модуль or a.name.startswith(модуль + ".")
                   for a in node.names):
                return True
    return False


def _импортируемые_имена(путь: Path, пакет: str) -> set[str]:
    """Имена модулей пакета, которые импортирует файл.

    Понимает обе формы: абсолютную (`from engine.x import y` — так пишет
    `api/`) и относительную (`from .x import y` — так пишут внутри пакета).
    """
    try:
        tree = ast.parse(путь.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return set()
    out: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.level:
                if node.module:
                    out.add(node.module.split(".")[-1])
            elif node.module:
                части = node.module.split(".")
                if len(части) >= 2 and части[0] == пакет:
                    out.add(части[-1])
        elif isinstance(node, ast.Import):
            for alias in node.names:
                части = alias.name.split(".")
                if len(части) >= 2 and части[0] == пакет:
                    out.add(части[-1])
    return out


def кто_зовёт(engine: Path, пакет: str) -> dict[str, list[str]]:
    """{модуль: [модули того же пакета, которые его импортируют]}."""
    обратное: dict[str, list[str]] = {}
    for path in sorted(engine.glob("*.py")):
        if path.name == "__init__.py":
            continue
        for имя in _импортируемые_имена(path, пакет):
            список = обратное.setdefault(имя, [])
            if path.stem not in список:
                список.append(path.stem)
    return обратное


def тесты_точки_входа(файл: Path) -> list[str]:
    """Тесты, которые импортируют `api/service.py` или `api/router.py`."""
    модуль = f"api.{файл.stem}"
    out: list[str] = []
    for f in sorted((ROOT / "tests").glob("*.py")):
        try:
            tree = ast.parse(f.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        if _импортирует(tree, модуль):
            out.append(f"tests/{f.name}")
    return out


def реестр_модулей(engine: Path, тест_каталоги: list[Path], пакет: str,
                   путь_от_корня: str,
                   заголовок: str, примечание: list[str],
                   якоря: dict[str, str] | None = None) -> str:
    """Один и тот же поэлементный реестр для любого пакета продукта.

    Общий, а не три копии: правило «реестр генерируется, а не пишется руками»
    должно выполняться одинаково для всех трёх продуктов, иначе расхождение
    между ними снова станет расхождением в прозе.
    """
    строки = [f"# {заголовок}", ""] + примечание + [""]
    модули = sorted(p for p in engine.glob("*.py") if p.name != "__init__.py")
    обратное = кто_зовёт(engine, пакет)
    точки: dict[str, list[Path]] = {}
    for api_файл in ТОЧКИ_ВХОДА:
        for имя in _импортируемые_имена(api_файл, пакет):
            точки.setdefault(имя, []).append(api_файл)
    тесты_входов = {п.stem: тесты_точки_входа(п) for п in ТОЧКИ_ВХОДА}
    всего_строк = 0
    всего_элементов = 0
    без_тестов = 0
    косвенно = 0
    for path in модули:
        src = path.read_text(encoding="utf-8", errors="replace")
        src_lines = src.split("\n")
        всего_строк += строк_в_файле(src)
        tree = ast.parse(src)
        elems = элементы(tree, src_lines)
        всего_элементов += len(elems)
        doc = первая_строка_докстринга(tree)
        строки.append(f"## {path.stem}")
        строки.append("")
        строки.append(f"- **путь**: `{путь_от_корня}/{path.name}`")
        строки.append(f"- **размер**: {строк_в_файле(src)} строк, SHA-256 blob `{sha256_blob(path)[:16]}…`")
        if doc:
            строки.append(f"- **что это**: {doc}")
        зачем = зачем_модуля(tree)
        if зачем.startswith(doc):
            зачем = зачем[len(doc):].strip(" .—-:")
        if зачем:
            строки.append(f"- **зачем**: {зачем}")
        if якоря:
            найденные = [spec for key, spec in якоря.items() if key in src]
            if найденные:
                строки.append("- **спека-якорь**: " + ", ".join(f"`{s}`" for s in найденные))
        коды = коды_состояний(path)
        if коды:
            строки.append(f"- **коды состояний** ({len(коды)}): " + ", ".join(f"`{c}`" for c in коды))
        т = тесты_для(path.stem, тест_каталоги)
        строки.append(f"- **тесты, которые зовут модуль**: {len(т)}" +
                      (f" — {', '.join(f'`{x}`' for x in т[:6])}" + ("…" if len(т) > 6 else "") if т else " (**прямого теста нет**)"))
        if not т:
            без_тестов += 1
            пути = []
            for api_файл in точки.get(path.stem, []):
                пути.append(f"`api/{api_файл.name}` (тестов на точку входа — "
                            f"{len(тесты_входов[api_файл.stem])})")
            for другой in sorted(обратное.get(path.stem, [])):
                чужие = тесты_для(другой, тест_каталоги)
                if чужие:
                    пути.append(f"`{путь_от_корня}/{другой}.py` "
                                f"(тестов, зовущих его, — {len(чужие)})")
            if пути:
                косвенно += 1
                строки.append("- **откуда достижим**: " + ", ".join(пути) +
                              " — **это путь в коде, а не тест поведения: "
                              "сам модуль ни один тест не зовёт**")
            else:
                строки.append("- **откуда достижим**: ниоткуда — ни одного теста "
                              "и ни одного импорта из `api/service.py`, "
                              "`api/router.py` или проверенного модуля пакета")
        строки.append("")
        строки.append("| строка | тип | элемент | назначение |")
        строки.append("|---:|---|---|---|")
        for ln, kind, name, purpose in elems:
            purpose = purpose.replace("|", "\\|")[:160]
            строки.append(f"| {ln} | {kind} | `{name}` | {purpose} |")
        строки.append("")
    header = [
        "",
        f"Всего **{len(модули)} модулей**, **{всего_строк} строк**, "
        f"**{всего_элементов} элементов верхнего уровня**. "
        f"Без прямого теста — **{без_тестов}**"
        + (f", из них достижимы косвенно (через `api/` или другой модуль "
           f"с тестами) — **{косвенно}**, без пути вообще — "
           f"**{без_тестов - косвенно}**." if без_тестов else "."),
        "",
        "---",
        "",
    ]
    n = len(примечание) + 2
    return "\n".join(строки[:n] + header + строки[n:]) + "\n"


def реестр_helix() -> str:
    return реестр_модулей(
        ENGINE, [TESTS_HELIX, ROOT / "tests"], "helix_pipeline", "helix_pipeline/engine",
        "HELIX — поэлементный реестр модулей ядра",
        [
            "**Сгенерировано, не написано руками**: `PYTHONUTF8=1 python scripts/реестр_продуктов.py`.",
            "Номера строк — из AST живого кода, назначение — из докстринга самого элемента,",
            "поэтому реестр не устаревает молча: при правке кода его пересобирают той же командой.",
            "",
            "Тесты ищутся в двух каталогах — `helix_pipeline/tests/` и корневом `tests/`:",
            "`market_text` и `claude_classifier` зовёт только корневой тест, и поиск",
            "по одному каталогу объявлял их непроверенными.",
            "",
            "Сопровождение: `HELIX_ЕДИНЫЙ_ПАСПОРТ.md` (раздел 5 — что за блоки, раздел 2 — масштаб).",
        ],
        SPEC_ANCHORS,
    )


def реестр_ak_master() -> str:
    return реестр_модулей(
        ROOT / "engine", [ROOT / "tests", TESTS_HELIX], "engine", "engine",
        "AK-MASTER — поэлементный реестр модулей движка",
        [
            "**Сгенерировано, не написано руками**: `PYTHONUTF8=1 python scripts/реестр_продуктов.py`.",
            "Тот же генератор, что и для HELIX: номера строк из AST, назначение из докстринга.",
            "",
            "Тесты ищутся в корневом `tests/` и в `helix_pipeline/tests/`.",
            "Если модуль не зовёт ни один тест, строка «откуда достижим» показывает,",
            "кто его импортирует: `api/service.py`, `api/router.py` или другой модуль",
            "пакета, у которого тесты есть. Это **путь в коде, а не проверка поведения**,",
            "и так он и подписан.",
            "",
            "Канон AK-MASTER (14 блоков, 13 ENFORCED + 1 DOC_ANCHOR) считает штатный",
            "`python -m engine.coverage_validator`; этот реестр — про код, а не про канон.",
            "Граница продуктов соблюдена: `engine/` не импортирует `helix_pipeline/` и `mr_helix/`",
            "(`ЧИТАЙ_ПЕРВЫМ.md`, раздел 1).",
        ],
        None,
    )


def капсулы() -> list[dict]:
    import yaml
    data = yaml.safe_load(MR_MANIFEST.read_text(encoding="utf-8"))
    return data["capsules"]


def статусы_капсул() -> dict[str, dict]:
    """Статусы из штатного валидатора, а не свои."""
    sys.path.insert(0, str(ROOT))
    from mr_helix.engine.capsule_coverage_validator import CapsuleCoverageValidator
    v = CapsuleCoverageValidator()
    отчёт = v.validate()
    return {c["capsule_id"]: c for c in отчёт["capsules"]}


def якорь_в_спеке(cid: str) -> str:
    """Заголовок «# 01.1 NAME» в спеке PACK_xx — что именно требует спека."""
    pack = cid.split(".")[0].zfill(2)
    for f in sorted(MR_SPEC.glob(f"MR_HELIX_v5_PACK_{pack}_*.md")):
        for n, line in enumerate(
                f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            if re.match(rf"^#{{1,4}}\s+{re.escape(cid)}\b", line):
                return f"`{f.name}:{n}` — {line.strip('# ').strip()[:110]}"
    return ""


def реестр_mr_helix() -> str:
    caps = капсулы()
    st = статусы_капсул()
    строки = [
        "# Мистер Хеликс — реестр по каждой капсуле",
        "",
        "**Сгенерировано, не написано руками**: `PYTHONUTF8=1 python scripts/реестр_продуктов.py`.",
        "Статус капсулы берёт штатный `mr_helix/engine/capsule_coverage_validator.py`:",
        "`ENFORCED` — символы есть в коде И существует тест, который их зовёт;",
        "`PARTIAL` — символы есть, теста нет; `SPEC_ONLY` — в коде ничего нет.",
        "Символ в коде ≠ поведение по спеке — это правило самого валидатора.",
        "",
        "Источник списка капсул — спеки `mr_helix/docs/spec/PACK_00..05`, а не карты",
        "требований: карт пять, у PACK_00 её нет, и полнота по картам молча теряла",
        "целый пакет из пятнадцати капсул (история — в шапке `capsule_manifest.yaml`).",
        "",
    ]
    по_пакетам: dict[str, list[dict]] = {}
    for c in caps:
        по_пакетам.setdefault(c["id"].split(".")[0].zfill(2), []).append(c)

    всего_символов = 0
    for pack in sorted(по_пакетам):
        группа = по_пакетам[pack]
        строки.append(f"## PACK {pack} — {len(группа)} капсул")
        строки.append("")
        for c in группа:
            cid = c["id"]
            запись = st.get(cid, {})
            модуль = c["module"]
            путь = MR_ENGINE / f"{модуль}.py"
            размер = строк_в_файле(путь.read_text(encoding="utf-8", errors="replace")) if путь.exists() else 0
            строки.append(f"### {cid} — {c['name']}")
            строки.append("")
            строки.append(f"- **статус**: `{запись.get('status', 'не определён')}`"
                          + (f" · тест: `{запись['tests'][0]}`" if запись.get("tests") else ""))
            строки.append(f"- **модуль**: `mr_helix/engine/{модуль}.py` ({размер} строк)")
            як = якорь_в_спеке(cid)
            if як:
                строки.append(f"- **требование спеки**: {як}")
            строки.append("")
            строки.append("| символ | строка в модуле | тип | назначение | тесты, где зовётся |")
            строки.append("|---|---:|---|---|---:|")
            for sym in c.get("symbols", []):
                всего_символов += 1
                ln, kind, purpose = "", "", ""
                if путь.exists():
                    tree = ast.parse(путь.read_text(encoding="utf-8", errors="replace"))
                    for node in tree.body:
                        имена = []
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                            имена = [node.name]
                            kind = "класс" if isinstance(node, ast.ClassDef) else "функция"
                            purpose = первая_строка_докстринга(node)
                        elif isinstance(node, ast.Assign):
                            имена = [t.id for t in node.targets if isinstance(t, ast.Name)]
                            kind = "константа"
                        if sym in имена:
                            ln = node.lineno
                            break
                т = тесты_для(sym, [MR_TESTS])
                строки.append(f"| `{sym}` | {ln or '—'} | {kind or '—'} | "
                              f"{purpose.replace('|', chr(92) + '|')[:120]} | {len(т)} |")
            строки.append("")
    header = [
        "",
        f"Всего **{len(caps)} капсул** в {len(по_пакетам)} пакетах; "
        f"символов в реестре — **{всего_символов}**.",
        "",
        "---",
        "",
    ]
    return "\n".join(строки[:11] + header + строки[11:]) + "\n"


def main() -> int:
    на_экран = "--stdout" in sys.argv
    документы = (
        (реестр_helix(), OUT_HELIX),
        (реестр_mr_helix(), OUT_MR),
        (реестр_ak_master(), OUT_AK),
    )
    for текст, путь in документы:
        if на_экран:
            print(текст)
        else:
            путь.write_text(текст, encoding="utf-8", newline="\n")
            print(f"{путь.relative_to(ROOT)}: {len(текст.split(chr(10)))} строк, {len(текст)} знаков")
    return 0


if __name__ == "__main__":
    sys.exit(main())
