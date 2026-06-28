## 2024-05-24 - Avoid len() on Unresolved QuerySets
**Learning:** Calling `len()` on an unresolved QuerySet (e.g., `len(User.objects.filter(email=...))`) is a severe performance anti-pattern because it forces the database to evaluate and load all matching records into memory. In this codebase, it was found in the email confirmation flow (`common/djangoapps/student/views/management.py`).
**Action:** Always use `.exists()` for efficient boolean existence checks, which executes a fast `EXISTS` SQL query instead of loading objects.
