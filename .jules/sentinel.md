## 2024-05-24 - Unsafe os.system Usage
**Vulnerability:** Shell injection risk from unsanitized input passed to `os.system`.
**Learning:** Legacy Python scripts occasionally use `os.system` out of convenience, exposing them to shell injection, particularly when variables are passed inside formatted strings without escaping.
**Prevention:** Consistently use the `subprocess` module (`subprocess.run`, `subprocess.call`) passing arguments as a list to avoid inadvertently evaluating shell variables or operators.
