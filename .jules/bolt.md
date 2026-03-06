## 2024-05-24 - Preload CourseOverviews for user enrollments
**Learning:** Iterating over `CourseEnrollment.enrollments_for_user(user)` in a loop and accessing `enrollment.course_overview` without preloading causes an N+1 query problem, as `course_overview` is lazily loaded.
**Action:** Use `CourseEnrollment.enrollments_for_user_with_overviews_preload(user)` when iterating over enrollments and accessing `course_overview` to preload the data in a single query.
