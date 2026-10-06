## 2026-10-06 - Query anti-pattern
**Learning:** Using .count() == 0 and [0] index access causes an unnecessary COUNT query followed by an entire queryset evaluation. Also, variable shadowing can make these patterns confusing.
**Action:** Replace two-query anti-patterns with a single QuerySet.first() call, and use .exists() instead of .count() == 0 for pure existence checks. Always rename variables that shadow outer scope arguments during refactoring.
