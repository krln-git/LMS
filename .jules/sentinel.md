## 2024-05-18 - Command Injection via os.system
**Vulnerability:** Command injection vulnerability in `clean_xml.py` management command where `os.system` was used with a formatted string containing user-controlled paths.
**Learning:** Using `os.system` with formatted strings is dangerous as it passes the entire string to the shell, allowing shell metacharacters to be executed.
**Prevention:** Always use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list to safely handle untrusted input.
