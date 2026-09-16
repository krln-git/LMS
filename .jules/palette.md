## 2024-05-24 - ARIA labels for icon-only buttons in Underscore templates
**Learning:** When assigning localized string expressions to HTML attributes (such as `aria-label`) in Open edX Backbone/Underscore templates, it is critical to use `<%- gettext('Text') %>` instead of Mako syntax, and to enclose the expression in explicit HTML quotes (e.g., `aria-label="<%- gettext('Text') %>"`) to prevent parsing errors and accessibility issues.
**Action:** Always check icon-only buttons in `.underscore` templates for missing `aria-label` attributes and use the correct translation syntax.
