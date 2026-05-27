## 2024-05-25 - Replace .count() == 0 with .exists() for existence checks
**Learning:** In Django, using `.count() == 0` for simple boolean existence checks executes a full SQL `COUNT(*)` query, which is significantly slower than using `.exists()` that generates a more efficient SQL `EXISTS` query and stops scanning at the first match.
**Action:** Always use `.exists()` instead of `.count() == 0` when only checking for the presence or absence of records in the database.
