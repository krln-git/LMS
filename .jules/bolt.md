## 2024-05-24 - Avoid len() and count() == 0 on QuerySets
**Learning:** Evaluating length or counting for simple existence checks evaluates the whole QuerySet or issues an expensive COUNT. Use .exists() instead.
**Action:** Always use .exists() when checking if a QuerySet has any elements to prevent performance bottlenecks.
