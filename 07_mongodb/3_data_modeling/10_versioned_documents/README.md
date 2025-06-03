### Versioned Documents — Realistic Collection

This example models document versioning. Each version of a document is stored as a separate document with a shared `documentId` and an incremented `version` number.

🧱 **Fields**:

- `_id` _(string)_: Unique ID for each version (can include version tag).
- `documentId` _(string)_: Stable ID linking all versions of the same document.
- `version` _(integer)_: Sequential version number.
- `title` _(string)_: Title of the document.
- `content` _(string)_: Body text of that version.
- `timestamp` _(ISO string)_: When the version was created or published.

📌 **Use Cases**:

- Ideal for tracking changes to legal agreements, product documentation, and technical specs.
- Useful in systems that require edit history or rollback functionality.
- Suitable for content management and document approval workflows.

✅ **Advantages**:

- Preserves historical versions without overwriting data.
- Easy to query for latest or previous versions.
- Supports audit and compliance requirements.

🚫 **Limitations**:

- Can grow quickly with frequent edits.
- Requires logic to manage version consistency and retrieval.
- Not ideal if only the latest version matters.
