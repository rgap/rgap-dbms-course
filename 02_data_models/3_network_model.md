# 🔗 Realistic Example: Network Data Model

## 🏗️ Use Case: Project Management System

In a large organization, employees can be assigned to multiple projects, and each project may involve multiple employees.

This creates a **many-to-many** relationship:

### Graph-Like Structure

```
Employee: Alice
├── Project: Website Redesign
└── Project: Marketing Dashboard

Employee: Bob
├── Project: Marketing Dashboard
└── Project: Data Migration

Employee: Carol
└── Project: Website Redesign

Project: Website Redesign
├── Employee: Alice
└── Employee: Carol

Project: Marketing Dashboard
├── Employee: Alice
└── Employee: Bob
```

---

## 📁 Record Representation with Pointers (Conceptual)

```
Record: Employee { ID: E01, Name: "Alice", Projects: [P01, P02] }
Record: Employee { ID: E02, Name: "Bob", Projects: [P02, P03] }
Record: Employee { ID: E03, Name: "Carol", Projects: [P01] }

Record: Project { ID: P01, Title: "Website Redesign", Employees: [E01, E03] }
Record: Project { ID: P02, Title: "Marketing Dashboard", Employees: [E01, E02] }
Record: Project { ID: P03, Title: "Data Migration", Employees: [E02] }
```

- Each **Employee record** has pointers to their **Project records**
- Each **Project record** has pointers to **Employee records**

This bidirectional linkage enables efficient navigation from either side.

---

## 🗄️ Where It’s Stored

The network model is typically implemented in systems like **IDMS** or **TurboIMAGE**, which store data as **records** with **direct physical pointers**.

Simulated representations may also exist in XML using cross-references:

```xml
<Employee id="E01" name="Alice">
  <Projects>
    <ProjectRef id="P01"/>
    <ProjectRef id="P02"/>
  </Projects>
</Employee>
...
```

But native network DBMS store these with **pointer chains** on disk or in memory.
