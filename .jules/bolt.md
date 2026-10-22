## 2024-05-24 - Optimize Django query performance
**Learning:** Replacing `.count() == 0` and subsequent index access with `.first()` reduces database queries, as does replacing pure existence checks with `.exists()`.
**Action:** Always prefer `.first()` when the object is needed immediately and `.exists()` for existence checks to reduce overhead.
