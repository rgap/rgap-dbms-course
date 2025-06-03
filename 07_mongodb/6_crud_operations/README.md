# 📚 MongoDB CRUD Operations: Theory and Practice

This module introduces MongoDB's basic operations for working with data: **Create**, **Read**, **Update**, and **Delete** — commonly known as **CRUD**. These are the core building blocks of nearly every application that interacts with a database.

---

## 🔍 What is CRUD?

CRUD stands for:

- **Create** – Add new documents to a collection.
- **Read** – Retrieve data from a collection.
- **Update** – Modify existing documents.
- **Delete** – Remove documents from a collection.

MongoDB performs all of these operations using JavaScript-like syntax via the Mongo Shell (`mongosh`) or drivers in other programming languages.

---

## 🧠 Key Concepts

| Term       | Definition                                                               |
| ---------- | ------------------------------------------------------------------------ |
| Document   | A single data record in MongoDB, expressed in BSON (similar to JSON).    |
| Collection | A group of related documents, similar to a table in SQL.                 |
| Database   | A container for collections.                                             |
| Field      | A key-value pair inside a document.                                      |
| Filter     | A query object used to match documents (e.g., `{ age: { $gt: 18 } }`).   |
| Projection | Specifies which fields to return in query results (e.g., `{ name: 1 }`). |

---

## ✍️ Create Operations

These operations insert new documents into a collection:

### ➕ `insertOne()`

Inserts a single document:

```js
db.users.insertOne({ name: "Carlos", age: 30 });
```

### ➕ `insertMany()`

Inserts multiple documents:

```js
db.users.insertMany([
  { name: "Ana", age: 25 },
  { name: "Luis", age: 35 },
]);
```

If the collection doesn’t exist, it will be created automatically.

---

## 📖 Read Operations

Used to retrieve documents from a collection:

### 🔍 `find()`

Retrieves multiple documents:

```js
db.users.find({ age: { $gt: 25 } });
```

### 🔍 `find()` with projection:

Return only selected fields:

```js
db.users.find({ age: { $gt: 25 } }, { name: 1 });
```

---

## ♻️ Update Operations

Used to modify existing documents:

### 🔄 `updateOne()`

Modifies one matching document:

```js
db.users.updateOne({ name: "Carlos" }, { $set: { active: false } });
```

### 🔄 `updateMany()`

Modifies all matching documents:

```js
db.users.updateMany({ active: true }, { $set: { active: false } });
```

### 🔁 `replaceOne()`

Replaces the entire document:

```js
db.users.replaceOne({ name: "Carlos" }, { name: "Carl", email: "carl@example.com" });
```

---

## 🗑️ Delete Operations

Used to remove documents:

### 🔴 `deleteOne()`

Deletes the first matching document:

```js
db.users.deleteOne({ name: "Ana" });
```

### 🔴 `deleteMany()`

Deletes all matching documents:

```js
db.users.deleteMany({ active: false });
```

---

## 🔒 Transaction Scope

All of these operations are **atomic at the document level**. This means that each individual insert, update, or delete operation affects one document completely or not at all.
