import re
from pathlib import Path

def check_html_buttons():
    print("Checking for icon-only buttons without aria labels/hidden or equivalent:")
    pattern = re.compile(r'<button[^>]*>\s*<span[^>]*class="[^"]*fa [^"]*"[^>]*>\s*</span>\s*</button>', re.IGNORECASE)

    for html_file in Path('.').rglob('*.html'):
        try:
            content = html_file.read_text()
            matches = pattern.finditer(content)
            for m in matches:
                button_tag = m.group(0)
                if 'aria-label' not in button_tag and 'aria-hidden' not in button_tag and 'sr-only' not in button_tag:
                    print(f"Found match in {html_file}: {button_tag}")
        except Exception:
            pass

check_html_buttons()
