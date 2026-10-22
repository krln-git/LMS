## 2023-10-24 - Avoid .count() == 0 for Existence Checks
**Learning:** Checking `.count() == 0` on Django querysets evaluates the entire query and count before subsequent list-index access (e.g. `[0]`) issues another query. This is a common anti-pattern that causes unnecessary database overhead.
**Action:** Always replace `.count() == 0` with `.exists()` for pure existence checks, or with `.first()` when the object is needed immediately to evaluate everything in a single DB trip.
