## 2024-05-24 - Missing ARIA Labels on Icon-Only Buttons in Underscore Templates
**Learning:** It is easy to miss accessibility on icon-only buttons created dynamically in Backbone/Underscore JS templates. The `<%- gettext('...') %>` pattern must be carefully interpolated into `aria-label` attributes.
**Action:** Always ensure any template creating icon-only buttons includes an `aria-label` utilizing the translation tags for internationalization.
