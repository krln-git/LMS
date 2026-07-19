## 2024-07-20 - QuerySet Existence Check Optimization
**Learning:** Using `len()` on a Django QuerySet forces the database to evaluate and load all matching records into memory, which is a severe performance anti-pattern.
**Action:** Always replace `len(queryset) != 0` or `queryset.count() == 0` with `queryset.exists()` for efficient database-level boolean existence checks.
