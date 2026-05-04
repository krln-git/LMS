## 2024-05-04 - XSS via unescaped variables in underscore templates
**Vulnerability:** In `lms/static/js/discovery/views/facets.js`, dynamic properties (`facetName`, `displayName`) were directly passed into an underscore template rendered via jQuery `.html()`, leading to potential Cross-Site Scripting (XSS) if the names contained malicious characters.
**Learning:** Variables passed into JavaScript templates that ultimately render into the DOM using methods like `.html()` must be properly escaped if they are not guaranteed to be safe HTML.
**Prevention:** Use `_.escape()` on dynamic user-controlled variables (like display names) before passing them to underscore templates.
