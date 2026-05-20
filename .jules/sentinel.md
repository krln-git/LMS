## 2024-05-20 - Command Injection in XML Cleaning Script
**Vulnerability:** Found `os.system()` with formatted string passing paths directly to shell in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** Using `os.system` with f-strings or string concatenation for user-controlled or variable data opens up command injection vulnerabilities (CWE-78) when executing shell commands.
**Prevention:** Always use `subprocess.run` with a list of arguments (with `shell=False` which is default) instead of `os.system` when invoking external processes.
