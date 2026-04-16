## 2024-06-25 - Replace enrollment.course.id with enrollment.course_id to prevent N+1 queries
**Learning:** In Open edX, `CourseEnrollment.course` is a `ForeignKey` to `CourseOverview`, meaning accessing `.course.id` triggers an expensive N+1 query. To access just the course identifier without prefetching, use the raw foreign key attribute `enrollment.course_id` instead to avoid triggering an expensive N+1 database/Modulestore lookup.
**Action:** Replace all instances of `enrollment.course.id` with `enrollment.course_id` to prevent N+1 queries.
