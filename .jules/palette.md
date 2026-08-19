## 2026-08-19 - Add ARIA Labels to Icon Buttons
**Learning:** Found missing `aria-label` attributes on several icon buttons in Underscore templates (e.g., delete buttons) and Mako templates. In Underscore templates, we need to use `<%- gettext('Text') %>` inside the `aria-label`. In Mako templates, we use `"${_('Text')}"`
**Action:** Add ARIA labels to these buttons to improve accessibility for screen readers.
