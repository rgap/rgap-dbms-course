### Nested Embedded Arrays — Realistic Project Collection

This example models a `projects` collection. Each project contains an array of embedded documents that represent tasks. Each task has its own fields and belongs to the project document.

🧱 **Fields**:

- `_id` _(string)_: Unique project identifier.
- `title` _(string)_: Project title or name.
- `owner` _(string)_: User ID of the project owner.
- `tasks` _(array of objects)_: Each object includes:
  - `title` _(string)_: Task name.
  - `assignedTo` _(string)_: User ID of the assignee.
  - `completed` _(boolean)_: Task status.

📌 **Use Cases**:

- Suitable for representing tightly coupled 1:N relationships inside a single document.
- Useful when subdocuments are only relevant in the context of the parent.
- Ideal when all information is always retrieved together.

✅ **Advantages**:

- Efficient when accessing the parent and its children in one operation.
- Simplifies storage when data is naturally hierarchical.
- Eliminates the need for external lookups for subitems.

🚫 **Limitations**:

- Document size can grow rapidly with many nested entries.
- Difficult to access or update a single nested item in isolation.
- Not ideal for unbounded or shared subdocument structures.
