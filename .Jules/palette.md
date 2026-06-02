## 2024-06-02 - Missing ARIA Labels on CMS Action Icons
**Learning:** Action icons in CMS Underscore templates (like `.delete.action-icon`) systematically rely solely on the `title` attribute for screen readers, which is insufficient for robust accessibility across browsers. They lack `.sr` spans or `aria-label`s.
**Action:** Always verify that `.action-icon` buttons in Underscore templates explicitly include `aria-label="<%- gettext('...') %>"` along with `title` to guarantee accessibility without relying on tooltip behaviors.
