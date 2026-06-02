## 2024-05-15 - Command Injection in Management Commands
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `lms/djangoapps/courseware/management/commands/clean_xml.py`. `course_dir` and `export_dir` are derived from user input (command line arguments), which leads to a command injection vulnerability.
**Learning:** Legacy management commands or utility scripts often use `os.system` for convenience without sanitizing inputs.
**Prevention:** When remediating `os.system` command injection vulnerabilities (CWE-78) where the script expects standard behavior without throwing exceptions on non-zero exit codes (e.g., running `diff`), replace it with `subprocess.run([args], check=False)` to safely execute the command without a shell.
