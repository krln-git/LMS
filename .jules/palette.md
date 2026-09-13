## 2024-05-24 - Injecting Backbone localized strings into HTML attributes
**Learning:** When assigning localized string expressions (like Backbone `<%- gettext("Text") %>`) to HTML attributes (such as `aria-label`) in `.underscore` templates, always enclose the expression in explicit HTML double quotes to prevent parsing errors and ensure accessibility tags remain intact.
**Action:** Always wrap translation syntax in double quotes when injecting into DOM attributes in Backbone templates.
