## 2024-05-18 - Avoid unnecessary count queries
**Learning:** In Django, using `.count() == 0` generates an expensive SQL COUNT query when a simple existence check is needed. When followed by retrieving the item, it results in a two-query anti-pattern.
**Action:** Use `.exists()` for existence checks. Use `.first()` when checking existence and immediately retrieving an item.
