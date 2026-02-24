## 2025-02-12 - [Critical] SQL Injection in Management Command
**Vulnerability:** Found a SQL injection vulnerability in `openedx/core/djangoapps/user_api/management/commands/email_opt_in_list.py`. The command was manually concatenating user-provided strings into a raw SQL query using string formatting.
**Learning:** Even management commands (admin tools) must sanitize inputs. It's easy to overlook security in "internal" tools, but they can be used as attack vectors if an attacker gains partial access (e.g., ability to trigger commands).
**Prevention:** Always use parameterized queries (`%s` placeholders in Django/MySQL) for raw SQL execution. Never use string formatting or concatenation to build SQL queries with user input.
