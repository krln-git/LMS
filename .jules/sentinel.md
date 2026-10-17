## 2024-10-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Command injection vulnerability via `os.system` with unvalidated variables.
**Learning:** f-strings used directly in `os.system` without proper sanitization can lead to arbitrary command execution if variables are malicious.
**Prevention:** Always use `subprocess.run` with a list of arguments instead of string formatting for system commands.
