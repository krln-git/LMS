## 2025-02-20 - Command Injection in clean_xml
**Vulnerability:** Found `os.system` usage with f-string formatting in `lms/djangoapps/courseware/management/commands/clean_xml.py`. This allows command injection if `course_dir` contains shell metacharacters.
**Learning:** Management commands often process file paths that might be user-controlled or at least controllable by an admin who might be tricked. Even admin-facing code should be secure.
**Prevention:** Always use `subprocess.call` (or `run`) with a list of arguments to avoid shell interpretation.
