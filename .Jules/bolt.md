## 2024-05-24 - Database Query Optimization
**Learning:** Pure existence checks using `.count() == 0` generate an unnecessary database `COUNT` SQL query (unlike `len()`, which evaluates the QuerySet in-memory). Moreover, checking count and then fetching the first element with `[0]` results in a two-query anti-pattern.
**Action:** Use `.exists()` instead of `.count() == 0` for pure existence checks. If fetching the first item, use `.first()` directly to consolidate into a single query.
