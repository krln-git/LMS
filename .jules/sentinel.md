## 2026-08-03 - Command injection via os.system in management commands
**Vulnerability:** Unsanitized user input could be executed via os.system.
**Learning:** Using os.system with formatted strings (like f-strings) allows for command injection if variables contain shell metacharacters.
**Prevention:** Always use subprocess.run with arguments passed as a list, and avoid using shell=True.
