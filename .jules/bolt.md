
## 2024-05-24 - Avoid N+1 queries when accessing ForeignKey IDs
**Learning:** In Django, accessing `enrollment.course.id` triggers a database lookup for the `CourseOverview` if the `course` relation isn't prefetched.
**Action:** Always use the raw database column attribute (e.g., `enrollment.course_id`) when only the identifier is needed to avoid unnecessary N+1 queries.
