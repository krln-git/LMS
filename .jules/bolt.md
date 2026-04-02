## 2024-03-24 - [DjangoXBlockUserStateClient set_many N+1 issue]
**Learning:** In batch operations like `DjangoXBlockUserStateClient.set_many`, calling `get_or_create` inside a loop results in an N+1 query issue, causing poor performance.
**Action:** Resolve this by pre-fetching the existing `StudentModule` instances using `self._get_student_modules(username, list(block_keys_to_state.keys()))` and checking against the prefetched dict before calling `get_or_create`.
