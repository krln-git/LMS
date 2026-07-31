## 2024-05-24 - Optimize existence checks using .exists() and .first() instead of .count()
**Learning:** Checking existence in Django using `.count() == 0` is a severe performance anti-pattern because it forces a full `COUNT(*)` query. Combining it with indexing like `qs[0]` causes multiple database queries.
**Action:** Always replace `.count() == 0` with `.exists()` for boolean checks, and use `.first()` if the object itself is needed to reduce database queries and memory overhead.
