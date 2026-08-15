## 2024-05-24 - Optimize Django QuerySet existence checks
**Learning:** Replacing `len(QuerySet) > 0` or `QuerySet.count() > 0` with `QuerySet.exists()` avoids evaluating entire QuerySets in memory or issuing a `COUNT` query, which is a common anti-pattern in Django that causes performance degradation.
**Action:** Proactively replace existence checks using `.count()` or `len()` with `.exists()` when looking for performance improvements in Django codebases.
