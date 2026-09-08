## 2024-05-18 - Prevent Command Injection via os.system
**Vulnerability:** Unsanitized user inputs (course directory paths) passed to `os.system` using f-strings.
**Learning:** Using `os.system` with dynamically constructed strings (even f-strings) is highly vulnerable to command injection if the variables contain shell metacharacters.
**Prevention:** Always use `subprocess.run` (or `subprocess.Popen`) with a list of arguments instead of shell execution for invoking external commands.
