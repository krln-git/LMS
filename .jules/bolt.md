## $(date +%Y-%m-%d) - Prevent N+1 queries by using course_id instead of course.id
**Learning:** In Open edX, `CourseEnrollment.course` is a `ForeignKey` to `CourseOverview`, meaning accessing `.course.id` triggers an expensive N+1 database/Modulestore lookup if the relation wasn't prefetched.
**Action:** Use `.course_id` (the raw foreign key attribute) instead of `.course.id` to access the course identifier without triggering additional queries.
