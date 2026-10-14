## 2026-10-14 - Command Injection using os.system
**Vulnerability:** Found os.system executing a shell command with a format string interpolating variable content, leading to shell injection.
**Learning:** Python's os.system calls the shell. Formatting user or dynamic variables directly into the shell string exposes the application to command injection.
**Prevention:** Use subprocess.run() with a list of arguments (setting shell=False by default) and no string formatting to execute commands safely.
