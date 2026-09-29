## 2024-05-24 - Command Injection via os.system
**Vulnerability:** Command Injection vulnerability due to the use of `os.system` with f-strings and variable inputs like paths.
**Learning:** f-strings should not be passed to shell execution paths.
**Prevention:** Use `subprocess.run` with list arguments instead of `os.system` to prevent shell injection.
