## 2024-05-24 - Fix command injection in clean_xml.py
**Vulnerability:** Command injection via os.system and unsanitized directory paths in clean_xml.py
**Learning:** Even management commands using os.system for basic tasks like "diff" are vulnerable if path variables are directly interpolated into the command string.
**Prevention:** Always use subprocess.run with a list of arguments instead of string interpolation for shell commands.
