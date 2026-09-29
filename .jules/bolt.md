## 2024-05-24 - Unnecessary count and two-query anti-pattern
**Learning:** Checking `.count() == 0` when checking existence executes an unnecessary DB count query, and doing so prior to accessing `user[0]` causes two DB round trips.
**Action:** Always use `.exists()` for existence checks and `.first()` when retrieving a single element to minimize DB queries.
