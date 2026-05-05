## 2024-05-05 - SQL Injection in raw query formatting
**Vulnerability:** A raw SQL query using string formatting `format()` and string concatenation (`",".join([f'"{val}"' for val in values])`) was directly passed to `cursor.execute()`, which allows SQL injection.
**Learning:** In Django management commands, raw SQL queries must dynamically construct the correct number of parameterized placeholders (`%s`) for `IN` clauses based on list length, and pass the exact values as a flattened list into the `params` argument of `cursor.execute()`. Formatting serialized string values directly into queries bypasses driver protections.
**Prevention:** Never use Python string formatting for values in SQL execution. Always use `%s` placeholders and `cursor.execute(query, params)`.
