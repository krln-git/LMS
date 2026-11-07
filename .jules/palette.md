## 2024-05-24 - Modal Close Buttons A11y
**Learning:** Using both `aria-label` on the parent element and a visually hidden text span inside it causes screen readers to announce the label twice and may introduce minor visual regressions.
**Action:** Add the localized text label exclusively as the `aria-label` attribute on the interactive control element directly instead of nesting it.
