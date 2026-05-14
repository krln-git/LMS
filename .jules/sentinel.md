## 2024-05-14 - Fix SQL Injection in Email Opt-in List Command
**Vulnerability:** Raw SQL query construction via string formatting with serialized list input (`_sql_list`).
**Learning:** In Django raw queries with `IN` clauses, using string formatters rather than parameter passing allows SQL injection if the values are untrusted or manipulated.
**Prevention:** Dynamically generate parameterized placeholders (e.g., `','.join(['%s'] * len(values))`) and pass the actual values as a flattened list via `cursor.execute(query, params)`. Duplicate parameters appropriately if the format string placeholder appears multiple times.
