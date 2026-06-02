## 2024-05-24 - Avoid `.count() == 0` for existence checks
**Learning:** In Django, using `.count() == 0` for an existence check triggers a `COUNT` query which is slower than checking for existence, especially for large tables. Furthermore, checking `.count() == 0` and then subsequently retrieving the first element (e.g. `user[0]`) triggers two database queries (`COUNT` and `LIMIT 1`).
**Action:** Use `.first()` when retrieving the first element and checking for existence simultaneously, and `.exists()` when simply checking for existence.
