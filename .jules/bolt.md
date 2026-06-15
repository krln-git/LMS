## 2024-06-16 - Prevent len() on Django Querysets
**Learning:** Found usage of `len(User.objects.filter(...)) != 0` in `common/djangoapps/student/views/management.py`. Calling `len()` evaluates the queryset and loads everything into memory instead of doing a simple `COUNT` query.
**Action:** Always use `.exists()` for boolean existence checks instead of `len()` on unresolved querysets.
