## 2025-02-18 - Avoid PartitionService initialization in hot paths
**Learning:** `PartitionService` initialization (and subsequent calls like `get_user_partition`) can be expensive as it may trigger Modulestore access if the course object is not fully pre-loaded.
**Action:** In high-traffic functions (like `can_show_verified_upgrade`), perform cheaper checks (like `enrollment.upgrade_deadline`) first to short-circuit and avoid unnecessary `PartitionService` instantiation.
