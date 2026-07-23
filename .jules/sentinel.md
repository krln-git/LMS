## 2024-07-23 - Command Injection in clean_xml.py
**Vulnerability:** Command injection via os.system using string formatting with user-provided arguments in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** `os.system` with shell interpolation leaves scripts open to OS command execution if inputs contain shell metacharacters. Even in admin scripts, this is an unsafe pattern, particularly when dealing with paths that might include spaces or special characters.
**Prevention:** Always use the `subprocess` module with argument arrays (e.g., `subprocess.run(["diff", "-r", course_dir, export_dir], check=False)`) instead of string interpolation with `os.system`.
