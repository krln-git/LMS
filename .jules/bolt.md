## 2024-05-24 - Avoiding count() == 0
**Learning:** Using `.count() == 0` for pure existence checks or when immediately needing the first object triggers unnecessary COUNT queries, which can be inefficient on large tables.
**Action:** Always use `.exists()` for existence checks or `.first()` when the object is needed immediately to reduce database load.
