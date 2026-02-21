# Sentinel Journal

## 2025-02-09 - SQL Injection in Management Command Utility
**Vulnerability:** The `delete_rows` utility function in `openedx/core/djangoapps/util/row_delete.py` constructed raw SQL queries using string formatting with `table_name` and `primary_id_name` arguments. While intended for internal use, it lacked validation, making it vulnerable to SQL injection if these arguments ever came from untrusted sources.
**Learning:** Even internal utility functions should validate inputs when constructing raw SQL, as they might be reused in unexpected contexts. Django's `raw()` method does not automatically protect against injection in the query string itself, only in parameters.
**Prevention:** Always validate or whitelist table and column names when dynamic SQL construction is necessary. Use `re.match` with a strict allowlist (e.g., `^[a-zA-Z0-9_]+$`) to ensure only valid identifiers are used.
