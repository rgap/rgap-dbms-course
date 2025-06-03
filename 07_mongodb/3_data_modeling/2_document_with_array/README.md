### Document with Array — Realistic User Collection

This example represents a `users` collection where each document includes one or more array fields. Arrays are used to list multiple values under a single logical attribute.

🧱 **Fields**:

- `_id` _(string)_: Unique identifier.
- `username` _(string)_: Unique login or display name.
- `email` _(string)_: For contact and authentication.
- `skills` _(array of strings)_: List of capabilities or proficiencies.

📌 **Use Cases**:

- Appropriate for storing multiple values that belong to a single category.
- Useful when representing lists that vary in length across documents.
- Suitable for static or semi-dynamic collections of items.
