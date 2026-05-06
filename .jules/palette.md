## 2024-05-18 - Video Social Sharing Close Button Accessibility
**Learning:** Using `<div>` for buttons and not managing focus during container toggling creates a severely degraded experience for keyboard/screen reader users.
**Action:** Always use semantic `<button>` tags with `aria-label` for icon-only actions, properly close self-closing `<span/>` tags containing icons, add `aria-hidden="true"` to decorative icons, and explicitly manage focus (e.g. `this.toggleBtn.focus()`) when custom containers like modals/share menus are opened or closed.
