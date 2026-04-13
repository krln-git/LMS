## 2024-05-24 - [Fix Command Injection in clean_xml]
**Vulnerability:** Shell command injection via `os.system` using unsanitized directory paths in `lms/djangoapps/courseware/management/commands/clean_xml.py`.
**Learning:** Using `os.system` with f-strings or string concatenation for external commands exposes the application to command injection if the arguments (like file paths) are not strictly controlled or sanitized. This is particularly relevant for paths coming from user input or command-line arguments.
**Prevention:** Use the `subprocess` module with argument lists (e.g., `subprocess.run(['diff', '-r', dir1, dir2])`) instead of executing raw shell strings.
