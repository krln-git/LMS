
## 2024-05-09 - Video Sharing Menu Keyboard Accessibility
**Learning:** Custom UI toggles like the video share popover must manually manage focus returning to the trigger button when closed and moving inside when opened, and should use semantic `<button>` tags instead of `<div>`s for interactive icons.
**Action:** Always verify keyboard focus states and tab order when implementing custom interactive elements, and prefer semantic HTML tags.
