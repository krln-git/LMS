## 2024-05-18 - Command Injection in lms/djangoapps/courseware/management/commands/clean_xml.py
**Vulnerability:** Unsanitized user input passed to `os.system()` causing potential command injection in `check_roundtrip()`.
**Learning:** Using `os.system` with string formatting or concatenation leaves the application vulnerable to command injection if input contains shell metacharacters.
**Prevention:** Use `subprocess.run` (or `subprocess.check_call`) with a list of arguments and `check=False` (to mimic `os.system`'s behavior where it doesn't strictly raise on non-zero return, unless required) to avoid shell interpolation.
