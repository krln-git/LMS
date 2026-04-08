## 2024-04-09 - Accessible Help Toggles
**Learning:** Found a common pattern in the student account forms where "help" buttons (like "Need help signing in?") toggle a hidden container (`#login-help`, `#reset-help`) using `display: none` -> `display: block` but lack ARIA attributes (`aria-expanded`, `aria-controls`) to inform screen reader users of the state change.
**Action:** When implementing custom UI toggles that show/hide content, always ensure keyboard accessibility by properly managing `aria-expanded` and linking the button to the content with `aria-controls`.
