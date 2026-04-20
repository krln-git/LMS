
## 2026-04-20 - Focus Management for Toggled Containers
**Learning:** When building custom UI toggles (like social sharing menus), replacing `div` with native `<button>` elements improves screen reader access, but keyboard users still get trapped if focus isn't managed.
**Action:** Always programmatically return focus to the original toggle button when a container is closed (`toggleBtn.focus()`), and shift focus to the first interactive element (like the close button) when opened.
