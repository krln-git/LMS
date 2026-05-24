## 2024-05-18 - Accessible Close Button in Video Share
**Learning:** Replacing `div` elements styled with `.btn-link` to native `<button>` elements in Open edX templates maintains visual design while adding semantic a11y properties, and dynamically translated strings used as attributes need explicit HTML quotes.
**Action:** Always use `<button>` instead of `<div>` for interactive close toggles, ensuring `aria-label` is translated and decorative icons have `aria-hidden="true"`.
