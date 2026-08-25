## 2024-05-02 - Optimize Database Queries
**Learning:** In Django, using `.count() == 0` generates an inefficient `COUNT` query, and using it for checking existence and then indexing (like `q[0]`) results in two queries. Replacing them with `.exists()` and `.first()` improves database query performance.
**Action:** Always prefer `.exists()` for checking existence and `.first()` when retrieving the first item from a queryset.
