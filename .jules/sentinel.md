## 2024-03-26 - Prevent Command Injection via Subprocess
**Vulnerability:** Use of `os.system(f'diff -r {course_dir} {export_dir}')` in `check_roundtrip` which executes a formatted string in the shell, causing command injection vulnerabilities.
**Learning:** `os.system` runs commands via shell interpolation which is fundamentally unsafe. Python's `subprocess` module avoids this by accepting arguments as a list.
**Prevention:** Always use `subprocess.call` or `subprocess.run` with a list of arguments instead of a single formatted string for executing shell commands.
