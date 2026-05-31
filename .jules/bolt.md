## 2024-05-14 - Optimizing Django Exists Checks
**Learning:** Using `.count() == 0` followed by array indexing (e.g., `user[0]`) forces Django to execute a `SELECT COUNT(*)` query and then a separate `SELECT ... LIMIT 1` query. Using `.count() == 0` for simple boolean existence checks forces a full table scan instead of an early return.
**Action:** Always replace `.count() == 0` followed by array indexing with `.first()`. Replace `.count() == 0` used purely for boolean conditions with `.exists()`.
