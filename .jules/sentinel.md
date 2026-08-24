## 2024-05-18 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` which allows command injection if `course_dir` contains special shell characters.
**Learning:** Legacy management commands sometimes use `os.system` with f-strings for quick shell execution without considering input sanitization or safer alternatives like `subprocess.run`.
**Prevention:** Use `subprocess.run` with a list of arguments and `check=False` (to preserve behavior if non-zero exit codes are expected but shouldn't crash the script) instead of `os.system` when invoking shell tools.
