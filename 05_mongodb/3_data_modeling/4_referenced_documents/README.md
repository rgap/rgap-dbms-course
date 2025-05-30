### Referenced Documents — Realistic Collection Design

This example separates data into two collections: `users` and `orders`. The `orders` documents reference the `users` documents using a foreign key (`userId`).

🧱 **Users Fields**:

- `_id` _(string)_: Unique identifier.
- `username` _(string)_: Used for login/display.
- `email` _(string)_: For contact and authentication.

🧱 **Orders Fields**:

- `_id` _(string)_: Unique identifier for the order.
- `userId` _(string)_: References the `_id` of the user.
- `total` _(float)_: Amount of the order.
- `createdAt` _(ISO string)_: Timestamp of the order.
- `status` _(string)_: Order status (e.g., shipped, delivered).

📌 **Use Cases**:

- Preferred when modeling one-to-many relationships between collections.
- Useful when referenced data may change independently or be shared across multiple documents.
- Appropriate for separating concerns and avoiding duplication.

✅ **Advantages**:

- Prevents data duplication.
- Enables clean, modular data models.
- Scales well for large datasets.

🚫 **Limitations**:

- Requires multiple queries or aggregation to combine related data.
- Slightly more complex than embedded models in terms of access patterns.
