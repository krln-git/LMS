## 2024-05-15 - Command Injection in XML Export Tool
**Vulnerability:** Unsanitized variables in `os.system` call.
**Learning:** String interpolation with `os.system` creates a command injection risk when handling directory paths.
**Prevention:** Use `subprocess.run` with an array of arguments and strictly avoid `os.system` for dynamic commands.
