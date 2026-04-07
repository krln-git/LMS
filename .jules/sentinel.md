## 2024-05-24 - Fix SQL injection in email_opt_in_list
**Vulnerability:** Raw SQL query used string formatting directly for a list of values (`IN ( {course_id_list} )`).
**Learning:** Using `",".join(['"val"'])` to construct `IN` clauses is susceptible to SQL injection and bypasses database parameterization.
**Prevention:** Use `",".join(["%s"] * len(values))` for the query string and pass a flattened list of parameters to `cursor.execute(query, params)`.
