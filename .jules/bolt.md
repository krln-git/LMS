## 2024-05-24 - Optimize Django ORM existence and first-item checks
**Learning:** Found instances where `.count() == 0` is used for existence checks, and sometimes followed by an index access (e.g. `user[0]`). This triggers a `COUNT` query followed by a `LIMIT 1` query (or full query evaluation).
**Action:** Replace `.count() == 0` with `.exists()` when strictly checking for existence. When checking existence and subsequently accessing the first element, use `.first()` to combine both operations into a single query.
