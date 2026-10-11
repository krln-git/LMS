## 2023-10-12 - Optimize inefficient ORM count queries
**Learning:** In Django, using `.count() == 0` followed by index access like `user[0]` causes multiple database queries. Using `.first()` instead evaluates the queryset with a single optimized query. Additionally, `.exists()` is more efficient than `.count() == 0` when checking for existence.
**Action:** Always prefer `.first()` when retrieving a single object or checking existence and returning it, and use `.exists()` for simple existence checks.
