## 2024-10-05 - Add ARIA labels to icon-only buttons
**Learning:** Icon-only buttons using font-awesome without screen-reader text or aria-labels are completely inaccessible. Adding aria-label with existing localized gettext strings provides context without visual changes.
**Action:** Always check icon-only buttons (`fa-trash-o` etc) and inject aria-label attributes where `sr` spans are missing.
