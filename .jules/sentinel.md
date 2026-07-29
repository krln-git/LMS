## 2024-07-29 - Command injection in courseware management commands
**Vulnerability:** Found `os.system()` with unsanitized string interpolation (`os.system(f'diff -r {course_dir} {export_dir}')`) in a Django management command handling XML course data.
**Learning:** Even internal management commands processing data from files or arguments can be vulnerable to command injection if paths or filenames are crafted maliciously.
**Prevention:** Always use `subprocess.run()` with a list of arguments instead of passing concatenated strings to `os.system()` or `subprocess` with `shell=True`.
