## 2024-05-24 - Accessibility for icon-only buttons in Underscore templates
**Learning:** Icon-only delete buttons in `cms/templates/js/*.underscore` lack `aria-label`s. We must use `<%- gettext('...') %>` for ARIA labels in these templates.
**Action:** Always add `aria-label="<%- gettext('Text') %>"` to icon-only buttons in `.underscore` templates.
