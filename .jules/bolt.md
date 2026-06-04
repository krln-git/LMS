
## 2024-05-30 - Replace .count() == 0 with .first() and .exists()
**Learning:** Found an anti-pattern in Django querysets: checking `.count() == 0` followed by accessing `[0]` results in two database queries instead of one. Also, `.count() == 0` for basic existence check is slower than using `.exists()`.
**Action:** Always replace `.count() == 0` checks followed by indexing with `.first()`. Replace standalone `.count() == 0` existence checks with `.exists()`.
