### String Fields

String fields store sequences of characters and are used for text-based data.

🧱 **Example Fields**:

- `_id`: A custom string used as a document identifier.
- `username`: A string representing a unique display or login name.
- `email`: A string storing a user's email address.

📌 **Use Cases**:

- Representing names, descriptions, addresses, messages, and emails.
- Useful for storing identifiers that aren't numeric (e.g., slugs, SKUs).
- Commonly used in text search and sorting.

✅ **Advantages**:

- Flexible and human-readable.
- Well-supported for indexing and full-text search.
- Easy to display and manipulate in applications.

🚫 **Limitations**:

- Sensitive to encoding and case sensitivity unless handled properly.
- May require normalization (e.g., lowercase, trimming) for consistent querying.
