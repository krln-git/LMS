## 2024-05-25 - Command Injection in clean_xml Management Command
**Vulnerability:** Command injection via `os.system` and f-strings in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** Using `os.system` with formatted strings containing user-provided file paths allows arbitrary command execution.
**Prevention:** Use `subprocess.run` with a list of arguments and `check=False` to safely execute commands without a shell.
