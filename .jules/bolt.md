## 2024-05-14 - [N+1 query in dict values]
**Learning:** Changing a dictionary key from `obj.relation.id` to `obj.relation_id` does not prevent an N+1 query if `obj.relation` is still evaluated as the dictionary value.
**Action:** Always apply `.select_related('relation')` to the source QuerySet to resolve the root N+1 issue when resolving related objects in bulk.
