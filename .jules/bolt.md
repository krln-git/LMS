## YYYY-MM-DD - Avoid N+1 Query in `CourseEnrollment.course`
**Learning:** Accessing `enrollment.course.id` instead of `enrollment.course_id` on standard querysets triggers an unnecessary N+1 database or Modulestore lookup because it evaluates the non-prefetched `course` ForeignKey.
**Action:** When extracting only the course identifier from `CourseEnrollment`, strictly use `enrollment.course_id`.
