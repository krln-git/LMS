## 2024-03-31 - Refactor div buttons to native button tags
**Learning:** Close and copy actions in older modal components are sometimes implemented as styled `<div>` tags (`btn-link`) instead of semantic `<button>` tags, and often lack explicit `aria-label` or `aria-hidden` attributes on their inner icons.
**Action:** Always use native `<button type="button">` for custom interactive elements to inherit keyboard support, and ensure decorative inner icon `<span>` elements use explicitly closed tags and `aria-hidden="true"` for screen reader compliance.
