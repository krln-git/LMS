## 2024-05-24 - Command Injection Risks in Test Scripts and Management Commands
**Vulnerability:** Use of `os.system` and `os.popen` with string interpolation in management commands and scripts
**Learning:** Even in internal tools or management commands, using shell execution with string interpolation creates a command injection risk.
**Prevention:** Always use `subprocess.run` with a list of arguments or parsed with `shlex.split` instead of shell execution like `os.system` or `os.popen`.
