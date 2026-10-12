## 2023-10-12 - Prevent Command Injection with subprocess.run
**Vulnerability:** Python `os.system()` using formatted strings with variables without sanitation.
**Learning:** Passing unsanitized user inputs to `os.system()` can easily result in arbitrary shell command execution.
**Prevention:** Use `subprocess.run` with a list of arguments, and pass `check=False` to preserve non-throwing behavior if it was expected.
