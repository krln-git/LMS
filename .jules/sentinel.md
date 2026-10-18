## 2024-05-24 - Fix command injection in clean_xml
**Vulnerability:** Command injection in `os.system` using `f-string` and variables.
**Learning:** `os.system` with string formatting allows executing arbitrary commands if path variables contain shell metacharacters. Even `path` objects need safe handling.
**Prevention:** Use `subprocess.run` with a list of arguments and `str()` casting for path objects instead of string concatenation/formatting.
