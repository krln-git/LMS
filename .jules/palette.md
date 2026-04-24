## 2024-04-25 - Native Buttons in Open edX Templates
**Learning:** Found interactive elements like "close" and "copy" implemented as `<div>` tags with `.btn-link` classes. This lacks native keyboard navigability and semantics.
**Action:** Always refactor these to native `<button type="button">` tags. The existing `.btn-link` utility correctly styles `<button>` elements, so no custom CSS is needed. Ensure decorative FontAwesome icons within these buttons have `aria-hidden="true"` so screen readers only announce the label or inner text.
