## 2025-02-12 - Django ORM: .count() + Indexing Triggers Dual Queries
**Learning:** Using `.count() == 0` for an existence check, immediately followed by accessing the first element via index (e.g., `user[0]`), is a codebase-specific anti-pattern that triggers two separate database queries (`COUNT` and then `LIMIT 1`).
**Action:** Replace this pattern with `.first()` to perform both the existence check and retrieval in a single query, halving the DB hits. For simple existence checks without retrieval, always prefer `.exists()` over `.count() == 0`.
