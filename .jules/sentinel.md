## 2024-05-18 - Fix Command Injection in clean_xml
**Vulnerability:** Command injection in clean_xml.py via os.system and unvalidated variables
**Learning:** f-strings inside os.system are dangerous and allow shell injection
**Prevention:** Always use subprocess.run with lists of arguments for system commands, avoid os.system completely
