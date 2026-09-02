## 2024-05-24 - Prevent Command Injection in `clean_xml.py`
**Vulnerability:** Unsanitized variables `course_dir` and `export_dir` passed to `os.system` via string formatting.
**Learning:** Command injection is possible when using `os.system` with dynamically generated strings.
**Prevention:** Replace `os.system` with `subprocess.run`, passing the command and arguments as a list. Ensure arguments are cast to string to avoid TypeErrors.
