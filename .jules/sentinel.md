## 2024-05-24 - Command Injection in clean_xml.py
**Vulnerability:** Unsanitized user input passed to os.system() in check_roundtrip().
**Learning:** f-strings combined with os.system() create command injection vulnerabilities when paths are not sanitized.
**Prevention:** Use subprocess.run() with arguments passed as a list and do not rely on shell=True.
