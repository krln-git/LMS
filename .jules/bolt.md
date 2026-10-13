## 2024-05-24 - Optimizing Django Queries
**Learning:** Replace .count() == 0 with .exists() or .first() to prevent evaluating full QuerySets.
**Action:** Use .exists() for pure existence checks and .first() when the object is needed immediately.
