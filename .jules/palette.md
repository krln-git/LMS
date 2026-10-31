## 2026-10-31 - Add aria-label to icon-only buttons
**Learning:** When adding icon-only buttons (like 'Delete' actions), ensure both a `title` for sighted users (tooltips) and an `aria-label` for screen readers are present, as relying solely on `title` or nested visually-hidden spans can be inconsistent across screen readers.
**Action:** Next time, review all interactive elements that do not contain visible text and verify they include a screen reader accessible label.
