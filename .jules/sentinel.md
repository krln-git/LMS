## 2024-04-24 - [Fix Command Injection in clean_xml.py]
**Vulnerability:** Found a command injection vulnerability where unsanitized user input (`course_dir` and `export_dir`) could be passed to a shell via `os.system`.
**Learning:** Using `os.system` with f-strings is dangerous and can lead to command injection if variables contain shell metacharacters.
**Prevention:** Always use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list to avoid shell execution of variables.
