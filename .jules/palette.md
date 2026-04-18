## 2024-04-18 - Video Social Sharing Accessibility
**Learning:** When building custom UI toggles (e.g., expanding/collapsing share menus), explicitly set and dynamically toggle `aria-expanded` via JavaScript on the control element, and return focus to the toggle button when closed to maintain keyboard accessibility compliance.
**Action:** Always link toggle controls to their target containers with `aria-controls` and programmatically manage their `aria-expanded` state and focus.
