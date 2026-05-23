## 2024-05-31 - OS Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `lms/djangoapps/courseware/management/commands/clean_xml.py`, which is susceptible to command injection if `course_dir` or `export_dir` contain malicious characters.
**Learning:** Using string interpolation with `os.system` without shell escaping allows arbitrary command execution.
**Prevention:** Use `subprocess.run` with a list of arguments and `check=False` to avoid invoking a shell and safely pass arguments.
