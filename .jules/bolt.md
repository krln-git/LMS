## 2024-05-24 - N+1 overhead with Django ForeignKeys to un-prefetched models
**Learning:** Accessing `enrollment.course.id` on an un-prefetched ForeignKey triggers an expensive database and Modulestore lookup for the `course` model, causing N+1 query problems.
**Action:** Always use the raw foreign key attribute like `enrollment.course_id` instead of `enrollment.course.id` to access just the identifier without triggering a fetch.
