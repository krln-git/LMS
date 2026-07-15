## 2024-05-14 - Add screen-reader text to icon-only delete buttons
**Learning:** Icon-only buttons lacking screen reader text are inaccessible to visually impaired users navigating via screen readers. We need to make sure to add `span` with class `sr` for screen reader accessibility in Mako and underscore templates.
**Action:** Always add screen-reader-only text (e.g. `<span class="sr">`) to icon-only buttons, especially destructive ones like delete buttons.
