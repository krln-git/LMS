## 2024-11-06 - Command Injection via os.system
**Vulnerability:** Unsanitized user input (`course_dir`, `export_dir`) in `os.system(f"diff -r {course_dir} {export_dir}")` allowed arbitrary command execution.
**Learning:** Management commands frequently use string interpolation with shell commands, bypassing safe arguments passing.
**Prevention:** Always use `subprocess.run` with an argument list, and explicitly cast path variables to strings.
