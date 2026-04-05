
## 2024-05-15 - CourseEnrollment Modulestore N+1 bottleneck
**Learning:** Accessing `enrollment.course.id` triggers a severe N+1 Modulestore lookup bottleneck, because accessing the `.course` property fetches the full `CourseDescriptor` from the Modulestore, which is slow and memory-intensive.
**Action:** Always use `enrollment.course_id` (the raw `CourseKeyField`) when only the course identifier is needed.
