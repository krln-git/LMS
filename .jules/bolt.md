## 2026-10-03 - Avoid two-query anti-patterns in Django
**Learning:** The anti-pattern of using `.count() == 0` followed by an index access like `user[0]` causes a full COUNT database query followed by a separate SELECT query. Using `.first()` performs a single SELECT query with LIMIT 1.
**Action:** Always replace `filter().count() == 0` + index fetching with `filter().first()`.
