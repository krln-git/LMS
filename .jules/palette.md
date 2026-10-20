## 2024-10-21 - Reusing translation strings for accessibility metadata
**Learning:** When adding accessibility attributes like aria-label to template files, reusing the exact localized translation strings (via Mako or Underscore syntax) used in the element’s tooltip ensures screen reader text aligns perfectly with internationalization and prevents regressions.
**Action:** Always check the element’s existing `title` or adjacent hidden text for translation functions before hardcoding screen-reader strings.
