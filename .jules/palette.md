## 2023-10-24 - Missing ARIA labels on Icon-only buttons
**Learning:** Icon-only delete buttons in Underscore templates often lack `aria-label` attributes, relying solely on `title` and visually hidden screen reader tags which may not be robust enough for all assistive technologies. It is critical to add explicit `aria-label`s.
**Action:** When encountering icon-only interactive elements, ensure an `aria-label` matching the functionality (e.g., `<%- gettext('Delete') %>`) is explicitly provided.
