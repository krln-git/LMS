## 2024-05-15 - Django QuerySet Existence Checks
**Learning:** Checking `QuerySet.count() == 0` or `len(QuerySet) == 0` forces a full COUNT(*) query or evaluates the entire QuerySet into memory, which is a performance bottleneck.
**Action:** Use `.exists()` for efficient boolean existence checks, which executes a fast `EXISTS()` query.
