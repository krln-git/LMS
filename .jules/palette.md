## 2024-05-24 - Add quotes to dynamically generated Mako variables in HTML attributes
**Learning:** In Mako templates, dynamically generated translated strings used as HTML attribute values (like `aria-label=${_("...")}`) must be explicitly wrapped in quotes. Otherwise, only the first word of the rendered string becomes the attribute value, causing screen readers to misread the label.
**Action:** Always wrap `${...}` expressions in standard HTML quotes (`aria-label="${...}"`) when using them as attribute values.
