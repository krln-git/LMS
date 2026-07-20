## 2024-07-20 - Fix Command Injection in clean_xml.py
**Vulnerability:** Found `os.system()` being used with formatted strings for shell commands (`os.system(f'diff -r {course_dir} {export_dir}')`), enabling command injection if directory names are malicious.
**Learning:** `os.system` passes strings directly to the shell. This can be exploited by users if they have any control over directory paths (even partial control or uploaded directories).
**Prevention:** Use `subprocess.run` with a list of arguments and `check=False` to safely execute without shell expansion, matching the legacy `os.system` behavior of piping output directly to stdout.
