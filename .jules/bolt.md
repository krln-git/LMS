## 2026-10-14 - Optimize course creator status check
**Learning:** The standard Django idiom for checking existence and retrieving the first matching element is `.first()` (which implicitly limits the query and returns `None` if empty), avoiding the anti-pattern of `.count() == 0` followed by array-indexing `[0]` which evaluates the whole QuerySet when indexing.
**Action:** When replacing `.count() == 0` existence checks where the object is immediately needed, always use `.first()`. Also ensure you don't shadow argument names when re-assigning variables.
