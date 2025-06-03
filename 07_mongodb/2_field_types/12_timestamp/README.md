### Timestamp Fields

The `Timestamp` type is a BSON internal type used by MongoDB primarily for replication and oplog entries. It consists of a Unix time value and an increment counter.

🧭 The "t" value is the Unix timestamp (in seconds), and "i" is an increment value used to order operations happening at the same second.

🧱 **Example Fields**:

- `_id`: A string ID for the record.
- `createdAt`: A BSON `Timestamp` with `t` (seconds since epoch) and `i` (operation order within that second).

📌 **Use Cases**:

- Internal MongoDB replication and oplog tracking.
- Situations where precise operation ordering is important.
- Tracking changes within the same second across distributed systems.

✅ **Advantages**:

- Uniquely identifies operation time and order.
- Useful in sharded cluster synchronization.
- Native to MongoDB’s internal architecture.

🚫 **Limitations**:

- Not meant for general user-facing date/time use (use `Date` instead).
- Not human-readable without decoding.
- Cannot be directly manipulated or formatted like standard dates.
