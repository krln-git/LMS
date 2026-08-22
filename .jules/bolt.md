## 2024-05-24 - Avoid `.count() == 0` for query existence check
**Learning:** In Django, using `QuerySet.count() == 0` executes a `COUNT` query which is unnecessary if we only want to check existence. `QuerySet.exists()` executes a more efficient `EXISTS` query. Also, checking for existence just to grab the first element `if q.count() > 0: item = q[0]` is a two-query anti-pattern that can be replaced with `QuerySet.first()`.
**Action:** Use `.exists()` or `.first()` instead of checking `.count() == 0` or `.count() > 0`.
