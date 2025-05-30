# 🧱 MongoDB Data Modeling: Design Strategies and Structures

Data modeling in MongoDB is a **crucial skill** that determines the performance, maintainability, and scalability of your application. This section explores the theoretical underpinnings of MongoDB's flexible schema, and how to use embedded documents or references depending on your needs.

---

## 🧠 What is Data Modeling?

Data modeling is the process of **defining how data is stored, accessed, and related** within a database system. Unlike traditional SQL systems where modeling follows strict normalization rules, MongoDB emphasizes **performance, developer experience, and flexibility**.

In MongoDB, we model **documents** instead of rows, and **collections** instead of tables.

---

## ⚙️ Schema Design in MongoDB

### Dynamic Schema

MongoDB does not enforce a schema by default, meaning each document in a collection can have different fields. This is known as a **schema-less** or **flexible schema** model.

### Schema Validation (Optional)

Since MongoDB 3.2, it's possible to enforce **document structure validation** using JSON schema rules.

---

## 🌳 Embedded Documents vs. Referenced Documents

MongoDB supports two core strategies for modeling relationships:

### 1. Embedded Documents

Data is nested inside the parent document. This is ideal for **one-to-few** or **containment** relationships.

Example:

```json
{
  "name": "John",
  "address": {
    "street": "Main St",
    "number": 123
  }
}
```

### 2. Referenced Documents

Data is stored in separate documents and linked using an `ObjectId` reference. Best for **one-to-many** or **many-to-many** relationships.

Example:

```json
{
  "name": "John",
  "address_ids": [ObjectId("..."), ObjectId("...")]
}
```

---

## ⚖️ When to Use Embedded vs Referenced

See `modeling_criteria.md` for a deeper discussion, but here’s a quick overview:

| Characteristic      | Embedded                    | Referenced                     |
| ------------------- | --------------------------- | ------------------------------ |
| Data size           | Small                       | Potentially large or unbounded |
| Update frequency    | Frequently updated together | Updated separately             |
| Read access pattern | Always read together        | Accessed independently         |
| Duplication of data | Acceptable                  | Should be minimized            |

---

## 🧱 Additional Design Considerations

- MongoDB limits document size to **16MB**.
- Use **ObjectId** for linking if referencing.
- Index fields that are used in queries.
- Avoid deep nesting when possible (>3 levels).
- Think in terms of **use cases**, not just normalization.
