## 2024-05-24 - Avoid `.count() == 0` for querysets
**Learning:** In Django, using `.count() == 0` on a queryset is inefficient as it triggers a `COUNT(*)` query. For existence checks, `.exists()` is faster. If the first object is needed immediately, `.first()` avoids fetching all results and acts as an existence check.
**Action:** Always replace `.count() == 0` with `.exists()` for pure existence checks, or with `.first()` when the object is needed immediately, to reduce database queries.
