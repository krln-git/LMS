## 2024-05-20 - Add ARIA label to delete button in textbook UI
**Learning:** Icon-only buttons using FontAwesome often lack accessible text for screen readers in legacy templates.
**Action:** Always check icon-only buttons in `.underscore` templates and ensure they have `aria-label` attributes using localized string syntax (e.g. `aria-label="<%- gettext('Delete') %>"`).
