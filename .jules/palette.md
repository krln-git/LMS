## 2024-05-24 - Add aria-expanded and aria-controls to custom UI toggles
**Learning:** When building custom UI toggles (e.g., expanding/collapsing content with display: none/block), explicitly set and dynamically toggle `aria-expanded` (true/false) via JavaScript on the control element, and use `aria-controls` to link it to the target content for accessibility compliance.
**Action:** Always ensure custom toggles have `aria-expanded` and `aria-controls` attributes that are dynamically updated to reflect the current state of the target content.
