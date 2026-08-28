## 2024-05-01 - Prevent command injection in clean_xml
**Vulnerability:** Found `os.system` using string formatting with uncontrolled variables (`course_dir` and `export_dir`) in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** This creates a command injection risk where crafted directory names could execute arbitrary shell commands.
**Prevention:** Use `subprocess.run` with a list of arguments instead of shell strings.
