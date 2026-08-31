## 2024-05-18 - Avoid using `.count() == 0` for querysets in Django
**Learning:** In Django, using `.count() == 0` triggers a potentially expensive COUNT query on the database. It is much more efficient to use `.exists()` to check for the presence of records.
**Action:** When checking if a queryset is empty, use `.exists()` instead of checking the `.count()`. If you need the item, use `.first()` instead of checking `.count() > 0` and then indexing into the list.
