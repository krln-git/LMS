## 2024-05-24 - Optimize existence check in Course Creators view
**Learning:** QuerySet existence checks like `len() == 0` or `.count() == 0` evaluate the whole query. Always use `.exists()` to prevent unnecessary memory and processing load.
**Action:** proactively look for and replace `len(QuerySet) > 0` or `.count() == 0` with `.exists()`
