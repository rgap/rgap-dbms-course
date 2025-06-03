### Array Fields

Array fields store ordered lists of values. Each array can contain elements of any type, including other arrays or objects.

🧱 **Example Fields**:

- `_id`: A string identifier.
- `username`: A string representing the user.
- `skills`: An array of strings listing the user's technical skills.

📌 **Use Cases**:

- Storing tags, categories, skills, or preferences.
- Representing 1:N relationships inside a document.
- Useful for items that vary in quantity between documents.

✅ **Advantages**:

- Allows multiple values in a single field.
- Can be indexed with multikey indexes for fast lookups.
- Flexible for both simple and complex nested structures.

🚫 **Limitations**:

- May complicate querying, especially for conditions on multiple elements.
- Hard to update individual items without rewriting the array.
- Can grow large quickly if not carefully bounded.
