## 2026-11-02 - Optimize existence check
**Learning:** Using `.count() == 0` in Django queries performs a SQL COUNT operation which is less efficient than `.exists()` for pure existence checks. This codebase uses it in a few places.
**Action:** Replace `.count() == 0` with `.exists()` (or `.first()` when object is needed) to reduce database load.
