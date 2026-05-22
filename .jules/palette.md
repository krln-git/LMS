## 2025-05-22 - Add ARIA labels to icon-only buttons in Mako templates
**Learning:** Icon-only buttons (like thumbs up/down icons for feedback) lack semantic context for screen readers in Open edX templates. We must add translatable `aria-label="${_('...')}"` attributes and hide the decorative FontAwesome icons using `aria-hidden="true"`.
**Action:** Always check icon-only buttons for missing `aria-label` and `aria-hidden="true"` attributes to ensure full accessibility for screen-reader users.
