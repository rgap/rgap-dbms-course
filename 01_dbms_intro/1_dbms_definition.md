## 🏗️ What Is a DBMS?

A **Database Management System** (DBMS) is software designed to **store**, **retrieve**, and **manage** data efficiently and securely. It acts as an interface between users (or applications) and the underlying data storage.

> A DBMS abstracts the complexity of file handling, enabling users to focus on **data models** and **queries**, rather than low-level data manipulation.

### Example (Using Flat Files):

```txt
users.txt
----------
1, Ana, ana@email.com
2, Bob, bob@email.com
```

**A READ operation:**

```python
with open("users.txt", "r") as f:
    for line in f:
        fields = line.strip().split(", ")
        if fields[1] == "Ana":
            print(fields[2])
```

✅ You must handle:

- File opening/closing
- Data parsing (string splitting)
- Data integrity (what if format is inconsistent?)
- Searching manually (no query language)

**A READ operation using a DBMS**

```sql
-- SQL query
SELECT email FROM users WHERE name = 'Ana';
```

```js
// MongoDB query
db.users.find({ name: "Ana" }, { email: 1, _id: 0 });
```

✅ The DBMS handles:

- File storage and structure
- Indexing and performance
- Concurrency and locks
- Data types and constraints
- Query parsing and optimization
