## 2024-05-23 - Use exists() instead of count() == 0 for Existence Checks
**Learning:** In Django codebases like Open edX, use `QuerySet.exists()` instead of `len(QuerySet) != 0` or `QuerySet.count() == 0` for simple existence checks to avoid fetching all rows into memory or executing unnecessary `COUNT(*)` queries. The database performs an optimized `EXISTS (SELECT (1) FROM ... LIMIT 1)` check when using `.exists()`.
**Action:** When checking if any rows exist that match a condition, always use `exists()`. Only use `count()` when the exact numerical count is actually required.
