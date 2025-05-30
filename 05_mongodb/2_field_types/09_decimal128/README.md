### Decimal128 Fields

Decimal128 is a high-precision numeric type designed for financial and scientific use cases that require exact decimal representation.

💡 This format is shown when exported from MongoDB — internally it's stored as a BSON Decimal128 type to maintain high precision.

🧱 **Example Fields**:

- `_id`: A string identifier.
- `product`: A string name of the item.
- `value`: A Decimal128 number used for precise financial value.

📌 **Use Cases**:

- Financial records (e.g., currency, tax, interest rates).
- Scientific measurements requiring high accuracy.
- Systems where floating-point precision loss is unacceptable.

✅ **Advantages**:

- Preserves exact values without floating-point rounding issues.
- Supports very large or very small decimal values.
- Compatible with many decimal-based calculations (e.g., accounting).

🚫 **Limitations**:

- Not as widely supported as basic numbers in external libraries.
- Slightly higher storage and computation cost.
- Must be explicitly declared or inserted using `$numberDecimal` in some drivers.
