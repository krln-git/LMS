## 2024-05-15 - SQL Injection in Management Commands
**Vulnerability:** SQL Injection in `email_opt_in_list` and `bulk_user_org_email_optout` via raw string concatenation (`.format()`) for `IN` clauses and `VALUES` in `cursor.execute()`.
**Learning:** Using `.format()` with lists of strings or values directly into SQL strings allows for SQL Injection, especially when values come from potentially untrusted sources or file inputs.
**Prevention:** Always use parameterized queries (`%s` placeholders) and pass the values as a flattened list to the `params` argument of `cursor.execute()`.
