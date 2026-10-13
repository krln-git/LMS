## 2024-10-13 - [Command Injection via os.system and f-strings]
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `clean_xml.py` which allows command injection.
**Learning:** Using `os.system` with f-strings is dangerous as it passes the unescaped string directly to the shell.
**Prevention:** Always use `subprocess.run` with an argument list and defensively cast arguments to strings.
