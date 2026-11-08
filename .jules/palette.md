## 2024-11-09 - Add ARIA labels to icon-only buttons
**Learning:** Icon-only buttons (like delete and edit actions in Underscore templates) without visible text labels require `aria-label` attributes for screen reader accessibility, matching the localized strings used for tooltips (e.g., `<%- gettext("Delete") %>`).
**Action:** Always verify icon-only buttons in templates have proper `aria-label` or `sr-only` text if there is no visible text.
