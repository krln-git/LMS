## 2024-05-24 - Fix os.system command injection in clean_xml
**Vulnerability:** Command injection vulnerability in `clean_xml.py` via `os.system` with string interpolation.
**Learning:** Shell command execution via `os.system` combined with string interpolation of variables like `course_dir` leads to command injection risks. The fix is to use `subprocess.run` with a list of arguments, properly passing `check=False` to preserve the non-failing behavior of `os.system` and converting variables to strings to avoid type execution errors.
**Prevention:** Always use `subprocess.run` with an argument list instead of `os.system` when executing external commands with variable interpolation. Never parse an interpolated string with `shlex.split`. Ensure types are cast to string for safety.
