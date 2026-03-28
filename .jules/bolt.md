## 2024-03-29 - Defer Modulestore operations
**Learning:** `PartitionService` initialization and `is_mode_upsellable` checks are expensive because they can trigger Modulestore access.
**Action:** Prioritize cheaper property checks (like `enrollment.is_active` and `enrollment.upgrade_deadline`) in hot paths before executing expensive, system-heavy operations.
