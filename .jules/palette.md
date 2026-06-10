## 2024-05-19 - Interactive Divs as Close Buttons
**Learning:** Found an interactive `div` element acting as a close button without proper keyboard support, role, or `aria-label` in `lms/templates/courseware/program_marketing.html`.
**Action:** Replace `div` with `button`, and add `aria-label="Close modal"` to natively restore keyboard tab order and screen reader interactability. Avoid relying solely on visual cues or class names for a11y.
