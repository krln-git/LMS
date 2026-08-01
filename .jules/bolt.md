## 2024-05-18 - Avoid len() on Django QuerySets
**Learning:** Using `len()` on an unresolved Django QuerySet (e.g., `len(User.objects.filter(...))`) forces the database to evaluate the query and load all matching records into memory, which can cause severe performance degradation for large datasets.
**Action:** Always use the `.exists()` method for efficient boolean existence checks on QuerySets to avoid unnecessary data loading.
