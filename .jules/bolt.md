## 2024-05-19 - Inefficient QuerySet Evaluation
**Learning:** Found an instance in Django where `len(User.objects.filter(...))` was used for a simple existence check. This forces the evaluation and loading of the entire queryset into memory.
**Action:** Always replace `len(QuerySet)` with `.exists()` when checking for the existence of records to prevent performance degradation and high memory usage.
