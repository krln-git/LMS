## 2026-04-29 - Prevent N+1 query in signals.py
**Learning:** In Open edX, accessing un-prefetched ForeignKeys like `enrollment.course.id` triggers expensive Modulestore lookups.
**Action:** Use the raw foreign key attribute `enrollment.course_id` instead.
