## 2024-05-16 - Optimizing QuerySet existence checks
**Learning:** Using `.count() == 0` for an existence check followed by `[0]` index access triggers two separate queries.
**Action:** Always replace `.count() == 0` + `[0]` with `.first()` to perform existence and retrieval in a single query, and replace `.count() == 0` used solely for existence checks with `.exists()`.
