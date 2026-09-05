## 2024-05-18 - Avoid two-query anti-pattern in Django
**Learning:** In Django, using `.count() == 0` and then accessing the first element with `[0]` is a two-query anti-pattern.
**Action:** Use `.first()` which returns the object or `None`, executing only a single query.
