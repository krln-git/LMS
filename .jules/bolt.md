## 2024-05-24 - Optimize QuerySet existence check
**Learning:** In Django, using `len(QuerySet) != 0` evaluates the entire QuerySet and fetches all matching rows from the database.
**Action:** Use `QuerySet.exists()` for a simple existence check to execute a much faster `SELECT (1) AS a` query, minimizing database load.
