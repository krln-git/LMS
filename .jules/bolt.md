## 2024-05-20 - Optimize count() == 0 checks in Django
**Learning:** Inefficient use of `.count() == 0` for existence checks or before indexing adds overhead. `user.count() == 0` was shadowing the function parameter `user`.
**Action:** Use `.exists()` for pure existence checks and `.first()` when the object is needed immediately to reduce DB load. Always resolve variable shadowing for clarity.
