## 2024-05-21 - Replace .count() == 0 with .exists() and .first()
**Learning:** Using `.count() == 0` for an existence check immediately followed by accessing the first element via an index (e.g., `user[0]`) is an anti-pattern that triggers two separate database queries (`COUNT` and `LIMIT 1`). Additionally, using `.count() == 0` solely for boolean existence checks adds overhead.
**Action:** Use `.first()` to perform both the existence check and retrieval in a single query, and replace `.count() == 0` used solely for boolean checks with `.exists()`.
