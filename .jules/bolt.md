## 2024-09-14 - Optimize Django Database Queries
**Learning:** Replacing pure existence `.count() == 0` checks with `.exists()` avoids unnecessary database COUNT queries. When checking existence and then retrieving an item, replacing the two-query anti-pattern with a single `QuerySet.first()` call is more efficient.
**Action:** Always use `.exists()` for pure existence checks and `.first()` when retrieving the first item, to reduce database load.
