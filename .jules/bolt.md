## 2024-06-13 - Inefficient Object Existence and Retrieval Checks
**Learning:** Found usage of `.count() == 0` for both basic existence checks and, worse, followed immediately by index access (e.g., `user[0]`). This forces database evaluation, loading data, and potentially triggering two separate database queries instead of one. This is a common performance anti-pattern.
**Action:** Replace `.count() == 0` with `.exists()` when only a boolean existence check is needed. When followed by retrieval, replace the existence check and index access with `.first()` to perform both in a single query.
