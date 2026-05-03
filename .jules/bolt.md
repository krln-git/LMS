## 2024-05-04 - [Avoid N+1 queries by using course_id]
**Learning:** Accessing the un-prefetched `CourseEnrollment.course` ForeignKey via `enrollment.course.id` triggers an expensive N+1 database/Modulestore lookup, as `.course` is a ForeignKey to `CourseOverview`.
**Action:** Always use the raw foreign key attribute `enrollment.course_id` when extracting just the course identifier without prefetching.
