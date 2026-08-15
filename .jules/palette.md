## 2024-05-24 - Screen Reader Labels in Underscore Templates
**Learning:** When assigning Mako `gettext()` translated text to HTML attributes like `aria-label` in Open edX Underscore templates, the `<%- gettext("Text") %>` syntax should be enclosed in quotes to ensure proper parsing when the evaluated string contains spaces.
**Action:** Always ensure Mako or Javascript dynamic template variables are wrapped in HTML quotes (e.g. `aria-label="<%- gettext(...) %>"`) when dynamically generating accessibility attributes to avoid breaking HTML rendering.
