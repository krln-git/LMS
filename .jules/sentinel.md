## 2024-05-24 - Command Injection via os.system
**Vulnerability:** Found `os.system` being used with string formatting (`f'diff -r {course_dir} {export_dir}'`) in a management command (`clean_xml.py`).
**Learning:** Using `os.system` with dynamically constructed strings can lead to command injection if the variables (like directory paths) contain shell metacharacters.
**Prevention:** Always use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass arguments as a list of strings rather than a single formatted string to safely escape shell arguments and prevent injection.
