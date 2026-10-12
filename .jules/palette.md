## 2026-10-12 - Add missing aria-hidden attributes to decorative icons
**Learning:** Many FontAwesome icons used for decoration or paired with visible text are missing the `aria-hidden="true"` attribute, which causes screen readers to read out confusing text or the unicode character of the icon itself. This occurs frequently across various Underscore templates.
**Action:** Always ensure that decorative icons, or those paired with descriptive text/tooltips, include the `aria-hidden="true"` attribute to prevent them from being read aloud by assistive technologies.
