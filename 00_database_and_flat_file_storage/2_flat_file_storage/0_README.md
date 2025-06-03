## 🕰️ Flat File Storage

A **flat file** is a file that stores data in a plain or structured format (like CSV or JSON), without relationships or indexing mechanisms.

Example: `users.csv`

```txt
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
```

Early applications stored data in flat files such as `.txt`, `.csv`, or custom formats. Developers wrote manual logic to:

- Read and write to these files
- Parse the content
- Enforce structure and relationships

This approach is simple but problematic:

| Problem              | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| ❌ Redundancy        | Repeated code to handle structure, parsing, and validation |
| ❌ No Query Language | Developers had to write custom search logic                |
| ❌ No Concurrency    | Two processes writing at once would corrupt data           |
| ❌ No Transactions   | No way to rollback if something failed mid-write           |
| ❌ Poor Performance  | Scanning a large text file is very slow                    |

---

### 💡 When Are Flat Files Still Useful?

Flat files are not obsolete. They are often used for:

- Configuration files (e.g., `.env`, `.json`)
- Data exchange formats (e.g., `.csv`, `.xml`)
- Logging and event storage
- Simple one-time data storage needs

---

### 📁 This Folder's Purpose

To demonstrate the _limitations_ of file-based approaches:

- Simulate writing user records to a plain `.txt` file
- Understand the need for a system to manage databases

---

### ▶️ Run the scripts

Run the scripts `script.py` to simulate primitive data storage:

```bash
python script.py
```

Observe how we:

- Append records to a flat file
- Read and parse them manually

## Database Management Systems

To overcome the issues, developers and researchers built **Database Management Systems (DBMS)** (such as MySQL). These systems abstract the complexity of data storage and give you:

- A structured way to define and validate data
- A powerful query language (like SQL)
- Built-in concurrency control and atomic transactions
- Tools for indexing, relationships, and scaling

With a DBMS, you can stop worrying about file formats and focus on modeling your data and writing queries.
