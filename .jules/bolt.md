## 2024-06-03 - Replace .count() == 0 with .exists() and .first()
**Learning:** Using `.count() == 0` followed by array indexing (e.g. `[0]`) triggers two database queries (`COUNT` and `LIMIT 1`). Also, checking existence with `.count() == 0` evaluates the entire result set size.
**Action:** Use `.first()` to replace the count check and retrieval with a single query, and use `.exists()` when simply checking for existence.
