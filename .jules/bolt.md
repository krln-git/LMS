## 2024-05-18 - Avoid COUNT Queries for Existence Checks
**Learning:** In Django, using `.count() == 0` on a QuerySet generates a `COUNT` SQL query, which can be slow on large tables. Evaluating existence and then indexing `[0]` generates two separate database queries. These are codebase-specific performance anti-patterns that can easily be optimized.
**Action:** Replace `.count() == 0` pure existence checks with `.exists()`, which uses an efficient `EXISTS` SQL query. Replace `.count() > 0` followed by index access `[0]` with a single `.first()` call.
