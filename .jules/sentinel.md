## 2024-05-18 - Prevent Command Injection with subprocess
**Vulnerability:** Found `os.system` using string formatting to construct shell commands with user-controlled variables.
**Learning:** `os.system` evaluates shell syntax. If `course_dir` or `export_dir` contained shell metacharacters, arbitrary commands could be executed.
**Prevention:** Use the `subprocess` module (`subprocess.call`, `subprocess.run`) and pass arguments as a list rather than a single formatted string to bypass shell evaluation.
