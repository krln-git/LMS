## 2024-05-24 - Fix SQL injection in bulk user org email optout
**Vulnerability:** SQL injection vulnerability found in `bulk_user_org_email_optout.py` due to string formatting used to construct bulk raw SQL INSERT queries with user-provided CSV data.
**Learning:** Even internal management commands parsing simple CSVs must use parameterized queries when dropping down to raw SQL, as malicious data in the CSV can lead to command injection. String `.format()` should never be used to construct SQL query values.
**Prevention:** Use placeholder syntax (`%s`) and pass variables securely as a flattened parameter list in `cursor.execute(query, params)`.
