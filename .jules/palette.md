## 2024-05-24 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** In Open edX templates, icon-only buttons often rely solely on the title attribute, missing aria-labels required for reliable screen reader accessibility.
**Action:** Ensure all icon-only buttons in .underscore templates explicitly include an aria-label populated with `<%- gettext(...) %>`.
