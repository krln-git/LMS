## 2024-04-06 - Accessible Modal Close Buttons
**Learning:** Found that some older components implemented modal close controls using `<div>` wrappers containing nested hidden `<input>` elements. This breaks native keyboard accessibility and screen reader expectations for interactive controls.
**Action:** Always replace `<div>`-based interactive controls with native `<button type="button">` elements incorporating `sr-only` text and `aria-hidden="true"` on decorative icons to ensure full A11y compliance.
