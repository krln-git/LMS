## 2024-05-08 - Command Injection in clean_xml.py
**Vulnerability:** Unsanitized variables `course_dir` and `export_dir` were being passed directly to `os.system` via string interpolation (`f"diff -r {course_dir} {export_dir}"`).
**Learning:** This is a classic command injection vulnerability where a malicious user could provide a crafted `course_dir` or `export_dir` to execute arbitrary system commands.
**Prevention:** Replace `os.system` with `subprocess.run` and pass command arguments as a list (e.g., `subprocess.run(["diff", "-r", str(course_dir), str(export_dir)], check=False)`) to ensure variables are treated as arguments, not executable shell code.
