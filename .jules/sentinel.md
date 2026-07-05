## 2024-07-05 - Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` which executes an OS command with interpolated strings directly.
**Learning:** `os.system` with f-strings or string concatenation is a classic command injection vector if paths are not sanitized or come from untrusted sources.
**Prevention:** Use `subprocess.run` with a list of arguments (`subprocess.run(['diff', '-r', course_dir, export_dir], check=False)`) which prevents shell injection by default.
