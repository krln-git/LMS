## 2024-10-14 - Add SR text to icon-only buttons in CMS templates
**Learning:** While adding `aria-label` to the button element is common, in these `.underscore` templates adding an explicit `<span class="sr">...</span>` containing the translation tag alongside the icon is the established pattern for ensuring icon-only buttons are screen reader friendly.
**Action:** Always ensure that icon-only interactive elements in CMS templates use `<span class="sr">` tags with translated string tags when `<button>` title attributes are present but may not provide adequate screen-reader accessible names.
