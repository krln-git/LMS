## 2024-05-13 - Add aria-labels to icon-only buttons
**Learning:** The video player component had icon-only buttons for transcript feedback (thumbs up/down) that were entirely missing accessible names, rendering them unusable for screen reader users. This highlights a codebase pattern where secondary interactive features sometimes miss basic ARIA requirements compared to core functionality.
**Action:** Always verify icon-only buttons (like thumbs up/down icons) have explicit `aria-label` attributes to ensure they are accessible.
