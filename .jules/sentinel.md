## 2024-03-28 - XSS in XBlock Iframe View Name
**Vulnerability:** A template variable `{{ view_name }}` was rendered directly into a `<script>` block using the `|safe` filter, opening the potential for Cross-Site Scripting (XSS) if a user could control `view_name`.
**Learning:** Even though `view_name` might currently be hardcoded or internally generated, using `|safe` inside JavaScript string literals breaks the defense-in-depth principle. A change in routing or logic could easily introduce XSS.
**Prevention:** Always use the `|escapejs` filter when rendering variables inside `<script>` tags, especially strings.
