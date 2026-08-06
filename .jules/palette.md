## 2025-05-15 - Mako template attributes
**Learning:** When assigning Mako expressions to HTML attributes, they must be wrapped in explicit HTML quotes (e.g., `aria-label="${_('Text')}"`) to prevent accessibility issues.
**Action:** Always wrap evaluated Mako strings in quotes within HTML tags.
