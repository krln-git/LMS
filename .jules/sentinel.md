## 2024-08-11 - Prevent Command Injection in XML Cleaning Tool
**Vulnerability:** Command injection in `clean_xml.py` via `os.system` with f-strings using user-provided paths.
**Learning:** Legacy scripts often use `os.system` for convenience but fail to properly sanitize inputs which could be paths containing shell metacharacters.
**Prevention:** Use `subprocess.run` with a list of arguments and cast variables to strings to ensure safe execution without a shell.
