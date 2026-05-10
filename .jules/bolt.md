## 2024-05-10 - Replace .count() == 0 with .exists() and .first()
**Learning:** Using `.count() == 0` followed by array indexing (e.g., `user[0]`) executes two queries (`COUNT` and `LIMIT 1`). Using `.first()` does both an existence check and retrieval in a single query. Furthermore, `.exists()` should be used instead of `.count() == 0` for simple existence checks.
**Action:** Scan for `.count() == 0` patterns when reviewing Django ORM logic and convert them to `.first()` if the element is later accessed, or `.exists()` if only checking existence.
