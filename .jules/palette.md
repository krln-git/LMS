
## 2024-03-10 - Adding Accessible Labels to Icon-Only Feedback Buttons
**Learning:** Found an accessibility pattern where icon-only buttons (like transcript feedback "thumbs up/down" buttons) lacked `aria-label`, `title`, and `aria-hidden="true"` for inner decorative icons.
**Action:** When creating or modifying icon-only buttons in Open edX templates, always add translated `aria-label` (using `"${_('...')}"`) and `title` attributes to the `<button>` element, and make sure any internal FontAwesome `<span>` elements have `aria-hidden="true"` so screen readers ignore the decorative icon and read the label instead.
