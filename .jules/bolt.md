## 2024-05-24 - Avoid N+1 queries by accessing foreign key ID directly
**Learning:** Accessing `enrollment.course.id` triggers an N+1 query as it loads the full `course` object just to retrieve its ID.
**Action:** Always use the implicitly available foreign key id attribute like `enrollment.course_id` instead to retrieve the ID directly without database roundtrips.
