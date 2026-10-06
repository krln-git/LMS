## 2024-05-24 - Command Injection Risk in clean_xml.py
**Vulnerability:** `os.system(f"diff -r {course_dir} {export_dir}")` allows command injection if `course_dir` or `export_dir` contain malicious input.
**Learning:** Passing unvalidated path variables into `os.system()` with an f-string is unsafe, even in management commands.
**Prevention:** Always use `subprocess.run()` with a list of arguments and defensively cast variables using `str()` to prevent command injection and type errors.
