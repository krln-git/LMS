## 2024-05-24 - Django ORM Inefficiencies
**Learning:** Using `len(QuerySet) != 0` evaluates the entire queryset and loads all results into memory. Using `.count() == 0` is also inefficient as it executes a full `COUNT(*)` query when only a boolean existence check is needed.
**Action:** Always replace `len(QuerySet) != 0` or `.count() == 0` with `.exists()` for boolean checks, or `.first() is None` if the object is subsequently needed.
