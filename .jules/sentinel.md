## 2024-05-24 - Command Injection in clean_xml Management Command
**Vulnerability:** `os.system` was used with string formatting `f"diff -r {course_dir} {export_dir}"` which allows command injection.
**Learning:** Management commands often take user input from CLI arguments which can contain shell metacharacters.
**Prevention:** Always use `subprocess.run` with a list of arguments instead of `os.system` with shell string construction.
