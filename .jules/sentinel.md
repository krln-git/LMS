## 2024-05-30 - [XSS Vulnerability in Wiki Base Template]
**Vulnerability:** Found `{{ message|safe }}` inside a `<script>` tag in `lms/templates/wiki/base.html`, rendering Django template variables within a JavaScript string literal directly.
**Learning:** This is a classic XSS vulnerability since user input (like message contents) might contain double quotes or backslashes, or even malicious JS code (`"`); `alert(1); //`), leading to arbitrary code execution.
**Prevention:** When passing variables from Django templates to JavaScript strings, always use the `|escapejs` filter instead of `|safe` to ensure strings are correctly encoded for Javascript injection.
