## 2024-05-23 - Command Injection via os.system
**Vulnerability:** Command injection vulnerability in `clean_xml.py` using `os.system` with string concatenation.
**Learning:** Python `os.system` with formatted strings is dangerous and allows arbitrary command execution if an attacker controls `course_dir` or `export_dir`.
**Prevention:** Use `subprocess.run` with a list of arguments.
