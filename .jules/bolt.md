## 2024-10-08 - Use .exists() and .first() instead of .count()
**Learning:** Inefficient use of QuerySet.count() == 0 followed by index access evaluates the entire queryset and creates unnecessary DB overhead. Instead, use .exists() for simple checks and .first() when an object needs to be accessed.
**Action:** Always prefer .exists() over .count() == 0 to reduce DB query overhead, and use .first() to safely evaluate lazily when expecting 0 or 1 result.
