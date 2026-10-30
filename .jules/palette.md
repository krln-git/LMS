## 2024-10-31 - Add ARIA Labels to Icon-Only Buttons in Underscore Templates
**Learning:** When improving accessibility for icon-only elements like delete buttons, explicitly adding aria-label (and avoiding redundant visually hidden span tags) ensures clear screen reader announcements while maintaining visual consistency.
**Action:** Always ensure icon-only buttons in templates have proper aria-label attributes using the correct localized string syntax (e.g. `<%- gettext(\"Text\") %>`).
