## 2024-05-23 - Command Injection via os.system
**Vulnerability:** Found `os.system(f"diff -r {course_dir} {export_dir}")` which is susceptible to command injection.
**Learning:** Developers often use `os.system` for quick shell commands, but string formatting with user or external input creates command injection vulnerabilities.
**Prevention:** Always use `subprocess.run` with a list of arguments instead of shell strings to safely execute external commands.
