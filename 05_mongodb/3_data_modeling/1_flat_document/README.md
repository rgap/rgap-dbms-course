### Flat Document — Realistic User Collection

This example represents a typical `users` collection using flat documents (no nesting or arrays).

Each user document includes basic scalar fields, stored in a single level:

🧱 **Fields**:

- `_id` _(string)_: Unique identifier (could be ObjectId or custom).
- `username` _(string)_: Unique login or display name.
- `email` _(string)_: For contact and authentication.
- `firstName`, `lastName` _(string)_: Personal names.
- `age` _(int)_: Demographic use.
- `isActive` _(boolean)_: Account status.
- `signupDate` _(ISO string)_: Registration timestamp.

📌 **Use Cases**:

- Best for storing simple, independent attributes.
- Suited for read-optimized systems with predictable schemas.
- Useful when relationships or grouped data aren't needed.
