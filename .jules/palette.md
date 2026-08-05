## 2024-05-19 - Missing aria-labels on action-icon buttons
**Learning:** Icon-only buttons used for actions (like "delete") in multiple CMS underscore templates lack `aria-label` attributes, relying only on `title` which is insufficient for screen readers.
**Action:** Always add explicit `aria-label` attributes alongside `title` for icon-only buttons to ensure they are accessible.
