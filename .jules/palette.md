## 2024-05-24 - Accessibility for Interactive Elements
**Learning:** Custom interactive elements (like `div`s as buttons) and togglable regions often lack keyboard accessibility. We must use native buttons and actively manage `aria-expanded` / `.focus()` when creating interactive UI.
**Action:** Always refactor `.btn-link` `div` elements to native `<button type="button">`. Manage `aria-expanded` attributes dynamically via JavaScript and correctly move focus when a togglable container is shown/hidden.
