## 2024-06-08 - Fix OS Command Injection in clean_xml.py
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` which uses untrusted input and allows arbitrary command execution.
**Learning:** Legacy management scripts might contain OS-level commands (e.g. `diff`) assuming inputs like directory paths are safe, which opens up command injection vulnerabilities (CWE-78).
**Prevention:** Avoid `os.system` and string interpolation when calling OS utilities. Use `subprocess.run` with array-based arguments and safely cast inputs to strings (e.g. `str(path)`). Set `check=False` when recreating expected legacy behavior that ignores non-zero exit codes.
