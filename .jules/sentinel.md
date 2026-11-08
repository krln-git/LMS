## 2024-05-24 - Command Injection in Courseware Management Command
**Vulnerability:** Command injection in `lms/djangoapps/courseware/management/commands/clean_xml.py` via `os.system` using unvalidated directory paths.
**Learning:** Management commands often use string formatting in `os.system` for utility scripts, missing the risk of directory paths containing special characters that could execute arbitrary commands.
**Prevention:** Use `subprocess.run` with argument lists instead of `os.system` with formatted strings, as argument lists safely pass data to executables without shell evaluation.
