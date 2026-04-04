## 2024-06-25 - Replace div-based buttons with semantic HTML in templates
**Learning:** In Open edX templates, some interactive elements like close buttons are incorrectly implemented as styled `<div>` tags (e.g., `<div class="btn-link">`). When building or modifying custom UI toggles, explicit toggling of `aria-expanded` is required.
**Action:** Always refactor `<div>` buttons into native `<button type="button">` elements to ensure keyboard navigability. Explicitly set and dynamically toggle `aria-expanded` via JavaScript on the control element.
