## 2023-10-21 - Missing ARIA labels on icon-only buttons
**Learning:** Icon-only delete buttons in Backbone templates often rely solely on title attributes for context. Adding aria-label attributes that reuse the existing localized translation strings ensures screen readers correctly interpret the buttons.
**Action:** Always add aria-label attributes to icon-only buttons, even if they have title attributes.
