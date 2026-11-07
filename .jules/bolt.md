## 2024-05-24 - Avoid .count() == 0 for querysets
**Learning:** Checking existence with `.count() == 0` triggers a potentially expensive COUNT query. If the first element is also fetched immediately after (e.g., `user[0]`), this triggers two queries.
**Action:** Use `.exists()` for pure existence checks, or `.first()` when retrieving the object and avoiding index access, to minimize DB queries.
