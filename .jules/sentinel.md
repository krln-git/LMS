## 2024-05-15 - Fix Command Injection in Management Command
**Vulnerability:** Command injection risk via os.system with user-provided path variables.
**Learning:** Management commands often handle file paths using os.system, which is vulnerable if paths contain shell metacharacters.
**Prevention:** Always use subprocess.run with a list of arguments and cast path-like objects to strings.
