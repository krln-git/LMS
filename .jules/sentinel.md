## Sentinel Journal

## 2024-05-18 - [Fix DOM XSS in Enrollment Error Message]
**Vulnerability:** A DOM-based Cross-Site Scripting (XSS) vulnerability was found in `lms/static/js/student_account/enrollment.js`. The `showMessage` function was dynamically injecting untrusted data from a JSON response (`textContent`) directly into the DOM using string interpolation inside an `.innerHTML` assignment.
**Learning:** This existed because modern ES6 template strings (backticks) make it easy to inadvertently interpolate variables directly into HTML strings without realizing that the DOM parser will execute any script tags within that variable if passed to `.innerHTML`. It's a common pattern when developers want to quickly template a UI component in pure JavaScript.
**Prevention:** When constructing HTML strings for `.innerHTML`, **never** interpolate untrusted data or API responses. Leave placeholders (e.g., empty spans) in the HTML string, query the element after injection, and safely set its content using `.textContent`.
