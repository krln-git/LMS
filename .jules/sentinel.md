## 2024-05-18 - Fix XSS Vulnerability in Enrollment Error Messages
**Vulnerability:** Cross-Site Scripting (XSS) in `lms/static/js/student_account/enrollment.js`.
**Learning:** `innerHTML` was used to inject an error message string directly into the DOM. Since the error message (`textContent`) came from `message.detail` (which could originate from server responses or user input), injecting it via `innerHTML` opens up a potential XSS vulnerability.
**Prevention:** Always use `textContent` to inject dynamically generated text or error messages into the DOM, avoiding `innerHTML` when the content can contain unescaped user input or variables.
