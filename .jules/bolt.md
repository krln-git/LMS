## 2024-05-24 - Optimize CourseCreator queries
**Learning:** Replaced an expensive `.count() == 0` check (which executes a full COUNT query) with `.exists()` (which is more efficient) and a `.first()` pattern.
**Action:** When checking if a QuerySet has items without needing to count them all, always use `.exists()`. For getting the first item or returning None if the QuerySet is empty, use `.first()` rather than checking `.count()` and indexing.
