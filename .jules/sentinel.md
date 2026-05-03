## 2024-05-03 - Fix SQL Injection in raw query IN clause
**Vulnerability:** SQL injection caused by using string formatting (`",".join([f'"{val}"' for val in values])`) to generate `IN` clauses for raw SQL queries (`cursor.execute()`).
**Learning:** Using `.format()` for serialized lists directly inserts them into the SQL string, bypassing database driver sanitization and allowing for SQL injection if input is not completely controlled.
**Prevention:** When writing raw SQL queries with `IN` clauses, dynamically generate placeholders (`','.join(['%s'] * len(values))`) and pass the values as a flattened list in the `params` argument to `cursor.execute()`.
