## 2024-05-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system` using formatted strings (`os.system(f'diff -r {course_dir} {export_dir}')`) in a Django management command.
**Learning:** Using string interpolation with `os.system` or `subprocess.call(shell=True)` exposes the system to command injection if user inputs or directory paths contain shell metacharacters.
**Prevention:** Always use `subprocess.call` or `subprocess.run` with a list of arguments (`['diff', '-r', course_dir, export_dir]`) and avoid `shell=True` unless absolutely necessary.
