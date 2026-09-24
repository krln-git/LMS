## 2024-05-15 - Django QuerySet optimization anti-patterns
**Learning:** Found multiple instances where `.count() == 0` and `.count() > 0` are used for existence checks, and sometimes followed by an index access (e.g., `q[0]`), resulting in unnecessary and inefficient queries.
**Action:** Use `.exists()` for pure existence checks and `.first()` when checking existence and immediately retrieving the first item.
