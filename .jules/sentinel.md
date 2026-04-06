## 2024-04-06 - SQL Injection in bulk user org email optout
**Vulnerability:** Raw string formatting was used to inject CSV data (`user_id` and `org`) directly into a bulk SQL `INSERT ... ON DUPLICATE KEY UPDATE` query in `bulk_user_org_email_optout.py`.
**Learning:** Even management commands processing internal or uploaded CSV files are vulnerable to SQL injection if input is not parameterized, and bulk operations can still use parameterized queries by generating sufficient placeholders `%s` and passing a flattened list of parameters to `cursor.execute()`.
**Prevention:** Always use parameterized SQL queries (`%s` placeholders and passing the `params` list to `cursor.execute(query, params)`) even in one-off scripts or management commands.
