
## 2024-04-25 - Improve accessibility of close buttons in template
**Learning:** Found an interactive close button implemented as a div (`<div class="btn-link close-btn float-right">`) in Mako templates, lacking screen reader support and proper keyboard focus interaction.
**Action:** Replace pseudo-buttons with native `<button type="button">` elements, adding `aria-label="${_('Close')}"` for screen readers and `aria-hidden="true"` to decorative FontAwesome icons to enhance accessibility. Ensure hardcoded text uses the Mako `_()` function for internationalization.
