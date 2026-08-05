## 2024-05-18 - Avoid len() on QuerySets
**Learning:** In Django, using `len()` on a `.filter()` QuerySet forces the evaluation of the entire QuerySet and loads all results into memory. This is a common performance anti-pattern.
**Action:** Always use `.exists()` when checking for existence or `.count()` when only the number of items is needed.
