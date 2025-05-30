# 🧩 Consistency — Valid State Before & After

**Consistency** ensures that any transaction moves the database from one valid state to another, maintaining **rules**, **constraints**, and **relationships** defined in the schema.

---

## 🧠 What Makes a State "Valid"?

A valid database state means:

- All **data types** are correct (e.g., `price` must be a number).
- All **constraints** hold (e.g., `stock >= 0`).
- All **relationships** are intact (e.g., no orphaned foreign keys).

If a transaction **violates any rule**, it is **rejected** and the database remains unchanged.

---

## 📌 Real-World Analogy

📦 Warehouse System:

- Every product must have a **non-negative stock**.
- Prices must be **positive**.
- Each product must belong to a **valid category**.

If someone tries to insert a product with `-10` in stock, the database **rejects** the insert to stay consistent.

---

## 🔒 What Enforces Consistency?

- **Data types** (`INT`, `TEXT`, `NUMERIC`)
- **Constraints**:
  - `CHECK (stock >= 0)`
  - `UNIQUE(name)`
  - `NOT NULL`
  - `FOREIGN KEY (category_id)`
- **Triggers or stored procedures** (optional advanced logic)

---

## 🚫 Without Consistency

| Violation                | Result                |
| ------------------------ | --------------------- |
| `NULL` in `NOT NULL`     | Rejects the operation |
| Negative in `CHECK` rule | Rejects the operation |
| Missing FK reference     | Rejects the operation |

---

## ✅ Summary

| Term          | Meaning                                  |
| ------------- | ---------------------------------------- |
| Consistent DB | All constraints and schema rules hold    |
| Transaction   | Must respect all rules, or it is aborted |
| Enforced by   | DB schema, not just application logic    |

Consistency ensures that even in failure, the database **never becomes corrupted**.
