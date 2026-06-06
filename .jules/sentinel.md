## 2024-05-24 - Command Injection in management commands
**Vulnerability:** Unsanitized user input (`course_dir` and `output_dir` arguments) being directly interpolated into an `os.system()` shell command in `clean_xml.py`.
**Learning:** Even internal management commands and scripts expecting standard behavior without throwing exceptions on non-zero exit codes (like `diff`) can introduce severe command injection vulnerabilities if `os.system()` is used.
**Prevention:** Always replace `os.system()` with `subprocess.run([args], check=False)` to safely execute commands without a shell, while still allowing expected non-zero exit codes without raising exceptions.
