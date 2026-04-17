## 2024-05-24 - Avoid N+1 queries from enrollment.course.id
**Learning:** In the Open edX codebase, `CourseEnrollment.course` is a `ForeignKey` to `CourseOverview` (or `Course`). Accessing `enrollment.course.id` without `select_related('course')` forces an implicit database query to fetch the related object just to get the ID.
**Action:** Always use the raw foreign key attribute `enrollment.course_id` instead of `enrollment.course.id` to prevent expensive N+1 queries in serializers and signals.
