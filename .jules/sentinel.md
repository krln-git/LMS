## 2024-05-24 - Fix Command Injection in clean_xml
**Vulnerability:** Found a command injection vulnerability in `lms/djangoapps/courseware/management/commands/clean_xml.py` where `os.system` was used with a formatted string `f'diff -r {course_dir} {export_dir}'`. User-provided course or export directories could execute arbitrary shell commands.
**Learning:** String formatting in shell commands creates command injection risks. Even in management commands, paths should be treated as untrusted data if they originate externally.
**Prevention:** Use `subprocess.call` or `subprocess.run` with a list of arguments (e.g., `['diff', '-r', course_dir, export_dir]`) instead of a single string and `shell=True` (or `os.system`).
