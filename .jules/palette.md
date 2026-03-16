## 2024-05-24 - Dynamic ARIA expanded on Backbone Views
**Learning:** Legacy Backbone/jQuery views (like `FormView.js`) don't automatically sync DOM state with ARIA attributes. A common pattern is having generic toggle methods (like `toggleHelp`) that change `display` and icon classes but forget to update the corresponding `aria-expanded` attributes on the triggering element.
**Action:** When auditing legacy jQuery/Backbone views for accessibility, specifically look for generic toggle handlers and ensure they update `aria-expanded` correctly.
