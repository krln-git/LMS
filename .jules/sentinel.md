## 2024-04-20 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system` using string interpolation with unescaped arguments (`course_dir` and `export_dir`) which leads to a command injection risk.
**Learning:** `os.system` with string concatenation is a critical vulnerability when handling user-provided arguments like paths.
**Prevention:** Always use `subprocess` functions like `subprocess.call` or `subprocess.run` and pass arguments as a list to avoid shell execution.
