## 2024-07-28 - Icon-only buttons lacking ARIA labels
**Learning:** In the video template, there are thumbs-up and thumbs-down feedback buttons that are icon-only but do not have aria-labels or aria-hidden on the icon. This makes them inaccessible to screen readers.
**Action:** When finding icon-only buttons, always ensure they have an aria-label and the child icon has aria-hidden="true".
