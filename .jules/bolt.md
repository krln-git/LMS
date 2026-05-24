## 2025-02-28 - Optimizing count() == 0 existence checks
**Learning:** Using `.count() == 0` for boolean existence checks or when followed by fetching the first element (e.g., `user[0]`) triggers multiple database queries (`COUNT` and `LIMIT 1`).
**Action:** Replace `.count() == 0` checks with `.first()` when retrieving the item, and `.exists()` when purely checking for existence to combine operations into a single query and improve performance.
