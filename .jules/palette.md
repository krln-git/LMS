## 2024-06-05 - Close Button Accessibility
**Learning:** Found an interactive close control implemented as a `<div>` with a `<span>` containing an icon. Interactive controls should be native `<button>` tags with `aria-label`s.
**Action:** Replace `div` wrappers with `<button>` tags for interactive controls to restore keyboard tab order and screen reader interactability, avoiding the need for extra ARIA roles.
