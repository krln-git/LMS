## 2024-05-28 - Avoid N+1 Query in DjangoXBlockUserStateClient.set_many
**Learning:** `DjangoXBlockUserStateClient.set_many` iterates through `block_keys_to_state.items()` and performs a `get_or_create` for each block key. This causes an N+1 query problem, especially noticeable when saving states for many blocks simultaneously (e.g., in batch operations).
**Action:** Pre-fetch `StudentModule` instances using `self._get_student_modules` before iterating through the blocks to update, significantly reducing the number of database queries during batch updates.
