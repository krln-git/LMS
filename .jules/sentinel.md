## 2024-04-30 - Fix Command Injection in XML cleaning script
**Vulnerability:** Found `os.system()` with formatted string containing user-controlled paths (`f'diff -r {course_dir} {export_dir}'`), allowing arbitrary command execution.
**Learning:** String interpolation with `os.system` is dangerous, even in admin/management scripts, as input can break out of arguments.
**Prevention:** Use `subprocess.run` with a list of arguments instead to bypass shell evaluation completely.
