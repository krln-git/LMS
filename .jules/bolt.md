## 2024-06-18 - [N+1 Query in enrollments_for_user]
**Learning:** `CourseEnrollment.enrollments_for_user(user)` does not prefetch the `course_overview` object. Accessing `enrollment.course_overview` in a loop over these enrollments causes an N+1 database query problem.
**Action:** Always use `CourseEnrollment.enrollments_for_user_with_overviews_preload(user)` when iterating enrollments that require access to `course_overview`.
