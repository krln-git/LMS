## 2024-05-22 - Legacy Backbone Toggles Need Explicit ARIA Management
**Learning:** Legacy Backbone views often use `display: block/none` for toggles without managing ARIA states. Screen readers can't tell if a button expands content or just does nothing (or where the content is).
**Action:** When working with jQuery `toggle()` or CSS `display` manipulation, always manually toggle `aria-expanded` and link the button to the content with `aria-controls`.
