## 2024-05-18 - Avoid COUNT queries for existence and first element retrieval
**Learning:** In Django, using `.count() == 0` generates an expensive `COUNT` SQL query, evaluating the whole QuerySet when we just need to know if any record exists. Even worse is checking `.count() == 0` and then retrieving `[0]` - this is a two-query anti-pattern that can be solved by `.first()`.
**Action:** Use `QuerySet.exists()` to check for pure existence, which generates a faster `EXISTS` SQL query. When checking existence and then retrieving an item, use `QuerySet.first()` to do both in a single query.
