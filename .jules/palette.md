## 2024-05-24 - Fix self-closing non-void tags and add aria-hidden
**Learning:** In HTML5 templates (such as Open edX Mako/underscore templates), avoid using self-closing syntax for non-void elements like `<i>` or `<span>`, as it causes rendering/parsing issues. Additionally, decorative FontAwesome icons inside buttons should be hidden from screen readers using `aria-hidden="true"`.
**Action:** Always use explicit closing tags (e.g., `<i></i>`) and ensure decorative icons have `aria-hidden="true"`.
