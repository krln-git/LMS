## 2024-05-28 - Quote Dynamic ARIA Labels
**Learning:** In Open edX Mako templates, dynamically generated strings used as HTML attribute values (like `${_('...')}`) must be explicitly wrapped in standard HTML quotes (e.g., `aria-label="${_('...')}"`). If omitted, spaces in the rendered text cause the browser to truncate the attribute, creating invalid HTML and breaking accessibility for screen readers.
**Action:** Always verify that dynamic attributes are enclosed in standard quotes when using Mako variables or translations inside HTML elements.
