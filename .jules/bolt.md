## 2024-05-25 - Avoid .count() == 0
**Learning:** Inefficient Django queries checking `.count() == 0` evaluate the whole queryset, or trigger a full COUNT query, when `.first()` or `.exists()` is more optimal.
**Action:** Always replace `.count() == 0` with `.exists()` for existence checks, or with `.first()` when the object is needed immediately, to reduce database queries.
