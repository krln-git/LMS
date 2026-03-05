## 2026-03-05 - [Pytest execution]
**Learning:** Full `pytest` execution is unstable due to missing dependencies (`kombu`, `celery`, `lxml`). Mocking `sys.modules` to bypass this often fails due to deep import chains.
**Action:** Use isolated Python execution scripts to verify logic or use `py_compile.compile` for syntax checks.
