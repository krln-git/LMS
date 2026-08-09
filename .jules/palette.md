## 2024-05-24 - Missing ARIA Labels on Icon-Only Delete Buttons
**Learning:** Found several icon-only delete buttons in CMS underscore templates that had a 'title' attribute but no 'aria-label'. The 'title' attribute is often not read reliably by screen readers, making these buttons inaccessible.
**Action:** Always explicitly add 'aria-label' attributes to icon-only buttons (like those with 'action-icon' class), even if a 'title' tooltip is present, to ensure proper accessibility for screen reader users.
