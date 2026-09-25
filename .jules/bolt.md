## 2025-02-20 - Replace count with exists and first in course_creators views
**Learning:** .count() == 0 check evaluates database count, which is inefficient. Using .exists() instead avoids this and QuerySet.first() replaces the two query anti-pattern of existence check followed by an index fetch.
**Action:** When checking for QuerySet existence, use .exists() instead of .count() == 0, and .first() instead of index lookup when existence check precedes an item return.
