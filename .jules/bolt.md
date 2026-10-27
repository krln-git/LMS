## 2024-05-18 - Replacing .count() == 0 in Django
**Learning:** Using `.count() == 0` evaluates a `COUNT` query at the database level which is slower. Using `.first()` or `.exists()` is much faster.
**Action:** Always prefer `.exists()` for existence checks, and `.first()` when the object is needed.
