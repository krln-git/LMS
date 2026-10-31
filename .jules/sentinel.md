## 2024-05-24 - Command Injection in clean_xml.py
**Vulnerability:** os.system was used with string formatting, allowing arbitrary command execution if course_dir or export_dir contained malicious inputs.
**Learning:** In Python, string formatting should not be passed to os.system. The path variables were `path` instances and not validated.
**Prevention:** Use `subprocess.run` with a list of arguments, and ensure path variables are cast to string with `str()` to prevent type-related errors when calling `subprocess`.
