## 2024-05-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Use of `os.system()` with unsanitized arguments allows command injection.
**Learning:** `os.system(f"diff -r {course_dir} {export_dir}")` allows command injection if `course_dir` contains special characters.
**Prevention:** Use `subprocess.run()` with a list of arguments and convert arguments to strings.
