## 2025-02-23 - Command Injection in clean_xml
**Vulnerability:** Command injection in `os.system` via user-supplied `course_dir` in `clean_xml.py`
**Learning:** Management commands can sometimes perform system level operations without adequate string sanitization, particularly when shelling out to utilities like `diff`.
**Prevention:** Use `subprocess.run` with list arguments (and without `shell=True`) whenever executing system commands, especially when taking any external input.
