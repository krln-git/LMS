## 2024-05-20 - Avoid N+1 Queries with CourseEnrollment
**Learning:** Accessing `enrollment.course.id` on an un-prefetched `CourseEnrollment` object triggers an expensive N+1 database/Modulestore lookup. Using `.values_list('course_id', flat=True)` retrieves only the course identifier and significantly improves query performance.
**Action:** When querying `CourseEnrollment` to extract only the associated course identifiers, always use `.values_list('course_id', flat=True)`. Avoid iterating over standard querysets to access `enrollment.course.id`.
