# 💾 Atomicity Demo with PostgreSQL, Prisma, and Docker

This project demonstrates the **Atomicity** property of ACID in a real-world money transfer system. It uses:

- 🐘 PostgreSQL (via Docker) for reliable storage
- ⚙️ Prisma ORM (with explicit table mapping)
- 🚀 Express.js (Node.js) as the API layer

The goal is to show that **a transfer operation either fully succeeds (both accounts updated) or fully fails (no change at all)** — exactly what atomicity means.

---

## 📚 What Is Atomicity?

**Atomicity** ensures that **all operations in a transaction are treated as a single unit** — they either all succeed or none of them are applied.

In this case:

- If Alice sends Bob $100,
  - ✅ Alice’s balance must decrease by $100
  - ✅ Bob’s balance must increase by $100
- If either operation fails (e.g., Bob doesn’t exist),
  - ❌ **Neither account should be changed**

This is implemented using **Prisma’s `$transaction()`**, which wraps multiple operations into a single all-or-nothing database transaction.

---

## 📁 Project Structure

```txt
.
├── docker-compose.yml          # Starts PostgreSQL and seeds DB using init.sql
├── init-db/
│   └── init.sql                # SQL script that creates `account` table and seeds Alice & Bob
└── server/
    ├── .env                    # DB connection string
    ├── app.js                  # Express.js server entry point
    ├── package.json            # Dependencies (Prisma, Express, etc.)
    ├── prisma/
    │   └── schema.prisma       # Prisma model mapped to lowercase SQL table
    └── routes/
        └── accounts.js         # API routes to get accounts and transfer money
```

---

## ⚙️ Setup Instructions

### 1. 🐳 Start the PostgreSQL Database

This creates the `bankdb` database and initializes the `account` table.

```bash
docker compose up -d
```

> It uses `init-db/init.sql` to define the table and seed Alice and Bob.

---

### 2. 📦 Install Server Dependencies

```bash
cd server
npm install
```

---

### 3. 🔧 Generate the Prisma Client

```bash
npx prisma generate
```

> Prisma reads `schema.prisma`, which maps the `Account` model to the actual lowercase table:

```prisma
model Account {
  ...
  @@map("account")
}
```

---

### 4. 🚀 Start the API Server

```bash
nodemon app.js
```

Visit: [http://localhost:3001/api/accounts](http://localhost:3001/api/accounts)

You should see:

```json
[
  { "id": 1, "name": "Alice", "balance": 1000 },
  { "id": 2, "name": "Bob", "balance": 500 }
]
```

---

## 🔁 Transfer Route: Proving Atomicity

### Endpoint

```
POST /api/accounts/transfer
Content-Type: application/json
```

### Payload

```json
{
  "from": "Alice",
  "to": "Bob",
  "amount": 100
}
```

### Behavior

This executes:

```js
await prisma.$transaction([
  prisma.Account.update({
    where: { name: from },
    data: { balance: { decrement: amount } },
  }),
  prisma.Account.update({
    where: { name: to },
    data: { balance: { increment: amount } },
  }),
]);
```

- If **both succeed** → COMMIT ✅
- If **either fails** (e.g., Bob doesn’t exist) → ROLLBACK ❌

---

### 🔬 Test Failure (Rollback)

```json
{
  "from": "Alice",
  "to": "Charlie",
  "amount": 100
}
```

- Charlie doesn't exist → second update fails
- Alice’s balance **remains unchanged**
- Response:
  ```json
  {
    "success": false,
    "message": "No 'Charlie' found"
  }
  ```

---

## ✅ Why Atomicity Is Guaranteed

1. **Transaction Used**: Prisma’s `$transaction()` wraps both balance updates in a true SQL transaction.
2. **Rollback-on-Failure**: If either update fails (e.g. due to a constraint, bad name), Prisma automatically rolls back the entire transaction.
3. **PostgreSQL Reliability**: PostgreSQL enforces transactional semantics and ACID guarantees.
4. **Balance Constraints**: The schema has a `CHECK (balance >= 0)` to prevent invalid writes.

---

## 🧠 Summary

| Feature               | Description                                      |
| --------------------- | ------------------------------------------------ |
| 🔄 Transaction Safety | Ensures full transfer succeeds or fails entirely |
| 🔐 ACID: Atomicity    | No partial update; DB is never left inconsistent |
| 📦 Tech Stack         | PostgreSQL + Prisma + Docker + Express           |
