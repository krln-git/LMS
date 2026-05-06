## 2024-05-24 - Double-escaping UI Regressions with jQuery .text()

**Vulnerability:** XSS vulnerabilities often originate from using jQuery `.html()` with dynamically rendered, user-controlled data.
**Learning:** Naively replacing `.html()` with `.text()` can cause UI double-escaping if the underlying model or view already escapes the content before rendering it (e.g., via `_.escape()` or a pre-escaping templating engine). This displays raw HTML entities to the user.
**Prevention:** Always verify whether the content is already safely escaped before deciding whether to switch `.html()` to `.text()`, and if so, determine whether `.text()` would introduce a UI bug or simply be redundant. If `.text()` breaks it but an XSS risk is present, ensure correct `_.escape()` or an equivalent is used during rendering.

## 2024-05-24 - Unsafe DOM extraction via jQuery .html()

**Vulnerability:** XSS vulnerability found in contenteditable elements where input is fetched via `.html()` instead of `.text()`.
**Learning:** Even if data is properly escaped before being rendered, extracting user input using `.html()` allows a user to type raw HTML into an editable element, which will then be extracted as raw HTML and potentially saved or re-rendered dangerously.
**Prevention:** Always use `.text()` or `.val()` when retrieving user input from the DOM to ensure HTML entities and tags are treated as plain text.
