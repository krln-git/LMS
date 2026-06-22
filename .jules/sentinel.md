## 2024-06-22 - Command Injection in clean_xml.py
**Vulnerability:** Found an OS command injection vulnerability via `os.system` using unsanitized `course_dir` in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** Legacy scripts sometimes use `os.system` for convenience (e.g. running `diff`) without realizing user input could be injected into the shell command execution.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` when expecting standard behavior without throwing exceptions on non-zero exit codes.
