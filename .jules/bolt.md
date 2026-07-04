## 2024-05-23 - [Django QuerySet Evaluation Anti-Pattern]
**Learning:** Found multiple instances where `len(QuerySet) != 0` and `QuerySet.count() == 0` were used for boolean existence checks. These execute a full data retrieval or a `COUNT(*)` query respectively, which is highly inefficient on large tables.
**Action:** Always use `.exists()` for existence checks or `.first()` if an object is needed immediately after to avoid unnecessary database load and memory usage.
