## 2024-05-24 - Command Injection in Management Commands
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` which allows command injection via unescaped path variables.
**Learning:** Even internal management tools using `os.system` with f-strings or string concatenation are vulnerable if input paths contain shell metacharacters.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` when running system commands to avoid shell evaluation.
