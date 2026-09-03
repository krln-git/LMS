## 2024-11-06 - Prevent command injection in management commands
**Vulnerability:** Unsanitized variables passed to `os.system`
**Learning:** f-strings in `os.system` are a common pattern for shell injection when dynamic course/export directories are used.
**Prevention:** Always use `subprocess.run` with array-based commands and `check=False` (if natural exception swallowing is needed) instead of `os.system`
