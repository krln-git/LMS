## 2024-11-04 - Explicit ARIA Labels for Icon-Only Buttons
**Learning:** While the `title` attribute acts as a fallback accessible name, it is insufficient on its own for icon-only buttons as some screen readers may ignore it or handle it inconsistently.
**Action:** Always add an explicit `aria-label` to icon-only buttons (like delete/trash icons), reusing the same translation string as the `title` attribute to ensure reliable screen reader announcements.
