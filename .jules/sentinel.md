## 2024-05-24 - Command Injection in clean_xml.py
**Vulnerability:** Unsanitized variables passed to `os.system` allowing command injection.
**Learning:** In `clean_xml.py`, course and export directory paths are concatenated directly into an `os.system` string to execute a diff.
**Prevention:** Use `subprocess.run` with a list of arguments to avoid shell parsing and command injection risks.
