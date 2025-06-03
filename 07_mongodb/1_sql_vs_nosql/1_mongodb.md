## 🔍 MongoDB

**MongoDB** is a high-performance, open-source, NoSQL database designed to store and manage document-oriented information. It uses a **flexible schema**, storing data as BSON (Binary JSON) documents inside **collections** rather than rows in tables.

MongoDB was originally developed in 2007 while working at a company called **10gen**, which later became **MongoDB Inc**. The first public release came in February 2009, and the project quickly gained popularity due to its ease of use, horizontal scalability, and strong support for modern web apps.

MongoDB = Document Store + Horizontal Scaling + JavaScript-Like Queries

---

## 🧬 Key Concepts Recap

- **Database** → holds many **collections**
- **Collection** → holds many **documents**
- **Document** → JSON-like structure with fields and values (flexible, not rigid)

Example document:

```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "orders": [123, 456],
  "address": {
    "street": "Main St",
    "number": 123
  }
}
```

---

## 🕰️ Historical Context of NoSQL and MongoDB

| Year  | Event                                                               |
| ----- | ------------------------------------------------------------------- |
| 1970  | Codd introduces Relational Model (RDBMS)                            |
| 2006  | Cloud-native architectures grow; flexibility needed                 |
| 2007  | MongoDB created by 10gen                                            |
| 2009  | NoSQL movement gains momentum                                       |
| 2010s | Big data, mobile, and agile boost NoSQL usage                       |
| 2020s | MongoDB offers Atlas (cloud), ACID support, full-stack integrations |

---

## 🧪 When Do You Need a Database at All?

Ask yourself:

- Do I need to store data **long-term**?
- Does the data need to be **queried** or **searched**?
- Will multiple **users or systems** need access to the same data?

If the answer is yes to any of these, you probably need a database.

---

## ❓ When to Use MongoDB

MongoDB is an excellent choice when:

- Your data is **semi-structured** or frequently changing.
- You need **high write throughput** (e.g., logging, sensor data).
- You want to embed related data within documents for performance.
- Your dev team is familiar with JavaScript or JSON.
- You want to **scale horizontally** in a distributed system.
- Your app fits a microservices or serverless architecture.

🛑 Don’t use MongoDB if:

- You need many **complex JOINs** or **cross-document ACID** guarantees.
- You require **strong schema enforcement**.
- You're working on **traditional enterprise apps** like ERPs with heavy relational logic.
