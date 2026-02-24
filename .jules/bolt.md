## 2025-02-18 - Open edX Course Enrollment Optimization
**Learning:** `CourseEnrollment` in Open edX links to `CourseOverview` via `course` FK, and `CourseOverview` links to `CourseMode` via `modes` related name. This allows efficient prefetching.
**Action:** Use `CourseEnrollment.objects.select_related('course').prefetch_related('course__modes')` when needing mode details for multiple enrollments to avoid N+1 queries.
