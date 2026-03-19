## 2024-05-18 - Prevent Command Injection using subprocess
**Vulnerability:** Found a command injection vulnerability in `clean_xml.py` where user input (`course_dir` and `export_dir`) could be passed directly into an `os.system` call without sanitization.
**Learning:** `os.system` with f-strings is dangerous because it executes the string directly in the shell, allowing for arbitrary command execution.
**Prevention:** Avoid `os.system`. Use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list of strings. This prevents shell interpretation of metacharacters and safely escapes the arguments.
