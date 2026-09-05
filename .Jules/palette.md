## 2024-05-20 - ARIA Labels for Icon-Only Feedback Buttons
**Learning:** Icon-only buttons for transcript feedback (thumbs up/down) in video templates lack accessible names, rendering them invisible to screen readers.
**Action:** Always add `aria-label` with translated strings (e.g., `${_("Thumbs up")}`) to icon-only `<button>` elements, and set `aria-hidden="true"` on the purely decorative inner `<span>` icons.
