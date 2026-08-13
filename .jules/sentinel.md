## 2024-05-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Command injection vulnerability in clean_xml.py via os.system and f-strings.
**Learning:** Management commands often take user or file paths as input, which can be dangerous if passed directly to the shell.
**Prevention:** Always use subprocess.run with arguments as a list and never use shell=True or os.system.
