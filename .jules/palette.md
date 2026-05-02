## 2024-10-25 - Converting Fake Button Elements to Native Buttons
**Learning:** Fake `<div>` buttons (even with `.btn-link` styles) lack native keyboard navigability, focus indicators, and screen reader announcements. Using self-closing tags for `<span>` is invalid in HTML5.
**Action:** Always refactor interactive `<div>` elements into native `<button type="button">` elements. Add `aria-label` with localized text via Mako (e.g., `${_('Text')}`) and hide decorative icons using `aria-hidden="true"`. The `.btn-link` utility correctly un-styles native buttons automatically.
