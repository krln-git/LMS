## 2024-06-01 - Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` where `course_dir` and `export_dir` are derived from unsanitized user inputs, enabling command injection (CWE-78).
**Learning:** Django management commands often use system calls directly without considering that command line options might be maliciously crafted, expecting standard behavior without throwing exceptions on non-zero exit codes.
**Prevention:** Use `subprocess.run([args], check=False)` to safely execute commands without a shell, and ensure dynamic path variables are cast to strings when passed as a list of arguments.
