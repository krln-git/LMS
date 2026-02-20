## 2025-02-14 - ARIA roles for anchor buttons
**Learning:** Legacy CMS templates heavily rely on `<a>` tags for button-like actions (e.g., "New Section", "Collapse All") with `href="#"`. This is an accessibility anti-pattern as screen readers announce them as links, confusing users about the interaction type.
**Action:** When refactoring legacy templates, prioritize adding `role="button"` to anchor tags that trigger actions, or convert them to `<button>` elements if CSS allows.
