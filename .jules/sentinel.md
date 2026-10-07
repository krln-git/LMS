## 2024-10-06 - Replacing os.system and os.popen with subprocess.run
**Vulnerability:** Command injection vulnerabilities from unsafe use of os.system and os.popen
**Learning:** These functions allow arbitrary command execution if input is not sanitized
**Prevention:** Always use subprocess.run with a list of arguments, and avoid shell=True
