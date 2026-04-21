## 2024-04-21 - Fix Command Injection in Management Command
**Vulnerability:** Found `os.system` using unsanitized string interpolation (f-strings) in `clean_xml.py` to execute a shell command (`diff`).
**Learning:** Even management commands (internal tools) can be vectors for command injection if variables like directory paths are passed unescaped to `os.system`.
**Prevention:** Use the `subprocess` module (`subprocess.call`, `subprocess.run`) with lists of arguments rather than single interpolated strings to prevent command injection.
