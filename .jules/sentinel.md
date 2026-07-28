## 2024-05-18 - Command Injection in clean_xml.py
**Vulnerability:** Command injection vulnerability in `clean_xml.py` using `os.system(f'diff -r {course_dir} {export_dir}')`.
**Learning:** Shell commands constructed with `os.system` and formatted strings allow command injection if variables contain shell metacharacters.
**Prevention:** Always use `subprocess.run` with a list of arguments (avoiding `shell=True`) to execute external commands safely without invoking a shell.
