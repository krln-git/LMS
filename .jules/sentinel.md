## 2024-05-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` which interpolates user-controlled variables directly into a shell string without sanitization, creating a command injection risk.
**Learning:** Legacy maintenance scripts sometimes rely on `os.system` for convenience when dumping output to stdout. In this codebase, even admin commands are vulnerable to injection via file path strings.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` to safely execute binaries while avoiding shell execution and directly mapping outputs. Ensure variable types (like Paths) are cast to strings inside the argument list.
