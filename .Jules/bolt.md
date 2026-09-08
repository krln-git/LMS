## 2024-05-18 - Avoid COUNT queries for existence checks
**Learning:** Checking `.count() == 0` generates an unnecessary `COUNT` SQL query, which evaluates the entire matching set, while `.exists()` executes an `EXISTS` query that safely short-circuits.
**Action:** Always use `.exists()` or `not ...exists()` over `.count() == 0` for QuerySet pure existence checks.
