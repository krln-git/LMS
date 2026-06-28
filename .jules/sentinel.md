## 2023-10-25 - Fix Command Injection in clean_xml.py
**Vulnerability:** Command injection via os.system and f-strings in management command argument processing.
**Learning:** The application expected direct stdout printing from diff, leading to the use of os.system.
**Prevention:** Always use subprocess.run with lists and avoid capture_output if stdout passthrough is desired.
