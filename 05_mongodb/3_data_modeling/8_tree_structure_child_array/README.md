### Tree Structure (Child Arrays) — Realistic Category Collection

This example models hierarchical relationships using nested arrays. Each document embeds its child categories directly within a `subcategories` field.

🧱 **Fields**:

- `_id` _(string)_: Unique identifier for the root category.
- `name` _(string)_: Name of the category.
- `subcategories` _(array)_: List of embedded child categories, which may themselves contain more `subcategories`.

📌 **Use Cases**:

- Useful when the full tree or subtree is often accessed together.
- Suitable for small to moderately sized hierarchies that don’t change frequently.
- Appropriate when categories are tightly coupled and don’t need to be referenced elsewhere.

✅ **Advantages**:

- Entire hierarchy can be loaded in a single read.
- Simple structure for rendering navigational menus.
- Good for scenarios where nested relationships are static or bounded.

🚫 **Limitations**:

- Difficult to update or move a single nested node.
- Larger trees can hit MongoDB’s 16MB document size limit.
- Cannot efficiently query deeply nested items independently.

---

### 📚 Example Structure from categories_nested.json

- **Electronics**
  - **Laptops**
    - **Ultrabooks**
    - **Gaming Laptops**
  - **Smartphones**
