## 2024-11-01 - Replace .count() == 0 with .exists() and .first()
**Learning:** In Django, using `.count() == 0` evaluates the entire queryset or performs a COUNT query which is slower than `.exists()` for pure existence checks, or `.first()` when the object is needed immediately.
**Action:** Always replace `.count() == 0` with `.exists()` or `.first()` depending on context.
