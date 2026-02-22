## 2024-05-24 - Enterprise Modal A11y
**Learning:** Custom modal implementations often lack critical ARIA attributes (role="dialog", aria-modal="true", aria-labelledby, aria-describedby), making them inaccessible to screen reader users.
**Action:** When auditing modals, prioritize checking for these attributes and ensure proper focus management, especially when not using a standardized component library like Paragon.
