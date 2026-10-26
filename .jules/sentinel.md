## 2024-10-26 - Command Injection via os.system
**Vulnerability:** Command injection in `clean_xml.py` due to passing interpolated strings with user input (`course_dir`, `export_dir`) to `os.system`.
**Learning:** Shell execution with `os.system` and formatted strings is highly dangerous when any path components or user inputs are involved, as it allows arbitrary command execution. `subprocess.run` with an argument list is safer because it bypasses the shell completely.
**Prevention:** Use `subprocess.run(["command", "arg1", "arg2"])` instead of `os.system`. Cast variables to strings, e.g., `str(course_dir)`, to avoid type issues when passing into `subprocess.run` arguments.
