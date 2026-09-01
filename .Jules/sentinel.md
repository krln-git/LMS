## 2024-05-24 - Fix command injection in scripts and clean_xml
**Vulnerability:** Found uses of `os.system` and `os.popen` executing strings containing variables that could be influenced by user input without sanitization.
**Learning:** These functions pass strings to a shell, which allows command injection if arguments are not properly sanitized.
**Prevention:** Use `subprocess.run` with a list of arguments (avoiding `shell=True`) to prevent shell injection, and use `shlex.split` for dynamically constructed commands.
