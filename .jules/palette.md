## 2024-03-05 - Added ARIA attributes to icon-only buttons in video block
**Learning:** Found that Open edX uses a mix of FontAwesome icon spans and `div` elements acting as buttons. Screen readers can read out the font awesome unicode or ignore `div` buttons entirely if they aren't marked as `button`.
**Action:** Always verify if an interactive element with a click handler is an actual `<button>` rather than a `<div>` or `<a>`, and explicitly hide decorative inner `<span>` icons with `aria-hidden="true"` while applying the `aria-label` to the parent button.
