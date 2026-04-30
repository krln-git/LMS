
## 2026-04-30 - Prevent N+1 queries by using raw foreign key attributes
**Learning:** In Open edX, `CourseEnrollment.course` is a `ForeignKey` to `CourseOverview`. Using `enrollment.course.id` to access the course ID evaluates the related model, triggering an expensive N+1 database/Modulestore lookup if the course isn't prefetched.
**Action:** Use the raw foreign key attribute `enrollment.course_id` instead to access the ID directly without an extra query.
