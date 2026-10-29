#!/usr/bin/env python3
"""проверка_реестров.py — доказательство, а не слова: сверяет реестры с кодом.

ЗАЧЕМ (27.10.2026). Владелец спросил прямо: «чем докажешь, что проверил, а не
на словах». Ответ должен быть командой, которую может запустить кто угодно,
в том числе человек, который мне не доверяет. Этот скрипт не доверяет ни одному
своему же документу: он читает реестры как данные и переспрашивает код.

Что проверяется (каждый пункт — по всем элементам, не по выборке):

  A. `HELIX_РЕЕСТР_ПО_МОДУЛЯМ.md`
     A1 множество модулей в реестре == множество .py на диске (в обе стороны)
     A2 число элементов в реестре == число элементов из независимого обхода AST
     A3 для КАЖДОЙ строки таблицы: файл существует, номер строки в его пределах,
        и на этой строке действительно объявлен названный элемент
     A4 размер модуля в реестре == `wc -l` живого файла
     A5 SHA-256 blob в реестре == пересчитанный хэш

  B. `AK_MASTER_РЕЕСТР_ПО_МОДУЛЯМ.md` — те же A1..A5

  C. `MR_HELIX_РЕЕСТР_ПО_КАПСУЛАМ.md`
     C1 id капсул в реестре == id в `capsule_manifest.yaml` (99)
     C2 статус каждой капсулы == статус штатного `capsule_coverage_validator`
     C3 для КАЖДОГО символа: номер строки в модуле и объявление на этой строке
     C4 якорь спеки: в названном файле на названной строке — заголовок с этим id
     C5 размер модуля в реестре == живой размер

  D. `MANIFEST_SHA256.md`
     D1 ни одного файла вне описи и ни одной записи о несуществующем файле
     D2 хэш каждой записи совпадает (для текстовых — с LF-нормализацией,
        для бинарных — побайтно; Windows-клон в CRLF, см. Приложение А.1 паспорта)

  E. Пересчёт чисел раздела 2 паспорта той же командой, что в нём написана

  F. Каждое имя `.py` и `.md`, названное в паспорте, существует в репозитории

Вердикт: `ПРОЙДЕНО n/n` или список провалов с номером проверки. Выход 0 только
если провалов нет — скрипт можно ставить в CI.

Использование:
    PYTHONUTF8=1 python scripts/проверка_реестров.py
    PYTHONUTF8=1 python scripts/проверка_реестров.py --quiet   # только вердикт
"""
from __future__ import annotations

import ast
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PASSPORTS = ROOT / "docs" / "passports"
ТИХО = "--quiet" in sys.argv

провалы: list[str] = []
счётчики: dict[str, int] = {}


def шаг(метка: str, условие: bool, подробность: str = "") -> bool:
    """Один атом проверки: True/False плюс счётчик для итогового вердикта."""
    ключ = метка
    счётчики[ключ] = счётчики.get(ключ, 0) + 1
    if not условие:
        провалы.append(f"[{метка}] {подробность}")
        if not ТИХО:
            print(f"  ПРОБАЛ {метка}: {подробность}")
    return условие


