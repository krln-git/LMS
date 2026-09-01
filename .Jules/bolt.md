## 2024-05-13 - Replace QuerySet.count() == 0 with .exists() and .first()
**Learning:** In Django, using `.count() == 0` generates an unnecessary database COUNT query. When followed by an index fetch like `qs[0]`, it results in two queries. Replacing these with `.exists()` and `.first()` optimizes performance.
**Action:** Replace `.count() == 0` checks with `.exists()` for pure existence checks and `.first()` when retrieving the item immediately.
