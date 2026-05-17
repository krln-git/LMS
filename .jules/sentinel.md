## 2024-05-30 - Fix SQL Injection in user_api management commands
**Vulnerability:** SQL injection via string formatting (`.format()`) in `email_opt_in_list.py` and string concatenation in `bulk_user_org_email_optout.py` used in management commands.
**Learning:** Even management commands using raw queries must use proper positional parameterized queries (`cursor.execute(query, params)`). Building SQL queries by string formatting or string concatenation is an injection risk.
**Prevention:** Always use parameterized SQL placeholders (`%s`) and pass variables in the `params` tuple when using `cursor.execute()`. For lists inside an `IN` clause, use `",".join(["%s"] * len(values))` and unpack the list in the params list.
