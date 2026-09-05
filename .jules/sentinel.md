## 2024-05-18 - Fix Command Injection in clean_xml.py
**Vulnerability:** Unsanitized variables `course_dir` and `export_dir` passed into `os.system` string interpolation.
**Learning:** This causes command injection vulnerabilities as the variable can contain spaces or command separators.
**Prevention:** Use `subprocess.run` with a list of arguments rather than shell string interpolation.
