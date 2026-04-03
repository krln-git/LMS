## 2024-04-03 - Avoid os.system for shell commands
**Vulnerability:** Command injection vulnerability via os.system(f'diff -r {course_dir} {export_dir}') where course_dir could contain shell metacharacters.
**Learning:** os.system with dynamically constructed strings allows command injection if the input is not sanitized.
**Prevention:** Use subprocess.call or subprocess.run with a list of arguments instead of a single string.
