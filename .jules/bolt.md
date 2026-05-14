## 2024-05-15 - Django ORM Optimization: Replace .count() == 0 with .first() or .exists()
**Learning:** Using `.count() == 0` followed by index access like `user[0]` triggers two separate database queries (`COUNT` and `LIMIT 1`). Using `.count() == 0` just to check existence is also slower than `.exists()`.
**Action:** Replace `.count() == 0` + `user[0]` with `.first()` to combine existence check and retrieval into a single query. Replace boolean `.count() == 0` existence checks with `.exists()`.
