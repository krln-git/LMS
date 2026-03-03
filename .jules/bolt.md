## 2024-05-23 - Defer Expensive is_mode_upsellable Checks
**Learning:** `is_mode_upsellable` (and specifically `PartitionService` initialization) is an expensive operation in Open edX because it can trigger Modulestore access. We should avoid calling it when it is not needed.
**Action:** Always check cheaper, local properties of an `enrollment` (like `enrollment.is_active`, `enrollment.mode`, or `enrollment.upgrade_deadline`) in hot paths like `can_show_verified_upgrade` before falling back to `is_mode_upsellable`.
