## 2024-10-29 - Command Injection in clean_xml.py
**Vulnerability:** Unsanitized user inputs (course_dir and export_dir) were passed to os.system via an f-string in lms/djangoapps/courseware/management/commands/clean_xml.py.
**Learning:** Command injection can easily occur when passing f-strings containing variables to os.system, as it executes them through a shell.
**Prevention:** Use subprocess.run with an argument list (e.g., ["cmd", str(arg)]) instead of os.system to safely pass arguments without shell interpretation.
