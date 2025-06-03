### Polymorphic Documents — Realistic Collection

This example uses polymorphic documents: all records are stored in the same collection, but each one represents a different type and has different fields depending on that type.

🧱 **Fields**:

- `_id` _(string)_: Unique identifier.
- `type` _(string)_: Specifies the kind of animal (e.g., "Cat", "Dog", "Bird").
- Shared field: `name` _(string)_.

🔀 **Type-Specific Fields**:

- Cats: `breed`, `meows`, `indoor`
- Dogs: `breed`, `barks`, `trained`
- Birds: `species`, `canFly`, `vocabulary` (array)

📌 **Use Cases**:

- Appropriate for storing heterogeneous entities that share a base identity but differ in structure.
- Useful when entities belong to the same conceptual group but require different schemas.
- Ideal for modeling subtype hierarchies or product variations.

✅ **Advantages**:

- All related items live in one collection.
- Allows flexible and dynamic schemas.
- Works well for APIs or systems that must support multiple types uniformly.

🚫 **Limitations**:

- Inconsistent field presence across documents.
- Harder to validate and index due to schema variability.
- Risk of increasing query complexity and maintenance cost as more types are added.
