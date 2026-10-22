## 2026-10-22 - Icon-only buttons with SR text still need tooltips
**Learning:** Icon-only buttons that use `<span class="sr">` are accessible to screen readers but remain visually inaccessible to sighted users on hover if they lack a `title` attribute.
**Action:** Always ensure icon-only buttons have both an `aria-label` (or SR span) for screen readers and a `title` attribute for sighted user tooltips.
