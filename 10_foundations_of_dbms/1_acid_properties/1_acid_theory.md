# 🔒 ACID Properties in Depth

In database systems, **ACID** is the gold standard for transaction reliability. Each letter represents a property that a DBMS must support to ensure data remains **consistent, safe, and usable** even under failure or high concurrency.

---

## 🧩 Breakdown of ACID

| Property        | Description                                           | Example Scenario                                              |
| --------------- | ----------------------------------------------------- | ------------------------------------------------------------- |
| **Atomicity**   | A transaction must be all-or-nothing.                 | Money transfer either debits AND credits, or neither happens. |
| **Consistency** | The DB must remain in a valid state before and after. | Schema rules, constraints, and relationships must hold.       |
| **Isolation**   | Concurrent transactions appear isolated.              | Alice edits profile while Bob changes password. No conflicts. |
| **Durability**  | Once committed, changes persist despite crashes.      | After power loss, you still see your last payment was saved.  |

---

## ✅ Why It Matters

Without ACID, you might face:

- Partial writes
- Dirty reads
- Corrupted data after a system crash
- Lost transactions in high concurrency apps

---

## 💡 Real DBMS Support

| DBMS           | Atomicity | Consistency | Isolation     | Durability    |
| -------------- | --------- | ----------- | ------------- | ------------- |
| PostgreSQL     | ✅        | ✅          | ✅ MVCC       | ✅ WAL        |
| MySQL (InnoDB) | ✅        | ✅          | ✅ Locks      | ✅ WAL        |
| SQLite         | ✅        | ✅          | ✅ Serialized | ✅ Journaling |

> Even lightweight DBMSs like SQLite implement ACID using **journals** and **locking mechanisms**.

---

## 🧪 Coming Up

In the next file `2_acid_sql_demo.sql`, you’ll test these properties in SQL using:

- BEGIN / COMMIT / ROLLBACK
- Violating constraints
- Simulating crash scenarios

➡️ After that, we’ll break down what each query is doing in `2_acid_sql_demo_explained.md`.
