## 2024-05-17 - Keyboard Focus Management in Custom Modals
**Learning:** When building custom toggle elements like social share menus, focus must be explicitly managed. Self-closing spans (e.g. `<span />`) should also be avoided in HTML templates to prevent rendering issues.
**Action:** Always verify keyboard focus is directed to the first interactive element when opening a toggle menu, and returned to the trigger button when closing. Convert generic `<div>` buttons to `<button>` with ARIA labels.