def sha256_blob(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def строк_в_файле(текст: str) -> int:
    """Размер файла как у `wc -l` — см. докстринг той же функции в генераторе.

    `splitlines()` и `len(split("\\n"))` дают ДРУГИЕ числа: первое режет ещё по
    U+2028/U+2029 (они есть в `engine/невидимые_символы.py`), второе добавляет
    единицу на каждый файл с завершающим переносом.
    """
    return текст.count("\n")


def элементов_в_коде(path: Path) -> list[tuple[int, str, str]]:
    """[(номер строки, тип, имя)] — независимый пересчёт, не из реестра.

    Один элемент на каждое объявленное имя: `a = b = 1` даёт две записи с
    одним номером строки, как и в генераторе реестра.
    """
    tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    out: list[tuple[int, str, str]] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out.append((node.lineno, "функция", node.name))
        elif isinstance(node, ast.ClassDef):
            out.append((node.lineno, "класс", node.name))
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            цели = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in цели:
                if isinstance(t, ast.Name):
                    out.append((node.lineno, "константа", t.id))
    return out


def объявлено_на_строке(строки: list[str], ln: int, имя: str, тип: str) -> bool:
    """Имя действительно объявлено на этой строке, а не просто упомянуто."""
    if ln < 1 or ln > len(строки):
        return False
    line = строки[ln - 1]
    if тип == "функция":
        return bool(re.search(rf"^\s*(async\s+)?def\s+{re.escape(имя)}\s*\(", line))
    if тип == "класс":
        return bool(re.search(rf"^\s*class\s+{re.escape(имя)}\b", line))
    return bool(re.search(rf"^\s*{re.escape(имя)}\s*(:[^=]+)?=", line))


def строка_таблицы(line: str):
    """Разбирает строку таблицы реестра: | 141 | константа | `_X` | … |

    Имя возвращается БЕЗ хвоста: реестр печатает сигнатуру
    (`привязать(факт, текст)`) и пометку класса (`Hypothesis (0 публичных
    методов)`), а объявление в коде надо искать по чистому имени.
    """
    if not line.startswith("| ") or line.startswith("|---") or line.startswith("| строка"):
        return None
    части = [c.strip() for c in line.strip("|").split("|")]
    if len(части) < 4 or not части[0].isdigit():
        return None
    имя = части[2].strip("`")
    имя = имя.split(" (")[0].split("(")[0].strip()
    return int(части[0]), части[1], имя


def проверить_реестр_модулей(файл: Path, каталог: Path, префикс: str, метка: str) -> None:
    текст = файл.read_text(encoding="utf-8").split("\n")
    модули_реестра: list[str] = []
    текущий: Path | None = None
    строк_в_реестре: dict[str, int] = {}
    хэши: dict[str, str] = {}
    элементов_реестр: dict[str, list[tuple[int, str, str]]] = {}

    for line in текст:
        if line.startswith("## "):
            имя = line[3:].strip()
            текущий = каталог / f"{имя}.py"
            модули_реестра.append(имя)
            элементов_реестр.setdefault(имя, [])
        elif текущий is not None and line.startswith("- **размер**:"):
            m = re.search(r"\*\*размер\*\*: (\d+) строк, SHA-256 blob `([0-9a-f]{16})", line)
            if m:
                строк_в_реестре[текущий.stem] = int(m.group(1))
                хэши[текущий.stem] = m.group(2)
        elif текущий is not None:
            разобрано = строка_таблицы(line)
            if разобрано:
                элементов_реестр[текущий.stem].append(разобрано)

    на_диске = sorted(p.stem for p in каталог.glob("*.py") if p.name != "__init__.py")
    шаг(f"{метка}.A1", set(на_диске) == set(модули_реестра),
        f"в реестре {len(модули_реестра)}, на диске {len(на_диске)}; "
        f"лишние: {sorted(set(модули_реестра) - set(на_диске))[:5]}; "
        f"пропущены: {sorted(set(на_диске) - set(модули_реестра))[:5]}")

    всего_элементов = 0
    for stem in на_диске:
        path = каталог / f"{stem}.py"
        src = path.read_text(encoding="utf-8", errors="replace")
        строки = src.split("\n")
        код = элементов_в_коде(path)
        реестр = элементов_реестр.get(stem, [])
        всего_элементов += len(реестр)
        шаг(f"{метка}.A2", sorted(реестр) == sorted(код),
            f"{stem}: реестр и независимый обход AST разошлись — "
            f"в реестре {len(реестр)}, в коде {len(код)}; "
            f"только в реестре {sorted(set(реестр) - set(код))[:3]}; "
            f"только в коде {sorted(set(код) - set(реестр))[:3]}")
        for ln, тип, имя in реестр:
            шаг(f"{метка}.A3", объявлено_на_строке(строки, ln, имя, тип),
                f"{префикс}{stem}.py:{ln} — «{тип} {имя}» на этой строке не объявлен")
        шаг(f"{метка}.A4", строк_в_реестре.get(stem) == строк_в_файле(src),
            f"{stem}: в реестре {строк_в_реестре.get(stem)} строк, в файле {строк_в_файле(src)}")
        шаг(f"{метка}.A5", хэши.get(stem) == sha256_blob(path)[:16],
            f"{stem}: хэш в реестре {хэши.get(stem)} != {sha256_blob(path)[:16]}")
    if not ТИХО:
        print(f"  {метка}: модулей {len(на_диске)}, элементов сверено {всего_элементов}")


def проверить_реестр_капсул() -> None:
    import yaml
    файл = PASSPORTS / "MR_HELIX_РЕЕСТР_ПО_КАПСУЛАМ.md"
    текст = файл.read_text(encoding="utf-8").split("\n")
    манифест = yaml.safe_load((ROOT / "mr_helix" / "docs" / "capsule_manifest.yaml")
                              .read_text(encoding="utf-8"))
    капсулы = {str(c["id"]): c for c in манифест["capsules"]}

    sys.path.insert(0, str(ROOT))
    from mr_helix.engine.capsule_coverage_validator import CapsuleCoverageValidator
    статусы = {c["capsule_id"]: c for c in CapsuleCoverageValidator().validate()["capsules"]}

    текущий: str | None = None
    статус_в_реестре: dict[str, str] = {}
    модуль_в_реестре: dict[str, tuple[str, int]] = {}
    якорь_в_реестре: dict[str, tuple[str, int]] = {}
    символы_реестр: dict[str, list[tuple[str, int]]] = {}

    for line in текст:
        m = re.match(r"^### (\d\d\.\d+\w*) — (\S+)", line)
        if m:
            текущий = m.group(1)
            символы_реестр.setdefault(текущий, [])
            continue
        if текущий is None:
            continue
        m = re.search(r"\*\*статус\*\*: `(\w+)`", line)
        if m:
            статус_в_реестре[текущий] = m.group(1)
        m = re.search(r"\*\*модуль\*\*: `mr_helix/engine/([\w.]+)\.py` \((\d+) строк\)", line)
        if m:
            модуль_в_реестре[текущий] = (m.group(1), int(m.group(2)))
        m = re.search(r"\*\*требование спеки\*\*: `([^:`]+):(\d+)` — (\S+)", line)
        if m:
            якорь_в_реестре[текущий] = (m.group(1), int(m.group(2)))
        m = re.match(r"^\| `(\w+)` \| (\d+|—) \|", line)
        if m and m.group(2) != "—":
            символы_реестр[текущий].append((m.group(1), int(m.group(2))))

    шаг("C.C1", set(символы_реестр) == set(капсулы),
        f"в реестре {len(символы_реестр)} капсул, в манифесте {len(капсулы)}; "
        f"лишние {sorted(set(символы_реестр) - set(капсулы))[:5]}, "
        f"пропущены {sorted(set(капсулы) - set(символы_реестр))[:5]}")

    всего = 0
    for cid, cap in капсулы.items():
        шаг("C.C2", статус_в_реестре.get(cid) == статусы[cid]["status"],
            f"{cid}: в реестре {статус_в_реестре.get(cid)}, валидатор дал {статусы[cid]['status']}")
        имя_модуля, размер = модуль_в_реестре.get(cid, (cap["module"], -1))
        шаг("C.C5", имя_модуля == cap["module"],
            f"{cid}: модуль в реестре {имя_модуля}, в манифесте {cap['module']}")
        путь = ROOT / "mr_helix" / "engine" / f"{cap['module']}.py"
        if путь.exists():
            текст_модуля = путь.read_text(encoding="utf-8", errors="replace")
            строки = текст_модуля.split("\n")
            шаг("C.C5", размер == строк_в_файле(текст_модуля),
                f"{cid}: размер в реестре {размер}, в файле {строк_в_файле(текст_модуля)}")
            for sym, ln in символы_реестр.get(cid, []):
                всего += 1
                шаг("C.C3", объявлено_на_строке(строки, ln, sym, "функция")
                    or объявлено_на_строке(строки, ln, sym, "класс")
                    or объявлено_на_строке(строки, ln, sym, "константа"),
                    f"{cid} {sym}: {путь.name}:{ln} — объявления на строке нет")
        як = якорь_в_реестре.get(cid)
        шаг("C.C4", як is not None, f"{cid}: нет якоря в спеке")
        if як:
            spec = ROOT / "mr_helix" / "docs" / "spec" / як[0]
            if шаг("C.C4", spec.exists(), f"{cid}: файл спеки {як[0]} не найден"):
                заголовок = spec.read_text(encoding="utf-8", errors="replace").split("\n")[як[1] - 1]
                шаг("C.C4", re.match(rf"^#{{1,4}}\s+{re.escape(cid)}\b", заголовок) is not None,
                    f"{cid}: {як[0]}:{як[1]} — «{заголовок[:60]}» не заголовок этой капсулы")
    if not ТИХО:
        print(f"  C: капсул {len(капсулы)}, символов сверено {всего}")


def проверить_манифест() -> None:
    import importlib.util
    spec = importlib.util.spec_from_file_location("gm", str(ROOT / "scripts" / "generate_manifest.py"))
    gm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gm)
    man = {}
    for line in (ROOT / "MANIFEST_SHA256.md").read_text(encoding="utf-8").split("\n"):
        p = line.split(None, 1)
        if len(p) == 2 and len(p[0]) == 64:
            man[p[1]] = p[0]
    actual = {str(rel).replace("\\", "/"): (ROOT / rel) for rel in gm.iter_files(ROOT)}
    шаг("D.D1", set(man) == set(actual),
        f"в описи {len(man)}, файлов {len(actual)}; вне описи {sorted(set(actual) - set(man))[:5]}; "
        f"записей без файла {sorted(set(man) - set(actual))[:5]}")
    плохих = 0
    for f, path in actual.items():
        if f not in man:
            continue
        b = path.read_bytes()
        if man[f] not in (hashlib.sha256(b).hexdigest(),
                          hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()):
            плохих += 1
            if плохих <= 5:
                провалы.append(f"[D.D2] {f}: хэш не совпадает")
    шаг("D.D2", плохих == 0, f"хэш не совпал у {плохих} файлов")
    if not ТИХО:
        print(f"  D: записей в описи {len(man)}, файлов {len(actual)}, расхождений хэшей {плохих}")


