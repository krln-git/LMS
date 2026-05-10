## 2024-05-11 - Fixed FontAwesome Accessibility for Links
**Learning:** Found an accessibility issue where FontAwesome icons within links/buttons on forms lacked the `aria-hidden="true"` attribute. When decorative icons like caret-right are missing `aria-hidden="true"`, screen readers may attempt to read out unhelpful characters.
**Action:** Always ensure that decorative FontAwesome icons (`<i class="fa ..."></i>`) have `aria-hidden="true"` so they are properly skipped by screen readers.
