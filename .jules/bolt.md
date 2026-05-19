## 2024-05-20 - Avoid N+1 Query in Boolean Checks and Retrieves
**Learning:** In Django, using `.count() == 0` for an existence check immediately followed by accessing the first element via an index (e.g., `user[0]`) is an anti-pattern that triggers two separate database queries (`COUNT` and `LIMIT 1`). Using `.count() == 0` just to check if records exist is also less efficient than `EXISTS()`.
**Action:** Replace this pattern with `.first()` to perform both the existence check and retrieval in a single query. Replace `.count() == 0` used solely for boolean existence checks with `.exists()`.
