## 2024-05-15 - Enclose ARIA labels evaluated strings in quotes
**Learning:** When assigning localized string expressions to HTML attributes (such as `aria-label`) in templates, they must be enclosed in explicit HTML quotes to prevent parsing errors and accessibility issues if the evaluated string contains spaces.
**Action:** Always add explicit double quotes around localized string expressions (e.g., `aria-label="${_('Text')}"`) when used as HTML attributes.
