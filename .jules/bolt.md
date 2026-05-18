## 2024-05-18 - Avoid using `.count() == 0` for existence checks and retrieval in Django
**Learning:** In Django, using `.count() == 0` to check for existence and then accessing the first element via index (e.g., `user[0]`) triggers two separate database queries (`COUNT` and `LIMIT 1`). Additionally, using `.count() == 0` just for an existence check is less efficient than using `.exists()`.
**Action:** Always replace `.count() == 0` followed by an index access with `.first()` to perform both the existence check and retrieval in a single query. Use `.exists()` when only checking for existence.
