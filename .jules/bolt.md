## 2024-05-18 - Avoid COUNT() and LIMIT 1 queries
**Learning:** Checking `.count() == 0` and then accessing `[0]` on a Django QuerySet executes two separate queries (`COUNT()` and `LIMIT 1`). Using `.first()` executes both the existence check and retrieval in a single query. Using `.count() == 0` for boolean existence checks executes `COUNT()` which is slower than `.exists()`.
**Action:** Use `.first()` instead of `.count() == 0` when you need the first object if it exists. Use `.exists()` instead of `.count() == 0` for boolean existence checks.
