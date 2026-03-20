## 2024-05-20 - Replace insecure os.system and os.popen calls
**Vulnerability:** Found uses of `os.system()` and `os.popen()` with string interpolation to construct and run shell commands (`diff` and `pytest`), which is vulnerable to command injection.
**Learning:** Legacy scripts sometimes use outdated `os` module functions for shell interactions. These need to be identified and migrated.
**Prevention:** Use `subprocess.call()` or `subprocess.run()` instead of `os.system()` or `os.popen()`, and always pass arguments as a list rather than a formatted string to prevent command injection, avoiding `shell=True` unless absolutely necessary (and even then, strictly validating inputs).
