## 2024-05-18 - Added ARIA labels to Backbone icon-only buttons
**Learning:** In Open edX Backbone templates (`.underscore`), icon-only buttons often rely on `title` attributes for accessibility. However, screen readers prefer explicit `aria-label` attributes for icon-only buttons. The correct translation syntax in Backbone templates for attribute assignment is `<%- gettext("Text") %>`.
**Action:** When adding ARIA labels to icon-only buttons in Backbone templates, always use the `<%- gettext("...") %>` syntax and enclose it in quotes, like `aria-label="<%- gettext('Text') %>"`.
