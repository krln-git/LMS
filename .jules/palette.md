## 2024-05-14 - Accessible Icon-Only Buttons
**Learning:** When dealing with icon-only buttons in Underscore templates, we need to ensure they have an `aria-label` attribute in addition to a visual `title` tooltip so they are accessible to screen readers without breaking internationalization. The `aria-label` should use the exact same localized string as the `title`.
**Action:** Add `aria-label="<%- gettext('Delete') %>"` to delete buttons that only have a FontAwesome trash icon and a title attribute.
