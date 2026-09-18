## 2023-10-24 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** In Backbone/Underscore templates, icon-only buttons often rely solely on `title` attributes, which are insufficient for robust screen reader accessibility. Explicit `aria-label` attributes using localized strings (`<%- gettext("...") %>`) are necessary.
**Action:** Always ensure icon-only buttons include an explicit `aria-label` attribute and `aria-hidden="true"` on the visual icon element to provide a fully accessible experience.
