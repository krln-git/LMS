## 2024-11-01 - Command Injection via os.system and f-strings
**Vulnerability:** Found `os.system` executing shell commands with interpolated user-controlled path variables (e.g., `os.system(f"diff -r {course_dir} {export_dir}")`).
**Learning:** Passing user-controllable arguments directly to `os.system` via string interpolation introduces a critical command injection vulnerability if paths contain malicious shell characters or spaces.
**Prevention:** Always use `subprocess.run` with a list of arguments (e.g., `["diff", "-r", str(course_dir), str(export_dir)]`) to ensure arguments are escaped and executed directly without an intermediate shell.
