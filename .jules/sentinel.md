## 2024-05-23 - Command Injection in clean_xml.py
**Vulnerability:** Found `os.system` using string interpolation with user-provided directory paths in a management command.
**Learning:** Management commands often handle file paths and can be vulnerable to command injection if input paths are not sanitized or if shell execution is used improperly.
**Prevention:** Always use `subprocess.run` with an array of arguments for OS commands rather than `os.system` with shell string interpolation.
