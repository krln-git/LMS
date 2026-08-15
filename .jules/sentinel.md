## 2024-08-15 - [Prevent Command Injection in clean_xml.py]
**Vulnerability:** Command injection vulnerability in `clean_xml.py` using `os.system(f"diff -r {course_dir} {export_dir}")` where `course_dir` and `export_dir` can be maliciously crafted strings.
**Learning:** This occurred because `os.system` passes arguments to the shell and expands them without proper sanitization.
**Prevention:** Use `subprocess.run()` with a list of arguments and `check=False` to securely execute commands instead of relying on shell execution.
