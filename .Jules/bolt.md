## 2024-05-24 - Optimize QuerySet count and index access
**Learning:** In Django, checking existence using `.count() == 0` generates an unnecessary database `COUNT` query. When an item is retrieved immediately after an existence check, it is a two-query anti-pattern. `.exists()` and `.first()` are more efficient, producing an `EXISTS` query and a single `LIMIT 1` query respectively.
**Action:** Always use `.exists()` for pure existence checks and `.first()` when checking existence and retrieving an item.
