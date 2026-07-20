## 2024-05-01 - Icon-Only Button ARIA Labels
**Learning:** The codebase relies on `title` attributes for tooltips on icon-only buttons, but frequently misses `aria-label`, making them inaccessible to screen readers because child icons have `aria-hidden="true"`.
**Action:** Always ensure `aria-label` is added alongside `title` for icon-only action buttons.
