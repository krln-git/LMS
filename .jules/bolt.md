## 2024-05-24 - Replace two-query anti-pattern with QuerySet.first() or .exists()
**Learning:** In Django, using `.count() == 0` for existence checks triggers an unnecessary database COUNT query. When followed by index access (e.g., `user[0]`), it results in two separate database queries when one would suffice.
**Action:** Use `.exists()` for pure existence checks to avoid full COUNT queries. When you need both to check existence and retrieve the object, use `.first()`, which returns the first matching object or `None` in a single query.
