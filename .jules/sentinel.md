## 2024-05-18 - [Fix SQL Injection in user_api bulk opt-out]
**Vulnerability:** SQL Injection in bulk_user_org_email_optout.py via unsanitized formatting of CSV input into SQL queries using `.format()`.
**Learning:** Raw SQL execution should never use string formatting (`.format()`) with untrusted input.
**Prevention:** Always use parameterized queries (e.g., `%s` placeholders) and pass parameters as a separate list to `cursor.execute(query, params)`.
