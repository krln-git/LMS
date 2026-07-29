## 2024-07-29 - Avoid len(QuerySet) for boolean existence checks
**Learning:** Using len(QuerySet) or != 0 forces the database to evaluate and load all matching records into memory, which is a severe performance anti-pattern.
**Action:** Always use .exists() for efficient boolean existence checks.
