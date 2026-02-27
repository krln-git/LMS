
## 2024-05-19 - N+1 Query in `DjangoXBlockUserStateClient.set_many`
**Learning:** The memory explicitly mentioned an N+1 query bottleneck in `DjangoXBlockUserStateClient.set_many` where it iterates over `block_keys_to_state` and executes `StudentModule.objects.get_or_create(...)` in a loop, rather than using bulk operations or prefetching.
**Action:** When updating multiple XBlock states for a user, use `bulk_create` / `bulk_update` or pre-fetch existing `StudentModule` rows, modify them in-memory, and save them more efficiently (or fallback to the loop).
