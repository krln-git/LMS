## 2024-07-08 - Use .exists() instead of .count() == 0 for database existence checks
**Learning:** Using `len(queryset)` or `queryset.count() == 0` forces Django to execute a `COUNT(*)` query on the database, which is inefficient when we only need to check if at least one record exists.
**Action:** Replaced `.count() == 0` with `.exists()` (or `not queryset.exists()`) for better database query performance in `cms/djangoapps/course_creators/views.py`.
