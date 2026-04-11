## 2024-04-12 - Fix video social sharing accessibility
**Learning:** Interactive UI toggles implemented as `<div>` elements break keyboard accessibility. Modals/toggles require explicit `aria-expanded`, `aria-controls`, and manual focus management to ensure screen reader users aren't trapped or disoriented.
**Action:** Always refactor `<div>`-based buttons to native `<button>` elements, add `aria-hidden="true"` to decorative icons, and explicitly manage focus during show/hide transitions.
