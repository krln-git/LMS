## 2024-05-18 - Avoid N+1 Query on CourseEnrollment.course.id
**Learning:** In Open edX, `CourseEnrollment.course` is a `ForeignKey` to `CourseOverview`. Accessing `enrollment.course.id` without prefetching triggers an expensive N+1 database/Modulestore lookup.
**Action:** Always use the raw foreign key attribute `enrollment.course_id` instead of `enrollment.course.id` when only the course identifier is needed.
