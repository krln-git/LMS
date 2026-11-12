## 2024-05-24 - Command Injection via os.system
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `lms/djangoapps/courseware/management/commands/clean_xml.py` which allows command injection if `course_dir` or `export_dir` contains shell metacharacters.
**Learning:** Using `os.system` with f-strings or string concatenation is inherently unsafe for executing shell commands with variable arguments.
**Prevention:** Always use `subprocess.run` with a list of arguments to ensure safe execution without a shell interpreting metacharacters.
