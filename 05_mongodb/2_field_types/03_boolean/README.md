### Boolean Fields

Boolean fields store binary values: `true` or `false`. They are commonly used for flags and toggles.

🧱 **Example Fields**:

- `_id`: A string identifying the user.
- `username`: A string representing the user’s name.
- `isActive`: A boolean indicating if the account is active.
- `isAdmin`: A boolean indicating if the user has admin rights.

📌 **Use Cases**:

- Representing on/off states, user roles, visibility flags, or logical switches.
- Useful for filtering and condition-based logic.
- Common in user management, feature toggling, and status tracking.

✅ **Advantages**:

- Very lightweight and efficient.
- Ideal for binary conditions.
- Clear intent and easy to query.

🚫 **Limitations**:

- Only two possible values (true or false); can’t express additional states (e.g., “pending”).
- May need additional fields or enums if more than two states are required.
