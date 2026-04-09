## 2024-04-09 - Fix os.system command injection in clean_xml.py
**Vulnerability:** Found a command injection vulnerability in `lms/djangoapps/courseware/management/commands/clean_xml.py` where `os.system(f'diff -r {course_dir} {export_dir}')` is used.
**Learning:** `os.system()` with formatted strings can be exploited by an attacker providing malicious input that includes shell metacharacters like `;`, `&`, or `|`. In this case, `course_dir` and `export_dir` (which is derived from `course_dir`) are constructed using user input.
**Prevention:** Use `subprocess.call` or `subprocess.run` with a list of arguments (e.g., `['diff', '-r', course_dir, export_dir]`) to avoid shell injection vulnerabilities, as this ensures arguments are safely passed without shell interpretation.
