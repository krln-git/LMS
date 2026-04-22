## 2024-04-22 - Fix SQL Injection in Bulk User Email Optout
**Vulnerability:** SQL injection vulnerability found in `openedx/core/djangoapps/user_api/management/commands/bulk_user_org_email_optout.py` where user inputs (org values) were inserted into an SQL string via `.format()` instead of using parameterized queries.
**Learning:** Using raw SQL strings with formatted inputs bypassing Django's ORM protections creates a serious SQL injection risk, particularly when handling bulk CSV operations.
**Prevention:** Always use `cursor.execute(query, params)` with parameterized inputs (`%s`) instead of string interpolation when raw SQL is necessary.
