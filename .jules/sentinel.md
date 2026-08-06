## 2024-08-06 - Prevent command injection in clean_xml.py
**Vulnerability:** Command injection risk via os.system with formatted strings.
**Learning:** Using os.system with f-strings for user-provided paths allows arbitrary shell command execution.
**Prevention:** Use subprocess.run() with a list of arguments and check=False (if non-zero exit codes are expected) to safely execute shell commands.
