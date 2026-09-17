## 2023-10-25 - Avoid .count() == 0 and two-query anti-patterns
**Learning:** Checking for pure existence using `.count() == 0` generates an unnecessary database COUNT query instead of a more efficient EXISTS query. Additionally, using `.count() > 0` (or `== 0`) followed by indexing (e.g., `user[0]`) is a two-query anti-pattern that can be solved with a single QuerySet `.first()` call.
**Action:** Replace `QuerySet.count() == 0` with `not QuerySet.exists()` for pure existence checks. Replace `.count()` checks followed by item retrieval with `QuerySet.first()`.
