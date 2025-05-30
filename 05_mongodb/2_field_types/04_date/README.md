### Date Fields

Date fields store date and time information in ISO 8601 format or as native BSON `Date` objects in MongoDB.

🧱 **Example Fields**:

- `_id`: A unique string for the event.
- `title`: A string title of the event.
- `startDate`: A date indicating when the event begins.

📌 **Use Cases**:

- Representing timestamps for creation, updates, expiration, or scheduling.
- Essential for time-based filtering and ordering.
- Common in logs, calendars, billing cycles, and audit trails.

✅ **Advantages**:

- Native support for time-based queries and sorting.
- Stores both date and time with time zone awareness.
- Easily indexable for time-based performance optimization.

🚫 **Limitations**:

- Requires consistent format (e.g., UTC vs local time).
- JSON exports may need to be parsed back into Date objects in client apps.
- Incorrect string formatting may break parsing or querying.
