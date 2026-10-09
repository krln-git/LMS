## 2023-10-10 - Replace .count() == 0 with .first() and .exists()
**Learning:** In Django, using `.count() == 0` on a QuerySet performs a database query to count the results. If you only need the first element, use `.first()` instead. If you only need to check if any records exist, use `.exists()` instead. This avoids evaluating the QuerySet in memory and executing an unnecessary `COUNT()` query.
**Action:** Use `.first()` when retrieving the first element and `.exists()` when checking for existence.
