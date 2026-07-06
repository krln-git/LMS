## 2024-05-24 - Command Injection in Management Commands
**Vulnerability:** Found `os.system` using string interpolation for file paths in `clean_xml.py`.
**Learning:** Management scripts can sometimes inadvertently introduce shell injection vulnerabilities if they rely on shell commands for standard operations like `diff`.
**Prevention:** Use `subprocess.run` with `shell=False` and pass arguments as a list of strings instead of relying on `os.system`.
