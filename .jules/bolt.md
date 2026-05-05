## 2024-05-18 - Avoid N+1 Modulestore Lookups with CourseEnrollment
**Learning:** In Open edX, accessing `enrollment.course.id` triggers an expensive N+1 Modulestore/database lookup because the un-prefetched `.course` ForeignKey evaluates the `CourseOverview` model unnecessarily.
**Action:** Always use `.values_list('course_id', flat=True)` when only extracting course identifiers, or use the raw foreign key attribute `enrollment.course_id` if the enrollment object is already instantiated, to prevent severe N+1 overhead.
