## 2025-02-12 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system` being used with unsanitized dynamically constructed strings (`os.system(f'diff -r {course_dir} {export_dir}')`), which is a critical command injection vulnerability.
**Learning:** The script relied on shell execution instead of standard `subprocess.run` with argument lists, exposing the system to potential arbitrary command execution via crafted directory paths.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` (to mimic legacy `os.system` behavior without throwing exceptions on non-zero exits) to safely execute system commands without a shell.
