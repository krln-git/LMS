## 2024-03-25 - Fix OS Command Injection in clean_xml.py
**Vulnerability:** Command injection vulnerability via `os.system` using unsanitized `course_dir` and `export_dir` variables.
**Learning:** Using `os.system` with f-strings directly interpolates user input into shell commands, allowing attackers to execute arbitrary commands by injecting shell metacharacters.
**Prevention:** Use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list rather than a single formatted string, which bypasses the shell and prevents injection.