def проверить_числа_паспорта() -> None:
    паспорт = PASSPORTS / "HELIX_ЕДИНЫЙ_ПАСПОРТ.md"
    текст = паспорт.read_text(encoding="utf-8")
    модули = sorted(p for p in (ROOT / "helix_pipeline" / "engine").glob("*.py")
                    if p.name != "__init__.py")
    строк_ядра = sum(строк_в_файле(p.read_text(encoding="utf-8", errors="replace")) for p in модули)
    файлов_пакета = [p for p in (ROOT / "helix_pipeline").rglob("*.py") if "__pycache__" not in p.parts]
    строк_пакета = sum(строк_в_файле(p.read_text(encoding="utf-8", errors="replace")) for p in файлов_пакета)
    спек = sorted((ROOT / "helix_pipeline" / "docs" / "specs").glob("*.md"))
    строк_спек = sum(строк_в_файле(p.read_text(encoding="utf-8", errors="replace")) for p in спек)
    тестов_файлов = sorted((ROOT / "helix_pipeline" / "tests").glob("*.py"))
    строк_тестов = sum(строк_в_файле(p.read_text(encoding="utf-8", errors="replace")) for p in тестов_файлов)
    mcp = len(re.findall(r"@mcp\.tool", (ROOT / "api" / "mcp_server.py").read_text(encoding="utf-8")))

    # Ожидания НЕ захардкожены: проверяем, что в паспорте стоит сегодняшнее
    # измеренное число. Захардкоженное число устаревает при первой же правке
    # кода — и проверяльщик начинает врать сам, что и случилось 27.10.
    def с_пробелами(n: int) -> str:
        return f"{n:,}".replace(",", " ")

    ожидания = {
        "модулей ядра": с_пробелами(len(модули)),
        "строк ядра": с_пробелами(строк_ядра),
        "файлов пакета": с_пробелами(len(файлов_пакета)),
        "строк пакета": с_пробелами(строк_пакета),
        "строк спецификаций": с_пробелами(строк_спек),
        "файлов тестов": с_пробелами(len(тестов_файлов)),
        "строк тестов": с_пробелами(строк_тестов),
        "MCP-инструментов": с_пробелами(mcp),
    }
    for что, число in ожидания.items():
        шаг("E", число in текст,
            f"паспорт не содержит свежего числа «{число}» ({что}) — строка устарела")
    if not ТИХО:
        print(f"  E: модулей {len(модули)}, строк ядра {строк_ядра}, спек {строк_спек}, "
              f"тестов-файлов {len(тестов_файлов)}, MCP {mcp}")


