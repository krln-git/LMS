## 2025-01-24 - Command Injection in Python Scripts via `os.system`
**Vulnerability:** A script in `lms/djangoapps/courseware/management/commands/clean_xml.py` was using `os.system` with string formatting, allowing arbitrary command execution if the path arguments contained shell metacharacters.
**Learning:** When executing shell commands like `diff` that legitimately return non-zero exit codes to indicate standard outcomes (e.g., differences found), the correct secure alternative to `os.system` is `subprocess.run([args], check=False)` to avoid throwing `CalledProcessError` exceptions.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` (when exit codes are expected) to bypass the shell securely and safely evaluate dynamic path variables.
