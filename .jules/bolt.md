## 2024-05-15 - N+1 overhead and model instantiation on CourseEnrollment
**Learning:** Accessing `enrollment.course.id` on an un-prefetched `CourseEnrollment` triggers severe N+1 overhead and unnecessary model instantiation.
**Action:** When querying `CourseEnrollment` to extract only the associated course identifiers, always use `.values_list('course_id', flat=True)` instead of iterating over standard querysets.
