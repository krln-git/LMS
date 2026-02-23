## 2024-05-22 - [XBlock Children Access]
**Learning:** XBlock `get_children()` instantiates all child blocks, which can be expensive (database/modulestore hits). XBlocks typically have a `.children` attribute containing a list of `UsageKey`s. When only needing child IDs (e.g., for position tracking), accessing `.children` directly avoids heavy instantiation.
**Action:** Always prefer `.children` (list of keys) over `.get_children()` (list of instances) when only metadata/IDs are needed. Check for attribute existence first for robustness.
