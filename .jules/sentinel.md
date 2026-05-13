## 2024-05-13 - Fix XSS in .html() and dangerouslySetInnerHTML
**Vulnerability:** User input was rendered without escaping using jQuery `.html()` and React `dangerouslySetInnerHTML`.
**Learning:** Even when standard library methods like React are used, using raw injection functions (`dangerouslySetInnerHTML`) or unescaped jQuery injection (`.html()`) on dynamic user inputs like search queries bypasses built-in XSS protections.
**Prevention:** Always use safe methods like `.text()` in jQuery or standard React text bindings (e.g. `<div>{value}</div>`) when rendering user input.
