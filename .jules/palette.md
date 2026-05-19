## 2024-05-18 - Add ARIA labels to icon-only buttons in Open edX templates
**Learning:** Icon-only buttons in Mako templates often lack accessible names, but any added labels must be wrapped in standard HTML quotes and use the Mako internationalization syntax `${_('...')}` to ensure they are safely rendered and translatable.
**Action:** Always add `aria-label="${_('...')}"` or `title="${_('...')}"` to icon-only buttons and explicitly wrap the dynamic translation string in quotes to prevent valid HTML truncation and ensure screen reader accessibility.
