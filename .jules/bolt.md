## 2024-05-23 - Avoid full QuerySet evaluation
**Learning:** Checking for empty QuerySets using `.count() == 0` performs an expensive `SELECT COUNT(*)` query, while `.exists()` is more efficient and only checks for a single match.
**Action:** Use `.exists()` instead of `.count() == 0` when just checking for existence to avoid unnecessary database processing time.
