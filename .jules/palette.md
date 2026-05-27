## 2024-05-27 - Icon-only feedback buttons missing ARIA labels
**Learning:** Found transcript feedback buttons in `lms/templates/video.html` using FontAwesome icons (`fa-thumbs-up`) without screen reader accessibility (no `aria-label` on the button, and missing `aria-hidden="true"` on the decorative icon itself).
**Action:** When inspecting templates (especially Open edX Mako templates), verify that all icon-only interactive elements (buttons/links) have translated `aria-label`s and that decorative child nodes have `aria-hidden="true"`.
