## 2024-05-24 - Django QuerySet Evaluation Inefficiency
**Learning:** In Django, using `.count() == 0` is less efficient than `.exists()` or `.first()` because it evaluates the entire query count when you only need to know existence or fetch the first item.
**Action:** Always replace `.count() == 0` with `.exists()` for pure existence checks, or with `.first()` when the object is needed immediately, to reduce database queries. Rename shadowed variables when refactoring queries to improve readability.
