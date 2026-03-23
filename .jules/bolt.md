
## 2024-05-14 - Replace .count() and len() with .exists()
**Learning:** Using .count() == 0 or len() != 0 for checking existence is inefficient because it triggers a SELECT COUNT(*) or fetches all matching rows into memory.
**Action:** Always use .exists() when only checking if any rows exist.
