## 2024-05-15 - Icon-only button accessibility in widgets
**Learning:** Icon-only buttons used for closing modals frequently lack ARIA labels and visually hidden text, relying solely on CSS classes for the icon, making them invisible to screen readers.
**Action:** Always add an `aria-label` attribute to the interactive element, `aria-hidden="true"` to the decorative icon, and a `span.sr` containing the action text to ensure comprehensive accessibility support.
