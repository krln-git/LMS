## 2024-05-18 - Avoid two-query anti-patterns and COUNT queries for existence checks
**Learning:** In Django, using `.count() == 0` generates an inefficient COUNT query. Furthermore, checking `.count() == 0` and then indexing `[0]` on the QuerySet results in two separate database queries.
**Action:** Always use `.exists()` for simple existence checks. When checking existence and subsequently fetching the item, combine them using `.first()`, which fetches the item safely without raising an exception if it does not exist, executing only a single query.
