## 📊 Database Modeling Process

```
[1] Real-World Requirements
     ↓
[2] Conceptual Model - ER Model
    - Describes entities and relationships
    - Usually represented using Entity-Relationship (ER) diagrams
     ↓
[3] Logical Model - Relational Model
    - Defines data as relations (tables) with:
      attributes, domains, primary keys, foreign keys, constraints
    - DBMS-independent (pure design)
     ↓
[4] Database Schema (or Schema)
    - Concrete implementation of the Relational Model
    - Specifies table names, column names, data types, keys, etc.
    - Written using SQL (e.g., `CREATE TABLE`)
    - It can be a Relational Schema or a Non-Relational Schema
     ↓
[5] Physical Model
    - How data is stored on disk: files, indexes, partitions, blocks
    - DBMS-specific optimizations
     ↓
[6] Database Instance
    - The actual data inside the tables at a given point in time
    - Changes frequently (inserts, updates, deletes)
```

---

## 📘 Database Schema (or Schema)

- The **schema** defines the **structure**: tables, columns, data types, constraints, relationships, etc.
- It is defined **once** and typically changes infrequently.

### Example:

```sql
CREATE TABLE Students (
  ID INT PRIMARY KEY,
  Name VARCHAR(50),
  Major VARCHAR(50)
);
```

✅ Describes what kinds of data will be stored  
✅ Enables consistency and validation

---

## 🏗️ Schema vs Instance in a DBMS

A fundamental concept in DBMS is understanding the **difference between a database's structure** and its **actual content at any point in time**. This distinction is captured in the terms **schema** and **instance**.

---

## 📗 Instance (Database State)

- An **instance** is the **actual content** of the database at a specific moment in time.
- It refers to the **current values** stored in tables.
- Changes frequently as records are inserted, updated, or deleted.
- Also called the **extension** of the database.

### Example:

```text
+----+--------+--------+
| ID | Name   | Major  |
+----+--------+--------+
| 1  | Alice  | CS     |
| 2  | Bob    | EE     |
+----+--------+--------+
```

✅ Represents live data  
❌ Not part of the database design itself

---

## 🧰 Summary Table

| Concept  | Description                          | Changes Over Time? |
| -------- | ------------------------------------ | ------------------ |
| Schema   | Structure/Design of the database     | Rarely             |
| Instance | Actual data stored at a given moment | Frequently         |
