## 2024-05-06 - Avoid N+1 queries by using raw foreign key attributes
**Learning:** In Open edX, CourseEnrollment.course is a ForeignKey. Iterating over querysets and accessing enrollment.course.id triggers an N+1 Modulestore lookup. Using .values_list('course_id', flat=True) avoids unnecessary model instantiation.
**Action:** Use .values_list('course_id', flat=True) to extract identifiers without prefetching.
