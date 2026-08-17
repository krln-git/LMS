## 2024-05-24 - Backbone/Underscore Template ARIA Labels
**Learning:** When assigning localized text to ARIA attributes in Open edX Backbone/Underscore templates (`.underscore`), use `<%- gettext("Text") %>` syntax to ensure proper translation and escaping, rather than Mako syntax.
**Action:** Always use `<%- gettext() %>` for localized ARIA labels in `.underscore` templates.
