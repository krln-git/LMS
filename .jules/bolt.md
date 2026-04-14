## 2024-04-14 - Expensive Modulestore lookup on CourseEnrollment
**Learning:** Accessing `enrollment.course.id` triggers an expensive N+1 Modulestore lookup for `CourseOverview`. Using the raw foreign key attribute `enrollment.course_id` prevents this.
**Action:** Always use `course_id` on enrollment objects to get the course identifier without triggering additional queries.
