## 2024-05-24 - [Command Injection in `clean_xml`]
**Vulnerability:** Found `os.system()` being called with an f-string containing unsanitized variables (`course_dir` and `export_dir`).
**Learning:** Using `os.system` with formatted strings is highly vulnerable to command injection if the variables contain shell metacharacters.
**Prevention:** Use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list to safely execute system commands without invoking a shell.
