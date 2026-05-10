## 2024-05-10 - Refactoring raw SQL formatting
**Vulnerability:** SQL injection via string formatting (`.format()`) in raw SQL queries, specifically involving IN clauses and INSERT statements in management commands.
**Learning:** Using string formatting for SQL variables causes SQL injection. Named string variables also require positional parameterized placeholders `%s`, which must be duplicated in the params list for every occurrence in the query.
**Prevention:** Always dynamically generate placeholders (e.g., `','.join(['%s'] * len(values))`) and pass variables as a flattened list via the execution `params` list, instead of using `.format()`.
