## 2024-05-24 - Avoid len() on QuerySets
**Learning:** Calling `len()` on a Django QuerySet forces the database to evaluate and load all matching records into memory, which is a severe performance anti-pattern for existence checks.
**Action:** Always use `.exists()` (or `.first() is None` if the object is needed) for efficient boolean existence checks.
