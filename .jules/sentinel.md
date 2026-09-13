## 2024-05-24 - Fix Command Injection in Utility Scripts
**Vulnerability:** Usage of `os.system` and `os.popen` with concatenated strings.
**Learning:** These functions pass strings to the shell, making them vulnerable to command injection if paths or inputs contain shell metacharacters.
**Prevention:** Use `subprocess.run` with `shlex.split` or list arguments to avoid invoking the shell.
