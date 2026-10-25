## 2024-10-25 - Command Injection via os.system in clean_xml.py
**Vulnerability:** Found `os.system` being used with f-strings to construct shell commands (`os.system(f"diff -r {course_dir} {export_dir}")`).
**Learning:** While these arguments might not directly originate from user input in all contexts, passing dynamically constructed strings to `os.system` is a critical command injection risk, as it runs via the shell.
**Prevention:** Always use `subprocess.run` or `subprocess.Popen` with a list of arguments instead of a single formatted string, and avoid using `shell=True`.
