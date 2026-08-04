## 2024-05-24 - Avoid len() on QuerySets
**Learning:** Found usage of `len(User.objects.filter(...))` in the codebase. This is a common Django anti-pattern that evaluates the entire QuerySet and loads all matching rows into memory just to check for existence or count rows.
**Action:** Always prefer `.exists()` when checking for existence, or `.count()` when counting. This prevents loading unneeded objects into memory and sends an optimized SQL query (`SELECT (1) AS "a"... LIMIT 1` or `SELECT COUNT(*)`).
