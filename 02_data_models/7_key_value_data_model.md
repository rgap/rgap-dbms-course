# 🔑 Realistic Example: Key-Value Data Model

## 🌐 Use Case: User Session Storage in Web Applications

A web app needs to store temporary data for logged-in users — like cart contents, authentication tokens, or preferences — quickly and efficiently. This is ideal for a **key-value model**.

---

## 🧱 Example Entries

```
Key: session:12345
Value: {
  "userId": "u001",
  "cart": ["prod_101", "prod_205"],
  "theme": "dark",
  "lastLogin": "2025-06-01T10:30:00Z"
}

Key: session:67890
Value: {
  "userId": "u002",
  "cart": [],
  "theme": "light",
  "lastLogin": "2025-06-01T11:15:00Z"
}
```

Each key uniquely identifies a user session. The corresponding value is typically a JSON-like object.

---

## 🚀 Why It Works

- Super fast **read/write** using a key
- Values can be any format (string, object, binary)
- No complex queries—just retrieve by key

---

## 🗄️ Where It’s Stored

Key-value pairs are stored in **key-value databases**, including:

- Redis
- Amazon DynamoDB
- Riak

Redis stores everything in-memory for speed, ideal for ephemeral data like sessions and caches.
