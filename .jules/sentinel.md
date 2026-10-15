## 2024-10-15 - Command Injection in clean_xml.py
**Vulnerability:** Command injection vulnerability via `os.system` using an f-string.
**Learning:** A common pattern of passing formatted strings to `os.system` can lead to command injection if variables are improperly handled or contain spaces.
**Prevention:** Use `subprocess.run` with a list of arguments, and ensure variables are correctly cast to strings. Pass `check=False` to preserve os.system behaviour.
