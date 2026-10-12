## 2026-10-12 - Inefficient Django Query Patterns
**Learning:** Using `.count() == 0` followed by index access evaluates multiple queries and is slower than a single `.first()` query. Pure existence checks should use `.exists()` instead of `.count() == 0`.
**Action:** Always replace `.count() == 0` with `.exists()` for pure existence checks, and use `.first()` when the object is needed immediately to reduce DB queries.
