## 2023-10-24 - Missing ARIA Labels on Icon-only Buttons
**Learning:** Found multiple instances of icon-only delete buttons in CMS Underscore templates that lack `aria-label` attributes.
**Action:** Always include `aria-label` on icon-only buttons, even if a `title` attribute is present.
