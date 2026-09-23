## 2024-05-30 - Fix command injection with subprocess.run
**Vulnerability:** Command injection vulnerability via `os.system` using an f-string to interpolate variables into a shell command.
**Learning:** When mitigating command injection by replacing `os.system` with `subprocess.run`, do not interpolate variables into an f-string and then parse it with `shlex.split`, as this will cause errors if the variables contain spaces. Instead, construct the argument list directly (e.g., `["cmd", str(var)]`).
**Prevention:** Always construct argument lists directly using `subprocess.run` instead of invoking the shell.
