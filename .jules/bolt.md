## 2024-11-06 - Replace .count() == 0 with .exists() or .first()
**Learning:** Checking if a QuerySet is empty by evaluating `.count() == 0` triggers an expensive SQL `COUNT(*)` query, and if you intend to fetch the result right after, it triggers two DB roundtrips.
**Action:** Replace `.count() == 0` with `.exists()` when only checking for existence, or `.first()` when retrieving the item.
