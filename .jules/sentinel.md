## 2024-05-13 - Command Injection in clean_xml.py
**Vulnerability:** Unsanitized variables passed to os.system() using f-strings.
**Learning:** f-strings in os.system() are highly vulnerable to command injection. If variables are attacker-controlled, they can append shell commands.
**Prevention:** Use subprocess.run() with a list of arguments and check=False (if exceptions on non-zero exit codes are not desired).
