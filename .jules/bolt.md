## 2024-05-24 - Inefficient QuerySet counting
**Learning:** Using `.count() == 0` for pure existence checks or when retrieving the first object is an inefficient pattern. Using `.exists()` or `.first()` is faster.
**Action:** Always use `.exists()` when checking if any objects match a query, or `.first()` when the object itself is needed.
