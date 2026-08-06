## 2024-10-18 - Avoid evaluating entire QuerySets and count() when exists() suffices
**Learning:** Found multiple instances where Django querysets were evaluated using `len(queryset) != 0` or `.count() == 0` just to check for existence. This evaluates the whole queryset and is unperformant.
**Action:** Use `.exists()` instead of `len()` or `.count() == 0` to check for existence, preventing entire result sets from being loaded into memory or doing full table counts.
