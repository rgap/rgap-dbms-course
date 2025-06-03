### Null Fields

Null fields explicitly store the `null` value to represent missing, optional, or undefined data.

🧱 **Example Fields**:

- `_id`: A string identifier.
- `username`: A string representing the user.
- `phone`: A field explicitly set to `null` to indicate that a phone number is not available.

📌 **Use Cases**:

- Marking fields as intentionally empty or not yet provided.
- Differentiating between "unset" (missing) and "null" (known but empty).
- Designing flexible schemas with optional fields.

✅ **Advantages**:

- Makes optional fields explicit.
- Can be queried specifically using `{ field: null }`.
- Useful for form input placeholders and defaults.

🚫 **Limitations**:

- Must distinguish between `null` and missing fields (`{}` vs `{ field: null }`).
- Can be misinterpreted as deleted or absent data.
- Overuse may lead to ambiguous document states.
