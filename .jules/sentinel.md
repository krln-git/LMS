## 2024-05-23 - Command Injection in clean_xml
**Vulnerability:** Found `os.system` usage with f-strings `os.system(f'diff -r {course_dir} {export_dir}')` in `lms/djangoapps/courseware/management/commands/clean_xml.py`. This is a command injection risk as `course_dir` could contain arbitrary shell characters.
**Learning:** Legacy management scripts often use `os.system` for convenience but pass untrusted user input directly to the shell, exposing command execution vulnerabilities.
**Prevention:** Use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list to avoid command injection.
