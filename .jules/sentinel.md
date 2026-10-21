## 2024-05-24 - Command Injection in clean_xml
**Vulnerability:** Use of os.system with unescaped string formatting for diff command.
**Learning:** Unsanitized user inputs in os.system can lead to command injection.
**Prevention:** Use subprocess.run with arguments passed as a list.
