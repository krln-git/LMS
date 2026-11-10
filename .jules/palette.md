## 2024-11-10 - Screen Reader Text for Icon-Only Buttons
**Learning:** Found several destructive actions (e.g., delete buttons) in CMS UI templates that are icon-only without explicit ARIA labels or screen-reader accessible spans, making them inaccessible.
**Action:** Ensure that all icon-only buttons include a visually hidden span with screen-reader text (`<span class="sr">...</span>`) or an `aria-label`.
