## 2024-05-24 - Fix Command Injection in clean_xml management command
**Vulnerability:** Found `os.system` using an f-string to construct a shell command (`os.system(f'diff -r {course_dir} {export_dir}')`) in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** Using string interpolation with `os.system` allows an attacker to inject arbitrary shell commands if the variables (`course_dir`, `export_dir`) are user-controlled.
**Prevention:** Always use the `subprocess` module (`subprocess.call`, `subprocess.run`, `subprocess.Popen`) and pass arguments as a list of strings instead of a single formatted string. This prevents the shell from interpreting the arguments as commands.
