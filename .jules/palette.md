## 2024-06-18 - Missing ARIA Labels on Icon-only Action Buttons
**Learning:** Icon-only action buttons (like Delete) in underscore templates often rely solely on the `title` attribute, which is not reliably announced by all screen readers.
**Action:** Always add an explicit `aria-label` to icon-only buttons, even when a `title` or tooltip is present, to ensure robust accessibility.
