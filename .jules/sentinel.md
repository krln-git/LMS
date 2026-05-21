## 2024-05-24 - Command Injection via os.system
**Vulnerability:** Command injection vulnerability in `lms/djangoapps/courseware/management/commands/clean_xml.py` using `os.system` with f-strings.
**Learning:** `os.system` executes commands via a shell and should not be used with dynamic variables.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` when replacing `os.system` calls expecting non-zero exits, instead of passing a shell string.
