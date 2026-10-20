## 2024-05-24 - Command Injection in clean_xml.py
**Vulnerability:** Command injection via os.system(f'diff -r {course_dir} {export_dir}')
**Learning:** Using os.system with f-strings and unsanitized variables allows arbitrary command execution.
**Prevention:** Always use subprocess.run with an argument list and cast variables to strings.
