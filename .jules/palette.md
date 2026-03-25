
## 2024-05-24 - Accessible Expand/Collapse Controls
**Learning:** Custom expand/collapse components using `display: none/block` do not inherently communicate their state to screen readers, leaving users unaware of dynamically revealed content.
**Action:** When building or modifying custom UI toggles, explicitly set and dynamically toggle `aria-expanded` (true/false) via JavaScript on the control element, and use `aria-controls` to link it to the target content for accessibility compliance.
