# 🌲 Realistic Example: Hierarchical Data Model

## 🏢 Use Case: Organizational Directory

Consider an **international company** with departments and employees structured in a strict hierarchy.

### Tree Structure

```
Company
├── Country: USA
│   ├── Department: Engineering
│   │   ├── Employee: Alice
│   │   └── Employee: Bob
│   └── Department: HR
│       └── Employee: Carol
└── Country: Germany
    └── Department: Sales
        └── Employee: Daniel
```

- Each **Employee** belongs to **one Department**
- Each **Department** belongs to **one Country**
- Each **Country** belongs to **one Company**

---

## 🗄️ Where It’s Stored

The hierarchical model is stored in **tree-based database systems** like:

- IBM IMS
- Windows Registry
- XML files (used for config, documents, etc.)

These systems are optimized for **navigating through parent-child paths**.

---

## 📄 Storage Representation (XML-like)

```xml
<Company name="GlobalTech">
  <Country name="USA">
    <Department name="Engineering">
      <Employee name="Alice" id="E101" />
      <Employee name="Bob" id="E102" />
    </Department>
    <Department name="HR">
      <Employee name="Carol" id="E103" />
    </Department>
  </Country>
  <Country name="Germany">
    <Department name="Sales">
      <Employee name="Daniel" id="E201" />
    </Department>
  </Country>
</Company>
```

The **structure is rigid**, and navigation usually starts at the top level (root node) and follows the defined path downward.
