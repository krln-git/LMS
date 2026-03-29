## 2024-05-18 - Convert div buttons to native button tags in templates
**Learning:** Interactive elements like close or copy buttons are sometimes incorrectly implemented as styled `<div>` tags in templates. This prevents proper keyboard navigability and breaks screen reader support.
**Action:** Always refactor interactive `<div>` elements into native `<button type="button">` elements with appropriate `aria-label` or `title` attributes and set `aria-hidden="true"` on inner decorative icons.
