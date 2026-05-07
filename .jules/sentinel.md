## 2024-05-14 - Fix XSS in contenteditable DOM extraction
**Vulnerability:** Extracting user input from `contenteditable` DOM elements using jQuery `.html()` captures raw HTML (including script tags) typed by the user, which can lead to XSS if saved and re-rendered.
**Learning:** `contenteditable` elements behave like input fields but contain HTML. Using `.html()` on them is inherently unsafe if the goal is to extract the user's intended text.
**Prevention:** Always use `.text()` to extract user input safely as plain text from editable elements to avoid capturing potentially malicious raw HTML tags.
