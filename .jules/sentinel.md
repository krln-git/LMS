## 2025-01-20 - Prevent Command Injection via os.system
**Vulnerability:** Found `os.system(f'diff -r {course_dir} {export_dir}')` which exposes the application to command injection if paths contain shell metacharacters.
**Learning:** Legacy scripts frequently use `os.system()` with string formatting to shell out for simple tools like `diff`. Replacing this directly requires care since `os.system` returns an exit code but does not raise exceptions on non-zero exit codes (like `diff` finding differences).
**Prevention:** Always use `subprocess.run([...], check=False)` to execute commands with list arguments (bypassing the shell) while maintaining the original flow that doesn't expect exceptions to be raised on failure.
