## 2024-06-12 - Command Injection via os.system in Management Command
**Vulnerability:** Use of `os.system()` with formatted string inputs (`os.system(f'diff -r {course_dir} {export_dir}')`) allows potential command injection if user-controlled variables are used for paths.
**Learning:** `os.system` runs through a shell and directly parses the command string, making it vulnerable to shell metacharacters and escaping issues. It existed because it was an easy way to run `diff` and print output without exception handling for non-zero exit codes.
**Prevention:** Replace all `os.system` calls with `subprocess.run([args], check=False)` to execute commands safely without shell parsing, preventing command injection and safely handling expected non-zero exit codes.
