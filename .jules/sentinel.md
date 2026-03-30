## 2024-03-30 - Fix Command Injection in clean_xml Command
**Vulnerability:** Use of os.system() with unvalidated user input (course_dir) allows arbitrary command execution.
**Learning:** Using f-strings with os.system() directly exposes the system to command injection if input contains shell metacharacters.
**Prevention:** Always use subprocess.run() or subprocess.call() with a list of arguments instead of os.system() or shell=True.
