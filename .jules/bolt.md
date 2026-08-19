## 2026-08-19 - Optimize existence checks and QuerySet evaluation
**Learning:** Django's `.count()` generates a `COUNT` SQL query. When checking existence and subsequently accessing the first item, using `.count() == 0` followed by index access `[0]` causes unnecessary database queries. It's better to use `.first()` for a single evaluation, or `.exists()` if only existence checking is needed.
**Action:** Use `.first()` when checking existence and accessing the item, and `.exists()` instead of `.count() == 0` for pure existence checks.
