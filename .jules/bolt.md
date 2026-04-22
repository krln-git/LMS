## 2024-05-20 - Avoid .count() combined with indexing for existence checks
**Learning:** Using `QuerySet.count() == 0` for an existence check immediately followed by accessing the first element via an index (e.g., `user[0]`) is an anti-pattern. It triggers two separate database queries (`COUNT` and `LIMIT 1`).
**Action:** Replace this pattern with `.first()` to perform both the existence check and retrieval in a single query.
