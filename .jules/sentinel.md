## 2024-05-24 - Command Injection via path.py objects
**Vulnerability:** Command injection in os.system using path.py objects formatted into strings.
**Learning:** Python path.py instances can be implicitly cast to strings in f-strings, leading to command injection when passed to os.system. They also cause type errors if passed directly to subprocess.
**Prevention:** Always use subprocess.run with a list of arguments and explicitly cast path objects to strings (e.g., str(course_dir)) to prevent type errors and command injection.
