## 2024-03-07 - [DOM-based XSS via innerHTML]
**Vulnerability:** Untrusted API response (`message.detail`) was interpolated directly into an HTML template string and assigned to `.innerHTML` in `lms/static/js/student_account/enrollment.js`.
**Learning:** This exposes the application to DOM-based Cross-Site Scripting (XSS) if the backend returns unsanitized error messages containing malicious HTML/JS.
**Prevention:** Always use `.textContent` to inject untrusted data into the DOM dynamically. For template strings, only interpolate trusted data (like localized strings) into the `.innerHTML` payload.
