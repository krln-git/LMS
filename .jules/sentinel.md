## 2026-08-12 - [Preventing Command Injection in clean_xml]
**Vulnerability:** Command injection vulnerability in `clean_xml.py` through `os.system` execution with user-controlled parameters.
**Learning:** Dynamic strings like directory paths passed directly to shell execution (`os.system`) can allow arbitrary command execution.
**Prevention:** Use `subprocess.run` with a list of arguments and `check=False` to safely execute shell commands.
