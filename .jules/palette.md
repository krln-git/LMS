## 2024-05-24 - Missing ARIA Labels on Icon-only Buttons
**Learning:** Found that CMS underscore templates commonly miss `aria-label` attributes on icon-only buttons (like delete buttons with just a trash icon), even if they have `title` attributes. Tooltips/titles alone are not sufficient for screen readers.
**Action:** Always verify icon-only buttons have an `aria-label` matching their tooltip/title text, using the same localized string.
