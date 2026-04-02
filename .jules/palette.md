## 2024-04-02 - Add ARIA labels to transcript feedback buttons
**Learning:** Missing accessible names on icon-only buttons block screen reader users. The application template uses an inner icon span (`<span class="icon fa...">`) inside the button.
**Action:** When adding accessible names to icon-only buttons, set `aria-label` or `title` using the translation syntax (e.g., `aria-label="${_('Thumbs up')}"`) on the button element and ensure the inner icon span is hidden from screen readers using `aria-hidden="true"`.
