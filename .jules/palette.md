## 2024-05-04 - Accessible Close Buttons in Video Share Modal
**Learning:** Found an interactive close button implemented as a `<div class="btn-link">` with an un-hidden FontAwesome icon. This lacks keyboard accessibility and screen reader support compared to native interactive elements.
**Action:** When finding `div` elements styled as buttons with `.btn-link`, convert them to native `<button type="button">` elements, add translatable `aria-label`s for screen readers, and apply `aria-hidden="true"` to purely decorative inner icons.
