## 2024-05-26 - Command Injection via os.system
**Vulnerability:** A command injection vulnerability was identified in `clean_xml.py` where `os.system` was used with unsanitized user-controlled variables.
**Learning:** `os.system` executes commands via the shell, which allows shell metacharacters in input variables to break out of the intended command structure and execute arbitrary shell commands.
**Prevention:** Always use the `subprocess` module with a list of arguments (e.g., `subprocess.run([args], check=False)`) instead of string interpolation with `os.system`, as this passes arguments directly to the program and bypasses the shell.
