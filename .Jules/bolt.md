## 2024-05-15 - Django QuerySet count anti-pattern
**Learning:** Pure existence checks using QuerySet.count() == 0 are an anti-pattern as they evaluate a slow database COUNT query, and combining count checks with array index lookups creates a two-query anti-pattern when fetching single items.
**Action:** Always use QuerySet.exists() for pure existence checks to emit a faster EXISTS query, and replace two-query .count() + [0] index access patterns with a single QuerySet.first() call.
