## 2026-09-20 - Optimize existence checks
**Learning:** Using `.count() == 0` is a performance anti-pattern in Django as it generates a `COUNT` SQL query. `.exists()` is more efficient.
**Action:** Use `.exists()` instead of `.count() == 0` or `.count() > 0` for QuerySet existence checks.
