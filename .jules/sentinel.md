## 2024-05-24 - Prevent Command Injection in XML Cleaning Tool
**Vulnerability:** Found `os.system(f"diff -r {course_dir} {export_dir}")` in `clean_xml.py` which could allow command injection.
**Learning:** Using string interpolation for shell commands with `os.system` introduces command injection risks, even in management commands.
**Prevention:** Use `subprocess.run()` with a list of arguments instead of string formatting with a shell interpreter.
