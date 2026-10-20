## 2024-05-15 - Inefficient QuerySet count() usage
**Learning:** Found instances of `.count() == 0` used for existence checks and prior to index access. This is an anti-pattern that triggers a slow COUNT query instead of an efficient LIMIT 1.
**Action:** Always replace `.count() == 0` with `.exists()` for pure existence checks, or `.first()` when the object is needed immediately to reduce DB load.
