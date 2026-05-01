1. **Refactor "Close" button** in `lms/templates/video.html` from a `<div>` to a native `<button>` element.
2. **Refactor "Copy" button** in `lms/templates/video.html` from a `<div>` to a native `<button>` element.
3. **Enhance toggle accessibility** by adding `aria-expanded` and `aria-controls` to the social share toggle button, and ensuring focus is managed in `xmodule/js/src/video/036_video_social_sharing.js` when the container is opened/closed.
4. Add `aria-label` to the close button for screen readers.
5. Add `aria-hidden="true"` to the FontAwesome icons inside the buttons so they are ignored by screen readers.
6. Verify changes using tests and formatters.
7. Submit the PR.
