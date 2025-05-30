# 00_history_and_motivation/README.md

## 🧠 Introduction: Why Build a DBMS from Scratch?

Before diving into building your own database, it's important to understand the historical context and _why_ databases exist at all. This folder explores the motivation behind the invention and widespread use of Database Management Systems (DBMS).

---

## 🕰️ Pre-DBMS Era: Flat Files

Early applications stored data in flat files such as `.txt`, `.csv`, or custom formats. Developers wrote manual logic to:

- Read and write to these files
- Parse the content
- Enforce structure and relationships

This approach was simple but problematic:

| Problem              | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| ❌ Redundancy        | Repeated code to handle structure, parsing, and validation |
| ❌ No Query Language | Developers had to write custom search logic                |
| ❌ No Concurrency    | Two processes writing at once would corrupt data           |
| ❌ No Transactions   | No way to rollback if something failed mid-write           |
| ❌ Poor Performance  | Scanning a large text file is very slow                    |

---

## ✅ Emergence of DBMS

To solve the above issues, database systems were introduced:

- Provide **structured storage**
- Enforce **schemas and constraints**
- Allow **declarative queries** (e.g. SQL)
- Handle **concurrency, transactions, and recovery**

Famous early systems:

- **1970s**: IBM System R → led to SQL
- **1980s**: Oracle, DB2, Informix
- **1990s+**: PostgreSQL, MySQL, SQLite

---

## 📁 This Folder's Purpose

To demonstrate the _limitations_ of file-based approaches:

- You'll simulate writing user records to a plain `.txt` file
- You'll see the need for structured data, indexing, and atomic updates

Once these issues become clear, the next modules will build up DBMS features step by step using Python.

---

## ▶️ Try It

Run `contrast_filesystems.py` to simulate primitive data storage:

```bash
python contrast_filesystems.py
```

Observe how we:

- Append records to a flat file
- Read and parse them manually

These are the kinds of problems a real DBMS solves.

---

Next: We’ll learn to write structured logs and begin building a low-level storage engine.
