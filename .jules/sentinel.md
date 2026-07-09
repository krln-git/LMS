## 2024-05-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system` using `f-strings` to execute shell commands with potentially unvalidated user input (`course_dir` and `export_dir`).
**Learning:** Using `os.system` with shell interpolation allows for command injection if variables contain shell metacharacters. The script relies on the command dumping output directly to standard output, making `check=False` the ideal replacement to safely execute the command without a shell while maintaining the expected output behavior.
**Prevention:** Always use `subprocess.run` with an array of arguments instead of `os.system` for safe command execution without shell interpretation.
