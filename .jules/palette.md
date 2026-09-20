## 2024-05-23 - Accessibility for Icon-only Buttons in Underscore Templates
**Learning:** When assigning localized string expressions like `<%- gettext("Text") %>` to HTML attributes (such as `aria-label`) in Backbone/Underscore templates, always enclose the expression in explicit HTML quotes to prevent parsing errors and accessibility issues if the evaluated string contains spaces.
**Action:** Always add `aria-label` with explicit HTML quotes to icon-only buttons in `.underscore` templates to ensure screen reader accessibility.
