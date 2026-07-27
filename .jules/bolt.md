## 2024-07-27 - Django QuerySet Existence Checks
**Learning:** Using `len(QuerySet)` on an unresolved QuerySet forces the database to evaluate and load all matching records into memory. This is a severe performance anti-pattern in Django when only checking for existence.
**Action:** Always use the `.exists()` method (e.g., `QuerySet.exists()`) instead of `len()` or `.count() == 0` for efficient boolean existence checks.
