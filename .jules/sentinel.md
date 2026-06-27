## 2025-02-28 - Replace Insecure Command Execution with Subprocess
**Vulnerability:** Found `os.system` being used to execute a shell command (`os.system(f'diff -r {course_dir} {export_dir}')`) in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** `os.system` executes commands in a shell and is vulnerable to command injection if paths or arguments contain shell metacharacters. In this repo, variables constructed from filesystem paths were directly interpolated into a shell string.
**Prevention:** Always use `subprocess.run` with a list of arguments (e.g., `subprocess.run(['diff', '-r', str(course_dir), str(export_dir)], check=False)`) to bypass the shell entirely and prevent command injection.
