## 2024-06-25 - ARIA Labels on Icon-Only Buttons
**Learning:** Found transcript feedback buttons in `lms/templates/video.html` that were completely inaccessible to screen readers because they only contained decorative FontAwesome icons without any text or ARIA labels.
**Action:** Always verify that icon-only buttons have an `aria-label` attribute (using `_('...')` for translation in Mako templates) and that the internal decorative icons have `aria-hidden="true"` to prevent screen readers from reading meaningless character codes.
