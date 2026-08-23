## 2024-05-24 - Fix Command Injection in clean_xml.py
**Vulnerability:** Unsanitized user input passed to `os.system` via `course_dir` and `export_dir` arguments.
**Learning:** Command injections can occur when paths constructed from user input are evaluated by shell interpreters.
**Prevention:** Replace `os.system` with `subprocess.run` and pass arguments as a list to avoid shell execution. Convert Path objects to strings before passing them to subprocess.
