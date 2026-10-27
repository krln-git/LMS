## 2024-10-27 - Command Injection via os.system
**Vulnerability:** Command injection vulnerability in `clean_xml.py` where `os.system` was executing an unescaped f-string with user-provided path inputs.
**Learning:** Even local file paths must be treated as untrusted input when passed to a shell. `os.system` executes through a shell and is inherently unsafe for variable interpolation.
**Prevention:** Always use `subprocess.run` (or similar) with arguments passed as a list, and avoid using `shell=True`. Additionally, defensively cast path objects to strings (`str()`) when passing them to subprocess lists.
