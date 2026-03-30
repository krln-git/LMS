## 2024-05-18 - Defer expensive is_mode_upsellable check
**Learning:** The `is_mode_upsellable` function can be very expensive because it accesses Modulestore and partitions, while local properties like `enrollment.upgrade_deadline` and `enrollment.is_active` are extremely cheap.
**Action:** Always perform local attribute checks (especially in hot paths like `can_show_verified_upgrade`) before executing functions that might trigger database or remote service calls.
