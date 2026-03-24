## 2026-03-24 - Short-circuit expensive is_mode_upsellable checks
**Learning:** PartitionService initialization and is_mode_upsellable checks in lms are expensive operations that can trigger Modulestore access.
**Action:** Prioritize cheaper checks (like enrollment.is_active, enrollment.mode, or enrollment.upgrade_deadline) in hot paths to avoid unnecessary execution.
