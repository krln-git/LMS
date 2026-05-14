## 2024-05-14 - Optimize Django ORM Existence Checks
**Learning:** Using `.count() == 0` for a simple existence check is inefficient because it triggers a `COUNT` query. Using `.count() == 0` followed by index access like `obj[0]` is worse because it triggers two queries (`COUNT` and `LIMIT 1`).
**Action:** Replace `.count() == 0` checks with `.exists()` when only boolean existence is needed. If the object needs to be retrieved, use `.first()` to combine the check and retrieval into a single query.
