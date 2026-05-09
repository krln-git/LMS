## 2024-05-23 - Prevent model hydration overhead when fetching values
**Learning:** When retrieving only specific fields like course identifiers from querysets (e.g., `CourseEnrollment`), iterating over full model objects incurs significant memory and processing overhead due to Django model hydration.
**Action:** Always use `.values_list('course_id', flat=True)` on the queryset when only the specific column values are needed. This prevents the heavy overhead of instantiating full model instances.
