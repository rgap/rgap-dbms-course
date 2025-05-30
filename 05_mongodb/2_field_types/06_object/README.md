### Object Fields

Object fields (also called embedded documents) contain nested key-value pairs grouped together under a single field.

🧱 **Example Fields**:

- `_id`: A string identifier.
- `username`: A string representing the user.
- `profile`: An embedded document containing:
  - `firstName`: The user’s given name.
  - `lastName`: The user’s surname.

📌 **Use Cases**:

- Organizing logically grouped data such as names, addresses, settings, or metadata.
- Structuring subdocuments that are always retrieved with the parent.
- Modeling simple 1:1 relationships within a single document.

✅ **Advantages**:

- Keeps related data together and easy to access.
- Reduces the need for joins or references.
- Supports indexing on nested fields.

🚫 **Limitations**:

- Cannot share embedded documents across other documents.
- Updating deeply nested fields can require precise targeting.
- Deep nesting can impact document size and complexity.
