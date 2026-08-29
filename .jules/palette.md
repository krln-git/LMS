## 2024-05-25 - ARIA labels for icon-only buttons with visual-only labels
**Learning:** Found social share buttons (Facebook, Twitter, LinkedIn) in the accomplishments banner that visually hid their text labels using screen-reader-only styling. However, when a button uses `.icon-only` class without an explicit `aria-label`, screen readers might read the HTML content awkwardly or not at all depending on the exact markup and CSS tricks.
**Action:** Always add explicit `aria-label` attributes to icon-only buttons even if they contain visually hidden text to ensure robust screen reader support.
