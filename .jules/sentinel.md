## 2024-06-25 - Prevent command injection in management commands
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `lms/djangoapps/courseware/management/commands/clean_xml.py`, which is vulnerable to command injection if `course_dir` or `export_dir` contain malicious shell characters.
**Learning:** Legacy management scripts often use `os.system` for convenience without considering the security implications of unsanitized paths, even if they are internal tools.
**Prevention:** Always use `subprocess.run` with a list of arguments (and `shell=False` implicitly) instead of `os.system` or `subprocess.Popen(..., shell=True)` to safely pass parameters to system commands without shell interpolation.
