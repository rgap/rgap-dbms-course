# 💥 Atomicity — All or Nothing

**Atomicity** is the principle that a transaction must either complete in full or have no effect at all. There is no "partial success" in a reliable database system.

---

## 📌 Real-World Analogy

Imagine withdrawing money from an ATM:

- You insert your card
- You request $100
- The system debits your account
- Then gives you cash

If the system debits your account **but crashes before giving the cash**, atomicity ensures that the **debit is undone** — either all steps succeed, or none.

---

## 💡 Formal Definition

> A transaction is **atomic** if it is indivisible:  
> either all its operations are executed, or none are.

Atomicity is enforced using:

- **Rollback logs**
- **Undo buffers**
- **Transaction boundaries** (`BEGIN`, `ROLLBACK`, `COMMIT`)

---

## 🚫 Without Atomicity

| Scenario                          | What Happens                     |
| --------------------------------- | -------------------------------- |
| Insert succeeds, then crash       | Partial data, inconsistent state |
| Multi-table update fails midway   | One table updated, others not    |
| Constraint violation after update | Database left in invalid state   |

---

## 📄 Demo Summary

We simulate a money transfer between two users:

- Decrease `Alice`'s balance
- Increase `Bob`'s balance

To ensure **atomicity**, both updates are wrapped in a SQL `BEGIN ... COMMIT` transaction block. If something fails, we roll back the entire transaction.

---

## ✅ Success Scenario

```sql
BEGIN;

UPDATE account SET balance = balance - 100 WHERE name = 'Alice';
UPDATE account SET balance = balance + 100 WHERE name = 'Bob';

COMMIT;
```

This transfers 100 from Alice to Bob.

---

## ❌ Failure Scenario

```sql
BEGIN;

UPDATE account SET balance = balance - 100 WHERE name = 'Alice';
UPDATE account SET balance = balance + (100 / 0) WHERE name = 'Bob'; -- force error

ROLLBACK;
```

In this case:

- The second line throws a division-by-zero error
- PostgreSQL aborts the transaction
- The `ROLLBACK` ensures **Alice’s balance is unchanged**

---

## 💡 Why This Proves Atomicity

| Guarantee      | Explanation                                            |
| -------------- | ------------------------------------------------------ |
| All-or-Nothing | Either both balances are updated, or none are          |
| Safe Failure   | If any operation fails, all changes are rolled back    |
| Manual Control | Uses `BEGIN`, `ROLLBACK`, `COMMIT` to manage atomicity |
