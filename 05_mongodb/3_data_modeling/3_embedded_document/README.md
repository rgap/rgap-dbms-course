### Embedded Document — Realistic User Collection

This example represents a `users` collection that uses embedded documents to logically group related fields together, such as names and addresses.

🧱 **Fields**:

- `_id` _(string)_: Unique identifier.
- `username` _(string)_: Unique login or display name.
- `email` _(string)_: For contact and authentication.
- `fullName` _(object)_: Contains `first` and `last` name fields.
- `address` _(object)_: Contains `street`, `city`, `district`, and `zip`.
- `isVerified` _(boolean)_: Indicates account verification status.

📌 **Use Cases**:

- Ideal for representing grouped data that is always retrieved together.
- Useful when the structure of the grouped fields is predictable and stable.
- Appropriate when the grouped values are tightly bound to the parent document.

✅ **Advantages**:

- Keeps related data together in one document.
- Reduces the need for joins or lookups.
- Improves read performance for complete profiles.

🚫 **Limitations**:

- Less flexible when the grouped structure varies across documents.
- May lead to duplication if the embedded data is shared across multiple documents.
- Harder to update shared embedded data in bulk.
