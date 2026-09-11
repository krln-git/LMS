## 2024-05-15 - Replace os.system with subprocess.run
**Vulnerability:** Command injection via os.system
**Learning:** Python os.system passes string directly to shell, risking injection
**Prevention:** Use subprocess.run with a list of arguments, rather than string concatenation.
