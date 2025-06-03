# 📄 Realistic Example: Document Data Model

## 🛒 Use Case: E-commerce Product Catalog

An online store needs to store flexible product data. Each product may have different specifications, variants, or embedded reviews. This makes it ideal for a **document model**.

---

## 🧱 Sample Document (JSON Format)

```json
{
  "_id": "prod_001",
  "name": "Wireless Headphones",
  "brand": "SoundMagic",
  "price": 79.99,
  "specs": {
    "battery_life": "30 hours",
    "bluetooth": true,
    "noise_cancellation": true
  },
  "variants": [
    { "color": "Black", "stock": 12 },
    { "color": "White", "stock": 5 }
  ],
  "reviews": [
    {
      "user": "Alice",
      "rating": 4,
      "comment": "Great sound quality."
    },
    {
      "user": "Bob",
      "rating": 5,
      "comment": "Excellent battery life."
    }
  ]
}
```

---

## 🔁 Why Document Model Works Here

- Each document is **self-contained** and stores everything about one product.
- The structure is **flexible**—some products may not have `variants` or `reviews`.
- Nested objects allow modeling **one-to-many** relationships within the same document.

---

## 🗄️ Where It’s Stored

This format is designed for **document-oriented databases**, especially:

- MongoDB
- Couchbase
- Firebase Firestore

Stored as **BSON** (binary JSON) internally for efficient access and indexing.
