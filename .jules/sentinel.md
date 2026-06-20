## 2024-05-24 - os.system Command Injection Vulnerability
**Vulnerability:** Found `os.system` being used with unsanitized/formatted input (`course_dir` and `export_dir`) to execute shell commands.
**Learning:** `os.system` executes through a shell and is vulnerable to command injection if paths contain special shell characters.
**Prevention:** Use `subprocess.run` with a list of arguments and `check=False` to safely execute the command without a shell while maintaining legacy behavior.
