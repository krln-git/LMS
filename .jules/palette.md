## 2024-05-20 - Refactor div buttons to native buttons
**Learning:** In Open edX templates, interactive elements like close or copy buttons are sometimes incorrectly implemented as styled `<div>` tags (e.g., `<div class="btn-link">`). Refactor these into native `<button type="button">` elements to ensure proper keyboard navigability and screen reader support.
**Action:** Always verify if an element acting like a button is using the semantic `<button>` tag instead of `<div>` or `<a>`. Add `aria-hidden="true"` to icon spans and `<span class="sr">` for screen reader text when needed.
