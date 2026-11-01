## 2024-11-01 - Missing ARIA Labels on Icon-only Action Buttons
**Learning:** In Backbone/Underscore.js template components (`cms/templates/js/*.underscore`), icon-only action buttons like delete (using `<span class="icon fa fa-trash-o">`) are often missing accessible names for screen readers. The `title` attribute is present but not sufficient on its own.
**Action:** Always add `aria-label` or equivalent to icon-only buttons using localized strings (e.g. `<%- gettext('Delete') %>`) to ensure screen readers announce the button's action correctly, in addition to the title tooltip.
