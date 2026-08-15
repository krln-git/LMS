## 2024-05-23 - Optimize QuerySet usage with first()
**Learning:** In Django, `.count()` generates a `COUNT` SQL query, not an in-memory evaluation like `len()`, but it can still be inefficient. More importantly, when checking existence *and* retrieving the item immediately after (e.g., `if count > 0: item = q[0]`), it executes two separate queries. Using `.first()` fetches the item safely in a single query.
**Action:** Always use `.first()` when retrieving the single matched record, avoiding `.count()` followed by array access.
