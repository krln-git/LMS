## 2025-05-15 - Optimizing Content Inspection
**Learning:** The `XBlockContentInspector` performs multiple full-string scans on potentially large HTML content to detect dependencies like MathJax. This is inefficient for the common case where these dependencies are absent.
**Action:** Use fast-path checks (e.g., checking for specific characters like `\` or `[`) to avoid expensive loops and substring searches when possible.
