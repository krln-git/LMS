## 2024-05-24 - Remove os.system and fix command injection risk in clean_xml
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `lms/djangoapps/courseware/management/commands/clean_xml.py` which allows command injection if `course_dir` or `export_dir` contains spaces or special characters.
**Learning:** `os.system` is dangerous, especially when formatting strings into the command. In Python, `subprocess.call` or `subprocess.run` with a list of arguments is much safer, avoiding the shell entirely.
**Prevention:** Always use `subprocess` with a list of arguments for system commands, instead of `os.system` with a formatted string. Avoid `shell=True` unless absolutely necessary.
