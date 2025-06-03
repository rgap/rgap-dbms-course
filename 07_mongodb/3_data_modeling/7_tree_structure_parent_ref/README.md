### Tree Structure (Parent Reference) — Realistic Category Collection

This example shows how to model hierarchical relationships using parent references. Each document represents a node in a tree and stores the `_id` of its parent node.

🧱 **Fields**:

- `_id` _(string)_: Unique category identifier.
- `name` _(string)_: Name of the category.
- `parentId` _(string or null)_: ID of the parent category. `null` indicates a root node.

📌 **Use Cases**:

- Suitable for representing tree-like data such as categories, departments, or locations.
- Useful when relationships can be stored via references instead of nesting.
- Ideal for hierarchical navigation and recursive processing.

✅ **Advantages**:

- Simple to update or reparent nodes.
- Efficient for representing large and deep trees.
- Easy to maintain a flat collection of all nodes.

🚫 **Limitations**:

- Requires multiple queries or recursive processing to reconstruct the full tree.
- Lacks natural containment — cannot retrieve all children in a single read.
- Harder to visualize or traverse without application logic.

---

### 📚 Example Structure from categories.json

- **Electronics** (`cat_001`)
  - **Laptops** (`cat_002`)
    - **Ultrabooks** (`cat_003`)
    - **Gaming Laptops** (`cat_004`)
  - **Smartphones** (`cat_005`)
