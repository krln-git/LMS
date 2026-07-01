## 2024-07-01 - Command Injection via os.system in clean_xml.py
**Vulnerability:** Found `os.system` being used with user-controlled input (`course_dir`) without sanitization in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** Legacy scripts often use `os.system` for convenience which leads to severe command injection if variables contain shell metacharacters.
**Prevention:** Always use `subprocess.run` with a list of arguments and never use `shell=True` to safely execute shell commands.
