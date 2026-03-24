## 2024-05-19 - Command Injection via os.system
**Vulnerability:** Command injection risk in `clean_xml.py` using `os.system` with f-strings and unsanitized user inputs.
**Learning:** `os.system` parses arguments through a shell which allows arbitrary command execution if input contains shell metacharacters.
**Prevention:** Use the `subprocess` module (`subprocess.call` or `subprocess.run`) with a list of arguments to execute commands directly without shell interpolation.
