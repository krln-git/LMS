## 2023-10-25 - Fix command injection in clean_xml.py
**Vulnerability:** Command injection via os.system and f-strings.
**Learning:** f-strings used with os.system can lead to command injection if variables are untrusted.
**Prevention:** Use subprocess.run with a list of arguments instead.
