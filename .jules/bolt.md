## 2024-05-15 - Optimizing empty QuerySet checks
**Learning:** Replacing `.count() == 0` with `.first()` (when the object is needed immediately) or `.exists()` avoids evaluating the entire QuerySet or performing a COUNT query, which is a common performance bottleneck in Django.
**Action:** Always use `.exists()` for pure existence checks and `.first()` when the first object is required to reduce DB load.
