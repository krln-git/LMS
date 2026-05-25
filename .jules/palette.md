
## 2024-05-25 - Interactive elements should use native semantic tags
**Learning:** Using `div` for interactive close buttons removes them from the natural tab order and requires additional ARIA roles to be exposed correctly to screen readers. Furthermore, FontAwesome icons used for decoration need `aria-hidden="true"` and non-void HTML tags like `span` must not be self-closing (`/>`) to ensure HTML validity.
**Action:** Always use `<button>` tags for clickable actions and ensure decorative icons are hidden from assistive technology with `aria-hidden="true"`.
