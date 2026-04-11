## 2024-04-11 - Prevent Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` which executes shell commands with user-controlled input (course_dir), allowing for potential OS command injection.
**Learning:** `os.system` runs strings directly in a subshell, making it vulnerable to injection if input isn't strictly controlled or sanitized. Using f-strings to format shell commands directly creates injection risks.
**Prevention:** Always use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list to ensure the shell does not evaluate arbitrary payload strings.
