## 2024-05-29 - Command Injection in os.system
**Vulnerability:** Found `os.system` executing a bash command with unsanitized formatted string parameters (`course_dir` and `export_dir`).
**Learning:** Using `os.system` with formatted strings allows attackers to append arbitrary shell commands.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` when replacing `os.system` to prevent shell evaluation, ensuring to cast path variables to strings.
