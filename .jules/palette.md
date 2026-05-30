## 2024-05-30 - Incomplete Screen Reader Attributes on Icon-only Action Buttons
**Learning:** Icon-only UI action buttons (like Delete/Trash) in the Underscore templates frequently rely solely on `title` attributes for text alternatives, which provides incomplete screen reader support across browsers compared to explicit `aria-label` attributes.
**Action:** When adding or auditing icon-only buttons in Underscore templates, always provide a properly quoted, translated `aria-label` alongside any `title` tooltips to ensure robust accessibility.
