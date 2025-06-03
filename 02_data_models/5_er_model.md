# 🧩 Realistic Example: Entity-Relationship (ER) Model

## 🏥 Use Case: Hospital Management System

This example models patients, doctors, and appointments in a hospital using an **ER diagram** structure.

---

## 🧱 Entity and Relationship Description

### Entities

- **Patient**: Has attributes like `PatientID`, `Name`, `DOB`
- **Doctor**: Has attributes like `DoctorID`, `Name`, `Specialty`
- **Appointment**: Represents the interaction and has attributes like `Date`, `Time`, `Room`

### Relationships

- A **Patient** _books_ an **Appointment**
- A **Doctor** _conducts_ an **Appointment**

This creates a **ternary relationship**:

- One appointment involves **one patient** and **one doctor**
- A doctor can conduct **many appointments**
- A patient can have **multiple appointments** with different doctors

---

## 📊 Diagram Sketch (Text-Based)

```
[Patient]───<books>────┐
                       │
                  [Appointment]──<conducted_by>──[Doctor]
```

Or shown with attributes:

```
[Patient]
  - PatientID (PK)
  - Name
  - DOB

[Doctor]
  - DoctorID (PK)
  - Name
  - Specialty

[Appointment]
  - AppointmentID (PK)
  - Date
  - Time
  - Room
  - PatientID (FK)
  - DoctorID (FK)
```

---

## 🗄️ Where It’s Stored

- This model is used during **database design** before creating tables.
- It's translated into a **relational schema** and then implemented in systems like **PostgreSQL**, **MySQL**, etc.
- Often created using tools like **ERDPlus**, **Draw\.io**, or **Lucidchart**.
