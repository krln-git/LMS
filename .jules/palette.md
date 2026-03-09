## 2024-06-18 - Fix self-closing span tags in LMS Templates
**Learning:** Found several instances of decorative FontAwesome icons in Open edX templates implemented as self-closing tags (`<span class="icon fa fa-close" />`). This is invalid HTML and can cause confusing DOM parsing and accessibility output for screen readers.
**Action:** When working on Open edX templates, actively grep for `<span class="icon fa [a-zA-Z\-0-9 ]*" />` and replace them with properly closed `<span></span>` tags that include `aria-hidden="true"`.
