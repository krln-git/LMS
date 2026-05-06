## 2024-05-24 - Avoid N+1 Query on CourseEnrollment.course.id
**Learning:** In Open edX, `CourseEnrollment.course` is a `ForeignKey` to `CourseOverview`. If you iterate over enrollments and access `enrollment.course.id` without `select_related('course')`, it triggers an N+1 database/Modulestore lookup which is severely expensive.
**Action:** Replace `enrollment.course.id` with `enrollment.course_id` to directly access the raw foreign key attribute, resolving the N+1 issue without requiring a full prefetch when only the identifier is needed.

## 2024-05-24 - Avoid N+1 Query on CourseEnrollment.course.id
**Learning:** In Open edX, `CourseEnrollment.course` is a `ForeignKey` to `CourseOverview`. If you iterate over enrollments and access `enrollment.course.id` without `select_related('course')`, it triggers an N+1 database/Modulestore lookup which is severely expensive.
**Action:** Replace `enrollment.course.id` with `enrollment.course_id` to directly access the raw foreign key attribute, resolving the N+1 issue without requiring a full prefetch when only the identifier is needed.
