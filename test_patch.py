import sys
content = open("lms/djangoapps/courseware/management/commands/clean_xml.py").read()
content = content.replace("import os\nimport sys", "import os\nimport subprocess\nimport sys")
content = content.replace(
    "os.system(f'diff -r {course_dir} {export_dir}')",
    "# 🛡️ Sentinel: Prevent command injection by avoiding a shell with subprocess.run\n    subprocess.run(['diff', '-r', str(course_dir), str(export_dir)], check=False)"
)
with open("lms/djangoapps/courseware/management/commands/clean_xml.py.patched", "w") as f:
    f.write(content)
