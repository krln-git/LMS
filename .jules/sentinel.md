## 2024-06-05 - Fix Command Injection in clean_xml
**Vulnerability:** Command injection vulnerability identified in `clean_xml.py` where `os.system` was used to execute a diff command with string concatenation.
**Learning:** Using `os.system` with dynamically constructed strings (especially file paths that could potentially be user-controlled or malicious) allows shell injection.
**Prevention:** Always use `subprocess.run` with a list of arguments (setting `check=False` if replacing standard behavior that ignores exit codes, and explicitly converting variables like `pathlib.Path` objects to strings via `str()`) to safely execute commands without a shell.
