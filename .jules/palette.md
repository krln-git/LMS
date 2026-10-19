## 2024-05-13 - Add aria-labels to icon-only buttons
**Learning:** Icon-only buttons with `title` attributes may not be reliably announced by screen readers. Explicit `aria-label` attributes using the same translation string are needed for robust accessibility.
**Action:** Always include an `aria-label` attribute on icon-only buttons, even if a `title` attribute is present.
