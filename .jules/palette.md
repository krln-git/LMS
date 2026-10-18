## 2024-10-18 - Add ARIA Labels to Delete Buttons
**Learning:** Icon-only delete buttons in CMS templates often lacked `aria-label` attributes, relying entirely on `title` and visually hidden content which might be insufficient for some screen readers.
**Action:** Always add `aria-label` to icon-only buttons using existing localized translation strings.
