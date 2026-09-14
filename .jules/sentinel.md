## 2025-03-05 - Prevent Command Injection in Management Commands
**Vulnerability:** Found `os.system` used with unsanitized inputs (`course_dir`, `export_dir`) in `clean_xml` management command.
**Learning:** Even internal management commands can be vectors for command injection if they construct shell commands using format strings.
**Prevention:** Always use `subprocess.run` with a list of arguments instead of string formatting with `os.system` or `os.popen`.
