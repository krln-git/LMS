## 2024-10-30 - Command Injection via os.system
**Vulnerability:** Unsanitized variables passed to os.system via f-string.
**Learning:** f-strings evaluated before os.system are vulnerable to command injection if variables contain shell metacharacters.
**Prevention:** Use subprocess.run with arguments passed as a list to avoid passing variables through the shell.
