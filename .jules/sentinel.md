## 2024-05-14 - Fix command injection vulnerability in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` which interpolates user input directly into a shell command, causing a potential command injection vulnerability.
**Learning:** Using `os.system` with formatted strings containing user-provided directory paths is unsafe because it executes directly in the shell.
**Prevention:** Use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list rather than a single formatted string.
