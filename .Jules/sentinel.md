## 2024-05-14 - Prevent Command Injection via subprocess.run
**Vulnerability:** Unsafe shell execution via os.system("diff -r ...") allows command injection.
**Learning:** Directly passing unvalidated strings to os.system() can lead to arbitrary command execution.
**Prevention:** Use subprocess.run() instead of os.system() and pass arguments as a list of strings.
