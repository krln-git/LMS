## 2024-05-20 - Optimize QuerySet evaluation
**Learning:** In Django, using `.count() == 0` triggers an unnecessary `COUNT` SQL query. If followed by indexing (e.g. `user[0]`), it creates a two-query anti-pattern. `.exists()` and `.first()` evaluate more efficiently at the database level.
**Action:** Replace pure existence checks with `.exists()` and two-query existence+retrieval anti-patterns with `.first()`.
