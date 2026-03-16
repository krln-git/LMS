## 2024-05-18 - [Django QuerySet `exists()` optimization]
**Learning:** Found several places where `len(QuerySet.filter(...)) != 0` and `QuerySet.filter(...).count() == 0` were used for existence checks. These execute unnecessary `COUNT(*)` or fetch all objects, leading to performance bottlenecks and N+1 query problems.
**Action:** Replaced them with `QuerySet.filter(...).exists()` which efficiently evaluates whether the queryset contains any rows.
