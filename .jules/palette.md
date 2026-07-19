## 2024-07-20 - Accessible Icon-Only Buttons
**Learning:** Found a recurring pattern in the app's components (like transcript feedback) where icon-only buttons lack ARIA labels, making them inaccessible. Additionally, child icon elements like `<span class="icon fa...">` need `aria-hidden="true"` to prevent screen readers from announcing redundant visual artifacts.
**Action:** Always add descriptive `aria-label`s to icon-only `<button>` tags and `aria-hidden="true"` to their internal decorative icons to ensure a clean, understandable screen reader experience.
