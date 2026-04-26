## 2024-04-26 - [Fix SQL Injection in bulk_user_org_email_optout]
**Vulnerability:** SQL Injection in raw database queries inside a management command where user input from CSVs was directly formatted into strings without parameterization.
**Learning:** Even management commands run by admins can be vulnerable if they construct raw SQL strings via `.format()` on unstructured/unvalidated inputs. Django's `.execute()` expects a param list for `IN` and `VALUES` arrays.
**Prevention:** Always dynamically generate placeholders (e.g. `%s`) and pass the values as a flattened list in the `params` argument to `cursor.execute(query, params)`.
