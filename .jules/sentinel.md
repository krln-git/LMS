## 2024-05-18 - Fix Command Injection in clean_xml
**Vulnerability:** Found `os.system` using string interpolation for a shell command in `clean_xml.py`, creating a command injection risk (CWE-78).
**Learning:** Even internal management scripts can be vulnerable to command injection when using `os.system` for convenience tools like `diff`.
**Prevention:** Always use `subprocess.run()` with a list of arguments instead of string formatting with `os.system()`.
