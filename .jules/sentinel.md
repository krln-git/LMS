## 2023-10-25 - Command Injection via os.system interpolation
**Vulnerability:** Unsanitized user inputs (course_dir) interpolated directly into os.system commands via f-strings.
**Learning:** f-string interpolation into shell execution functions like os.system creates direct command injection vectors.
**Prevention:** Use subprocess.run with explicit list arguments and avoid shell=True or string-based shell execution.
