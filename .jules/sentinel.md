# Sentinel's Journal

## 2024-05-22 - [Initializing Journal]
**Vulnerability:** N/A
**Learning:** Initialized Sentinel's journal.
**Prevention:** N/A

## 2024-05-22 - [XSS in Wiki Template]
**Vulnerability:** Found `{{ message|safe }}` inside a JavaScript string literal in `lms/templates/wiki/base.html`. This allows an attacker to break out of the string context and execute arbitrary JavaScript if they can control the `message` content. Even if the message content itself is safe HTML, it's not necessarily safe for a JS string context (e.g., it could contain quotes).
**Learning:** Django's `safe` filter prevents HTML escaping, which is dangerous when outputting data into a JavaScript context. The `escapejs` filter should be used instead for string literals in JS.
**Prevention:** Use `{{ message|escapejs }}` when rendering variables inside JavaScript string literals.
