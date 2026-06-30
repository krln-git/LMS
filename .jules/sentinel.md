
## 2024-06-30 - Fix command injection in clean_xml.py
**Vulnerability:** Found `os.system()` being used with dynamic variables for file paths in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** `os.system` passes strings directly to the shell, making it susceptible to command injection if variables contain shell metacharacters.
**Prevention:** Always use `subprocess.run` (or similar functions in `subprocess`) without `shell=True` and pass arguments as a list to safely execute system commands.
