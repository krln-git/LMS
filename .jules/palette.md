## 2024-04-03 - Refactored div buttons to native buttons in video template
**Learning:** Found interactive elements like close and copy buttons incorrectly implemented as styled `<div>` tags in Open edX templates, lacking keyboard navigability.
**Action:** Always refactor faux buttons to native `<button type="button">` elements and add `aria-label` or `aria-hidden` attributes to child icons for accessibility.
