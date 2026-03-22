## 2024-07-25 - Avoid Modulestore Checks in Hot Paths
**Learning:** Functions like `is_mode_upsellable` that initialize `PartitionService` can hit the Modulestore, making them expensive. Executing them before cheap attribute checks like `enrollment.is_active` or `enrollment.upgrade_deadline` in hot paths (like checking if an upgrade is possible) causes unnecessary overhead.
**Action:** When evaluating complex conditions, always perform cheap attribute checks and database `exists()` checks first. Delay Modulestore-dependent functions or partition evaluations until absolutely necessary.

## 2024-07-25 - QuerySet Caching Pitfalls
**Learning:** Evaluating a QuerySet with `len(course_enrollment) != 1` caches the result in memory. Replacing it with `not course_enrollment.exists()` removes the cache. If the code immediately accesses the elements of `course_enrollment` afterwards (e.g. `course_enrollment[0]`), the `.exists()` check would cause an extra database query because the result isn't cached.
**Action:** Be careful when replacing `len()` with `.exists()`. Only do it if the elements of the QuerySet are NOT accessed immediately afterwards.
