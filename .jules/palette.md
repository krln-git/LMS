## 2024-11-09 - Add aria-labels using exact localized tags
**Learning:** When improving accessibility for elements in Mako or Underscore templates, you must reuse the exact same localized translation tags used in titles/tooltips (e.g. `<%- gettext('Delete') %>`) to avoid breaking i18n.
**Action:** Always search for and mirror existing translation syntax when adding aria-labels to template files.
