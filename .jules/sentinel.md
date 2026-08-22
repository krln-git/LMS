## 2024-05-19 - Command Injection in clean_xml
**Vulnerability:** Found `os.system` using an interpolated string `f'diff -r {course_dir} {export_dir}'` in `clean_xml.py`
**Learning:** Hardcoded commands using formatted strings are prone to command injection, especially in management commands.
**Prevention:** Always use `subprocess.run` with a list of arguments for system calls.
