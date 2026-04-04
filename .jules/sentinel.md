## 2024-04-04 - Command Injection Risk in Management Commands
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` in `clean_xml.py` management command.
**Learning:** Even internal management commands and scripts that are not public-facing web endpoints can be vulnerable to command injection if they pass unvalidated input (like directory paths from CLI arguments) directly to `os.system()` with shell execution.
**Prevention:** Always use the `subprocess` module (e.g. `subprocess.run`) and pass arguments as a list (e.g. `subprocess.run(['diff', '-r', dir1, dir2])`) to avoid invoking the shell entirely.
