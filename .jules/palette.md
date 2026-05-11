## 2024-05-11 - Fix accessibility on help buttons in student_account/form_field.underscore
**Learning:** Decorative icons in HTML templates must include `aria-hidden="true"` to avoid confusing screen reader users. Furthermore, non-void tags like `<i>` should not use self-closing syntax (e.g., `<i />`) in HTML5 as it can lead to rendering issues.
**Action:** When adding FontAwesome icons to buttons, always use explicit closing tags (e.g., `<i></i>`) and include `aria-hidden="true"`.
