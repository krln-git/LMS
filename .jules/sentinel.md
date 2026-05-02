## 2024-05-02 - Fix SQL Injection in backfill_history
**Vulnerability:** SQL injection vulnerability in `openedx/core/djangoapps/content/course_overviews/management/commands/backfill_history.py` where a comma-separated string of IDs was concatenated into a raw SQL `IN` clause using `.format()`.
**Learning:** Using `.format()` for serialized list inputs in raw SQL exposes the system to injection if user input reaches `ID`. Parameterized `IN` clauses must use dynamically generated `%s` placeholders.
**Prevention:** Always use parameterized queries for `IN` clauses in `cursor.execute()`, by generating `','.join(['%s'] * len(values))` and passing the array of values via the `params` argument.
