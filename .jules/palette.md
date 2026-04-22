## 2024-04-23 - Native button elements for interactive icons
**Learning:** Interactive close buttons in Open edX templates are sometimes implemented as styled `<div>` tags with `.btn-link`, causing accessibility issues.
**Action:** Always refactor these into native `<button type="button">` elements with an `aria-label` and `aria-hidden="true"` on the decorative inner FontAwesome icon.
