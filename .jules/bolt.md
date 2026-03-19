## 2024-11-20 - Optimize `can_show_verified_upgrade`
**Learning:** PartitionService initialization and `is_mode_upsellable` checks in `lms` are expensive operations that can trigger Modulestore access. We should avoid evaluating them on hot paths when cheaper DB checks can fail fast.
**Action:** Always prioritize cheaper checks (like `enrollment.is_active`, `enrollment.mode`, or `enrollment.upgrade_deadline`) before expensive calls like `is_mode_upsellable`.
