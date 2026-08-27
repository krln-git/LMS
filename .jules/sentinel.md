## 2025-05-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f"diff -r {course_dir} {export_dir}")` which is susceptible to command injection if `course_dir` or `export_dir` contain shell metacharacters.
**Learning:** Using string interpolation with `os.system` in management commands can expose the system to shell injection attacks, even for internal administrative tools.
**Prevention:** Use `subprocess.run` with a list of arguments and `check=False` instead of `os.system` for shell commands.
