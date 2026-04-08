## 2024-05-23 - Command Injection via os.system
**Vulnerability:** Command injection vulnerability in `lms/djangoapps/courseware/management/commands/clean_xml.py` where `os.system()` was used with formatted strings containing user-provided directory paths.
**Learning:** Developers sometimes use `os.system` for quick shell commands like `diff`, inadvertently allowing shell metacharacters in paths to execute arbitrary commands.
**Prevention:** Always use the `subprocess` module (e.g., `subprocess.call` or `subprocess.run`) and pass arguments as a list of strings rather than a single formatted string to bypass the shell.
