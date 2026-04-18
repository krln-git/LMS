## 2024-04-18 - Prevent Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `lms/djangoapps/courseware/management/commands/clean_xml.py`, which is vulnerable to command injection via malicious directory paths.
**Learning:** Even internal management commands need input sanitization or safe execution contexts (`subprocess.run`), as directory inputs could be unsanitized.
**Prevention:** Use `subprocess.run` with array-based arguments (`['diff', '-r', course_dir, export_dir]`) instead of `os.system` and string formatting for all shell commands to avoid shell injection vulnerabilities.
