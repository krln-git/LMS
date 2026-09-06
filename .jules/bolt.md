## 2024-05-18 - Avoid unnecessary COUNT queries
**Learning:** Using `.count() == 0` generates an expensive database COUNT query. When checking for existence and retrieving the first item, this becomes a two-query anti-pattern (`.count() == 0` then `[0]`).
**Action:** Replace `.count() == 0` with `.exists()` for simple existence checks. When checking existence before retrieval, replace the entire block with a single `.first()` call.
