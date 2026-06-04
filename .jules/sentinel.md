## 2024-06-04 - Fix Command Injection in clean_xml.py
**Vulnerability:** Command injection vulnerability in `os.system(f'diff -r {course_dir} {export_dir}')` where an attacker could potentially execute arbitrary commands via crafted directory names.
**Learning:** `os.system()` passes strings directly to the shell without sanitization, which allows shell metacharacters to be evaluated.
**Prevention:** Always use `subprocess.run()` with a list of arguments and `check=False` when replacing `os.system()` for standard operations like `diff` where non-zero exit codes are expected.
