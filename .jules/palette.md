## 2024-10-09 - Missing ARIA Labels on Icon-only Buttons
**Learning:** Several icon-only delete buttons in CMS underscore templates rely solely on the `title` attribute for tooltip and accessible name generation. Screen readers and alternative assistive tech don't consistently announce `title` attributes, leading to unlabelled destructive actions.
**Action:** Always ensure icon-only buttons have an explicit `aria-label` (using translated strings like `<%- gettext('Delete') %>`) even if a `title` attribute is already present for tooltips.
