## 2024-05-24 - Command Injection in clean_xml.py
**Vulnerability:** Found `os.system` being used to call `diff -r {course_dir} {export_dir}` in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** Shell commands constructed via f-strings are vulnerable to command injection if paths contain shell metacharacters.
**Prevention:** Use `subprocess.run` with a list of arguments (without `shell=True`) for all system commands.
