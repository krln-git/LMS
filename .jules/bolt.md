## 2024-11-10 - Avoid .count() == 0 for database queries
**Learning:** In Django, using `.count() == 0` for pure existence checks or when immediately followed by `.first()` or index access like `[0]` evaluates the entire queryset or issues unnecessary count queries.
**Action:** Use `.exists()` for existence checks or `.first()` when the object is needed immediately to reduce database queries and improve performance.
