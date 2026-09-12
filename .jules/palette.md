## 2024-05-18 - Icon-only buttons with titles
**Learning:** Relying purely on `title` for accessibility on icon-only buttons is an anti-pattern as its behavior varies significantly across screen readers and devices. ARIA labels should always be used even if a `title` is present.
**Action:** Always add `aria-label` to icon-only buttons, reusing the exact same translation string (e.g. `<%- gettext("Delete") %>`) used in their title attribute to prevent internationalization regressions.
