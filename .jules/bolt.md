
## $(date +%Y-%m-%d) - Optimize User existence check with .exists()
**Learning:** Checking `len(QuerySet) != 0` evaluates the entire QuerySet and loads objects into memory, creating unnecessary overhead when only existence matters.
**Action:** Replace `len(QuerySet) != 0` with `QuerySet.exists()` for efficient existence checks that execute a `SELECT (1) ... LIMIT 1` database query.
