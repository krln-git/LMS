## 2024-05-14 - Replace .count() == 0 with .exists() for performance
**Learning:** In Django, using `.count() == 0` for pure existence checks forces the database to scan the table to count rows. This is an inefficient anti-pattern.
**Action:** Always replace `.count() == 0` with `.exists()` when only checking if a record exists.
