## 2024-05-18 - Avoid using count() == 0 for existence checks
**Learning:** Using `.count() == 0` on a Django QuerySet generates an unnecessary database COUNT query, which can be inefficient for simple existence checks.
**Action:** Always use `.exists()` instead of `.count() == 0` when only checking if a QuerySet has any matching records.
