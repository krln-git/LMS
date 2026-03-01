## 2024-05-24 - Add accessible names to icon-only buttons
**Learning:** Found that transcript feedback thumbs up/down buttons in `lms/templates/video.html` lacked accessible names or labels, which is a common pattern for icon-only buttons. Screen readers would read out "button" without context.
**Action:** When auditing or building icon-only buttons, always ensure an `aria-label` or `title` is set, and hide the inner icon element from screen readers with `aria-hidden="true"`. Use `title` for tooltip visibility, and translate using `${_('...')}` where available in Mako templates.
