## 2024-05-17 - Avoid .count() == 0 for existence checks in Django ORM
**Learning:** Using `.count() == 0` followed by `[0]` on a Django queryset triggers two separate database queries (`COUNT` and `LIMIT 1`). Using `.count() == 0` for pure existence checks triggers an unnecessary `COUNT` query when `.exists()` is more efficient.
**Action:** Always use `.first()` to perform both existence check and retrieval in a single query, and use `.exists()` for boolean existence checks without retrieval.
