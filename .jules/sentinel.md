
## 2024-05-24 - Command Injection in Management Commands
**Vulnerability:** Found `os.system()` being used with an f-string interpolating user input (`course_dir` and `export_dir`) in a Django management command (`clean_xml.py`).
**Learning:** Management commands that interact with the filesystem or run external tools sometimes use `os.system` out of convenience, leading to CWE-78 (OS Command Injection) if the input contains shell metacharacters.
**Prevention:** Always use `subprocess.run()` with a list of arguments and `check=False` (to mimic `os.system`'s non-throwing behavior and standard output dumping), and never use `shell=True` when handling user-provided file paths.
