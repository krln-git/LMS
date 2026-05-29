## 2024-05-23 - Optimize Django QuerySets: replace .count() == 0
**Learning:** Using `.count() == 0` for existence checks triggers an expensive `COUNT` database query. When used before accessing the first element via an index (e.g., `user[0]`), it triggers two separate queries (`COUNT` and `LIMIT 1`).
**Action:** Replace `.count() == 0` followed by index access with `.first()` to perform both operations in a single query, and replace `.count() == 0` used purely for boolean checks with `.exists()`.
