## 2024-05-18 - Command Injection in clean_xml
**Vulnerability:** Command injection via `os.system` using f-strings with unsanitized paths.
**Learning:** Even management commands using file paths can be vulnerable if input contains malicious characters.
**Prevention:** Always use `subprocess.run` with a list of arguments and cast paths to strings when interacting with external commands.
