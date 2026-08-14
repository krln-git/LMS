## 2024-08-14 - Command Injection Risk in Management Command
**Vulnerability:** Unsafe use of `os.system` with string interpolation for `diff` command.
**Learning:** Management commands can inadvertently introduce command injection risks if file paths are not sanitized before being passed to the shell.
**Prevention:** Always use `subprocess.run` with an argument list instead of `os.system` with string interpolation when executing external commands.
