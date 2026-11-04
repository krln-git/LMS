## 2024-11-04 - Replacing inefficient QuerySet.count() == 0 checks with .first() and .exists()
**Learning:** In Django, evaluating `.count() == 0` is less efficient than using `.exists()` for existence checks or `.first()` when the first object might be needed immediately, as the latter can reduce database queries and prevent evaluating entire querysets in memory.
**Action:** Always prefer `.exists()` to check if a QuerySet is empty, or `.first()` if an object from the QuerySet is subsequently needed, avoiding `.count() == 0`.
