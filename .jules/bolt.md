## 2024-05-10 - Django ORM Optimization: replace .count() == 0 with .exists() and .first()
**Learning:** Using `.count() == 0` followed by an index access `[0]` is a performance anti-pattern in Django that triggers two separate queries (`COUNT` and `LIMIT 1`). Additionally, using `.count() == 0` just to check for existence is slower than using `.exists()`.
**Action:** Always replace `.count() == 0` followed by `[0]` with `.first()`, which performs the existence check and retrieves the record in a single query. Always replace `.count() == 0` used solely for existence checks with `.exists()`.
