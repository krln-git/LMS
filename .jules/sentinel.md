## 2024-05-24 - Command Injection via os.system in Management Commands
**Vulnerability:** Command injection risk found in `clean_xml.py` where user-provided arguments (`course_dir`) were passed directly into an `os.system()` string.
**Learning:** Using formatted strings with `os.system` creates a critical command injection vulnerability if any variable is influenced by external input.
**Prevention:** Always use the `subprocess` module (`subprocess.call` or `subprocess.run`) and pass commands and arguments as a list of strings to safely bypass shell evaluation.
