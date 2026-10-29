# CI diagnostics, python 3.12, 2026-10-29T00:01:11Z

## tail tests/
...............................ssssssssss.........F.......ssss.......... [ 89%]
.............................................................s.......... [ 90%]
.s....s.............................................ss................s. [ 92%]
................................................................ssssss.. [ 93%]
............ss...................s...................................... [ 94%]
...................................ss................................... [ 96%]
........................................................................ [ 97%]
........ss.............................................................. [ 98%]
...............................................................ss        [100%]
=================================== FAILURES ===================================
______________________ test_манифест_репозитория_сходится ______________________

    @pytest.mark.slow
    def test_манифест_репозитория_сходится():
        """Тот же вызов, что стоит последним шагом в CI.
    
        Он не сходился с 11.07 по 07.09 — и именно поэтому CI не мог быть
        зелёным независимо от того, кто и когда регенерировал манифест.
        """
        готово = subprocess.run(
            [sys.executable, str(СКРИПТ), "--verify"],
            capture_output=True, text=True, timeout=600, cwd=str(КОРЕНЬ))
>       assert готово.returncode == 0, (
            "Манифест разошёлся с каталогом. Чинится одной командой — но "
            "ПОСЛЕДНИМ шагом, после сборки фронта и всех правок:\n"
            "    python3 scripts/generate_manifest.py > MANIFEST_SHA256.md\n"
            "Если сделать раньше, он снова разойдётся.\n\n"
            + готово.stdout[-3000:])
E       AssertionError: Манифест разошёлся с каталогом. Чинится одной командой — но ПОСЛЕДНИМ шагом, после сборки фронта и всех правок:
E             python3 scripts/generate_manifest.py > MANIFEST_SHA256.md
E         Если сделать раньше, он снова разойдётся.
E         
E         записей в манифесте: 1858
E         реальных файлов (кроме исключённых): 1859
E         упомянуты в манифесте, но отсутствуют: 0
E         хэш не совпадает: 0
E         есть в каталоге, но не в манифесте: 1
E         
E         не в манифесте (возможно, забыли добавить):
E           docs/CI_DIAGNOSTICS.md
E         
E         FAIL — манифест не соответствует реальному состоянию каталога
E         
E       assert 1 == 0
E        +  where 1 = CompletedProcess(args=['/opt/hostedtoolcache/Python/3.12.15/x64/bin/python', '/home/runner/work/102/102/scripts/genera...ли добавить):\n  docs/CI_DIAGNOSTICS.md\n\nFAIL — манифест не соответствует реальному состоянию каталога\n', stderr='').returncode

tests/test_манифест_считает_лишние_файлы.py:124: AssertionError
=============================== warnings summary ===============================
../../../../../opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/fastapi/testclient.py:1
  /opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

tests/test_tst_dv_resistance_regex.py:3
  /home/runner/work/102/102/tests/test_tst_dv_resistance_regex.py:3: SyntaxWarning: invalid escape sequence '\w'
    Найдено 28.08.2026 живым прогоном главы «Тени на рентгене»: суффикс \w*

tests/test_whole_word_reading.py:4
  /home/runner/work/102/102/tests/test_whole_word_reading.py:4: SyntaxWarning: invalid escape sequence '\w'
    с границами \b; корень+\w* и подстроки уходят.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/test_манифест_считает_лишние_файлы.py::test_манифест_репозитория_сходится - AssertionError: Манифест разошёлся с каталогом. Чинится одной командой — но ПОСЛЕДНИМ шагом, после сборки фронта и всех правок:
      python3 scripts/generate_manifest.py > MANIFEST_SHA256.md
  Если сделать раньше, он снова разойдётся.
  
  записей в манифесте: 1858
  реальных файлов (кроме исключённых): 1859
  упомянуты в манифесте, но отсутствуют: 0
  хэш не совпадает: 0
  есть в каталоге, но не в манифесте: 1
  
  не в манифесте (возможно, забыли добавить):
    docs/CI_DIAGNOSTICS.md
  
  FAIL — манифест не соответствует реальному состоянию каталога
  
assert 1 == 0
 +  where 1 = CompletedProcess(args=['/opt/hostedtoolcache/Python/3.12.15/x64/bin/python', '/home/runner/work/102/102/scripts/genera...ли добавить):\n  docs/CI_DIAGNOSTICS.md\n\nFAIL — манифест не соответствует реальному состоянию каталога\n', stderr='').returncode
1 failed, 5191 passed, 129 skipped, 3 warnings in 306.62s (0:05:06)

## tail helix_pipeline/tests
(нет файла)
