## 2024-08-01 - Command Injection via os.system in clean_xml.py
**Vulnerability:** Found os.system(f'diff -r {course_dir} {export_dir}') which allows command injection if course_dir or export_dir contains shell metacharacters.
**Learning:** Legacy management commands sometimes use os.system for system utilities like diff. These are dangerous when parsing paths.
**Prevention:** Use subprocess.run() with a list of arguments and shell=False (the default) to prevent shell evaluation.
