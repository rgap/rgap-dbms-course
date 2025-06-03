# 📊 Realistic Example: Relational Data Model

## 🏫 Use Case: University Course Registration

A university system that tracks students, courses, and which students are enrolled in which courses.

This scenario maps cleanly to the **relational model** using tables.

---

## 🧱 Table Structure (Relational Schema)

### Students Table

| student_id | name  | major |
| ---------- | ----- | ----- |
| 1          | Alice | CS    |
| 2          | Bob   | EE    |

### Courses Table

| course_id | title                   | credits |
| --------- | ----------------------- | ------- |
| DB101     | Intro to Databases      | 3       |
| AI201     | Artificial Intelligence | 4       |

### Enrollments Table (Relation Table)

| student_id | course_id |
| ---------- | --------- |
| 1          | DB101     |
| 1          | AI201     |
| 2          | DB101     |

---

## 🔑 Keys and Relationships

- `student_id` in Students is a **primary key**
- `course_id` in Courses is a **primary key**
- `Enrollments` uses **foreign keys** to reference both tables, enabling a **many-to-many relationship**

This is a textbook example of a normalized relational design.

---

## 🗄️ Where It’s Stored

This data would be stored in a **Relational Database Management System (RDBMS)** such as:

- MySQL
- PostgreSQL
- Oracle DB
- Microsoft SQL Server

These systems store data in **rows and columns**, use **indexes** for performance, and allow interaction via **SQL queries**.
