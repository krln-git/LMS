## 2026-03-10 - Optimize database existence checks
**Learning:** Checking for row existence using `len(QuerySet)` fetches all rows into memory, and `QuerySet.count()` might execute a `COUNT(*)` across multiple rows depending on the query, both of which are inefficient. Calling `QuerySet.exists()` executes a more optimal SQL query (`SELECT (1) ... LIMIT 1`) that terminates early once a matching row is found, resulting in better performance for simple boolean checks.
**Action:** Use `.exists()` over `len()` or `.count()` when only checking if a QuerySet is empty or not in Django codebases.
