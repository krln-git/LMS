## 2024-05-25 - Fix OS System Command Injection
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `clean_xml.py` which is vulnerable to command injection if `course_dir` or `export_dir` has shell metacharacters.
**Learning:** Using `os.system` with formatted strings opens up shell injection risks. `subprocess.run` with `check=False` is the safe alternative to run diff without an exception on non-zero exit codes.
**Prevention:** Always use `subprocess.run` with a list of arguments instead of shell strings, especially for user-provided paths. Set `check=False` if non-zero exit statuses are expected (like with `diff`).
