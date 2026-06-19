## 2024-06-20 - Severe QuerySet evaluation overhead with len()
**Learning:** Using `len()` on unresolved Django QuerySets (e.g., `len(User.objects.filter(...)) != 0`) forces the entire result set to be loaded into application memory from the database, which is a massive performance bottleneck when only a boolean existence check is needed.
**Action:** Always replace `len(QuerySet) != 0` with `QuerySet.exists()` to ensure the database only executes an optimized `SELECT 1` query without loading model instances into memory.
