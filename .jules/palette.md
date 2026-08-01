## 2024-05-13 - Add ARIA Labels to Thumbs Up/Down Buttons
**Learning:** Icon-only buttons lacking ARIA labels render them inaccessible to screen readers, especially in rating components. Adding `aria-label` makes them useful and `aria-hidden="true"` to the icon removes redundant information for screen readers.
**Action:** When creating icon-only buttons (like thumbs up/down), always add an `aria-label` (translating if needed) and mark the child icon `aria-hidden="true"`.
