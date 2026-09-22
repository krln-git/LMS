## 2024-05-20 - Replace Django .count() == 0 anti-pattern
**Learning:** Using .count() == 0 generates an inefficient COUNT SQL query. When checking existence and immediately retrieving an item, it creates a two-query anti-pattern. Pure existence checks should use .exists(), and existence+retrieval should use .first().
**Action:** Always replace .count() == 0 with .exists() for existence checks, and use .first() to replace existence checks followed by index fetching.
