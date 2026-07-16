## 2024-07-16 - QuerySet Evaluation Anti-Pattern
**Learning:** Calling `len()` on a Django QuerySet to check for existence evaluates the entire QuerySet and loads all matching records into memory, bypassing database-level optimizations.
**Action:** Always use `.exists()` for boolean existence checks instead of `len()` or `.count()` to ensure efficient database queries.
