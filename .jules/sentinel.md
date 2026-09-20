## 2024-05-14 - Fix command injection in clean_xml.py
**Vulnerability:** Command injection via os.system and shell string interpolation in clean_xml.py
**Learning:** f-strings should not be used with os.system when variables can be controlled
**Prevention:** Use subprocess.run with arguments as a list to avoid shell interpolation
