## 2024-10-24 - Command Injection in clean_xml.py
**Vulnerability:** Command injection vulnerability in `lms/djangoapps/courseware/management/commands/clean_xml.py` due to using `os.system` with string interpolation.
**Learning:** Passing variables containing paths directly to `os.system` via f-strings allows arbitrary command execution if the path contains shell metacharacters.
**Prevention:** Use `subprocess.run` with a list of arguments instead of a single string to safely pass variables to external commands. Cast path-like objects to strings.
