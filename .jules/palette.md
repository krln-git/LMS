## 2024-10-25 - Add ARIA labels to icon-only buttons in backbone templates
**Learning:** Icon-only action buttons in Backbone (.underscore) templates must include explicit `aria-label` attributes for screen readers, as the `title` attribute alone is insufficient for reliable accessibility and localized string tags (like `<%- gettext("...") %>`) should be used.
**Action:** Always check template files for icon-only `<button>` or `<a>` elements and ensure they have `aria-label` attributes using the appropriate translation function.
