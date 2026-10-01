## 2024-05-24 - Avoid len() on QuerySets
**Learning:** Calling `len()` on a Django QuerySet forces evaluation and loads all rows into memory, causing severe performance degradation for large datasets. This is a common anti-pattern found in older views.
**Action:** Always use `.exists()` when checking for the existence of records instead of `len()` or `.count() == 0`.
