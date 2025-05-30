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

- If you use `use <dbName>` on a non-existent database, it will be created **only when data is inserted**.
- Mongo Shell uses **JavaScript syntax**, so you can declare variables, loops, and functions like a typical JS environment.

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
show collections
db.createCollection("students")
db.students.insertOne({ name: "Ana", grade: 8 })
db.students.find()
```

---

## 📁 Folder Contents

```
3_mongo_shell_basics/
├── README.md             # This file
├── mongo_commands.sh     # Shell script of example commands
└── notes.md              # Notes and behavior insights
```

➡️ Continue with: `mongo_commands.sh` to script these operations automatically.
