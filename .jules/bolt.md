## 2024-04-07 - N+1 query via ForeignKey property access in CourseEnrollment
**Learning:** Accessing `enrollment.course.id` on a standard QuerySet of CourseEnrollment triggers severe N+1 overhead. In Open edX, `.course` is a ForeignKey to `CourseOverview`, so accessing it forces a Modulestore lookup. Even accessing the ID via the relation triggers this.
**Action:** Always use `.values_list('course_id', flat=True)` when only the course identifier is needed, or explicitly use `enrollment.course_id` (the raw foreign key attribute) instead of `enrollment.course.id`.
