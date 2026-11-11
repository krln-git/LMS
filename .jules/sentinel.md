## 2024-05-24 - Command Injection Risk in Django Management Commands
**Vulnerability:** Found `os.system()` being used with unsanitized string formatting (`f'diff -r {course_dir} {export_dir}'`) in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** Management commands often handle user-provided paths (like `course_dir`). Using `os.system` or `subprocess.call(..., shell=True)` with these paths creates a high risk of command injection if the directory name contains shell metacharacters.
**Prevention:** Always use `subprocess.run()` with a list of arguments (e.g., `['diff', '-r', course_dir, export_dir]`) and avoid `shell=True` to ensure arguments are passed directly to the executable, bypassing the shell's interpretation.
