## 2023-10-24 - Icon-only buttons need direct ARIA labels
**Learning:** While title attributes provide hover tooltips, icon-only `<button>` elements in underscore templates require explicit `aria-label` attributes for reliable screen reader accessibility. Relying solely on `title` or inner visually-hidden text is often insufficient across all assistive technologies.
**Action:** Always apply `aria-label` directly to icon-only interactive elements, ensuring the translation string (e.g., `<%- gettext("Delete") %>`) matches the tooltip to maintain internationalization consistency.
