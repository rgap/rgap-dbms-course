# 🌍 Examples of Real-World Databases

Databases are fundamental to modern software systems.  
They allow applications to **persist**, **query**, and **manage structured data** efficiently.

Below are real-world categories and common use cases:

---

## 🏦 Banking Systems

- **Data Stored**: `accounts`, `customers`, `transactions`, `balances`
- **What features are needed?**
  - Ensure **consistency** and **durability**

---

## 🛍️ E-commerce Platforms (e.g., Amazon)

- **Data Stored**: `products`, `users`, `shopping carts`, `orders`, `reviews`
- **What features are needed?**
  - Handle **complex queries** (e.g., product search, filtering)
  - Scale to support **high read/write traffic**

---

## 🏥 Healthcare Systems

- **Data Stored**: `patients`, `doctors`, `visits`, `diagnoses`, `treatments`
- **What features are needed?**
  - Ensure **data privacy** and **compliance**
  - Fast and secure **patient data access**

---

## 🎓 University Systems

- **Data Stored**: `students`, `courses`, `grades`, `registrations`
- **What features are needed?**
  - Manage **entity relationships** (e.g., many-to-many between students and courses)
  - Keep **student records secure** and **queryable**

---

## 📱 Social Media Applications (e.g., Instagram)

- **Data Stored**: `posts`, `users`, `likes`, `followers`, `comments`
- **What features are needed?**
  - Ensure **high availability**
  - Model **graph-like relationships** (e.g., follow/followers)

---

## 📊 Business Intelligence

- **Use Case**: `data warehouses`, `OLAP cubes`, `dashboards`, `analytics tools`
- **What features are needed?**
  - Optimize for **read-heavy** operations

--

## 👥 Example: A Simple Users Database

Here’s a basic example of what a **users** database might look like:

```csv
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
```

### 📀 Where Can This Be Stored?

This data could be stored in:

- A **spreadsheet application** like **Excel** or **Google Sheets** (suitable for simple use cases, manual data entry, or prototyping)
- A **CSV file** (for small datasets or offline use)
- A **relational database** like **MySQL** or **PostgreSQL**
- A **cloud database** (e.g., **Firebase**, **Supabase**, **Amazon RDS**)
- A **NoSQL document store** like **MongoDB** (using fields like `_id`, `name`, `email`)







