## 2026-10-24 - ARIA labels for icon-only buttons
**Learning:** When auditing Django/Mako templates, icon-only buttons often have title attributes but lack corresponding aria-label attributes, which is essential for screen readers.
**Action:** Always copy the localized title string (e.g. `${_('Text')}`) into a new aria-label attribute on the button element to ensure accessibility.
