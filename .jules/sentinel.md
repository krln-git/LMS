## 2024-05-18 - Prevent Command Injection via os.system and os.popen
**Vulnerability:** Unsanitized user inputs passed to os.system and os.popen could lead to command injection.
**Learning:** Command injection can occur when using shell=True or passing untrusted strings directly to shell execution functions like os.system or os.popen.
**Prevention:** Always use subprocess.run with a list of arguments (or shlex.split to safely parse command strings) instead of passing raw string commands directly to the shell.
