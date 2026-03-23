## 2024-05-14 - Prevent Command Injection using subprocess.call
**Vulnerability:** A potential command injection vulnerability was found in `lms/djangoapps/courseware/management/commands/clean_xml.py` where `os.system` was used with a formatted string `f'diff -r {course_dir} {export_dir}'`. If `course_dir` or `export_dir` contained user-controlled input, arbitrary commands could be executed.
**Learning:** Using `os.system` with formatted strings is dangerous because it passes the string to a shell, which can interpret special characters and execute arbitrary commands.
**Prevention:** Instead of `os.system`, use the `subprocess` module (like `subprocess.call` or `subprocess.run`) and pass arguments as a list. This avoids passing the arguments through a shell and prevents command injection.
