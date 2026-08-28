## 2024-05-20 - Optimizing QuerySet checks and fetch patterns
**Learning:** Avoid `.count() == 0` for pure existence checks to bypass an unnecessary COUNT SQL query in favor of an EXISTS query. In addition, when checking existence followed by a fetch like `if q.count() > 0: return q[0]`, replace this two-query anti-pattern with a single `QuerySet.first()` call.
**Action:** Use `.exists()` instead of `.count() == 0` to check for existence, and use `.first()` when retrieving the first item if it exists.
