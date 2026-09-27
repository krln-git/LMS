## 2024-05-24 - Command Injection via os.system
**Vulnerability:** Unsanitized user inputs (paths) used in `os.system` string interpolation.
**Learning:** Even local management commands can be vulnerable to command injection if variables containing spaces or special characters are directly formatted into shell commands.
**Prevention:** Always use `subprocess.run` with a list of arguments instead of string interpolation for shell commands.
