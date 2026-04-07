## 2024-05-24 - N+1 Query on CourseEnrollment
**Learning:** Using enrollment.course.id triggers an N+1 database/Modulestore lookup because course is a ForeignKey to CourseOverview.
**Action:** Always use enrollment.course_id to access the foreign key identifier without triggering a prefetch.
