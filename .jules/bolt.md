## 2024-05-24 - QuerySet Optimization in CourseCreator views
**Learning:** In Django, using `.count() == 0` generates an explicit `COUNT` query which is inefficient if we only care about existence or retrieving the first element. We can use `.exists()` or `.first()` instead.
**Action:** Always prefer `.exists()` for existence checks and `.first()` when we need to check existence and retrieve the first element simultaneously.
