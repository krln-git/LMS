## 2024-05-18 - Fix SQL injection vulnerabilities in Django raw cursors
**Vulnerability:** Raw SQL queries executed via `cursor.execute()` were using unsafe string concatenation and `.format()` with user-controllable arrays directly interpolated into the SQL string instead of query parameters.
**Learning:** `cursor.execute()` with an `IN` clause over an array or multiple dynamic rows for `INSERT` needs manual expansion using correctly sized parameters placeholders array `.join(['%s'] * len(data))` passed to the database connector.
**Prevention:** Never use Python string formatting like `f""`, `.format()`, or string concatenation directly in SQL queries; always use query parameters with `execute(query, params)`.
