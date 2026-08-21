## 2024-05-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system` using string concatenation/f-strings with variables.
**Learning:** Command injection is possible if variables are unsanitized.
**Prevention:** Use `subprocess.run` with a list of arguments instead.
