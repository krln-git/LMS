## 2024-11-06 - Add aria-labels to icon-only buttons
**Learning:** Icon-only buttons often have `title` attributes but lack `aria-label` tags, and both should use matching localization (e.g. `<%- gettext(...) %>`) to avoid a11y issues and translation regressions.
**Action:** Always ensure icon-only buttons have an `aria-label` attribute matching localized text strings.
