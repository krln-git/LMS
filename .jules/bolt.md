## 2024-05-18 - Avoid double database hits when fetching first element
**Learning:** Checking `.count() == 0` before accessing the first element via index (`user[0]`) triggers two database queries (`COUNT` and `LIMIT 1`). Additionally, using `.count() == 0` for boolean existence checks executes a full count instead of a faster `EXISTS` query.
**Action:** Always use `.first()` to combine existence checks and retrieval into a single query, and use `.exists()` for pure boolean existence checks.
