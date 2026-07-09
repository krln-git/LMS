## 2024-07-09 - Accessible Share Buttons
**Learning:** Social sharing buttons in this app often use title attributes instead of aria-labels which is less accessible for some screen readers when dealing with icon-heavy buttons. Even if they contain action labels, making sure standard icon-only class buttons explicitly declare aria-labels is important for consistency.
**Action:** Always add aria-labels to elements tagged with `icon-only` regardless of inner span structure to guarantee screen reader behavior.
