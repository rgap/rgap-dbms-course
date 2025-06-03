## ✅ Example: Applying the Database Modeling Process

We’ll apply steps 1 to 5 using the **e-commerce** domain example.

---

### 1. Requirements Analysis

📝 **Goal**: Understand what data needs to be stored.

👥 **Stakeholder Interviews Reveal**:

- Users can place multiple orders.
- Each order can contain multiple products.
- Users can review products.

📦 **Key Business Objects**:

- Users
- Products
- Orders
- Reviews

📌 **Constraints**:

- A review must be written by a user who bought the product.
- Orders should store order dates and statuses.

---

### 2. Conceptual Design (ER Model)

🎯 **Entities**:

- `User` (user_id, name, email)
- `Product` (product_id, title, price)
- `Order` (order_id, user_id, order_date, status)
- `Review` (review_id, user_id, product_id, rating, comment)

🔗 **Relationships**:

- `User` places `Order` (1-to-many)
- `Order` contains `Product` (many-to-many, via `OrderItem`)
- `User` writes `Review` for `Product` (many-to-many)

🧹 **ER Diagram (Textual)**:

```
User ──────< Order >────── Product
  │                ▲             ▲
  │                │             │
  └────< Review ─┘             │
                              (via OrderItem)
```

---

### 3. Logical Design (Relational Model)

Translate the ER model into **normalized tables**:

🗂️ **Tables**:

- `users(user_id PK, name, email)`
- `products(product_id PK, title, price)`
- `orders(order_id PK, user_id FK, order_date, status)`
- `order_items(order_id FK, product_id FK, quantity)`
- `reviews(review_id PK, user_id FK, product_id FK, rating, comment)`

📅 **Normalization**: All tables are in **3NF** (no redundancy or transitive dependencies).

---

### 4. Physical Design

🔧 **Goal**: Plan how to store and access data efficiently.

💡 **Design Decisions**:

- Plan to add indexes to columns like `user_id` and `product_id` to improve search speed.
- Organize the `orders` table so it can be queried easily by date (e.g., for monthly reports).
- Enforce foreign key constraints to keep data consistent.

> These choices will guide how we write the SQL in the next step.

---

### 5. Database Schema (SQL Implementation)

🛠️ **Example Schema**:

```sql
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);

CREATE TABLE products (
  product_id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  price DECIMAL(10,2)
);

CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(user_id),
  order_date DATE,
  status VARCHAR(20)
);

CREATE TABLE order_items (
  order_id INT REFERENCES orders(order_id),
  product_id INT REFERENCES products(product_id),
  quantity INT,
  PRIMARY KEY (order_id, product_id)
);

CREATE TABLE reviews (
  review_id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(user_id),
  product_id INT REFERENCES products(product_id),
  rating INT,
  comment TEXT
);
```
