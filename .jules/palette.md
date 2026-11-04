## 2024-11-04 - Missing accessible label on source edit close button
**Learning:** The close button in the High Level Source Editing modal relies entirely on visual styling (empty span with class `close-icon`) and lacks an accessible name, making it unusable for screen reader users.
**Action:** Always ensure icon-only buttons include an `aria-label` or visually hidden text for screen readers.
