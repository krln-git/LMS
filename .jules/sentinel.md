## 2025-04-14 - Fix command injection vulnerability in clean_xml management command
**Vulnerability:** Command injection vulnerability in `lms/djangoapps/courseware/management/commands/clean_xml.py` using `os.system` with f-strings for user input `course_dir`.
**Learning:** `os.system` with f-strings can lead to command injection if variables are attacker-controlled. Shell commands should be executed safely without a shell environment where possible.
**Prevention:** Use `subprocess.call` or `subprocess.run` with a list of arguments instead of string formatting with a shell.
