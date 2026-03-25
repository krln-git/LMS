
## 2024-05-28 - [Resolved N+1 Queries in get_financial_aid_courses]
**Learning:** Evaluating `enrollment.course_overview` inside loops triggers N+1 queries because it loads the `CourseOverview` model lazily. In addition, iterating `CourseMode.objects.filter` inside a loop for each enrollment compounds the performance bottleneck.
**Action:** Always use `CourseEnrollment.enrollments_for_user_with_overviews_preload(user)` (which handles `.select_related('course')`) when course overviews are needed in loops. For related models like `CourseMode`, pre-fetch the data using an `__in` filter before entering the loop.
