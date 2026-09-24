## 2026-09-24 - Adding ARIA labels to icon-only template buttons
**Learning:** When assigning localized string expressions (like `<%- gettext('Text') %>`) to HTML attributes (such as `aria-label`) in `.underscore` templates, use explicit HTML quotes to prevent parsing errors.
**Action:** Always include localized string expressions within HTML quotes when adding accessibility metadata.
