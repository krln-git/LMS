## 2024-05-20 - Command Injection via `os.system`
**Vulnerability:** Found a command injection vulnerability in `lms/djangoapps/courseware/management/commands/clean_xml.py` where user-provided input (`course_dir`) was passed directly into a shell command using `os.system(f'diff -r {course_dir} {export_dir}')`.
**Learning:** This existed because Python's `os.system` executes strings in a subshell, allowing attackers to append malicious commands (e.g., `; rm -rf /`) if user input is not sanitized or parameterized.
**Prevention:** Always use the `subprocess` module (like `subprocess.call` or `subprocess.run`) and pass commands and arguments as a list rather than a single string. This bypasses the shell entirely, preventing command injection.
