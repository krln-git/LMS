## 2024-05-24 - Avoid accessing enrollment.course.id in loops
**Learning:** Accessing `enrollment.course` in `CourseEnrollment` triggers a heavy Modulestore lookup because it's a `@property` that fetches the `CourseDescriptor`. When looping over enrollments, `enrollment.course.id` results in a massive N+1 bottleneck.
**Action:** Always use `.values_list('course_id', flat=True)` when only the course ID is needed from a `CourseEnrollment` queryset to bypass the Modulestore entirely.
