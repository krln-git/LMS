## 2026-03-14 - Django QuerySet Existence Check
**Learning:** In Django QuerySets, using `.count() == 0` or `len(QuerySet) == 0` executes a `SELECT COUNT(*)` query or fetches all rows into memory, which is inefficient. Using `.exists()` is faster for simple existence checks as it doesn't fetch rows or evaluate `COUNT(*)`.
**Action:** Replaced `.count() == 0` with `not .exists()` in `cms/djangoapps/course_creators/views.py` and `lms/djangoapps/instructor_task/tasks_helper/module_state.py` to improve database query performance.
