## 2024-05-24 - Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `clean_xml.py`.
**Learning:** Management commands can be a source of command injection if they pass unsanitized input to shell commands using `os.system`.
**Prevention:** Use `subprocess.run` with an argument list instead of string formatting with `os.system` for executing shell commands.
