## 2025-02-14 - Fix div buttons in video share
**Learning:** Interactive UI elements (close/copy buttons) in Open edX templates are sometimes implemented as styled `<div>` elements rather than native `<button>` tags, breaking keyboard accessibility and screen reader support.
**Action:** Always verify that interactive elements use native semantic `<button>` tags, and explicitly define `aria-label` along with `aria-hidden="true"` on their child FontAwesome icons.
