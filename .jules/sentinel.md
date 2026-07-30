## 2024-05-23 - Prevent command injection in management commands
**Vulnerability:** Use of `os.system` with string formatting (`f"diff -r {course_dir} {export_dir}"`) in `clean_xml.py` allows command injection if directory names contain shell characters.
**Learning:** Management commands that interact with the filesystem using user-supplied paths must use safe execution methods.
**Prevention:** Always use `subprocess.run` with a list of arguments instead of `os.system` with shell strings.
