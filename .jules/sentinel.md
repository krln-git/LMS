## 2024-05-24 - SQL Injection Risk with Raw IN Clauses
**Vulnerability:** Raw SQL queries used `.format()` or `.join()` to inject list contents directly into the query string for `IN` clauses or `INSERT` values, causing SQL injection risks.
**Learning:** Python string formatting and joining does not properly escape SQL inputs, even if they look like strings, making them highly susceptible to SQL injection.
**Prevention:** Always use dynamically generated parameterized placeholders (e.g., `','.join(['%s'] * len(values))`) and pass the flattened list of variables to `cursor.execute(query, params)`.
