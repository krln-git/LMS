## 2024-05-24 - Command Injection via os.system
**Vulnerability:** Found `os.system(f"diff -r {course_dir} {export_dir}")` which is vulnerable to command injection if paths contain special characters.
**Learning:** Passing unescaped paths and interpolated strings to shell commands allows injection.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` when replacing `os.system` without raising errors.
