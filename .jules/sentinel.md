## 2024-09-18 - Command Injection in Script
**Vulnerability:** Dynamic shell execution using os.system with unvalidated input (e.g., f-strings).
**Learning:** f-strings passed directly to os.system lead to arbitrary command execution if input can be manipulated.
**Prevention:** Use subprocess.run with shlex.split to ensure arguments are safely passed and not evaluated as shell commands.
