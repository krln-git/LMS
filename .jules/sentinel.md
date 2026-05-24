## 2024-05-23 - Command Injection in clean_xml
**Vulnerability:** The `clean_xml` management command uses `os.system()` with an unescaped formatted string to execute a diff command, which is vulnerable to command injection if `course_dir` or `export_dir` contain malicious input.
**Learning:** `os.system()` directly executes commands in a shell environment, meaning any shell metacharacters in variables passed to it will be interpreted and executed by the shell.
**Prevention:** Use `subprocess.run()` with a list of arguments and `check=False` when executing external commands like `diff` where non-zero exit codes are expected but shell execution is not.
