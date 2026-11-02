## 2023-11-04 - ARIA Labels for Icon-Only Delete Buttons
**Learning:** When improving accessibility for icon-only elements like close/delete buttons, use `aria-label` and ensure you reuse the exact same localized translation strings (e.g. `<%- gettext("Text") %>`) that are used in the title attribute to prevent internationalization regressions.
**Action:** Always check icon-only buttons for missing `aria-label` attributes and add them using existing localization wrappers.