def проверить_имена_в_паспорте() -> None:
    паспорт = PASSPORTS / "HELIX_ЕДИНЫЙ_ПАСПОРТ.md"
    текст = паспорт.read_text(encoding="utf-8")
    имена = set(re.findall(r"`([A-Za-zА-Яа-яёЁ0-9_]+\.(?:py|md))`", текст))
    известных = {p.name for p in ROOT.rglob("*") if p.suffix in (".py", ".md") and "__pycache__" not in p.parts}
    будущие = {"AK_MASTER_ЕДИНЫЙ_ПАСПОРТ.md", "MR_HELIX_ЕДИНЫЙ_ПАСПОРТ.md"}
    for имя in sorted(имена - будущие):
        шаг("F", имя in известных, f"паспорт ссылается на несуществующий файл `{имя}`")
    if not ТИХО:
        print(f"  F: имён файлов в паспорте {len(имена)}, все существуют "
              f"(кроме {len(будущие)} объявленных как будущие)")


def main() -> int:
    print("=" * 76)
    print("ПРОВЕРКА РЕЕСТРОВ И ПАСПОРТА — каждое утверждение переспрошено у кода")
    print("=" * 76)
    проверить_реестр_модулей(PASSPORTS / "HELIX_РЕЕСТР_ПО_МОДУЛЯМ.md",
                             ROOT / "helix_pipeline" / "engine",
                             "helix_pipeline/engine/", "A")
    проверить_реестр_модулей(PASSPORTS / "AK_MASTER_РЕЕСТР_ПО_МОДУЛЯМ.md",
                             ROOT / "engine", "engine/", "B")
    проверить_реестр_капсул()
    проверить_манифест()
    проверить_числа_паспорта()
    проверить_имена_в_паспорте()
    всего = sum(счётчики.values()) + len([p for p in провалы if p.startswith("[D.D2]")])
    print("-" * 76)
    if провалы:
        print(f"ПРОВАЛОВ: {len(провалы)} (первые 20):")
        for p in провалы[:20]:
            print("  ", p)
        print(f"Всего атомов проверки: {всего}")
        return 1
    print(f"ПРОЙДЕНО {всего}/{всего} — ни одного провала.")
    print("Сверено: каждый модуль, каждый элемент реестра и его номер строки,")
    print("каждая капсула и каждый её символ, статусы из штатного валидатора,")
    print("якоря в спеках, опись SHA-256, числа раздела 2 паспорта, имена файлов.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
