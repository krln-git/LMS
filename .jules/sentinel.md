## 2024-11-05 - Avoid shell execution for parameterized commands
**Vulnerability:** Command injection via os.system and os.popen with unescaped input strings.
**Learning:** Directly passing interpolated variables to shell execution APIs introduces command injection risks in Python code.
**Prevention:** Use subprocess.run with a list of arguments and check=False (or True) instead of os.system, os.popen, or subprocess.Popen with shell=True to execute commands securely.
