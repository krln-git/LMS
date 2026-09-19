## 2024-05-24 - Django QuerySet Performance: `.count()` vs `.exists()` and `.first()`
**Learning:** In Django, using `.count() == 0` generates an unnecessary database COUNT query when checking existence. Using `.count()` followed by an index access (e.g., `q[0]`) is a two-query anti-pattern. `.exists()` and `.first()` are much more efficient.
**Action:** Always use `.exists()` for pure existence checks and `.first()` when retrieving the first item. Avoid `.count()` unless the actual number of items is needed.
