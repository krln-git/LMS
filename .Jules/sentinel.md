## 2026-09-07 - Command Injection in Management Command
**Vulnerability:** Command injection via os.system(f'diff -r {course_dir} {export_dir}')
**Learning:** Management commands often use shell operations for convenience, which can be vulnerable if inputs aren't sanitized.
**Prevention:** Always use subprocess.run with an argument list instead of string formatting with os.system.
