## 2024-05-24 - Add ARIA Labels to Video Transcript Feedback Buttons
**Learning:** Found icon-only buttons for thumbs up/down without ARIA labels, making them inaccessible to screen readers.
**Action:** Always add descriptive `aria-label`s to icon-only buttons and set `aria-hidden="true"` on the child icon elements.
