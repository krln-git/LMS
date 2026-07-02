## 2024-07-02 - Use .exists() instead of .count() == 0 for Existence Checks
**Learning:** In Django, evaluating `.count() == 0` is inefficient because it triggers a full `COUNT(*)` query on the database.
**Action:** Replace `.count() == 0` (or `len(...) != 0`) with `.exists()` for efficient boolean existence checks, which performs an `EXISTS` SQL query and stops at the first match.
