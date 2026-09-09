## 2025-01-20 - Django QuerySet Performance Insights
**Learning:** Found two common anti-patterns: `QuerySet.count() == 0` instead of `QuerySet.exists()`, which evaluates an unnecessary COUNT query rather than a faster EXISTS query, and checking count before indexing the first item (`user[0]`), which performs two queries instead of one (`QuerySet.first()`).
**Action:** Always replace `.count() == 0` with `.exists()` for pure existence checks, and use `.first()` when existence checking precedes fetching the first matching record.
