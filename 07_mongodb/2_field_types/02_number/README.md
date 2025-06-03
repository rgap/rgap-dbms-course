### Number Fields

Number fields store numeric values such as integers and floating-point numbers.

🧱 **Example Fields**:

- `_id`: A string ID for the product.
- `name`: A string for the product name.
- `price`: A floating-point number representing the product cost.
- `stock`: An integer representing quantity available.

📌 **Use Cases**:

- Representing quantities, prices, scores, ratings, measurements, or percentages.
- Suitable for arithmetic operations and range comparisons.
- Common in product inventories, analytics, and billing systems.

✅ **Advantages**:

- Native support for arithmetic and comparison operators.
- Efficient for sorting and filtering.
- Supports decimal and integer types.

🚫 **Limitations**:

- Floats may have rounding issues (use Decimal128 for precision).
- Type mismatch can occur if values are stored as strings instead of numbers.
