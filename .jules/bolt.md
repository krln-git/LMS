## 2024-11-04 - Avoid `.count() == 0` for query existence checks
**Learning:** In Django, using `.count() == 0` is inefficient because it performs a full `COUNT(*)` query, and checking its index `user[0]` afterwards triggers another query. Using `.first()` gets the object with `LIMIT 1` efficiently.
**Action:** Always replace `.count() == 0` with `.first()` if we need the object, or `.exists()` if we just need to check for existence, to save database queries.
