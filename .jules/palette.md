## 2024-05-20 - Interactive Divs Without Keyboard Support
**Learning:** Found an interactive `div` used as a close button without keyboard focusability or screen reader announcements. Using `.btn-link` on a `div` strips native semantics.
**Action:** Always refactor interactive `div` elements into native `<button type="button">` elements to restore keyboard navigability, and include `aria-label` with translated text (e.g., `${_('Close')}`) and `aria-hidden="true"` on decorative icons.
