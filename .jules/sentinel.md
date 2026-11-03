## YYYY-MM-DD - Fix command injection in clean_xml.py
**Vulnerability:** Found `os.system(f"diff -r {course_dir} {export_dir}")` which is vulnerable to command injection if `course_dir` or `export_dir` contains special characters or shell meta-characters.
**Learning:** Shell commands constructed via f-strings with variables that come from user input or external sources can lead to command injection.
**Prevention:** Use `subprocess.run` with a list of arguments instead of a shell string, which avoids shell interpretation. Also, ensure paths are cast to strings if they might be path objects.
