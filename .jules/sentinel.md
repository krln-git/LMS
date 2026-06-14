## 2024-05-24 - Command Injection via os.system
**Vulnerability:** Command injection vulnerability (CWE-78) found in `clean_xml.py` using `os.system(f'diff ...')` with dynamic arguments.
**Learning:** `os.system` runs commands through a shell, exposing applications to injection if arguments are unsanitized.
**Prevention:** Always use `subprocess.run` with a list of arguments and `check=False` when replicating legacy non-crashing behavior instead of `os.system` with f-strings.
