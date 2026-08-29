## 2024-05-13 - Replace `count()` with `exists()`
**Learning:** Django querysets should use `.exists()` instead of `.count() == 0` when checking existence, as it is faster.
**Action:** Always check if a `.count()` is used purely for a boolean condition.
