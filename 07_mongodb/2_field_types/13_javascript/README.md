### JavaScript Code Fields

MongoDB supports a special BSON type to store executable JavaScript code. This can be used in server-side operations, such as MapReduce or `$where` clauses.

🧱 **Example Fields**:

- `_id`: Unique string identifier.
- `name`: A label for the function.
- `code`: A JavaScript function stored as code.

📌 **Use Cases**:

- Storing reusable JavaScript for use in `$where` queries or MapReduce jobs.
- Legacy systems that rely on in-DB logic.
- Documenting dynamic behavior or rules as part of the data.

✅ **Advantages**:

- Adds behavior to data when used carefully.
- Supports custom filters and transformation logic in aggregation and queries.
- Can be executed directly by the MongoDB engine.

🚫 **Limitations**:

- Not recommended for modern systems due to security and performance concerns.
- Cannot be indexed or easily debugged.
- Disabled in many environments (especially Atlas or production replicas).

🛑 **Note**: Use of JavaScript in the database is discouraged in favor of application-side logic or Aggregation Pipelines.
