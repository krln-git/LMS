## 2024-05-16 - Prevent in-memory evaluation of QuerySets
**Learning:** Using `len()` on a Django QuerySet forces the database to evaluate and load all matching records into memory, which is a severe performance anti-pattern. `.count()` executes a full `COUNT(*)` query which is better but still inefficient for simple boolean checks.
**Action:** Always replace `len()` or `.count() == 0` with the `.exists()` method (or `.first() is None` if the object is needed) for efficient boolean existence checks.
