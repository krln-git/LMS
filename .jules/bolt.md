## 2024-05-28 - N+1 query issue when iterating over `CourseEnrollment.enrollments_for_user` and accessing `enrollment.course_overview`
**Learning:** Iterating over enrollments returned by `CourseEnrollment.enrollments_for_user(user)` and accessing the `.course_overview` property causes an N+1 query bottleneck because the `course_overview` instances are not pre-fetched.
**Action:** Use `CourseEnrollment.enrollments_for_user_with_overviews_preload(user)` instead when you need to access `course_overview` to prevent the N+1 query problem.
