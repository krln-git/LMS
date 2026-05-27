## 2024-05-24 - Optimize Django Database Queries
**Learning:** Using `.count() == 0` followed by index access triggers two DB queries (COUNT and LIMIT 1). It is an anti-pattern.
**Action:** Replace `.count() == 0` + index access with `.first()` for combined retrieval, and replace standalone `.count() == 0` checks with `.exists()`.
