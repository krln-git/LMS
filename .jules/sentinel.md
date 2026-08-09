## 2024-01-01 - Command injection via os.system
**Vulnerability:** Found os.system(f"diff -r {course_dir} {export_dir}") where input was not explicitly sanitized.
**Learning:** Using f-strings in os.system is vulnerable to shell injection if course_dir or export_dir originate from untrusted input.
**Prevention:** Use subprocess.run() passing a list of arguments.
