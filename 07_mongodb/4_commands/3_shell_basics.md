## 🚀 Mongosh

### 🔧 How to Access

```bash
mongosh
```

This launches an interactive shell connected to your local MongoDB server.

If installed via Docker, run:

```bash
docker exec -it <container_name> mongosh
```

When you start mongosh, it connects to the MongoDB instance and automatically uses the **test** database **by default**.

```sh
test> // this means you are currently operating in the 'test' database
```

This is similar to how:

- MySQL uses the **test** schema if nothing else is specified.
- PostgreSQL connects to the default database (like your username) if not provided.

### Show Databases

- `show dbs` to lists all databases
- MongoDB hides empty databases
- MongoDB only lists databases in **show dbs** if they contain at least one document in at least one collection.
- ✅ If a database has documents → it appears in show dbs
- ❌ If a database is empty (the **test** database) → it does not appear

### Switch to another database

- `use <dbName>` to switch to (or create) a database.
- If you use `use <dbName>` on a non-existent database, it will be created **only when data is inserted**.
- In MongoDB, you don’t "leave" a database like you exit a program. You switch to another database. MongoDB always keeps you in some database context.

---

## 📋 List of Basic Commands

| Command                       | Description                               |
| ----------------------------- | ----------------------------------------- |
| `show dbs`                    | Lists all databases                       |
| `use <dbName>`                | Switches to (or creates) a database       |
| `db.createCollection("name")` | Creates a new collection                  |
| `show collections`            | Lists collections in the current database |
| `db.collection.insertOne({})` | Inserts a single document                 |
| `db.collection.find()`        | Retrieves all documents                   |
| `db.collection.findOne()`     | Retrieves the first matching document     |
| `db.collection.updateOne()`   | Updates a single matching document        |
| `db.collection.deleteOne()`   | Deletes a single matching document        |

---

## 📌 Notes on Behavior

Mongo Shell uses **JavaScript syntax**, so you can declare variables, loops, and functions like a typical JS environment.

Example:

```js
const user = { name: "Maria", age: 27 };
db.users.insertOne(user);
```

---

## 🧪 Interactive Practice

Try these in your shell:

```js
show dbs
use testDB
show dbs
show collections
db.createCollection("students")
show dbs
db.students.insertOne({ name: "Juan", grade: 8 })
db.students.insertOne({ name: "Frank", grade: 10 })
db.students.find()
```
