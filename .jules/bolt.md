## 2024-08-09 - Avoid evaluating full QuerySet for existence checks
**Learning:** Evaluating the length of a QuerySet with `len()` when only checking existence forces the database to retrieve all matching rows, which is a performance bottleneck for large datasets.
**Action:** Always use `.exists()` on QuerySets instead of `len()` when you only need to know if any records match the filter.
