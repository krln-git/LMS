## 2024-05-24 - Interactive Elements Focus Management
**Learning:** Custom UI toggles (like the video social sharing modal) implemented with `<div>` tags rather than native HTML elements break keyboard accessibility. They prevent screen readers from announcing them as interactable.
**Action:** Always refactor interactive `<div>` elements into native `<button type="button">` tags. When a container is opened or closed, explicitly manage focus by moving it to the first interactive element inside (when opening) or back to the toggle button (when closing).
