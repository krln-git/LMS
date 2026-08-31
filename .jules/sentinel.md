## 2024-05-24 - Command Injection in Python
**Vulnerability:** Unsafe use of `os.system` and `os.popen` allowing command injection.
**Learning:** Command injection is possible if user input is not sanitized or when shell=True is implicitly used via os functions.
**Prevention:** Use `subprocess.run` with array of arguments and `check=False`.
