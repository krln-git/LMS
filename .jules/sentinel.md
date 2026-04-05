## 2024-05-24 - Command Injection Vulnerability
**Vulnerability:** Command injection vulnerability in `lms/djangoapps/courseware/management/commands/clean_xml.py` using `os.system(f'diff -r {course_dir} {export_dir}')`.
**Learning:** String formatting with variables in shell commands can lead to command injection if variables aren't sanitized.
**Prevention:** Use `subprocess.call` or `subprocess.run` with a list of arguments instead of shell strings to avoid shell injection.
