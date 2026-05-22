## 2024-05-22 - Optimizing Django Existance and Retrieve Queries
**Learning:** Checking `.count() == 0` for existence, or indexing `.count() == 0` results via `[0]`, are classic Django ORM performance anti-patterns that trigger two queries instead of one (COUNT + SELECT LIMIT 1) or scan too many rows.
**Action:** Always use `.exists()` for simple existence checks, and `.first()` when retrieving the first matched item, as they are optimized at the ORM/database level to limit results quickly.
