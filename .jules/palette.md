## YYYY-MM-DD - Fix Unquoted ARIA Labels in Mako Templates
**Learning:** Found multiple instances where `aria-label` was assigned an unquoted Mako expression (`aria-label=${_("Text")}`). This can cause HTML parsing issues, especially if the translation string contains spaces, rendering the label invalid for screen readers.
**Action:** Ensure all HTML attributes generated from template expressions are explicitly enclosed in quotes (e.g., `aria-label="${_("Text")}"`) to guarantee valid markup and correct accessibility parsing.
