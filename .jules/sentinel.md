## 2024-05-24 - Command Injection Vulnerability in clean_xml.py
**Vulnerability:** Unsanitized user input passed directly to `os.system` via string formatting, leading to command injection.
**Learning:** `os.system` is dangerous when used with dynamic paths. It evaluates the string as a shell command, allowing attackers to inject arbitrary commands using shell metacharacters.
**Prevention:** Use `subprocess.run` (or `subprocess.Popen`) instead of `os.system` and pass the command arguments as a list. This prevents the shell from interpreting the arguments as shell commands.
