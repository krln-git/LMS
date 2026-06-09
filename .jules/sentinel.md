## 2024-06-09 - Insecure os.system Usage for diff Command
**Vulnerability:** Found `os.system` used with string formatting (CWE-78: Command Injection) to execute a `diff` command in `clean_xml.py`.
**Learning:** The script expects standard behavior without throwing exceptions on non-zero exit codes (like `diff` outputs). Developers may use `os.system` because it's a quick way to run shell commands, but it's dangerous with user-controlled or dynamically generated variables like directory paths.
**Prevention:** When remediating `os.system` command injection vulnerabilities where the script expects standard behavior without throwing exceptions on non-zero exit codes, replace it with `subprocess.run([args], check=False)` and explicitly cast dynamic variables to strings to prevent TypeErrors.
