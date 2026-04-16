## 2024-05-18 - Fix os.system command injection
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `lms/djangoapps/courseware/management/commands/clean_xml.py` which was vulnerable to command injection if `course_dir` or `export_dir` contained shell metacharacters.
**Learning:** Shell commands should not be executed via `os.system` using unvalidated parameters, as string formatting allows for arbitrary code execution.
**Prevention:** Use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list rather than a single formatted string.
