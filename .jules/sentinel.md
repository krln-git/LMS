## 2024-06-03 - os.system Command Injection
**Vulnerability:** Command injection risk identified where `os.system` was used with string interpolation directly from `course_dir`.
**Learning:** Legacy scripting patterns using `os.system` combined with `f-strings` or formatted strings bypass safe argument escaping, leading to command execution vulnerabilities.
**Prevention:** Always use `subprocess.run` with a list of arguments and avoid `shell=True` to safely execute external commands without relying on string manipulation. For diff-like commands, explicitly use `check=False` to handle expected non-zero exit codes.
