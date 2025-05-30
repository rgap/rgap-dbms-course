# 🧠 Foundations of Database Management Systems (DBMS)

This module introduces the **core theoretical foundations** of databases that influence their implementation and performance. Before diving into storage engines or indexes, we need to understand what makes a database system robust, consistent, and reliable.

---

| Topic Area             | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| **ACID Properties**    | Guarantees for reliable transactions in DBMS                |
| **Schema & Instance**  | Difference between structure and actual data                |
| **Data Models**        | Logical structure of databases (relational, document, etc.) |
| **Abstraction Levels** | Internal vs external view of DBMS                           |
| **Query Languages**    | Declarative vs procedural access to data                    |

---

## 🧩 Subfolders and Topics

### `1_core_concepts/`

- Explains how DBMS guarantees consistency using **ACID**
- Defines **schema**, **instance**, and **data independence**
- Describes **3-level architecture**: internal, conceptual, external

### `2_data_models/`

- Compares relational, key-value, document, graph models
- Introduces Entity-Relationship (ER) diagrams and schema design

### `3_query_languages/`

- SQL vs Relational Algebra
- Declarative vs Procedural query styles
- Basic query examples in `.sql`

---

## 📌 Why This Matters

These theoretical foundations are what separate databases from simple file storage:

- ACID ensures that your **bank transaction or medical record** is not lost or half-complete
- Schemas and models help us build **reliable, validated, and scalable** apps
- Understanding query languages helps design **efficient queries and indexes**

---

## 🧪 Outcome

By the end of this module, you’ll be able to:

- Explain why databases need strict consistency models
- Describe how different data models impact performance and use cases
- Understand how SQL is just one interface to a deeper data model

---

➡️ Next up: Let’s start with `1_core_concepts/` and learn what makes transactions safe in real-world databases.
