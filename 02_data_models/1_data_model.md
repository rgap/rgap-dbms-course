# 📙 Data Models in DBMS

A **data model** is a conceptual framework that determines how data is organized, stored, and manipulated in a DBMS. It defines the logical structure of the database and the way data is accessed.

A data model defines what data means and how it’s related.
A database model defines how that data is physically stored and accessed.

## 🎩 Data Model vs Database Model

| Term           | Data Model                                         | Database Model                                          |
| -------------- | -------------------------------------------------- | ------------------------------------------------------- |
| **Definition** | An **abstract design pattern** for organizing data | A **concrete implementation** of that pattern by a DBMS |
| **Purpose**    | Conceptual framework (design/logic)                | Operational engine (execution/storage)                  |
| **Scope**      | Used by architects and designers                   | Used by developers and DBMS vendors                     |
| **Examples**   | Relational model, Document model, Graph model...   | MySQL (relational), MongoDB (document), Neo4j (graph)   |

---

## 📚 Why Are Data Models Important?

- Define how **real-world entities** are represented digitally.
- Serve as a blueprint for **database design** and **query formulation**.
- Allow consistency and clarity in data interpretation.

---

## 🧱 Types of Data Models

### 1. **Hierarchical Model (Introduced in the 1960s)**

- Organizes data in a **tree-like structure**.
- Each child has **one parent**, but parents can have many children.
- First implemented in IBM’s Information Management System (IMS) in 1968.

**Example**:

```
Company
├── Department A
│   └── Employee 1
└── Department B
    └── Employee 2
```

✅ Fast access to hierarchical data  
❌ Rigid structure, difficult to reorganize

---

### 2. **Network Model (Developed in late 1960s)**

- Data is represented as **graphs**, with records connected through **pointers**.
- Supports **many-to-many** relationships.
- Standardized by the CODASYL consortium in 1971.

**Example**: An employee may work in multiple projects.

✅ Flexible connections  
❌ Complex to maintain

---

### 3. **Relational Model (Proposed in 1970 by E. F. Codd)**

- Organizes data in tables (relations).
- Uses rows (tuples) and columns (attributes).
- Relationships managed through keys.
- Became mainstream in the 1980s with the rise of SQL-based RDBMS like Oracle, DB2, and later MySQL.

**Example**:

```sql
Table: Students
+----+--------+-------+
| ID | Name   | Major |
+----+--------+-------+
| 1  | Alice  | CS    |
| 2  | Bob    | EE    |
+----+--------+-------+
```

✅ Simplicity, SQL support, high adoption  
✅ Data independence  
❌ Performance overhead for highly connected data

---

### 4. **Entity-Relationship (ER) Model (Introduced in 1976 by Peter Chen)**

- Visual design model based on **entities**, **attributes**, and **relationships**.
- Usually used for database design before creating tables.

**Symbols**:

- Entities → Rectangles
- Attributes → Ovals
- Relationships → Diamonds

✅ Intuitive for planning  
❌ Needs translation into relational schema

**🔄 Difference from the Relational Model:**

- The **ER Model** is an **abstract design tool**, focused on **visual planning** of real-world entities and their interactions.
- The **Relational Model** is a **logical implementation model** that uses **tables, keys, and constraints** to store and query data.
- ER models typically **precede** relational models in the design lifecycle — once finalized, they are translated into **relational schemas**.

---

### 5. **Document Model (Popularized with NoSQL in the 2000s)**

- Data stored as documents (e.g., JSON, BSON).
- Each document is self-describing and can have nested structures.
- Widely adopted with the rise of MongoDB (2009) and CouchDB (2005).

**Example**:

```json
{
  "id": 1,
  "name": "Alice",
  "courses": ["DBMS", "AI"]
}
```

✅ Flexible schema, ideal for unstructured data  
❌ Limited query consistency across documents

---

### 6. **Key-Value Model (Adopted widely in 2000s for scalability)**

- Simple mapping of keys to values.
- Great for caching, session stores, and real-time data.
- Used in systems like Redis (2009), DynamoDB (2012), and Riak.

**Example**:

```
"user:1" → { "name": "Alice", "email": "a@example.com" }
```

✅ Fast access  
❌ Poor support for complex queries

---

## 🧠 Summary Table

| Model        | Structure | Use Case                    | First Introduced |
| ------------ | --------- | --------------------------- | ---------------- |
| Hierarchical | Tree      | XML, LDAP                   | 1960s (IMS 1968) |
| Network      | Graph     | Telecom, Engineering        | 1970s (CODASYL)  |
| Relational   | Tables    | Business, ERP, CRM          | 1970 (Codd)      |
| ER Model     | Diagram   | Conceptual database design  | 1976 (Chen)      |
| Document     | JSON/BSON | Web apps, content storage   | 2000s (NoSQL)    |
| Key-Value    | Dict/Map  | Caching, session management | 2000s            |
