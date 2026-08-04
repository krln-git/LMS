## 2024-05-24 - Avoid evaluating QuerySets in memory for existence checks
**Learning:** Found an anti-pattern where len(QuerySet) != 0 was used, which evaluates the entire query into memory instead of using an efficient EXISTS query.
**Action:** Always use .exists() for QuerySet existence checks.
