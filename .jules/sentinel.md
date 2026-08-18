## 2024-08-18 - Prevent Command Injection with subprocess.run
**Vulnerability:** Found `os.system` using un-sanitized string variables for arguments, creating a command injection risk.
**Learning:** Legacy scripts sometimes resort to `os.system(f"...")` out of convenience.
**Prevention:** Always use `subprocess.run` with lists of arguments for running shell commands.
