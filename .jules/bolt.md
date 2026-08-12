## 2024-05-24 - Optimize existence checks
**Learning:** Found anti-patterns checking for existence by evaluating len(QuerySet) > 0 or QuerySet.count() == 0, which unnecessarily hits the DB or loads records into memory.
**Action:** Use `.exists()` on querysets instead.
